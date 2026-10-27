"""Python replacements for the old NPA MATLAB helpers.

Erlang B/C match the log-gamma implementation in ``matlab/erlangB.m`` and
``matlab/erlangC.m``. Exponential sampling matches ``matlab/exponentialSamp.m``.
The discrete-time M/M/1 loop follows ``matlab/demo/simulateQueue.m``.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from scipy.special import gammaln


def exponential_sample(rate: float, size=None, rng=None) -> np.ndarray:
    """Sample from an exponential with rate ``lambda`` (MATLAB ``exponentialSamp``).

    NumPy's ``exponential`` uses the scale parameter ``1/lambda``. This helper
    keeps the rate parameterisation from the notes.
    """
    rng = np.random.default_rng(rng)
    u = rng.random(size)
    return -np.log(u) / rate


def erlang_b(offered_load, servers) -> np.ndarray:
    """Erlang B blocking probability ``B(m, a)``.

    Parameters
    ----------
    offered_load
        Offered traffic ``a`` (scalar or array).
    servers
        Number of servers ``m`` (int or array of ints).
    """
    a = np.atleast_1d(np.asarray(offered_load, dtype=float))
    m = np.atleast_1d(np.asarray(servers, dtype=int))
    blocking = np.empty((a.size, m.size))
    for i, ai in enumerate(a):
        for j, mj in enumerate(m):
            if mj < 0:
                raise ValueError("servers must be non-negative")
            if mj == 0:
                blocking[i, j] = 1.0
                continue
            if ai <= 0:
                blocking[i, j] = 0.0
                continue
            k = np.arange(mj)
            part_one = mj * np.log(ai) - gammaln(mj + 1)
            log_terms = np.concatenate(
                [k * np.log(ai) - gammaln(k + 1) - part_one, [0.0]]
            )
            blocking[i, j] = 1.0 / np.exp(log_terms).sum()
    return np.squeeze(blocking)


def erlang_c(offered_load, servers) -> np.ndarray:
    """Erlang C waiting probability ``C(m, a)``.

    Returns NaN when offered load is not strictly less than the number of
    servers, matching ``matlab/erlangC.m``.
    """
    a = np.atleast_1d(np.asarray(offered_load, dtype=float))
    m = np.atleast_1d(np.asarray(servers, dtype=int))
    waiting = np.empty((a.size, m.size))
    for i, ai in enumerate(a):
        for j, mj in enumerate(m):
            if mj <= 0:
                waiting[i, j] = np.nan
                continue
            if np.isclose(ai, mj):
                waiting[i, j] = 1.0
                continue
            if ai >= mj:
                waiting[i, j] = np.nan
                continue
            if ai <= 0:
                waiting[i, j] = 0.0
                continue
            k = np.arange(mj)
            part_one = (
                mj * np.log(ai) - gammaln(mj + 1) - np.log(1.0 - ai / mj)
            )
            log_terms = np.concatenate(
                [k * np.log(ai) - gammaln(k + 1) - part_one, [0.0]]
            )
            waiting[i, j] = 1.0 / np.exp(log_terms).sum()
    return np.squeeze(waiting)


def plot_erlang_curves(
    server_range,
    traffic_range,
    kind: str = "B",
    diagrams: str | Path | None = None,
    filename: str | None = None,
):
    """Draw Erlang B or C curves against offered load (MATLAB ``plotErlang``)."""
    import matplotlib.pyplot as plt

    kind = kind.upper()
    if kind not in {"B", "C"}:
        raise ValueError("kind must be 'B' or 'C'")
    servers = np.atleast_1d(np.asarray(server_range, dtype=int))
    traffic = np.atleast_1d(np.asarray(traffic_range, dtype=float))
    values = (
        erlang_b(traffic, servers) if kind == "B" else erlang_c(traffic, servers)
    )
    if values.ndim == 1:
        values = values.reshape(1, -1)
    # erlang_* returns shape (len(traffic), len(servers)); MATLAB stored (m, a).
    values = values.T

    fig, ax = plt.subplots(figsize=(8, 5))
    for row, m in zip(values, servers):
        ax.semilogy(traffic, row, linewidth=2, label=str(m))
    ax.set_xlim(float(traffic.min()), float(traffic.max()))
    ax.set_ylim(1e-3, 1.0)
    ax.grid(True, which="both", alpha=0.4)
    ax.set_xlabel("offered traffic, $a$")
    ax.set_ylabel(
        "probability of blocking" if kind == "B" else "probability of waiting"
    )
    ax.legend(title="$m$", ncols=2, fontsize=8)
    fig.tight_layout()
    if diagrams is not None:
        out = Path(diagrams)
        out.mkdir(parents=True, exist_ok=True)
        stem = filename or f"erlang{kind}-curves"
        fig.savefig(out / f"{stem}.svg")
        fig.savefig(out / f"{stem}.png")
    return fig, ax


def simulate_mm1(
    arrival_rate: float,
    service_rate: float,
    delta_t: float = 0.01,
    n_iters: int = 100_000,
    rng=None,
) -> np.ndarray:
    """Discrete-time birth-death simulation of an M/M/1 queue.

    Each step an arrival occurs with probability ``lambda * delta_t`` and a
    service completion with probability ``mu * delta_t``, as in
    ``matlab/demo/simulateQueue.m``.
    """
    rng = np.random.default_rng(rng)
    k = 0
    occupancy = np.empty(n_iters, dtype=int)
    p_arrival = arrival_rate * delta_t
    p_service = service_rate * delta_t
    if p_arrival + p_service > 1:
        raise ValueError("delta_t is too large for the given rates")
    draws = rng.random(n_iters)
    for i, p in enumerate(draws):
        if p < p_arrival:
            k += 1
        elif p < p_arrival + p_service and k > 0:
            k -= 1
        occupancy[i] = k
    return occupancy


def plot_mm1_occupancy(
    arrival_rate: float,
    service_rate: float,
    n_iters: int = 100_000,
    delta_t: float = 0.01,
    rng=1,
    diagrams: str | Path | None = None,
    filename: str | None = None,
):
    """Histogram of simulated occupancy against the geometric steady state."""
    import matplotlib.pyplot as plt

    occupancy = simulate_mm1(
        arrival_rate, service_rate, delta_t=delta_t, n_iters=n_iters, rng=rng
    )
    rho = arrival_rate / service_rate
    counts = np.bincount(occupancy)
    empirical = counts / counts.sum()
    ks = np.arange(len(empirical))
    geometric = (1.0 - rho) * rho**ks

    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(ks, empirical, width=0.8, alpha=0.6, label="time average")
    ax.plot(ks, geometric, "k.-", label=rf"$(1-\rho)\rho^k$, $\rho={rho:.2g}$")
    ax.set_xlabel("occupancy $k$")
    ax.set_ylabel("$P(k)$")
    ax.set_xlim(-0.5, max(20, int(ks.max())))
    ax.legend()
    fig.tight_layout()
    if diagrams is not None:
        stem = filename or f"mm1-occupancy-rho-{rho:.2g}-{n_iters}"
        write_figure(fig, stem, diagrams)
    return fig, ax


def poisson_pmf(k, mu):
    """Poisson probabilities ``P(k | mu) = mu^k exp(-mu) / k!``."""
    from scipy.stats import poisson

    return poisson.pmf(k, mu)


def write_figure(fig, stem: str, directory: str | Path) -> Path:
    """Save SVG and PNG next to each other, matching ``mlai.write_figure``."""
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    svg = directory / f"{stem}.svg"
    fig.savefig(svg)
    fig.savefig(directory / f"{stem}.png")
    return svg

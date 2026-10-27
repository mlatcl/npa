\ifndef{mm1Simulation}
\define{mm1Simulation}

\section{Discrete Simulation of $M/M/1$}

\notes{Lab 1 runs a discrete-time simulation of $M/M/1$. Because a birth-death process is a Markov chain on a clock of length $\Delta t$, each step has three outcomes: birth, death, or no change.}

\figure{\includepng{\diagramsDir/npa/discreteMM1State}{70%}}{Discrete-time $M/M/1$: from occupancy $k$ the next occupancy is $k+1$, $k-1$, or $k$.}{discrete-mm1-state}

\figure{\includepng{\diagramsDir/npa/probOutcome}{60%}}{Draw $U\sim\mathrm{Uniform}(0,1)$. Birth if $U<P(b)$; death if $P(b)\le U<P(b)+P(d)$ and $k>0$; otherwise stay.}{discrete-mm1-outcomes}

\notes{The continuous $M/M/1$ is the $\Delta t\to 0$ limit of this chain, as Coin Monopoly became a Poisson process. In the lab, take $\Delta t$ much smaller than $1/\lambda$ and $1/\mu$, and set $P(b)=\lambda\Delta t$, $P(d)=\mu\Delta t$.}

\slides{* Three outcomes per step: $+1$, $-1$, or stay
* $P(b)=\lambda\Delta t$, $P(d)=\mu\Delta t$
* Small $\Delta t$ approximates the continuous queue}

\include{snippets/_npa/includes/npa-python-setup.md}

\notes{The original MATLAB demo is `simulateQueue.m`. The helper `npa_plots.simulate_mm1` is the same loop. Compare the time-average occupancy with the geometric $P(k)=(1-\rho)\rho^k$, first at $\rho=1/2$ and then at $\rho=0.95$. The high-utilisation chain mixes slowly: 100 seconds is not enough; 1000 seconds is closer.}

\code{fig, ax = npa_plots.plot_mm1_occupancy(1.0, 2.0, n_iters=10_000, rng=1)
ax.set_title(r"$\rho=0.5$, first 100 seconds")
plt.show()
fig, ax = npa_plots.plot_mm1_occupancy(1.0, 2.0, n_iters=100_000, rng=1)
ax.set_title(r"$\rho=0.5$, first 1000 seconds")
plt.show()}

\code{fig, ax = npa_plots.plot_mm1_occupancy(1.9, 2.0, n_iters=10_000, rng=1)
ax.set_title(r"$\rho=0.95$, first 100 seconds")
plt.show()
fig, ax = npa_plots.plot_mm1_occupancy(1.9, 2.0, n_iters=100_000, rng=1)
ax.set_title(r"$\rho=0.95$, first 1000 seconds")
plt.show()}

\endif

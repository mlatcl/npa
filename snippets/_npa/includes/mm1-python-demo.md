\ifndef{npaMm1PythonDemo}
\define{npaMm1PythonDemo}

\include{snippets/_npa/includes/npa-python-setup.md}

\notes{The original MATLAB demo is `simulateQueue.m`. The helper `npa_plots.simulate_mm1` is the same loop. Compare the time-average occupancy with the geometric $P(k)=(1-\rho)\rho^k$, first at $\rho=1/2$ and then at $\rho=0.95$.}

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

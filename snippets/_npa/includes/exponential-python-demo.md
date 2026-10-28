\ifndef{npaExponentialPythonDemo}
\define{npaExponentialPythonDemo}

\include{snippets/_npa/includes/npa-python-setup.md}

\notes{The MATLAB helper `exponentialSamp.m` drew $U\sim\mathrm{Uniform}(0,1)$ and returned $-\log U/\lambda$. That is `npa_plots.exponential_sample`.}

\code{lam = 2.0
x = npa_plots.exponential_sample(lam, size=20_000, rng=1)
print("sample mean", x.mean(), "should be", 1/lam)
print("sample variance", x.var(), "should be", 1/lam**2)
plt.hist(x, bins=40, density=True, alpha=0.6, label="samples")
t = np.linspace(0, x.max(), 200)
plt.plot(t, lam * np.exp(-lam * t), label=r"$\lambda e^{-\lambda x}$")
plt.legend()
plt.show()}

\endif

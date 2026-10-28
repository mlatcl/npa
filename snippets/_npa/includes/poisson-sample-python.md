\ifndef{npaPoissonSamplePython}
\define{npaPoissonSamplePython}

\include{snippets/_npa/includes/npa-python-setup.md}

\notes{The MATLAB sampler `exponentialSamp.m` is `npa_plots.exponential_sample` (inverse CDF). Poisson counts are drawn with NumPy.}

\code{mu = 2.0
rng = np.random.default_rng(1)
k = rng.poisson(mu, size=20_000)
print("sample mean", k.mean(), "sample variance", k.var())}

\endif

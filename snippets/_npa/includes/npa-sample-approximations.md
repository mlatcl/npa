\ifndef{npaSampleApproximations}
\define{npaSampleApproximations}

\section{Sample-Based Approximations}

\notes{The expectation of $f(k)$ under $P(k)$ is $\langle f(k)\rangle=\sum_k f(k)P(k)$. From the pictorial definition,
$$
P(k)=\lim_{S\to\infty}\frac{s_k}{S},
$$
where $S$ is the number of independent trials and $s_k$ the number that landed in state $k$. For large $S$,
$$
\langle f(k)\rangle \approx \frac{1}{S}\sum_{i=1}^{S} f(k_i),
$$
with $k_i$ independent samples from $P(k)$. The *sample mean* $\bar k = S^{-1}\sum_i k_i$ is the special case $f(k)=k$. The same replacement of integrals by averages holds for densities.}

\slides{* $P(k)\approx s_k/S$ for large $S$
* $\langle f\rangle \approx S^{-1}\sum_i f(k_i)$
* Sample mean versus distribution mean: keep them distinct
* Later: time averages versus steady-state averages}

\notes{Most texts use “mean” for both the sample mean and the mean of the distribution. Keep the distinction. Later in the course we will also meet time averages, and we will assume that a time average equals an average under a steady-state distribution.}

\subsection{Mean of a Poisson}

\notes{The mean of $P(k\mid\mu)=\mu^k e^{-\mu}/k!$ is $\mu$. Pull $\mu e^{-\mu}$ out of the sum, cancel $k/k!$, shift the index $m=k-1$, and recognise the series for $e^{\mu}$. The variance is an exercise on Tutorial Sheet 1.}

\slides{* Poisson mean: $\langle k\rangle=\mu$
* Variance: Tutorial 1}

\include{snippets/_npa/includes/npa-python-setup.md}

\notes{We can check the Poisson mean by sampling. The helper `exponential_sample` is the inverse-CDF sampler from the old MATLAB `exponentialSamp.m`; Poisson counts are most easily drawn from NumPy.}

\code{mu = 2.0
rng = np.random.default_rng(1)
k = rng.poisson(mu, size=20_000)
print("sample mean", k.mean(), "sample variance", k.var())}

\endif

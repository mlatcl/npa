\ifndef{exponentialInterarrival}
\define{exponentialInterarrival}

\section{Interarrival Times}

\notes{The distribution of times between arrivals of a Poisson process is exponential,
$$
p(X)=\lambda e^{-\lambda X}.
$$
Stating that interarrival times are exponential with parameter $\lambda$ is the same as stating that arrivals are Poisson with rate $\lambda$. If students register at a rate $\lambda=2$ per minute, the gaps between them are exponential with the same $\lambda$.}

\figure{\includepng{\diagramsDir/npa/interArrivals}{60%}}{Arrival epochs $T_n$ and interarrival times $X_n=T_n-T_{n-1}$ for a Poisson process.}{poisson-interarrivals}

\notes{The derivation uses the CDF. $P(X_i>t)$ is the probability of no arrivals in an interval of length $t$, which is $e^{-\lambda t}$. Differentiating $1-e^{-\lambda t}$ recovers $\lambda e^{-\lambda X}$. That argument is written out as an example at the end of the original notes and as an exercise below.}

\slides{* Interarrival PDF $p(X)=\lambda e^{-\lambda X}$
* Equivalent to a Poisson process of rate $\lambda$
* $P(\text{no arrival in }t)=e^{-\lambda t}$ is the CDF’s complement}

\section{The Exponential Distribution}

\subsection{Memoryless}

\notes{The exponential is *memoryless*:
$$
P(X>s+t\mid X>t)=P(X>s).
$$
Having already waited $t$ does not change the distribution of the remaining wait. That is the property we will use for Markov queues.}

\slides{* Memoryless: $P(X>s+t\mid X>t)=P(X>s)$
* Remaining wait does not depend on time already waited}

\subsection{Mean and Variance}

\notes{For $p(X)=\lambda e^{-\lambda X}$,
$$
\langle X\rangle=\frac{1}{\lambda}, \qquad \mathrm{Var}(X)=\frac{1}{\lambda^2}.
$$
Confirming these is part of Tutorial 1.}

\include{snippets/_npa/includes/npa-python-setup.md}

\notes{The MATLAB helper `exponentialSamp.m` drew $U\sim\mathrm{Uniform}(0,1)$ and returned $-\log U/\lambda$. That is the inverse-CDF sampler.}

\code{lam = 2.0
x = npa_plots.exponential_sample(lam, size=20_000, rng=1)
print("sample mean", x.mean(), "should be", 1/lam)
print("sample variance", x.var(), "should be", 1/lam**2)
plt.hist(x, bins=40, density=True, alpha=0.6, label="samples")
t = np.linspace(0, x.max(), 200)
plt.plot(t, lam * np.exp(-lam * t), label="exponential pdf")
plt.xlabel("interarrival time")
plt.legend()
plt.show()}

\endif

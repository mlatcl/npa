\ifndef{poissonProcessDefinition}
\define{poissonProcessDefinition}

\section{Stochastic Processes}

\notes{A probabilistic process — a random process, or a stochastic process — is a random function: it maps inputs to a distribution over values rather than to a single value. The Wiener process sits behind Brownian motion. The Black–Scholes formula models the logarithm of a stock price as a Wiener process. Following [@Chan:performance00], a random process is a random function which, for a particular input, is a random quantity.}

\slides{* Random process: a random function
* Wiener process: Brownian motion; Black–Scholes on log-price
* This course: the Poisson process}

\section{The Poisson Process}

\notes{The Poisson *distribution* gives probabilities over counts. The Poisson *process* gives probabilities of $k$ arrivals as a function of time $t$ for a rate $\lambda$,
$$
P(k\mid t,\lambda)=\frac{(\lambda t)^k}{k!}e^{-\lambda t}.
$$
This is the Poisson distribution with $\mu$ replaced by $\lambda t$. The mean number of arrivals by time $t$ is therefore $\langle k\rangle=\lambda t$, so $\lambda$ is a rate. The Poisson process is a counting process whose counts are expected to grow linearly in time.}

\slides{* $P(k\mid t,\lambda)=(\lambda t)^k e^{-\lambda t}/k!$
* Poisson distribution with $\mu=\lambda t$
* $\langle k\rangle=\lambda t$: $\lambda$ is arrivals per unit time}

\include{snippets/_npa/includes/npa-python-setup.md}

\code{lam = 2.0
t = np.linspace(0, 5, 6)
# expected counts grow linearly
print(list(zip(t, lam * t)))}

\endif

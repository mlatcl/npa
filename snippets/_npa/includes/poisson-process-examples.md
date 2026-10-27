\ifndef{poissonProcessExamples}
\define{poissonProcessExamples}

\section{Worked Examples}

\subsection{Superposition}

\notes{Three independent Poisson registration queues: Physics and Fine Art at rate 4 per minute, Psychology of Sociology at rate 2, Computer Science and Aromatherapy at rate 5. Combined rate $\lambda=11$. After 15 minutes the expected number of arrivals is $165$.}

\slides{* Rates $4+2+5=11$
* After 15 minutes, $k=90$ has probability $\approx 5.5\times 10^{-11}$
* $k=180$ is nearer the mean: compute in the log domain, $\approx 0.015$}

\notes{Evaluate $P(k\mid\lambda=11,t=15)$ in the log domain,
$$
\log P = k\log(\lambda t)-\log(k!)-(\lambda t),
$$
because $180!$ will overflow a naive factorial.}

\include{snippets/_npa/includes/npa-python-setup.md}

\code{from scipy.stats import poisson
lam, t = 11.0, 15.0
mu = lam * t
print("P(k=90) =", poisson.pmf(90, mu))
print("P(k=180) =", poisson.pmf(180, mu))}

\subsection{Decomposition}

\notes{One hall, four desks by first letter of surname, with $P(d)=(0.20,0.27,0.25,0.28)$ and total rate 10 students per minute. Desk 1 is Poisson with rate $2$; $P(k=5\mid t=5)\approx 0.038$. Desk 4 has rate $2.8$; $P(k=20\mid t=10)\approx 0.025$.}

\code{print("desk 1, k=5, t=5:", poisson.pmf(5, 2.0 * 5))
print("desk 4, k=20, t=10:", poisson.pmf(20, 2.8 * 10))}

\endif

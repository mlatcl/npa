\ifndef{mmInfinity}
\define{mmInfinity}

\section{Other Markov Queues}

\notes{The $M/M/1$ queue is the simplest Markov queue. Two nearby members of the same birth-death family change one of Kendall's slots: a finite buffer $M/M/1/m$, and an unlimited number of servers $M/M/\infty$. Both keep Poisson arrivals and exponential service; only the rates $\lambda_k$ and $\mu_k$ change.}

\slides{* Next to $M/M/1$: finite buffer, or infinitely many servers
* Same detailed-balance recurrence, different $\lambda_k$, $\mu_k$}

\section{Infinite Servers: $M/M/\infty$}

\notes{Sometimes it is useful to give every customer their own server. Occupancy $k$ then has death rate $\mu_k=k\mu$ (each of the $k$ busy servers finishes independently at rate $\mu$) and a constant birth rate $\lambda_k=\lambda$. There is never a queue: a customer starts service immediately.}

\figure{\includepng{\diagramsDir/npa/stateMMinf}{80%}}{State diagram for the $M/M/\infty$ queue: unbounded $k$, death rate rising linearly with occupancy.}{mm-inf-state-diagram}

\figure{\includepng{\diagramsDir/npa/boundaryFlowMMinf}{50%}}{Boundary flow for $M/M/\infty$: $\lambda P(k-1)=k\mu P(k)$.}{mm-inf-boundary-flow}

\notes{Detailed balance is
$$
\lambda P(k-1)=k\mu P(k),
$$
so
$$
P(k)=\frac{\lambda}{k\mu}P(k-1)=P(0)\frac{a^k}{k!},\qquad a=\frac{\lambda}{\mu}.
$$
The dimensionless ratio $a$ is the *offered load*, with SI-adjacent unit the Erlang (after A. K. Erlang). It is *not* the utilisation: $\rho$ never exceeds 1, but $a$ for $M/M/\infty$ may be much larger than 1 because there is always a free server.}

\notes{Normalisation over $k=0,1,2,\ldots$ uses $\sum_{k=0}^{\infty}a^k/k!=e^{a}$, so $P(0)=e^{-a}$ and
$$
P(k)=\frac{a^k}{k!}e^{-a}:
$$
occupancy is Poisson with mean $a$. The proportion of time the system is in use is $1-P(0)=1-e^{-a}$.}

\slides{* $\mu_k=k\mu$, $\lambda_k=\lambda$
* Offered load $a=\lambda/\mu$ (Erlangs), not utilisation
* $P(k)=e^{-a}a^k/k!$: Poisson occupancy}

\endif

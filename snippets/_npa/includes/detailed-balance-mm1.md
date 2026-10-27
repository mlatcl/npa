\ifndef{detailedBalanceMm1}
\define{detailedBalanceMm1}

\section{Global Balance}

\notes{A stationary distribution satisfies *global balance*: at equilibrium the frequency of transitions out of $k$ equals the frequency of transitions into $k$ [@Bertsekas:data92, p.~260--262].}

\subsection{Discrete Time}

\notes{A chain is specified by a transition matrix $P_{ij}=\Pr(\text{next}=j\mid\text{now}=i)$. If $P(j)$ is the steady-state probability of state $j$, global balance is
$$
P(j)\sum_{i}P_{ji}=\sum_{i}P(i)P_{ij}:
$$
the probability of leaving $j$ equals the probability of arriving in $j$.}

\subsection{Continuous Time}

\notes{A process is specified by rates $q_{ij}$ from $i$ to $j$. Global balance becomes
$$
P(j)\sum_{i}q_{ji}=\sum_{i}P(i)q_{ij}.
$$}

\slides{* Global balance: flow out of $k$ equals flow into $k$
* Chain: $P(j)\sum_i P_{ji}=\sum_i P(i)P_{ij}$
* Process: rates $q_{ij}$ in place of $P_{ij}$}

\section{Detailed Balance}

\notes{In a birth-death process the only transitions are between neighbours, so $P_{ij}=0$ unless $|i-j|\le 1$. Global balance then reduces to *detailed balance* between $k-1$ and $k$:
$$
P(k-1)\,P_{k-1,k}=P(k)\,P_{k,k-1},
$$
or, with rates $\lambda_{k-1}$ (birth from $k-1$) and $\mu_k$ (death from $k$),
$$
P(k-1)\lambda_{k-1}=P(k)\mu_k.
$$}

\figure{\includepng{\diagramsDir/npa/boundaryFlow}{55%}}{Flow across the boundary between $k-1$ and $k$. At equilibrium $\lambda_{k-1}P(k-1)=\mu_k P(k)$.}{birth-death-boundary-flow}

\notes{Rearrangement gives the recurrence
$$
P(k)=\frac{\lambda_{k-1}}{\mu_k}P(k-1).
$$
Different queues are different choices of $\lambda_k$ and $\mu_k$. The $M/M/1$ queue takes both rates constant.}

\slides{* Neighbours only $\Rightarrow$ detailed balance
* $\lambda_{k-1}P(k-1)=\mu_k P(k)$
* $P(k)=(\lambda_{k-1}/\mu_k)P(k-1)$}

\section{The $M/M/1$ Queue}

\notes{Kendall's $M/M/1$ is Poisson arrivals at rate $\lambda$ and exponential service at rate $\mu$: a birth-death process with $\lambda_k=\lambda$ and $\mu_k=\mu$ for every $k\ge 1$, and no death from $0$.}

\figure{\includepng{\diagramsDir/npa/stateMM1}{70%}}{State diagram for the $M/M/1$ queue: unbounded $k$, no transition below $0$, constant rates.}{mm1-state-diagram}

\figure{\includepng{\diagramsDir/npa/boundaryFlowMM1}{55%}}{Boundary flow for $M/M/1$: $\lambda P(k-1)=\mu P(k)$.}{mm1-boundary-flow}

\notes{Detailed balance gives
$$
P(k)=\frac{\lambda}{\mu}P(k-1)=\rho^k P(0),\qquad \rho=\frac{\lambda}{\mu}.
$$
The ratio $\rho$ is the *utilisation*. Normalisation over $k=0,1,2,\ldots$ requires
$$
\sum_{k=0}^{\infty}P(k)=1=P(0)\sum_{k=0}^{\infty}\rho^k.
$$
The geometric series converges only for $\rho<1$,
$$
\sum_{k=0}^{\infty}\rho^k=\frac{1}{1-\rho},
$$
so $P(0)=1-\rho$ and
$$
P(k)=\rho^k(1-\rho).
$$
If $\rho\ge 1$ there is no steady state: the queue grows without bound.}

\slides{* $M/M/1$: $\lambda_k=\lambda$, $\mu_k=\mu$
* $\rho=\lambda/\mu$, $P(k)=\rho^k(1-\rho)$ for $\rho<1$
* $\rho\ge 1$: no stationary distribution}

\subsection{Mean Occupancy}

\notes{The mean number in the *system* (queue plus server) is
$$
\langle k\rangle=\sum_{k=0}^{\infty}kP(k)=\frac{\rho}{1-\rho}=\frac{\lambda}{\mu-\lambda}.
$$
That is not the mean queue length: a customer in service is in the system but not waiting. The occupancy variance is $\rho/(1-\rho)^2$; computing it is an exercise on Tutorial 2.}

\slides{* $\langle k\rangle=\rho/(1-\rho)=\lambda/(\mu-\lambda)$
* Includes the customer in service
* $\mathrm{Var}(k)=\rho/(1-\rho)^2$ (Tutorial 2)}

\endif

\ifndef{erlangDelayModel}
\define{erlangDelayModel}

\section{Erlang Delay: $M/M/m$}

\notes{$M/M/\infty$ is the unlimited-server extreme. A call centre, a trunk group with holding, or any pool of $m$ identical exponential servers with a waiting line is the *Erlang delay* system: Kendall $M/M/m$. Arrivals that find all servers busy join an unbounded queue. The system is lossless, so carried load equals offered load $a=\lambda/\mu$. The mean holding time is $\tau=1/\mu\equiv\bar{X}$.}

\figure{\includepng{\diagramsDir/npa/erlangDelayDiagram}{70%}}{Schematic of Erlang delay: offered load $a$ enters through a queue; nothing is lost, so carried load equals $a$.}{erlang-delay-schematic}

\figure{\includepng{\diagramsDir/npa/erlangDelay}{85%}}{State diagram of $M/M/m$: death rate climbs as $k\mu$ until $k=m$, then saturates at $m\mu$.}{erlang-delay-state}

\notes{Birth-death rates are
$$
\lambda_k=\lambda,\qquad
\mu_k=\begin{cases}
k\mu & 1\le k\le m,\\
m\mu & k>m.
\end{cases}
$$
Utilisation of the *server pool* is $\rho=\lambda/(m\mu)=a/m$. Stability still requires $\rho<1$, i.e. $a<m$: the arrival rate must be less than the full-pool service rate.}

\subsection{Detailed Balance}

\notes{For $k\le m$ the boundary is the $M/M/\infty$ boundary,
$$
\lambda P(k-1)=k\mu P(k)\qquad\Rightarrow\qquad P(k)=\frac{m\rho}{k}P(k-1)=\frac{(m\rho)^k}{k!}P(0).
$$}

\figure{\includepng{\diagramsDir/npa/boundaryFlowMMinf}{45%}}{Boundary flow while at least one server is free: $\lambda P(k-1)=k\mu P(k)$.}{erlang-delay-boundary-free}

\notes{For $k>m$ every server is busy, so the death rate is $m\mu$,
$$
\lambda P(k-1)=m\mu P(k)\qquad\Rightarrow\qquad P(k)=\rho P(k-1)=\rho^{k-m}P(m).
$$
With $P(m)=(m\rho)^m P(0)/m!$ this is
$$
P(k)=\frac{m^m\rho^k}{m!}P(0),\qquad k>m.
$$}

\figure{\includepng{\diagramsDir/npa/boundaryFlowMMm}{45%}}{Boundary flow once all $m$ servers are busy: $\lambda P(k-1)=m\mu P(k)$.}{erlang-delay-boundary-busy}

\notes{The stationary distribution is therefore piecewise
$$
P(k)=\begin{cases}
P(0)\,(m\rho)^k/k! & k\le m,\\
P(0)\,m^m\rho^k/m! & k>m.
\end{cases}
$$
Normalisation, summing the Poisson-like head and the geometric tail, gives
$$
P(0)=\left[\sum_{k=0}^{m-1}\frac{(m\rho)^k}{k!}+\frac{(m\rho)^m}{m!(1-\rho)}\right]^{-1}.
$$}

\slides{* $M/M/m$: $m$ servers, unbounded waiting line, lossless
* $\rho=a/m=\lambda/(m\mu)$; need $\rho<1$
* $P(k)$ Poisson-like for $k\le m$, geometric tail for $k>m$}

\endif

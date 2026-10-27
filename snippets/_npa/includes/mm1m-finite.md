\ifndef{mm1mFinite}
\define{mm1mFinite}

\section{Finite Buffer: $M/M/1/m$}

\notes{In $M/M/1$ the buffer is unbounded. A restricted buffer of $m-1$ waiting customers, plus one in service, caps occupancy at $m$. Kendall writes this $M/M/1/m$. Arrivals that find $k=m$ are *lost* and are assumed not to return, so carried load is strictly less than offered load.}

\figure{\includepng{\diagramsDir/npa/stateMM1m}{75%}}{State diagram for $M/M/1/m$: the chain stops at $m$; there is no transition $m\to m+1$.}{mm1m-state-diagram}

\figure{\includepng{\diagramsDir/npa/boundaryFlowMM1}{45%}}{Interior boundary flow is the same as $M/M/1$: $\lambda P(k-1)=\mu P(k)$.}{mm1m-boundary-flow}

\notes{For $1\le k\le m$ the rates are those of $M/M/1$, so detailed balance is unchanged,
$$
\lambda P(k-1)=\mu P(k)\qquad\Rightarrow\qquad P(k)=\rho^k P(0),\quad\rho=\frac{\lambda}{\mu}.
$$
Normalisation now runs over only $m+1$ states,
$$
\sum_{k=0}^{m}P(k)=P(0)\sum_{k=0}^{m}\rho^k=1.
$$
The inner sum is a finite geometric series,
$$
\sum_{k=0}^{m}\rho^k=\frac{1-\rho^{m+1}}{1-\rho}\quad(\rho\neq 1),
$$
so
$$
P(0)=\frac{1-\rho}{1-\rho^{m+1}},\qquad P(k)=\frac{\rho^k(1-\rho)}{1-\rho^{m+1}}.
$$
(If $\rho=1$ the $m+1$ states are equally likely and $P(k)=1/(m+1)$.) Unlike $M/M/1$, a steady state exists for every $\rho$, including $\rho\ge 1$: the finite buffer cannot grow without bound.}

\subsection{Blocking Probability}

\notes{An arrival is lost exactly when the system is full. PASTA (Poisson arrivals see time averages) gives the blocking probability as the occupancy of the last state,
$$
P(m)=\frac{\rho^m(1-\rho)}{1-\rho^{m+1}}.
$$
That is the fraction of offered traffic that is rejected.}

\slides{* $M/M/1/m$: cap at $m$ customers, lost arrivals do not return
* Same $\rho^k$ shape, truncated geometric $P(0)=(1-\rho)/(1-\rho^{m+1})$
* Blocking $P(m)$; steady state exists even for $\rho\ge 1$}

\endif

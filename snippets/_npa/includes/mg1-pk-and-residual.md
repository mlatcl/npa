\ifndef{mg1PkAndResidual}
\define{mg1PkAndResidual}

\section{$M/G/1$ and Pollaczek--Khinchin}

\notes{If service times are *generally* distributed we cannot use a birth-death process. The tool is mean residual service time, and it yields the Pollaczek--Khinchin formula: expected wait for any service-time distribution with finite variance,
$$
\bar{W}=\frac{\lambda\langle X^2\rangle}{2(1-\rho)},
$$
where $\rho=\lambda\bar{X}$ and $\bar{X}=\langle X\rangle$.}

\slides{* General service: no birth-death chain
* Residual service time $\bar{R}$
* Pollaczek--Khinchin: $\bar{W}=\lambda\langle X^2\rangle/(2(1-\rho))$}

\subsection{Assumptions}

\notes{The derivation uses three assumptions. The queue is FIFO. Arrival times are statistically independent of service times. Service times have finite variance. (The notes originally wrote ``arrival-time variance''; the 2005 paper, and the residual-time argument itself, require finite *service-time* variance.)}

\notes{Mean residual service time $\bar{R}$ is the leftover service seen by an arrival. Under those assumptions
$$
\bar{W}=\frac{\bar{R}}{1-\rho}.
$$
The rest of the argument is an expression for $\bar{R}$.}

\slides{* FIFO; arrivals independent of service; finite $\mathrm{Var}(X)$
* $\bar{W}=\bar{R}/(1-\rho)$}

\subsection{Residual Time from Completions}

\figure{\includepng{\diagramsDir/npa/residualTime}{80%}}{Residual service time over a busy period: a sawtooth of triangles with sides $X_i$. $M(t)$ is the number of completions in $[0,t]$.}{mg1-residual-graphical}

\notes{The area under the residual-time curve up to $t$ is
$$
A(t)=\frac12\sum_{i=1}^{M(t)}X_i^2.
$$
The time average is
$$
\frac{A(t)}{t}=\frac12\frac{M(t)}{t}\frac{\sum_{i=1}^{M(t)}X_i^2}{M(t)}.
$$
As $t\to\infty$, $M(t)/t\to\lambda$ and the sample second moment converges (finite variance), so
$$
\bar{R}=\frac12\lambda\langle X^2\rangle.
$$
Substitute into $\bar{W}=\bar{R}/(1-\rho)$ to recover Pollaczek--Khinchin. Sojourn time is then $\bar{T}=\bar{X}+\bar{W}$, and Little gives $\bar{N}_Q=\lambda\bar{W}$ and $\bar{N}=\lambda\bar{T}$. This derivation was Question 1 of the 2002--03 paper.}

\slides{* $A(t)=\frac12\sum X_i^2$
* $\bar{R}=\frac12\lambda\langle X^2\rangle$
* $\bar{T}=\bar{X}+\bar{W}$; Little for $\bar{N}_Q$, $\bar{N}$}

\subsection{Residual Time from an Arrival}

\figure{\includepng{\diagramsDir/npa/residualServiceOverview}{75%}}{The $i$th arrival sees residual $R_i$ on the customer in service and waiting times $X$ for each of the $k_i-1$ customers already queued.}{mg1-residual-arrival}

\notes{Write $W_i$ for the wait of the $i$th customer, $R_i$ for the residual it sees, $X_i$ for its own service, and $k_i$ for the occupancy on arrival. Then
$$
W_i=R_i+\sum_{j=1}^{k_i-1}X_{(j)}.
$$
Average over the first $I$ arrivals and let $I\to\infty$. Time averages equal steady-state means, and independence of the $i$th arrival from the work already present, together with Little on the queue, recover $\bar{W}=\bar{R}/(1-\rho)$.}

\slides{* $W_i=R_i+$ work already present
* Independence + Little $\Rightarrow$ $\bar{W}=\bar{R}/(1-\rho)$}

\endif

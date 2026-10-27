\ifndef{erlangLossModel}
\define{erlangLossModel}

\section{Erlang Loss: $M/M/m/m$}

\notes{Erlang delay holds overflowing customers. Erlang *loss* does not: if all $m$ servers are busy the arrival is rejected. Kendall writes $M/M/m/m$ --- $m$ servers and system capacity $m$, so the waiting line has length zero. Offered load is still $a=\lambda/\mu$, but carried load $a'$ is smaller because some traffic is blocked, as in $M/M/1/m$.}

\figure{\includepng{\diagramsDir/npa/erlangLossFlowChart}{70%}}{Flow chart of the Erlang loss system: offered load $a$ in, carried load $a'<a$ out.}{erlang-loss-flowchart}

\figure{\includepng{\diagramsDir/npa/erlangLoss}{85%}}{Markov chain for $M/M/m/m$: the chain stops at $m$; there is no queueing state.}{erlang-loss-state}

\notes{Birth-death rates are
$$
\lambda_k=\begin{cases}
\lambda & 0\le k<m,\\
0 & k\ge m,
\end{cases}
\qquad
\mu_k=k\mu\quad(1\le k\le m).
$$
The value of $\mu_k$ for $k>m$ is irrelevant: those states are unreachable.}

\subsection{Truncated Poisson}

\notes{Interior detailed balance is the $M/M/\infty$ relation,
$$
\lambda P(k-1)=k\mu P(k)\qquad\Rightarrow\qquad P(k)=\frac{a}{k}P(k-1)=\frac{a^k}{k!}P(0).
$$
There is no $k>m$ region to match. Normalisation over $k=0,\ldots,m$ produces the *truncated Poisson*
$$
P(0)=\left(\sum_{n=0}^{m}\frac{a^n}{n!}\right)^{-1},\qquad
P(k)=\frac{a^k/k!}{\sum_{n=0}^{m}a^n/n!}.
$$
As $m\to\infty$ this recovers $M/M/\infty$, as it must.}

\figure{\includepng{\diagramsDir/npa/boundaryFlowMMinf}{45%}}{Boundary flow for $k\le m$: $\lambda P(k-1)=k\mu P(k)$.}{erlang-loss-boundary}

\slides{* $M/M/m/m$: $m$ servers, no waiting line, blocked arrivals lost
* Same $\lambda P(k-1)=k\mu P(k)$ as $M/M/\infty$, truncated at $m$
* Occupancy is truncated Poisson}

\endif

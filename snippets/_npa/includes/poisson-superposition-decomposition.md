\ifndef{poissonSuperpositionDecomposition}
\define{poissonSuperpositionDecomposition}

\section{Properties of the Poisson Process}

\notes{In the next chapter we will derive the Poisson process from assumptions about arrivals. For now, five properties.}

\slidesincremental{
* Superposition of independent Poisson processes
* Decomposition of a Poisson flow
* Independence of arrivals in disjoint intervals
* Identical distributions on intervals of equal length
* Interarrival times are exponential
}

\subsection{Superposition}

\notes{If $N$ independent Poisson processes with rates $\lambda_1,\dots,\lambda_N$ are combined, the result is Poisson with rate $\lambda=\sum_n\lambda_n$. Two variables are independent when $P(x,y)=P(x)P(y)$.}

\figure{\includepng{\diagramsDir/npa/sumPoisson}{55%}}{Independent Poisson processes merged into one flow yield a Poisson process whose rate is the sum of the input rates.}{poisson-superposition}

\subsection{Decomposition}

\notes{The converse also holds. A Poisson process of rate $\lambda$ is split onto $N$ output channels, each arrival independently assigned to channel $n$ with probability $P(n)$. Then channel $n$ is Poisson with rate $\lambda_n=P(n)\lambda$.}

\figure{\includepng{\diagramsDir/npa/decomposePoisson}{70%}}{A Poisson process of rate $\lambda$ independently switched onto output $n$ with probability $P(n)=\lambda_n/\lambda$ yields Poisson outputs of rates $\lambda_n$.}{poisson-decomposition}

\subsection{Independence of Arrivals}

\notes{On two *disjoint* time intervals the numbers of arrivals $k_1$ and $k_2$ are independent: $P(k_1,k_2)=P(k_1)P(k_2)$.}

\subsection{Identical Intervals}

\notes{For a single rate $\lambda$, the number of arrivals in $(s,s+t]$ has the same distribution as the number in $(r,r+t]$ on an independent copy of the process.}

\endif

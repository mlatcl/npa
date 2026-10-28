\ifndef{npaGenNotesMg1}
\define{npaGenNotesMg1}

\notes{\section{Pollaczek-Khinchin formula}}

\notes{The Pollaczek-Khinchin formula is given as
$$
\ensuremath{\bar{W}}=\ensuremath{\frac{\lambda\left\langle X^{2}\right\rangle }{2(1-\rho)}}$$where $\ensuremath{\bar{W}}$ is expected waiting time,$\left\langle X^{2}\right\rangle =\left\langle X^{2}\right\rangle _{p(X)}$ is the second moment under the service time distribution, the utilisation factor is given as $\ensuremath{\rho}=\ensuremath{\lambda\bar{X}}$ and $\ensuremath{\bar{X}}=\left\langle X\right\rangle _{p(X)}$ is the mean under the service time distribution.}

\notes{\section{Proof of Pollaczek-Khinchin Formula}}

\notes{In the examples, we review the first part of a simple proof of the Pollaczek-Khinchin formula. In our proof we will make three assumptions:}

\notes{1. The queue is FIFO queue, *i.e.*customers are served in the order they arrive. This assumption may be relaxed but it will simplify our proof.
2. The arrival times are statistically independent of the service times.
3. The arrival time distribution has a variance which is finite.}

\notes{To formulate the proof we introduce a concept known as the mean residual service time, $\ensuremath{\bar{R}}$. We show that the average waiting time is related to the mean residual service time as follows: $$
\ensuremath{\bar{W}}=\ensuremath{\frac{\bar{R}}{1-\rho}\label{eqn:arrivals}}$$ We now have the average queueing time in terms of the mean residual service time. To complete the Pollaczek-Khinchin formula we simply need to calculate $\ensuremath{\bar{R}}$.}

\notes{\section{Residual Service Time from Departures Perspective}}

\notes{We again turn to a graphical proof to obtain the value of the mean residual service time. In Figure\  \ref{cap:meanResidualGraphical} we present a plot of the residual service time over time.}

\figure{\includepng{\diagramsDir/npa/residualTime}{100%}}{Graphical computation of mean residual time. $M\left(t\right)$ is the number of service completions in the interval $[0,\, t]$.}{cap:meanResidualGraphical}

\notes{The time average of the mean residual service time can then be calculated in terms of the area under the curve, $A\left(t\right)$, which is given by the area under each of the triangles,
$$
A(t)=1\sum_{i=1}^{M(t)}X_{i}^{2}.$$ The average service time is the area divided by time, $t$, $$
\begin{aligned}
\ensuremath{\frac{A(t)}{t}} & = & \ensuremath{\frac{M(t)}{t}\frac{A(t)}{M(t)}\\}
 & = & 1\ensuremath{\frac{M(t)}{t}\frac{\sum_{i=1}^{M(t)}X_{i}^{2}}{M(t)}}.
\end{aligned}
$$where we have introduced the number of arrivals after time $t$, as $M\left(t\right)$. As $t\ensuremath{\rightarrow\infty}$, if the variance of the service time distribution is finite, we find that$$
\ensuremath{\bar{R}}=1\ensuremath{\lambda\left\langle} X^{2}\right\rangle .$$ Again, assuming that time averages and ensemble averages are equal, we substitute back into (\ref{eqn:arrivals}) to obtain the Pollaczek-Khinchin formula $$
\ensuremath{\bar{W}}=\ensuremath{\frac{\lambda\left\langle X^{2}\right\rangle }{2(1-\rho)}}.$$This implies that the total waiting time in the system is $$
\ensuremath{\bar{T}}=\ensuremath{\bar{X}}+\ensuremath{\frac{\lambda\left\langle X^{2}\right\rangle }{2(1-\rho)}}$$ and through Little's formula we can obtain the expected queue length, $\ensuremath{\bar{N}_{Q}}$, and the expected number in the system, $\ensuremath{\bar{N}}$. **Note that derivation of this formula was Question 1 in the 2002-2003 paper**. Now consider Examples\  \ref{example:MarkovService},\  \ref{example:DeterministicService}  and\  \ref{example:uniformService} at the end of this chapter for the use of the Pollaczek-Khinchin formula.}

\notes{\subsection{Table of Delays and Average Numbers in System}}

\notes{In the table below we summarise average waiting times and various other characteristics of the systems for the Pollaczek-Khinchin formula.}

\notes{| Expected value | General | Exponential | Deterministic |
| --- | --- | --- | --- |
| $\ensuremath{\bar{W}}$ | $\ensuremath{\frac{\lambda}{2(1-\rho)}\left\langle} X^{2}\right\rangle$ | $\ensuremath{\frac{\rho}{\mu(1-\rho)}}$ | $\ensuremath{\frac{\rho}{2\mu(1-\rho)}}$ |
| $\ensuremath{\bar{T}}=\ensuremath{\bar{W}}+\ensuremath{\frac{1}{\mu}}$ | $\ensuremath{\frac{\lambda}{2(1-\rho)}\left\langle} X^{2}\right\rangle +\ensuremath{\frac{1}{\mu}}$ | $\ensuremath{\frac{1}{\mu(1-\rho)}}$ | $\ensuremath{\frac{2-\rho}{2\mu(1-\rho)}}$ |
| $\ensuremath{\bar{N_{Q}}}=\ensuremath{\lambda\bar{W}}$ | $\ensuremath{\frac{\lambda^{2}}{2(1-\rho)}\left\langle} X^{2}\right\rangle$ | $\ensuremath{\frac{\rho^{2}}{(1-\rho)}}$ | $\ensuremath{\frac{\rho^{2}}{2(1-\rho)}}$ |
| $\ensuremath{\bar{N}}=\ensuremath{\lambda\bar{W}}+\ensuremath{\rho}=$ | $\ensuremath{\frac{\lambda^{2}}{2(1-\rho)}\left\langle} X^{2}\right\rangle +\ensuremath{\rho}$ | $\ensuremath{\frac{\rho}{1-\rho}}$ | $\ensuremath{\frac{\rho(2-\rho)}{2(1-\rho)}}$ |}

\endif

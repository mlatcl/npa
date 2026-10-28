\ifndef{npaGenNotesMg1}
\define{npaGenNotesMg1}

\notes{\section{Pollaczek-Khinchin formula}}

\notes{The Pollaczek-Khinchin formula is given as
$$
\bar{W}=\frac{\lambda\left\langle X^{2}\right\rangle }{2(1-\rho)}$$where $\bar{W}$ is expected waiting time,$\left\langle X^{2}\right\rangle =\left\langle X^{2}\right\rangle _{p(X)}$ is the second moment under the service time distribution, the utilisation factor is given as $\rho=\lambda\bar{X}$ and $\bar{X}=\left\langle X\right\rangle _{p(X)}$ is the mean under the service time distribution.}

\notes{\section{Proof of Pollaczek-Khinchin Formula}}

\notes{In the examples, we review the first part of a simple proof of the Pollaczek-Khinchin formula. In our proof we will make three assumptions:}

\notes{1. The queue is FIFO queue, *i.e.*customers are served in the order they arrive. This assumption may be relaxed but it will simplify our proof.
2. The arrival times are statistically independent of the service times.
3. The arrival time distribution has a variance which is finite.}

\notes{To formulate the proof we introduce a concept known as the mean residual service time, $\bar{R}$. We show that the average waiting time is related to the mean residual service time as follows: \begin{equation}
\bar{W}=\frac{\bar{R}}{1-\rho}\label{eqn:arrivals}\end{equation} We now have the average queueing time in terms of the mean residual service time. To complete the Pollaczek-Khinchin formula we simply need to calculate $\bar{R}$.}

\notes{\section{Residual Service Time from Departures Perspective}}

\notes{We again turn to a graphical proof to obtain the value of the mean residual service time. In Figure\  \ref{cap:meanResidualGraphical} we present a plot of the residual service time over time.}

\figure{\includepng{\diagramsDir/npa/residualTime}{100%}}{Graphical computation of mean residual time. $M\left(t\right)$ is the number of service completions in the interval $[0,\, t]$.}{cap:meanResidualGraphical}

\notes{The time average of the mean residual service time can then be calculated in terms of the area under the curve, $A\left(t\right)$, which is given by the area under each of the triangles,
$$
A(t)=\frac{1}{2}\sum_{i=1}^{M(t)}X_{i}^{2}.$$ The average service time is the area divided by time, $t$, \begin{eqnarray*}
\frac{A(t)}{t} & = & \frac{M(t)}{t}\frac{A(t)}{M(t)}\\
 & = & \frac{1}{2}\frac{M(t)}{t}\frac{\sum_{i=1}^{M(t)}X_{i}^{2}}{M(t)}.\end{eqnarray*}where we have introduced the number of arrivals after time $t$, as $M\left(t\right)$. As $t\rightarrow\infty$, if the variance of the service time distribution is finite, we find that$$
\bar{R}=\frac{1}{2}\lambda\left\langle X^{2}\right\rangle .$$ Again, assuming that time averages and ensemble averages are equal, we substitute back into (\ref{eqn:arrivals}) to obtain the Pollaczek-Khinchin formula $$
\bar{W}=\frac{\lambda\left\langle X^{2}\right\rangle }{2(1-\rho)}.$$This implies that the total waiting time in the system is $$
\bar{T}=\bar{X}+\frac{\lambda\left\langle X^{2}\right\rangle }{2(1-\rho)}$$ and through Little's formula we can obtain the expected queue length, $\bar{N}_{Q}$, and the expected number in the system, $\bar{N}$. **Note that derivation of this formula was Question 1 in the 2002-2003 paper**. Now consider Examples\  \ref{example:MarkovService},\  \ref{example:DeterministicService}  and\  \ref{example:uniformService} at the end of this chapter for the use of the Pollaczek-Khinchin formula.}

\notes{\subsection{Table of Delays and Average Numbers in System}}

\notes{In the table below we summarise average waiting times and various other characteristics of the systems for the Pollaczek-Khinchin formula.}

\notes{| Expected value | General | Exponential | Deterministic |
| --- | --- | --- | --- |
| $\bar{W}$ | $\frac{\lambda}{2(1-\rho)}\left\langle X^{2}\right\rangle $ | $\frac{\rho}{\mu(1-\rho)}$ | $\frac{\rho}{2\mu(1-\rho)}$ |
| $\bar{T}=\bar{W}+\frac{1}{\mu}$ | $\frac{\lambda}{2(1-\rho)}\left\langle X^{2}\right\rangle +\frac{1}{\mu}$ | $\frac{1}{\mu(1-\rho)}$ | $\frac{2-\rho}{2\mu(1-\rho)}$ |
| $\bar{N_{Q}}=\lambda\bar{W}$ | $\frac{\lambda^{2}}{2(1-\rho)}\left\langle X^{2}\right\rangle $ | $\frac{\rho^{2}}{(1-\rho)}$ | $\frac{\rho^{2}}{2(1-\rho)}$ |
| $\bar{N}=\lambda\bar{W}+\rho=$ | $\frac{\lambda^{2}}{2(1-\rho)}\left\langle X^{2}\right\rangle +\rho$ | $\frac{\rho}{1-\rho}$ | $\frac{\rho(2-\rho)}{2(1-\rho)}$ |}

\endif

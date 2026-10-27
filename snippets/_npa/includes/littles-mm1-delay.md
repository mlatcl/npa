\ifndef{littlesMm1Delay}
\define{littlesMm1Delay}

\section{Average Delay in $M/M/1$}

\notes{For $M/M/1$ we already have $\bar{N}=\rho/(1-\rho)=\lambda/(\mu-\lambda)$. Little's formula converts that into mean sojourn time,
$$
\bar{T}=\frac{\bar{N}}{\lambda}=\frac{1}{\mu-\lambda}.
$$
This is time in the *system*, queueing plus transmission, not waiting time alone.}

\slides{* $\bar{N}=\rho/(1-\rho)$ from last lecture
* $\bar{T}=1/(\mu-\lambda)$
* Includes transmission, not only waiting}

\subsection{Queueing Time and Transmission Time}

\notes{Packet delay splits as $T=X+W$, transmission plus waiting, so $\bar{T}=\bar{X}+\bar{W}$. Little's formula applies to each piece separately.}

\notes{Arrivals at the server equal arrivals at the queue if nothing is dropped. The mean number in service is the utilisation $\rho$, and
$$
\rho=\lambda\bar{X}.
$$
For exponential service $\bar{X}=1/\mu$, so $\rho=\lambda/\mu$ as before. Utilisation is the fraction of time the server is busy, which is also $1-P(0)$. For a packet of $L$ bits on a line of $C$ bits per second, $X=L/C$.}

\notes{For the waiting line,
$$
\bar{N}_Q=\lambda\bar{W}.
$$
With $\bar{T}=\bar{X}+\bar{W}=1/\mu+\bar{W}$ we obtain
$$
\bar{W}=\frac{\rho}{\mu-\lambda},\qquad \bar{N}_Q=\frac{\rho^2}{1-\rho}.
$$}

\slides{* $T=X+W$, $\rho=\lambda\bar{X}=1-P(0)$
* $\bar{W}=\rho/(\mu-\lambda)$
* $\bar{N}_Q=\rho^2/(1-\rho)$}

\section{Graphical Argument}

\notes{Sketch arrivals $\alpha(\tau)$ and departures $\beta(\tau)$ against time. The area between the curves is both $\int_0^t N(\tau)\,d\tau$ and $\sum_{i=1}^{\alpha(t)} T_i$. Divide by $t$:
$$
\bar{N}_t=\bar{\lambda}_t\bar{T}_t.
$$
If a steady state exists, the $t\to\infty$ limit is $\bar{N}=\lambda\bar{T}$.}

\figure{\includepng{\diagramsDir/npa/littlesFormula}{70%}}{Arrivals $\alpha(\tau)$ and departures $\beta(\tau)$. The shaded area is both the integral of occupancy and the sum of sojourn times.}{littles-formula-graph}

\subsection{A Bar Queue}

\notes{The bartender spends 10 percent of her time cleaning between customers, so $\rho=0.9$. Typically three people are waiting, $\bar{N}_Q=3$. Then $\lambda=0.9/\bar{X}$ and $3=\lambda\bar{W}$, so $\bar{W}/\bar{X}=3/0.9=10/3$: waiting time is a little more than three times service time.}

\slides{* Area argument: $\int N=\sum T_i$ $\Rightarrow$ $\bar{N}_t=\bar{\lambda}_t\bar{T}_t$
* Bar: $\rho=0.9$, $\bar{N}_Q=3$ $\Rightarrow$ $\bar{W}/\bar{X}=10/3$}

\endif

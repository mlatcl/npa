\ifndef{littlesFormulaStatement}
\define{littlesFormulaStatement}

\section{Time Averages}

\notes{Birth-death analysis gave the mean number in the system. Quality of service asks for mean *delay*, and for the mean number waiting rather than the mean number in service. Little's formula relates those quantities. It applies to $G/G/1$ queues, not only to $M/M/1$, once the system is in steady state.}

\notes{Write $N(t)$ for occupancy as a function of time. The time average up to $t$ is
$$
\bar{N}_t=\frac{1}{t}\int_0^t N(\tau)\,d\tau,
$$
and we assume that the steady-state mean $\langle k\rangle$ equals $\lim_{t\to\infty}\bar{N}_t$ [@Bertsekas:data92, p.~156--157].}

\slides{* Time average $\bar{N}_t=(1/t)\int_0^t N(\tau)\,d\tau$
* Steady state: $\langle k\rangle=\lim_{t\to\infty}\bar{N}_t$
* Little applies to $G/G/1$ in steady state}

\section{Little's Formula}

\notes{Under that identification,
$$
\bar{N}=\lambda\bar{T}:
$$
mean number in the system equals arrival rate times mean delay.}

\subsection{A Nightclub Queue}

\notes{On Thursday nights the queue typically holds 20 people, and people arrive at 40 per hour. Little's formula gives
$$
\bar{T}=\frac{\bar{N}}{\lambda}=\frac{20}{40}=\tfrac{1}{2}\text{ hour}.
$$
If twenty people are waiting and they enter at forty per hour, half an hour is the wait one should expect. The formula does not use the arrival or service *distributions*, only steady state. It can be applied to the whole system or to a subsystem (the waiting line, or the server).}

\slides{* $\bar{N}=\lambda\bar{T}$
* Nightclub: $\bar{N}=20$, $\lambda=40\,\mathrm{h}^{-1}$ $\Rightarrow$ $\bar{T}=1/2$ hour
* Distribution-free; needs steady state}

\endif

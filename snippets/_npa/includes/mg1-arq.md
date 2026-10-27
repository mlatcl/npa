\ifndef{mg1Arq}
\define{mg1Arq}

\section{Automatic Repeat Request}

\notes{$M/G/1$ is a modelling tool, not only a formula. Bertsekas and Gallager's ARQ example (Example 3.15) is a stop-and-wait retransmission protocol as a general service time.}

\figure{\includepng{\diagramsDir/npa/ARQ}{70%}}{ARQ: transmit a packet, wait up to $n-1$ milliseconds for an acknowledgement, retransmit on timeout.}{mg1-arq}

\notes{Assumptions: each packet takes $1$ millisecond to send; the system waits at most $n-1$ milliseconds for an ack, then retransmits; an ack arrives if and only if the packet is received without error; packet errors occur independently with probability $p$; arrivals are Poisson at rate $\lambda$. Independence of errors is the weak one: a bad channel typically clusters errors.}

\notes{The interval from the start of a given packet's first transmission to the end of its successful transmission is $1+kn$ milliseconds with probability $(1-p)p^k$ --- $k$ failures and one success, a geometric:
$$
P(X=1+kn)=(1-p)p^k.
$$
The mean is
$$
\langle X\rangle=\sum_{k=0}^{\infty}(1+kn)(1-p)p^k=1+n\frac{p}{1-p},
$$
using $\sum p^k=1/(1-p)$ and $\sum kp^k=p/(1-p)^2$. The busy factor
$$
\rho=\lambda\langle X\rangle=\lambda+\lambda n\frac{p}{1-p}
$$
must still be less than one. As $p\to 1$ the second term diverges. Calling $\rho$ utilisation is slightly misleading: much of the ``busy'' time is waiting for an ack, not occupying the channel.}

\notes{The second moment is
$$
\langle X^2\rangle=1+\frac{2np}{1-p}+\frac{n^2(p+p^2)}{(1-p)^2},
$$
using $\sum k^2 p^k=(p+p^2)/(1-p)^3$. Pollaczek--Khinchin then gives the wait. This is Question 3 of the 2004--05 paper.}

\slides{* ARQ as $M/G/1$: geometric retransmission time
* $P(X=1+kn)=(1-p)p^k$, $\langle X\rangle=1+np/(1-p)$
* Independence of errors is the fragile assumption}

\endif

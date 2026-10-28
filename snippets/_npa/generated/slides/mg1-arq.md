\ifndef{npaGenSlidesMg1Arq}
\define{npaGenSlidesMg1Arq}

\newslide{Automatic Repeat Request (ARQ) System.}

\slides{* The $M/G/1$ queue system can be used for modelling various systems of interest.
* In an ARQ system packets are transmitted and the system waits for an acknowledgement.}

\newslide{Automatic Repeat Request (ARQ) System. (continued)}

\slides{* If no acknowledgement is received the system retransmits.
* In this section we review Example\  3.15 from Bertsekas and Gallager.
* A schematic of the system is given in Figure\  \ref{cap:ARQschemeatic}.}

\newslide{ARQ Schematic}

\slides{\figure{\includepng{\diagramsDir/npa/ARQ}{80%}}{The ARQ System.}{cap:ARQschemeatic}}

\newslide{ARQ Schematic (continued)}

\slides{* For the purposes of this analysis, we will assume
* That each packet takes 1 millisecond to be transmitted.
* The system waits a maximum of $n-1$ milliseconds for an acknowledgement. If there is no acknowledgement the system retransmits.
* The acknowledgement occurs if the packet is received without errors. Otherwise acknowledgement doesn't occur.
* The probability of an error in a packet is taken to be $p$ and we take errors to occur independently.
* Assume that packets arrive as a Poisson process with rate $\ensuremath{\lambda}$.}

\newslide{ARQ Contd}

\slides{* In practice, the fourth assumption is probably unrealistic (independence of errors).
* If an error occurs due to problems in the transmission channel, it is likely that several packets in a row will not be received, so the errors do not occur independently.}

\newslide{ARQ Contd (continued)}

\slides{* The time interval between transmission and re-transmission will be $1+kn$ milliseconds with probability $\left(1-p\right)p^{k}$.
* This time interval is associated with $k$ retransmissions and one successful transmission.
* The probability of this being the service time is given by$$
P\left(X=1+kn\right)=\left(1-p\right)p^{k}$$which is recognised as a geometric distribution.}

\newslide{Average Service Time}

\slides{* Using this distribution we can compute the expected service time which is given by

| \left\langle X\right\rangle | = | \sum_{k=0}^{\ensuremath{\infty}}\left(1+kn\right)\left(1-p\right)p^{k} |
| --- | --- | --- |
|  | = | \left(1-p\right)\left(\sum_{k=0}^{\ensuremath{\infty}}p^{k}+n\sum_{k=0}^{\ensuremath{\infty}}kp^{k}\right) |
|  | = | 1+n\ensuremath{\frac{p}{1-p}} since $\sum_{k=0}^{\ensuremath{\infty}}p^{k}=\ensuremath{\frac{1}{1-p}}$ and $\sum_{k=0}^{\ensuremath{\infty}}kp^{k}=\ensuremath{\frac{p}{\left(1-p\right)^{2}}}$ . |}

\newslide{ARQ Utilization Factor}

\slides{* We can therefore write the utilization factor, $\ensuremath{\rho}=\ensuremath{\lambda\left\langle} X\right\rangle$, as$$
\ensuremath{\rho}=\ensuremath{\lambda}+\ensuremath{\lambda} n\ensuremath{\frac{p}{1-p}}.$$
* This has to be less than 1.}

\newslide{ARQ Utilization Factor (continued)}

\slides{* Recall that the utilisation factor is $$
\ensuremath{\rho}=1-P\left(0\right).$$
* This implies that $$
P\left(0\right)=1-\ensuremath{\lambda}-\ensuremath{\lambda} n\ensuremath{\frac{p}{1-p}}$$
      Expand on this section --- what use is the utilization factor in this system?}

\newslide{ARQ Second Moment}

\slides{* The second moment of the service time is
\sum_{k=0}^{\ensuremath{\infty}}k^{2}p^{k}=\ensuremath{\frac{p+p^{2}}{\left(1-p\right)^{3}}}$$
* These moments can be used with the Pollaczek-Khinchin formula to obtain statistics for the queue.

| \left\langle X^{2}\right\rangle | = | \sum_{k=0}^{\ensuremath{\infty}}\left(1+kn\right)^{2}\left(1-p\right)p^{k} |
| --- | --- | --- |
|  | = | \left(1-p\right)\left(\sum_{k=0}^{\ensuremath{\infty}}p^{k}+2n\sum_{k=0}^{\ensuremath{\infty}}kp^{k}+n^{2}\sum_{k=0}^{\ensuremath{\infty}}k^{2}p^{k}\right) |
|  | = | 1+\ensuremath{\frac{2np}{1-p}}+\ensuremath{\frac{n^{2}\left(p+p^{2}\right)}{\left(1-p\right)^{2}}}since $$ |}

\newslide{$M/G/1$ Queues with Vacations}

\slides{* Consider a server which, when it is free, attends to some other business. For example it could transmit control and record keeping traffic. These periods are sometimes known as vacations (which is an American word that means holidays). The vacation periods are characterised by
* If a new arrival arrives during a vacation it must wait until the vacation is over before being dealt with.
* If a vacation ends and the server is idle it immediately goes on a new vacation.}

\newslide{$M/G/1$ with Vacations}

\slides{* Example 5 In the Notes
* We denote the length of these successive vacations to be $V_{1}$, $V_{2}$, $\ensuremath{\dots}$. We assume that $V_{1},$$V_{2}$, $\ensuremath{\dots}$ are i.i.d. random variables which are also independent of the customer times and the service times. We can then attempt to compute the mean residual service time for this queue for a *Poisson (Markov) arrival* system with *general service times* and *generally distributed vacation times*.}

\slides{\figure{\includepng{\diagramsDir/npa/vacationMG1}{80%}}{Schematic of $M/G/1$ queue}{vacationMG1}}

\newslide{Residual Service Time}

\slides{\figure{\includepng{\diagramsDir/npa/vacationResidual}{80%}}{Computation of residual service time for system with vacations.}{vacationResidual}}

\newslide{Residual Service Time (continued)}

\slides{* For this system 

| \ensuremath{\frac{1}{t}\int_{0}^{t}}r\left(\tau\right)d\tau | = | \ensuremath{\frac{1}{t}\sum_{i=1}^{M\left(t\right)}}1X_{i}^{2}+\ensuremath{\frac{1}{t}\sum_{i=1}^{L\left(t\right)}}1V_{i}^{2} |
| --- | --- | --- |
|  | = | \ensuremath{\frac{M\left(t\right)}{t}}1\ensuremath{\frac{\sum_{i=1}^{M\left(t\right)}X_{i}^{2}}{M\left(t\right)}}+\ensuremath{\frac{L\left(t\right)}{t}}1\ensuremath{\frac{\sum_{i=1}^{L\left(t\right)}V_{i}^{2}}{L\left(t\right)}}arrival process, $M\left(t\right)$, vacation process, $L\left(t\right)$. |}

\newslide{Average of Vacation Distribution}

\slides{* This means we have to deal with the average number of vacations. On average the proportion of time available for vacations is $\left(1-\ensuremath{\rho\right)}$, *i.e.*that time where the transmission line is not in use.
* If the average length of a vacation at time $t$ is $\ensuremath{\bar{V}_{t}}$ then the number of vacations that will have arrived at that time is $$
L\left(t\right)=\ensuremath{\frac{t\left(1-\rho\right)}{\bar{V}_{t}}}.$$Recalling $$
\ensuremath{\frac{1}{t}\int_{0}^{t}}r\left(\tau\right)d\tau=\ensuremath{\frac{M\left(t\right)}{t}}1\ensuremath{\frac{\sum_{i=1}^{M\left(t\right)}X_{i}^{2}}{M\left(t\right)}}+\ensuremath{\frac{L\left(t\right)}{t}}1\ensuremath{\frac{\sum_{i=1}^{L\left(t\right)}V_{i}^{2}}{L\left(t\right)}}$$
* Taking the limit of as $t\ensuremath{\rightarrow\infty}$ we can write $$
\ensuremath{\bar{R}}=1\ensuremath{\lambda\left\langle} X^{2}\right\rangle +\ensuremath{\frac{\left(1-\rho\right)\left\langle V^{2}\right\rangle }{2\bar{V}}}.$$}

\newslide{P-K Formula}

\slides{* So given that the assumptions that we used to develop the formula $$
\ensuremath{\bar{W}}=\ensuremath{\frac{\bar{R}}{1-\rho}}$$are still valid, we may write$$
\ensuremath{\bar{W}}=\ensuremath{\frac{\lambda\left\langle X^{2}\right\rangle }{2\left(1-\rho\right)}}+\ensuremath{\frac{\left\langle V^{2}\right\rangle }{2\bar{V}}}.$$}

\newslide{$M/G/1$ with Vacations --- Simple example}

\slides{* A bar has Poisson arrivals and one member of staff serving. When there are no customers at the bar, the staff member leaves the bar to check on the kitchen. Assuming these checks are exponentially distributed in length, with mean $\ensuremath{\bar{V}}$ and that customer service times are exponentially distributed with mean $\ensuremath{\bar{X}}$ what is the average waiting time in the queue?
  Exponential standard deviation = $\ensuremath{\frac{1}{\mu}}$, mean$=\ensuremath{\frac{1}{\mu}}$. So if mean is $\ensuremath{\bar{V}}$, standard deviation is $\ensuremath{\bar{V}}$ and variance is $\ensuremath{\bar{V}^{2}}$. Thus second moment is $\left\langle V^{2}\right\rangle =2\ensuremath{\bar{V}^{2}}$. Similarly for second moment of service time $\left\langle X^{2}\right\rangle =2\ensuremath{\bar{X}^{2}}$. Defining $\ensuremath{\rho}=\ensuremath{\lambda\bar{X}}$ we have $$
\ensuremath{\bar{W}}=\ensuremath{\frac{\lambda\bar{X}}{\left(1-\rho\right)}}+\ensuremath{\bar{V}}=\ensuremath{\frac{\rho}{\left(1-\rho\right)}}+\ensuremath{\bar{V}}.$$Deterministic vacations would have lead to $$
\ensuremath{\bar{W}}=\ensuremath{\frac{\lambda\bar{X}}{\left(1-\rho\right)}}+\ensuremath{\bar{V}}=\ensuremath{\frac{\rho}{\left(1-\rho\right)}}+\ensuremath{\bar{V}}.$$}

\endif

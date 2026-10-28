% generated — do not edit; scripts/convert/run.py
\ifndef{npaGenSlidesLittlesFormula}
\define{npaGenSlidesLittlesFormula}

<!-- original A4 foil 94: Little's Formula -->

\newslide{Little's Formula}

\slides{* Important quality of service issue is the average delay.
* We would also like to be able to compute
* the average number in the queue and
* the average time spent queueing.
* We introduce Little's formula, a very general formula.}

<!-- original A4 foil 94: Little's Formula -->

\newslide{Little's Formula (continued)}

\slides{* Can be applied to $G/G/1$ queues.
* Gives the relationship between
* Steady-state average size of a queue, $\bar{N}$.
* The steady-state arrival rate, $\lambda$.
* The steady-state customer delay, $\bar{T}$.}

<!-- original A4 foil 95: Time and Steady State Averages -->

\newslide{Time and Steady State Averages}

\slides{* We have already introduced the distribution means and sample based means.
* Time based averages are a further type of average.
* The time average is the average value of a particular function over time.$$
\bar{f}_{t}=\frac{1}{t}\int_{0}^{t}f\left(\tau\right)d\tau.$$}

<!-- original A4 foil 96: Time and Steady State Averages II -->

\newslide{Time and Steady State Averages II}

\slides{* The derivation of Little's formula relies on an assumption.
* Assume that averages under the steady state distribution are equivalent to the time average in the limit as $t\rightarrow\infty$,
* Average number in the system as a function of time is given by $$
\bar{N}_{t}=\frac{1}{t}\int_{0}^{t}N\left(\tau\right)d\tau$$and the time average after in the limit as $t\rightarrow\infty$ is given by $$
\bar{N}=\lim_{t\rightarrow\infty}\bar{N}\left(t\right).$$which we assume is equivalent to $\left\langle k\right\rangle _{p\left(k\right)}\equiv\bar{N}$. See pg 156-157 in [@Bertsekas:data92].}

<!-- original A4 foil 97: The Formula -->

\newslide{The Formula}

\slides{* Applies under steady state conditions.
* Under the steady state assumptions it states,$$
\bar{N}=\lambda\bar{T}.$$}

<!-- original A4 foil 97: The Formula -->

\newslide{The Formula (continued)}

\slides{* **Example**: Nightclub queue.
You are driving past a nightclub, wondering how long you will have to wait to go in. You notice on Thursday nights that the queue typically contains 20 people and that people arrive at a rate of 40 per hour.
According to Little's formula, how long would you expect to have to wait to get in?
**Answer**}

<!-- original A4 foil 98: Intuition -->

\newslide{Intuition}

\slides{* If we see there are twenty people in a queue and they enter a building at a rate of 40 per hour, we might expect to have to wait half-an-hour in the queue. Formally though, we will build upon the intuition with a simple graphical `proof' of the formula based upon that given in [@Bertsekas:data92].}

<!-- original A4 foil 99: Graphical Proof I -->

\newslide{Graphical Proof I}

\figure{\includepng{\diagramsDir/npa/littlesFormula}{80%}}{Graphical `proof' of Little's formula.}{cap:littlesGraphical}

<!-- original A4 foil 99: Graphical Proof I -->

\newslide{Graphical Proof I (continued)}

\slides{* Example 1, Chapter 7. Graphical Proof of Little's Formula.
* Sketch two curves vs time: the number of arrivals ($\alpha\left(\tau\right)$) and the number of departures ($\beta\left(\tau\right)$) .
* Also plot $N\left(t\right)$ the number in the queue as function of time.
* By looking at Figure\  \ref{cap:littlesGraphical} we note that the area between the lines in the top figure can be expressed as both $\int_{0}^{t}N(\tau)d\tau$ and $\sum_{i=1}^{\alpha\left(t\right)}T_{i}$. We may therefore equate these expressions,$$
\int_{0}^{t}N\left(\tau\right)d\tau=\sum_{i=1}^{\alpha(t)}T_{i}.$$
* $$
\int_{0}^{t}N\left(\tau\right)d\tau=\sum_{i=1}^{\alpha(t)}T_{i},$$
    introduce $\alpha\left(t\right)$
    $$
\int_{0}^{t}N\left(\tau\right)d\tau=\sum_{i=1}^{\alpha(t)}T_{i},$$
    introduce $\alpha\left(t\right)$
    $$
\int_{0}^{t}N\left(\tau\right)d\tau=\alpha\left(t\right)\frac{\sum_{i=1}^{\alpha\left(t\right)}T_{i}}{\alpha\left(t\right)}$$
    and divide both sides by $t$,
    $$
\int_{0}^{t}N\left(\tau\right)d\tau=\sum_{i=1}^{\alpha(t)}T_{i},$$
    introduce $\alpha\left(t\right)$
    $$
\int_{0}^{t}N\left(\tau\right)d\tau=\alpha\left(t\right)\frac{\sum_{i=1}^{\alpha\left(t\right)}T_{i}}{\alpha\left(t\right)}$$
    and divide both sides by $t$,
    $$
\frac{1}{t}\int_{0}^{t}N\left(\tau\right)d\tau=\frac{\alpha\left(t\right)}{t}\frac{\sum_{i=1}^{\alpha\left(t\right)}T_{i}}{\alpha\left(t\right)}.$$
    The equation now has the form of three averages.
    $$
\int_{0}^{t}N\left(\tau\right)d\tau=\sum_{i=1}^{\alpha(t)}T_{i},$$
    introduce $\alpha\left(t\right)$
    $$
\int_{0}^{t}N\left(\tau\right)d\tau=\alpha\left(t\right)\frac{\sum_{i=1}^{\alpha\left(t\right)}T_{i}}{\alpha\left(t\right)}$$
    and divide both sides by $t$,
    $$
\frac{1}{t}\int_{0}^{t}N\left(\tau\right)d\tau=\frac{\alpha\left(t\right)}{t}\frac{\sum_{i=1}^{\alpha\left(t\right)}T_{i}}{\alpha\left(t\right)}.$$
    The equation now has the form of three averages.
    $$
\bar{N}_{t}=\frac{1}{t}\int_{0}^{t}N\left(\tau\right).$$
    an average, over time, of the queue length
    $$
\int_{0}^{t}N\left(\tau\right)d\tau=\sum_{i=1}^{\alpha(t)}T_{i},$$
    introduce $\alpha\left(t\right)$
    $$
\int_{0}^{t}N\left(\tau\right)d\tau=\alpha\left(t\right)\frac{\sum_{i=1}^{\alpha\left(t\right)}T_{i}}{\alpha\left(t\right)}$$
    and divide both sides by $t$,
    $$
\frac{1}{t}\int_{0}^{t}N\left(\tau\right)d\tau=\frac{\alpha\left(t\right)}{t}\frac{\sum_{i=1}^{\alpha\left(t\right)}T_{i}}{\alpha\left(t\right)}.$$
    The equation now has the form of three averages.
    $$
\bar{N}_{t}=\frac{1}{t}\int_{0}^{t}N\left(\tau\right).$$
    an average, over time, of the queue length
    $$
\bar{\lambda}_{t}=\frac{\alpha\left(t\right)}{t},$$
    the average of the arrivals over time
    $$
\int_{0}^{t}N\left(\tau\right)d\tau=\sum_{i=1}^{\alpha(t)}T_{i},$$
    introduce $\alpha\left(t\right)$
    $$
\int_{0}^{t}N\left(\tau\right)d\tau=\alpha\left(t\right)\frac{\sum_{i=1}^{\alpha\left(t\right)}T_{i}}{\alpha\left(t\right)}$$
    and divide both sides by $t$,
    $$
\frac{1}{t}\int_{0}^{t}N\left(\tau\right)d\tau=\frac{\alpha\left(t\right)}{t}\frac{\sum_{i=1}^{\alpha\left(t\right)}T_{i}}{\alpha\left(t\right)}.$$
    The equation now has the form of three averages.
    $$
\bar{N}_{t}=\frac{1}{t}\int_{0}^{t}N\left(\tau\right).$$
    an average, over time, of the queue length
    $$
\bar{\lambda}_{t}=\frac{\alpha\left(t\right)}{t},$$
    the average of the arrivals over time
    $$
\bar{T}_{t}=\frac{\sum_{i=1}^{\alpha\left(t\right)}T_{i}}{\alpha\left(t\right)}$$
    the average waiting time
    $$
\int_{0}^{t}N\left(\tau\right)d\tau=\sum_{i=1}^{\alpha(t)}T_{i},$$
    introduce $\alpha\left(t\right)$
    $$
\int_{0}^{t}N\left(\tau\right)d\tau=\alpha\left(t\right)\frac{\sum_{i=1}^{\alpha\left(t\right)}T_{i}}{\alpha\left(t\right)}$$
    and divide both sides by $t$,
    $$
\frac{1}{t}\int_{0}^{t}N\left(\tau\right)d\tau=\frac{\alpha\left(t\right)}{t}\frac{\sum_{i=1}^{\alpha\left(t\right)}T_{i}}{\alpha\left(t\right)}.$$
    The equation now has the form of three averages.
    $$
\bar{N}_{t}=\frac{1}{t}\int_{0}^{t}N\left(\tau\right).$$
    an average, over time, of the queue length
    $$
\bar{\lambda}_{t}=\frac{\alpha\left(t\right)}{t},$$
    the average of the arrivals over time
    $$
\bar{T}_{t}=\frac{\sum_{i=1}^{\alpha\left(t\right)}T_{i}}{\alpha\left(t\right)}$$
    the average waiting time
    $$
\bar{N}_{t}=\bar{\lambda}_{t}\bar{T}_{t}.$$
    taking the limit as $t\rightarrow\infty$}

<!-- original A4 foil 100: Graphical Proof II -->

\newslide{Graphical Proof II}

<!-- original A4 foil 101: Little's Formula Derivation -->

\newslide{Little's Formula Derivation}

<!-- original A4 foil 102: Little's Formula Derivation -->

\newslide{Little's Formula Derivation}

<!-- original A4 foil 103: Little's Formula Derivation -->

\newslide{Little's Formula Derivation}

<!-- original A4 foil 104: Little's Formula Derivation -->

\newslide{Little's Formula Derivation}

<!-- original A4 foil 105: Little's Formula Derivation -->

\newslide{Little's Formula Derivation}

<!-- original A4 foil 106: Little's Formula Derivation -->

\newslide{Little's Formula Derivation}

<!-- original A4 foil 107: Little's Formula Derivation -->

\newslide{Little's Formula Derivation}

<!-- original A4 foil 108: Little's Formula -->

\newslide{Little's Formula}

\slides{* $$
\bar{N}=\lambda\bar{T}$$}

<!-- original A4 foil 108: Little's Formula -->

\newslide{Little's Formula (continued)}

\slides{* Applies regardless of the arrival and service time distributions.
* Relies on the system being in *steady state*.
* Can be used at the level of the system.
* Or the level of the queue.
* Or the level of service.}

<!-- original A4 foil 109: Average Delay in $M/M/1$ -->

\newslide{Average Delay in $M/M/1$}

\slides{* The mean of the steady state distribution for an $M/M/1$ queue is$$
\bar{N}=\frac{\lambda}{\mu-\lambda}=\frac{\rho}{1-\rho}.$$
* Can use Little's formula to tell us the average delay.
* From $\bar{N}=\lambda\bar{T}$ we rearrange to recover $$
\bar{T}=\frac{1}{\mu-\lambda}$$}

<!-- original A4 foil 109: Average Delay in $M/M/1$ -->

\newslide{Average Delay in $M/M/1$ (continued)}

\slides{* This is not the time spent in the queue!
* This is the time spent in the system: it includes* service time.*
* arises from *propagation delay.*
* length of phone call *etc*.}

<!-- original A4 foil 110: Little's Formula for Queueing Time and Transmission Time -->

\newslide{Little's Formula for Queueing Time and Transmission Time}

\slides{* The total delay can be divided into
* queueing time, $W$,}

<!-- original A4 foil 110: Little's Formula for Queueing Time and Transmission Time -->

\newslide{Little's Formula for Queueing Time and Transmission Time (continued)}

\slides{* and service time $X$. $$
T=X+W.$$
* Similarly the average delay may be decomposed as$$
\bar{T}=\bar{X}+\bar{W}.$$
* The queue and transmission may the be analysed independently using Little's formula.}

<!-- original A4 foil 111: The Transmission -->

\newslide{The Transmission}

\slides{* Assume that customers/packets do not leave the queue.
* Rate of arrivals at the queue must equal the rate of arrivals at transmission.}

<!-- original A4 foil 111: The Transmission -->

\newslide{The Transmission (continued)}

\slides{* We define the the average number under transmission as $\rho$ $$
\rho=\lambda\bar{X},$$where $\bar{X}$ is the average time spend under transmission for each packet.
* For the $M/M/1$ queue the average transmission time is given by $\bar{X}=\frac{1}{\mu}$,
* So for the $M/M/1$ queue we have$$
\rho=\frac{\lambda}{\mu},$$ a formula which we have already used in the last chapter.}

<!-- original A4 foil 112: Utilisation Factor -->

\newslide{Utilisation Factor}

\slides{* $\rho$ is the utilisation factor.
* Represents the fraction of time that the transmission line (or server) is in use.}

<!-- original A4 foil 112: Utilisation Factor -->

\newslide{Utilisation Factor (continued)}

\slides{* It is a measure of efficiency.
* It is also the steady state probability that the transmission line is in use.
* For a lossless system this probability is given by $1-P\left(0\right)$.}

<!-- original A4 foil 113: Utilisation Example -->

\newslide{Utilisation Example}

\slides{* Example 2, Chapter 7. Simple example of Little's formula. You are at a queue in a bar and notice that the bar tender spends 10% of her time cleaning between customers. If the typical number of people waiting to be served is 3 what is the ratio of time spent serving to time being served?}

<!-- original A4 foil 113: Utilisation Example -->

\newslide{Utilisation Example (continued)}

\slides{* **Answer**
    \answer{Information says $\rho=0.9$ and $\bar{N}_{Q}=3$. $$
\lambda=\frac{0.9}{\bar{X}}.$$
    $$
3=\lambda\bar{W}.$$
    Therefore $\frac{\bar{W}}{\bar{X}}=3\frac{1}{3}$. \}{6}}

<!-- original A4 foil 114: The Queue -->

\newslide{The Queue}

\slides{* For arrival rate $\lambda$, and $\bar{N}_{Q}$, the average number in queue, and $\bar{W}$, the average queueing (waiting) time.$$
\bar{N}_{Q}=\lambda\bar{W}$$
* For the $M/M/1$ queue $$
\bar{T}=\bar{X}+\bar{W}=\frac{1}{\mu}+\bar{W}$$ so the average time spent waiting in the queue is given by$$
\bar{W}=\bar{T}-\frac{1}{\mu}=\frac{\rho}{\mu-\lambda}.$$
* Average number in the queue is then$$
\bar{N}_{Q}=\frac{\rho^{2}}{1-\rho}.$$}

\endif

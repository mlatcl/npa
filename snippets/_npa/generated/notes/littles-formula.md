\ifndef{npaGenNotesLittlesFormula}
\define{npaGenNotesLittlesFormula}

\notes{\section{Time and Steady State Averages}}

\notes{We have already introduced the concept of distribution means and sample based means. In this section we introduce a further type of average, a time based average. The time average is the average value of a particular function over time. If that function is continuous it is given by$$
\ensuremath{\bar{f}_{t}}=\ensuremath{\frac{1}{t}\int_{0}^{t}}f\left(\tau\right)d\tau.$$The derivation of Little's formula that follows will rely on an assumption. We will assume that averages under the steady state distribution are equivalent to the time average in the limit as $t\ensuremath{\rightarrow\infty}$, where if the state of the system is given as a function of time as $N\left(t\right)$ the average number in the system as a function of time is given by $$
\ensuremath{\bar{N}_{t}}=\ensuremath{\frac{1}{t}\int_{0}^{t}}N\left(\tau\right)d\tau$$and the time average after in the limit as $t\ensuremath{\rightarrow\infty}$ is given by $$
\ensuremath{\bar{N}}=\lim_{t\ensuremath{\rightarrow\infty}}\ensuremath{\bar{N}\left(}t\right).$$which we assume is equivalent to $\left\langle k\right\rangle _{p\left(k\right)}\equiv\ensuremath{\bar{N}}$. See pg 156-157 in [@Bertsekas:data92] for more details.}

\notes{\section{The Formula}}

\notes{Little's formula applies under steady state conditions (see Section\  \ref{sec:steadyState}). Under the steady state assumptions it states,$$
\ensuremath{\bar{N}}=\ensuremath{\lambda\bar{T}}.$$In practice we can see what this means by considering a simple example of a nightclub queue.}

\notes{#### Question}

\notes{You are driving past a nightclub, wondering how long you will have to wait to go in. You notice on Thursday nights that the queue typically contains 20 people and that people arrive at a rate of 40 per hour.
According to Little's formula, how long would you expect to have to wait to get in?}


\notes{The waiting time is given by Little's formula. $\ensuremath{\bar{N}}=20$, $\ensuremath{\lambda}=40$ and $\ensuremath{\bar{T}}=\ensuremath{\frac{\bar{N}}{\lambda}}=20=1\textrm{hour}$.}

\notes{\subsection{Intuition}}

\notes{When phrased in these terms the formula seems fairly obvious. If we see there are twenty people in a queue and they enter a building at a rate of 40 per hour, we might expect to have to wait half-an-hour in the queue. In the examples section at the end of this chapter we build on this intuition with a simple graphical `proof' of the formula based upon that given in [@Bertsekas:data92].
The formula applies regardless of the arrival and service time distributions, it only relies on the system being in steady state. Little's formula can be used at the level of the entire system (queueing time and service time), as we have seen, or it may be applied at a lower level.}

\notes{\section{Average Delay in $M/M/1$}}

\notes{In the last chapter we computed that the average state of an $M/M/1$ queue was given by$$
\ensuremath{\bar{N}}=\ensuremath{\frac{\lambda}{\mu-\lambda}}=\ensuremath{\frac{\rho}{1-\rho}}.$$We can use Little's formula to tell us the average delay associated with the system. From $\ensuremath{\bar{N}}=\ensuremath{\lambda\bar{T}}$ we rearrange to recover the average delay as$$
\ensuremath{\bar{T}}=\ensuremath{\frac{1}{\mu-\lambda}}$$ This is not the time spent in the queue however, this is the time spent in the system which includes *propagation delay*, the delay in transmitting the packet.}

\notes{\subsection{Little's Formula for Queueing Time and Transmission Time}}

\notes{The total delay for packet switching systems can be divided into queueing time, $W$, and service time or transmission time, $X$. $T=X+W.$ Similarly the average delay may be decomposed as$$
\ensuremath{\bar{T}}=\ensuremath{\bar{X}}+\ensuremath{\bar{W}}.$$ Furthermore, both the queue itself and the transmission may the be analysed independently using Little's formula.}

\notes{\subsection{The Transmission}}

\notes{If we assume that customers/packets do not leave the queue then the rate of arrivals at the queue must equal the rate of arrivals at transmission. If we define the the average number under transmission as $\ensuremath{\rho}$ then we can write$$
\ensuremath{\rho}=\ensuremath{\lambda\bar{X}},$$where $\ensuremath{\bar{X}}$ is the average time spend under transmission for each packet. For the $M/M/1$ queue the average transmission time is given by the mean of an exponential distribution, $\ensuremath{\bar{X}}=\ensuremath{\frac{1}{\mu}}$, so for the $M/M/1$ queue we have$$
\ensuremath{\rho}=\ensuremath{\frac{\lambda}{\mu}},$$ a formula which we have already used in the last chapter.
The variable $\ensuremath{\rho}$ is known as the utilisation factor. It represents the fraction of time that the transmission line (or server) is in use and is therefore a measure of efficiency. Note that it is also the steady state probability that the transmission line is in use. For a lossless system (one that doesn't drop packets) this probability is given by $1-P\left(0\right)$. You can check that this is consistent for the $M/M/1$ by looking at equation (\ref{eq:MM1emptyProb}).
*Note*: time under transmission is often considered proportional to packet length. For packet length of $L$ bits and bandwidth of $C$ bits per second transmission time is $X=\ensuremath{\frac{L}{C}}$.}

\notes{\subsection{The Queue}}

\notes{Given $\ensuremath{\lambda}$, an arrival rate, $\ensuremath{\bar{N}_{Q}}$, the average number of packets waiting in the queue, and $\ensuremath{\bar{W}}$, the average packet waiting time, Little's formula gives $$
\ensuremath{\bar{N}_{Q}}=\ensuremath{\lambda\bar{W}}$$for the number in the queue. For the $M/M/1$ queue $\ensuremath{\bar{T}}=\ensuremath{\bar{X}}+\ensuremath{\bar{W}}=\ensuremath{\frac{1}{\mu}}+\ensuremath{\bar{W}}$ so the average time spent waiting in the queue is given by$$
\ensuremath{\bar{W}}=\ensuremath{\bar{T}}-\ensuremath{\frac{1}{\mu}}=\ensuremath{\frac{\rho}{\mu-\lambda}}.$$We can therefore recover the average number in the queue$$
\ensuremath{\bar{N}_{Q}}=\ensuremath{\frac{\rho^{2}}{1-\rho}}.$$}

\notes{## Examples}

\notes{1. **Graphical Proof of Little's Formula.**In this example we provide a graphical proof of Little's formula.
  First we sketch two curves, the number of arrivals ($\ensuremath{\alpha\left(\tau\right)}$) and the number of departures ($\ensuremath{\beta\left(\tau\right)}$) from a queue vs time.
  
    
    }

\figure{\includepng{\diagramsDir/npa/littlesFormula}{60%}}{littlesFormula}{littlesFormula}

\notes{
    
    \label{cap:littlesGraphical}
  
  By looking at Figure\  \ref{cap:littlesGraphical} we note that the area between the lines in the top figure can be expressed as both $\int_{0}^{t}N(\tau)d\tau$ and $\sum_{i=1}^{\ensuremath{\alpha\left(}t\right)}T_{i}$. We may therefore equate these expressions,$$
\int_{0}^{t}N\left(\tau\right)d\tau=\sum_{i=1}^{\ensuremath{\alpha(t)}}T_{i},$$we then introduce the number of arrivals on the right hand side,$$
\int_{0}^{t}N\left(\tau\right)d\tau=\ensuremath{\alpha\left(}t\right)\ensuremath{\frac{\sum_{i=1}^{\alpha\left(t\right)}T_{i}}{\alpha\left(t\right)}}$$and divide both sides by $t$,$$
\ensuremath{\frac{1}{t}\int_{0}^{t}}N\left(\tau\right)d\tau=\ensuremath{\frac{\alpha\left(t\right)}{t}\frac{\sum_{i=1}^{\alpha\left(t\right)}T_{i}}{\alpha\left(t\right)}}.$$The equation now has the form of three averages. The term on the left hand side of the equation is an average, over time, of the number in the system. This average is a function of time and we write it $$
\ensuremath{\bar{N}_{t}}=\ensuremath{\frac{1}{t}\int_{0}^{t}}N\left(\tau\right).$$We also note that the right hand side of the equation is also composed of two averages: $$
\ensuremath{\bar{\lambda}_{t}}=\ensuremath{\frac{\alpha\left(t\right)}{t}},$$is the average of the arrivals over time and $$
\ensuremath{\bar{T}_{t}}=\ensuremath{\frac{\sum_{i=1}^{\alpha\left(t\right)}T_{i}}{\alpha\left(t\right)}}$$ is the average waiting time. So we write$$
\ensuremath{\bar{N}_{t}}=\ensuremath{\bar{\lambda}_{t}\bar{T}_{t}}.$$Dividing both expressions by $t$, equating them, and taking the limit as $t\ensuremath{\rightarrow\infty}$ gives Little's formula. We wish to consider the steady state behaviour. The system may not have steady state behaviour. If the steady state exists, we can seek it in the limit as $t\ensuremath{\rightarrow\infty}$, giving $$
\ensuremath{\bar{N}}=\ensuremath{\lambda\bar{T}}$$}


\notes{1. **Simple example of Little's formula**. You are at a queue in a bar and notice that the bar tender spends 10% of her time cleaning between serving customers. If the typical number of people waiting to be served is $3$, what is the ratio of time spent waiting to being served? 
  Information says $\ensuremath{\rho}=0.9$ and $\ensuremath{\bar{N}_{Q}}=3$. $$
\ensuremath{\lambda}=\ensuremath{\frac{0.9}{\bar{X}}}.$$
  $$
3=\ensuremath{\lambda\bar{W}}.$$
  Therefore $\ensuremath{\frac{\bar{W}}{\bar{X}}}=31$.}

\endif

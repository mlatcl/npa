% generated — do not edit; scripts/convert/run.py
\ifndef{npaGenNotesMg1Arq}
\define{npaGenNotesMg1Arq}

\notes{\section{Automatic Repeat Request (ARQ) System.}}

\notes{The $M/G/1$ queue system can be used for modelling various systems of interest. In an ARQ system packets are transmitted and the system waits for an acknowledgement. If no acknowledgement is received the system retransmits. In this section we review Example\  3.15 from [@Bertsekas:data92]. A schematic of the system is given in Figure\  \ref{cap:ARQschemeatic}.
For the purposes of this analysis, we will assume}

\figure{\includepng{\diagramsDir/npa/ARQ}{80%}}{The ARQ System.}{cap:ARQschemeatic}

\notes{1. That each packet takes 1 millisecond to be transmitted.
2. The system waits a maximum of $n-1$ milliseconds for an acknowledgement. If there is no acknowledgement the system retransmits.
3. The acknowledgement occurs if the packet is received without errors. Otherwise acknowledgement doesn't occur.
4. The probability of an error in a packet is taken to be $p$ and we take errors to occur independently.
5. That packets arrive as a Poisson process with rate $\lambda$.}

\notes{In practice, the fourth assumption (independence of errors) is probably unrealistic . If an error occurs due to problems in the transmission channel, it is likely that several packets in a row will not be received, so the errors do not occur independently. The time interval between transmission and re-transmission will be $1+kn$ milliseconds with probability $\left(1-p\right)p^{k}$. This time interval is associated with $k$ retransmissions and one successful transmission. The probability of this being the service time is given by$$
P\left(X=1+kn\right)=\left(1-p\right)p^{k}$$which is recognised as a *geometric distribution*.}

\notes{\subsection{Average Service Time}}

\notes{Using this distribution we can compute the expected service time which is given by\begin{eqnarray*}
\left\langle X\right\rangle  & = & \sum_{k=0}^{\infty}\left(1+kn\right)\left(1-p\right)p^{k}\\
 & = & \left(1-p\right)\left(\sum_{k=0}^{\infty}p^{k}+n\sum_{k=0}^{\infty}kp^{k}\right)\\
 & = & 1+n\frac{p}{1-p}\end{eqnarray*} since $\sum_{k=0}^{\infty}p^{k}=\frac{1}{1-p}$ and $\sum_{k=0}^{\infty}kp^{k}=\frac{p}{\left(1-p\right)^{2}}$ .}

\notes{\subsection{ARQ Utilization Factor}}

\notes{Strictly speaking, it probably doesn't make sense to use the term `utilization factor' for the ARQ system. This is because during a large portion of the wait it is not actually `utilizing' the channel, it is merely waiting for an acknowledgement. However we can still consider, $\rho=\lambda\left\langle X\right\rangle $, to be the proportion of time that the system will be `busy'. This `busy factor',$$
\rho=\lambda+\lambda n\frac{p}{1-p},$$obviously still has to be less than 1, otherwise the steady state would not exist. This busy time is affected by three parameters: the rate of arrivals, $\lambda$, the amount of time that the system waits for an acknowledgement, $n$, and the probability of an error, $p$. Note that as $p\rightarrow1$ the second term $\rightarrow\infty$.}

\notes{\subsection{ARQ Second Moment}}

\notes{The second moment of the service time is\begin{eqnarray*}
\left\langle X^{2}\right\rangle  & = & \sum_{k=0}^{\infty}\left(1+kn\right)^{2}\left(1-p\right)p^{k}\\
 & = & \left(1-p\right)\left(\sum_{k=0}^{\infty}p^{k}+2n\sum_{k=0}^{\infty}kp^{k}+n^{2}\sum_{k=0}^{\infty}k^{2}p^{k}\right)\\
 & = & 1+\frac{2np}{1-p}+\frac{n^{2}\left(p+p^{2}\right)}{\left(1-p\right)^{2}}\end{eqnarray*}since $$
\sum_{k=0}^{\infty}k^{2}p^{k}=\frac{p+p^{2}}{\left(1-p\right)^{3}}$$ These moments can be used with the Pollaczek-Khinchin formula to obtain statistics for the queue.
Examples}

\notes{{1. The Residual Service Time\label{sub:theResidualServiceTime}
  The residual service time is the amount of service time that remains for the customer under service from the perspective of a customer who has just arrived in the queue. The first part of the proof occurs from the perspective of the arriving customer. The arriving customer is considered to be the $i$th customer. In the table below we introduce some simple definitions of terms.
  {lll}
    $W_{i}$ & = & Waiting time in queue of $i$th customer. \\
    $R_{i}$ & = & `Residual service time' seen by the $i$th customer. \\
    $X_{i}$ & = & Service time of the $i$th customer. \\
    $k_{i}$ & = & Number of customers in the system when the $i$th customer arrives. \\
  
  [0]
    Given the notation we can draw a simple schematic of the system as it is perceived by the $i$th arrival. This is shown in Figure\  \ref{cap:schemeaticRST}.
    [ht]
      \centering
      \figure{\includepng{\diagramsDir/npa/residualServiceOverview}{100%}}{residualServiceOverview}{residualServiceOverview}
      \caption{Schematic representation of residual service time.}
      \label{cap:schemeaticRST}
    
    We can use the figure to immediately write down that the wait for the $i$th customer will be given by$$
W_{i}=R_{i}+\sum_{j=i-(k_{i}-1)}^{i-1}X_{j}$$ summing over both sides (*i.e. *for all the arriving customers up to the $I$th) we obtain $$
\sum_{i=1}^{I}W_{i}=\sum_{i=1}^{I}R_{i}+\sum_{i=1}^{I}\sum_{j=i-(k_{i}-1)}^{i-1}X_{j}$$dividing through by $I$ gives us $$
\sum_{i=1}^{I}\frac{W_{i}}{I}=\sum_{i=1}^{I}\frac{R_{i}}{I}+\sum_{i=1}^{I}\sum_{j=i-(k_{i}-1)}^{i-1}\frac{X_{j}}{I}.$$ In the limit as $I\rightarrow\infty$ this becomes $$
\lim_{I\rightarrow\infty}\sum_{i=1}^{I}\frac{W_{i}}{I}=\lim_{I\rightarrow\infty}\sum_{i=1}^{I}\frac{R_{i}}{I}+\lim_{I\rightarrow\infty}\sum_{i=1}^{I}\frac{(k_{i}-1)X_{i}}{I},$$the terms of which are recognised as *time averages*. If we assume *time averages* are equivalent to *steady state averages* this gives $$
\left\langle W\right\rangle =\left\langle R\right\rangle +\left\langle \left(k-1\right)X\right\rangle .$$Now since the length of the queue as seen by the $i$th arrival is independent of the $i$th arrival's length (our second assumption) this means $\left\langle (k-1)X\right\rangle =\left\langle k-1\right\rangle \left\langle X\right\rangle $ and since $(k-1)$ is the length of the queue we may write $$
\bar{W}=\bar{R}+\bar{N}_{Q}\bar{X}$$ Using Little's theorem for the queue we have$$
\bar{N}_{Q}=\lambda\bar{W}$$which gives in turn$$
\bar{W}=\bar{R}+\lambda\bar{X}\bar{W}.$$Using the fact that $\rho=\lambda\bar{X}$ (which stems from Little's formula for the packets under service) gives us $$
\bar{W}=\bar{R}+\rho\bar{W}$$ Leading to$$
\bar{W}=\frac{\bar{R}}{1-\rho}.$$\}{0}}

\notes{### Answer}

\notes{1. **Markov Service times**. Compute the average waiting time associated with exponentially distributed service times using the Pollaczek-Khinchin formula.\label{example:MarkovService}
  [0]
    The exponentially distributed service times, $$
p\left(X\right)=\mu\exp\left(-\mu X\right),$$have a mean of $$
\bar{X}=\frac{1}{\mu}$$ and a variance of $\frac{1}{\mu^{2}}$ leading to a second moment$$
\left\langle X^{2}\right\rangle =\frac{2}{\mu^{2}}$$
    Substituting into the Pollaczek-Khinchin formula we obtain 
\bar{W} & = & \frac{\rho}{\mu\left(1-\rho\right)}\\
 & = & \frac{\rho}{\mu-\lambda}which is identical to those we derived for the $M/M/1$ queue.}

\notes{### Answer}

\notes{{1. **Deterministic Service times (**$M/D/1$**)**. Some systems have deterministic service times. For example, transmission of fixed length packets over a channel with a fixed bandwidth. \label{example:DeterministicService}
  [0]
    We represent a `deterministic distribution' as$$
P\left(X\right)=\delta\left(X-\frac{1}{\mu}\right)$$where $\delta\left(\cdot\right)$is the Dirac delta function.
    For this system $$
\left\langle X\right\rangle =\frac{1}{\mu}$$and $$
\left\langle X^{2}\right\rangle =\frac{1}{\mu^{2}}$$*i.e. * the variance is zero. Substituting into the Pollaczek-Khinchin formula we obtain $$
\bar{W}=\frac{\rho}{2\mu\left(1-\rho\right)}.$$\}{0}}

\notes{### Answer}

\notes{1. **Uniform Service Times** ($M/U/1$). Consider a uniform probability distribution is defined between 0 and $b$ for $X>0$ as$$
U\left(X|b\right)=\left\{ {cc}
\frac{1}{b} & 0<X\leq b\\
0 & X>b\right.$$show that the mean of this uniform distribution is given by $\frac{b}{2}$ and its variance by $\frac{b^{2}}{12}$ and find the expected waiting time for an $M/U/1$ queue.\label{example:uniformService}
  [0]
    For the mean we have
    
\left\langle X\right\rangle  & = & \int_{0}^{\infty}Xp\left(X\right)dX\\
 & = & \int_{0}^{\infty}XU\left(X|b\right)dX\\
 & = & \int_{0}^{b}\frac{X}{b}dX\\
 & = & \left[\frac{X^{2}}{2b}\right]_{0}^{b}\\
 & = & \frac{b^{2}}{2b}-0\\
 & = & \frac{b}{2}
    For the variance we also require
    
\left\langle X^{2}\right\rangle  & = & \int_{0}^{\infty}X^{2}p\left(X\right)dX\\
 & = & \int_{0}^{b}\frac{X^{2}}{b}dX\\
 & = & \left[\frac{X^{3}}{3b}\right]_{0}^{b}\\
 & = & \frac{b^{3}}{3b}-0\\
 & = & \frac{b^{2}}{3}
    The variance is $\left\langle X^{2}\right\rangle -\left\langle X\right\rangle ^{2}=\frac{b^{2}}{3}-\left(\frac{b}{2}\right)=\frac{b^{2}}{12}$.
2. For simplicity we consider $\mu=\frac{1}{\left\langle X\right\rangle }.$ So $\mu=\frac{2}{b}$ and thus $b=\frac{2}{\mu}$.
3. So we can write the second moment in terms of $\mu$. $\left\langle X^{2}\right\rangle =\frac{b^{2}}{3}$.
4. Substituting in $b=\frac{2}{\mu}$ we have $\left\langle X^{2}\right\rangle =\frac{4}{3\mu^{2}}$.
5. Substituting in to the Pollaczek-Khinchin formula we recover$$
\bar{W}=\frac{2\rho}{3\mu\left(1-\rho\right)}.$$
    
  

\subsection*{Answer}
6. $M/G/1$ Queues with Vacations
  Consider a server which, when it is free, attends to some other business. For example it could transmit control and record keeping traffic. These periods are sometimes known as vacations (which is an American word that means holidays). The vacation periods are characterised by
7. If a new arrival arrives during a vacation it must wait until the vacation is over before being dealt with.
8. If a vacation ends and the server is idle it immediately goes on a new vacation.
  
  [ht]
    \centering
    \figure{\includepng{\diagramsDir/npa/vacationMG1}{80%}}{vacationMG1}{vacationMG1}
    \caption{Schematic of $M/G/1$ queue}
  
  We denote the length of these successive vacations to be $V_{1}$, $V_{2}$, $\dots$. We assume that $V_{1},$$V_{2}$, $\dots$ are independent and identically distributed (i.i.d.) random variables which are also independent of the customer times and the service times. We can then attempt to compute the mean residual service time for this queue for a *Poisson (Markov) arrival* system with *general service times* and *generally distributed vacation times*.
  [0]
    We need to compute residual service time
    For a system with vacations the residual service time is given by 
\frac{1}{t}\int_{0}^{t}r\left(\tau\right)d\tau & = & \frac{1}{t}\sum_{i=1}^{M\left(t\right)}\frac{1}{2}X_{i}^{2}+\frac{1}{t}\sum_{i=1}^{L\left(t\right)}\frac{1}{2}V_{i}^{2}\nonumber \\
 & = & \frac{M\left(t\right)}{t}\frac{1}{2}\frac{\sum_{i=1}^{M\left(t\right)}X_{i}^{2}}{M\left(t\right)}+\frac{L\left(t\right)}{t}\frac{1}{2}\frac{\sum_{i=1}^{L\left(t\right)}V_{i}^{2}}{L\left(t\right)}\label{eq:forVacationResiduals}where we have introduced the arrival process, $M\left(t\right)$, and this time we have also introduced a process which indicates how many vacations there have been, $L\left(t\right)$. This means we have to deal with the average number of vacations. On average the proportion of time available for vacations is $\left(1-\rho\right)$, *i.e. *that time where the transmission line is not in use. If the average length of a vacation at time $t$ is $\bar{V}_{t}$ then the number of vacations that will have arrived at that time is $$
L\left(t\right)=\frac{t\left(1-\rho\right)}{\bar{V}_{t}}.$$Taking the limit of (\ref{eq:forVacationResiduals}) as $t\rightarrow\infty$ we can write $$
\bar{R}=\frac{1}{2}\lambda\left\langle X^{2}\right\rangle +\frac{\left(1-\rho\right)\left\langle V^{2}\right\rangle }{2\bar{V}}.$$So given that the assumptions that we used to develop the formula $$
\bar{W}=\frac{\bar{R}}{1-\rho}$$in Section\  \ref{sub:theResidualServiceTime} are still valid, we may write$$
\bar{W}=\frac{\lambda\left\langle X^{2}\right\rangle }{2\left(1-\rho\right)}+\frac{\left\langle V^{2}\right\rangle }{2\bar{V}}.$$\}{0}
    [ht]
      \centering
      \figure{\includepng{\diagramsDir/npa/vacationResidual}{80%}}{vacationResidual}{vacationResidual}
      \caption{Computation of residual service time for system with vacations.}
    
  

\subsection*{Answer}
9. $M/G/1$** with Vacations**. A bar has Poisson arrivals and one member of staff serving. When there are no customers at the bar, the staff member leaves the bar to check on the kitchen. Assuming these checks are exponentially distributed in length, with mean $\bar{V}$ and that customer service times are exponentially distributed with mean $\bar{X}$ what is the average waiting time in the queue?\label{example:vacationsExample}
  [0]
    Exponential standard deviation = $\frac{1}{\mu}$, mean$=\frac{1}{\mu}$. So if mean is $\bar{V}$, standard deviation is $\bar{V}$ and variance is $\bar{V}^{2}$. Thus second moment is $\left\langle V^{2}\right\rangle =2\bar{V}^{2}$. Similarly for second moment of service time $\left\langle X^{2}\right\rangle =2\bar{X}^{2}$. Defining $\rho=\lambda\bar{X}$ we have $$
\bar{W}=\frac{\lambda\bar{X}}{\left(1-\rho\right)}+\bar{V}=\frac{\rho}{\left(1-\rho\right)}+\bar{V}.$$Deterministic vacations would have lead to $$
\bar{W}=\frac{\lambda\bar{X}}{\left(1-\rho\right)}+\frac{\bar{V}}{2}=\frac{\rho}{\left(1-\rho\right)}+\frac{\bar{V}}{2}.$$
  

\subsection*{Answer}}

\endif

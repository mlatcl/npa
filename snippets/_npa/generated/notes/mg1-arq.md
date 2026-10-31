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
5. That packets arrive as a Poisson process with rate $\ensuremath{\lambda}$.}

\notes{In practice, the fourth assumption (independence of errors) is probably unrealistic . If an error occurs due to problems in the transmission channel, it is likely that several packets in a row will not be received, so the errors do not occur independently. The time interval between transmission and re-transmission will be $1+kn$ milliseconds with probability $\left(1-p\right)p^{k}$. This time interval is associated with $k$ retransmissions and one successful transmission. The probability of this being the service time is given by$$
P\left(X=1+kn\right)=\left(1-p\right)p^{k}$$which is recognised as a *geometric distribution*.}

\notes{\subsection{Average Service Time}}

\notes{Using this distribution we can compute the expected service time which is given by$$
\begin{aligned}
\left\langle X\right\rangle  & = & \sum_{k=0}^{\ensuremath{\infty}}\left(1+kn\right)\left(1-p\right)p^{k}\\
 & = & \left(1-p\right)\left(\sum_{k=0}^{\ensuremath{\infty}}p^{k}+n\sum_{k=0}^{\ensuremath{\infty}}kp^{k}\right)\\
 & = & 1+n\ensuremath{\frac{p}{1-p}}
\end{aligned}
$$ since $\sum_{k=0}^{\ensuremath{\infty}}p^{k}=\ensuremath{\frac{1}{1-p}}$ and $\sum_{k=0}^{\ensuremath{\infty}}kp^{k}=\ensuremath{\frac{p}{\left(1-p\right)^{2}}}$ .}

\notes{\subsection{ARQ Utilization Factor}}

\notes{Strictly speaking, it probably doesn't make sense to use the term `utilization factor' for the ARQ system. This is because during a large portion of the wait it is not actually `utilizing' the channel, it is merely waiting for an acknowledgement. However we can still consider, $\ensuremath{\rho}=\ensuremath{\lambda\left\langle} X\right\rangle$, to be the proportion of time that the system will be `busy'. This `busy factor',$$
\ensuremath{\rho}=\ensuremath{\lambda}+\ensuremath{\lambda} n\ensuremath{\frac{p}{1-p}},$$obviously still has to be less than 1, otherwise the steady state would not exist. This busy time is affected by three parameters: the rate of arrivals, $\ensuremath{\lambda}$, the amount of time that the system waits for an acknowledgement, $n$, and the probability of an error, $p$. Note that as $p\rightarrow1$ the second term $\ensuremath{\rightarrow\infty}$.}

\notes{\subsection{ARQ Second Moment}}

\notes{The second moment of the service time is$$
\begin{aligned}
\left\langle X^{2}\right\rangle  & = & \sum_{k=0}^{\ensuremath{\infty}}\left(1+kn\right)^{2}\left(1-p\right)p^{k}\\
 & = & \left(1-p\right)\left(\sum_{k=0}^{\ensuremath{\infty}}p^{k}+2n\sum_{k=0}^{\ensuremath{\infty}}kp^{k}+n^{2}\sum_{k=0}^{\ensuremath{\infty}}k^{2}p^{k}\right)\\
 & = & 1+\ensuremath{\frac{2np}{1-p}}+\ensuremath{\frac{n^{2}\left(p+p^{2}\right)}{\left(1-p\right)^{2}}}
\end{aligned}
$$since $$
\sum_{k=0}^{\ensuremath{\infty}}k^{2}p^{k}=\ensuremath{\frac{p+p^{2}}{\left(1-p\right)^{3}}}$$ These moments can be used with the Pollaczek-Khinchin formula to obtain statistics for the queue.
Examples}

\notes{1. The Residual Service Time\label{sub:theResidualServiceTime}
  The residual service time is the amount of service time that remains for the customer under service from the perspective of a customer who has just arrived in the queue. The first part of the proof occurs from the perspective of the arriving customer. The arriving customer is considered to be the $i$th customer. In the table below we introduce some simple definitions of terms.
  {lll}

| $W_{i}$ | = | Waiting time in queue of $i$th customer. |
| --- | --- | --- |
| $R_{i}$ | = | `Residual service time' seen by the $i$th customer. |
| $X_{i}$ | = | Service time of the $i$th customer. |
| $k_{i}$ | = | Number of customers in the system when the $i$th customer arrives. |}



\notes{\answer{
Given the notation we can draw a simple schematic of the system as it is perceived by the $i$th arrival. This is shown in Figure\  \ref{cap:schemeaticRST}.
}{0}}

\figure{\includepng{\diagramsDir/npa/residualServiceOverview}{100%}}{residualServiceOverview}{residualServiceOverview}

\notes{\answer{
We can use the figure to immediately write down that the wait for the  $i$ th customer will be given by $$
W_{i}=R_{i}+\sum_{j=i-(k_{i}-1)}^{i-1}X_{j}$$  summing over both sides ( i.e.  for all the arriving customers up to the  $I$ th) we obtain  $$
\sum_{i=1}^{I}W_{i}=\sum_{i=1}^{I}R_{i}+\sum_{i=1}^{I}\sum_{j=i-(k_{i}-1)}^{i-1}X_{j}$$ dividing through by  $I$  gives us  $$
\sum_{i=1}^{I}\ensuremath{\frac{W_{i}}{I}}=\sum_{i=1}^{I}\ensuremath{\frac{R_{i}}{I}}+\sum_{i=1}^{I}\sum_{j=i-(k_{i}-1)}^{i-1}\ensuremath{\frac{X_{j}}{I}}.$$  In the limit as  $I\ensuremath{\rightarrow\ensuremath{\infty}}$  this becomes  $$
\lim_{I\ensuremath{\rightarrow\ensuremath{\infty}}}\sum_{i=1}^{I}\ensuremath{\frac{W_{i}}{I}}=\lim_{I\ensuremath{\rightarrow\ensuremath{\infty}}}\sum_{i=1}^{I}\ensuremath{\frac{R_{i}}{I}}+\lim_{I\ensuremath{\rightarrow\ensuremath{\infty}}}\sum_{i=1}^{I}\ensuremath{\frac{(k_{i}-1)X_{i}}{I}},$$ the terms of which are recognised as  time averages . If we assume  time averages  are equivalent to  steady state averages  this gives  $$
\left\langle W\right\rangle =\left\langle R\right\rangle +\left\langle \left(k-1\right)X\right\rangle .$$ Now since the length of the queue as seen by the  $i$ th arrival is independent of the  $i$ th arrival's length (our second assumption) this means  $\left\langle (k-1)X\right\rangle =\left\langle k-1\right\rangle \left\langle X\right\rangle$  and since  $(k-1)$  is the length of the queue we may write  $$
\ensuremath{\bar{W}}=\ensuremath{\bar{R}}+\ensuremath{\bar{N}_{Q}\ensuremath{\bar{X}}}$$  Using Little's theorem for the queue we have $$
\ensuremath{\bar{N}_{Q}}=\ensuremath{\lambda\ensuremath{\bar{W}}}$$ which gives in turn $$
\ensuremath{\bar{W}}=\ensuremath{\bar{R}}+\ensuremath{\lambda\ensuremath{\bar{X}\bar{W}}}.$$ Using the fact that  $\ensuremath{\rho}=\ensuremath{\lambda\ensuremath{\bar{X}}}$  (which stems from Little's formula for the packets under service) gives us  $$
\ensuremath{\bar{W}}=\ensuremath{\bar{R}}+\ensuremath{\rho\ensuremath{\bar{W}}}$$  Leading to $$
\ensuremath{\bar{W}}=\ensuremath{\frac{\ensuremath{\bar{R}}}{1-\ensuremath{\rho}}}.$$
}{0}}




\notes{1. **Markov Service times**. Compute the average waiting time associated with exponentially distributed service times using the Pollaczek-Khinchin formula.\label{example:MarkovService}}



\notes{\answer{
The exponentially distributed service times, $$
p\left(X\right)=\ensuremath{\mu\ensuremath{\exp\left(}}-\ensuremath{\mu} X\right),$$have a mean of $$
\ensuremath{\bar{X}}=\ensuremath{\frac{1}{\ensuremath{\mu}}}$$ and a variance of $\ensuremath{\frac{1}{\ensuremath{\mu^{2}}}}$ leading to a second moment$$
\left\langle X^{2}\right\rangle =\ensuremath{\frac{2}{\ensuremath{\mu^{2}}}}$$
    Substituting into the Pollaczek-Khinchin formula we obtain $$
\begin{aligned}
\end{aligned}
$$which is identical to those we derived for the $M/M/1$ queue.

$$
\begin{aligned}
\ensuremath{\bar{W}} & = & \ensuremath{\frac{\ensuremath{\rho}}{\ensuremath{\mu\left(}1-\ensuremath{\rho\right)}}\}
 & = & \ensuremath{\frac{\ensuremath{\rho}}{\ensuremath{\mu}-\ensuremath{\lambda}}}
\end{aligned}
$$
}{0}}




\notes{1. **Deterministic Service times (**$M/D/1$**)**. Some systems have deterministic service times. For example, transmission of fixed length packets over a channel with a fixed bandwidth. \label{example:DeterministicService}}



\notes{\answer{
We represent a `deterministic distribution' as$$
P\left(X\right)=\delta\left(X-\ensuremath{\frac{1}{\ensuremath{\mu}}\right)}$$where $\delta\left(\ensuremath{\cdot\right)}$is the Dirac delta function.
    For this system  $$
\left\langle X\right\rangle =\ensuremath{\frac{1}{\ensuremath{\mu}}}$$ and  $$
\left\langle X^{2}\right\rangle =\ensuremath{\frac{1}{\ensuremath{\mu^{2}}}}$$ i.e.   the variance is zero. Substituting into the Pollaczek-Khinchin formula we obtain  $$
\ensuremath{\bar{W}}=\ensuremath{\frac{\ensuremath{\rho}}{2\ensuremath{\mu\left(}1-\ensuremath{\rho\right)}}}.$$
}{0}}




\notes{1. **Uniform Service Times** ($M/U/1$). Consider a uniform probability distribution is defined between 0 and $b$ for $X>0$ as$$
U\left(X|b\right)=\begin{array}{cc}
\ensuremath{\frac{1}{b}} & 0<X\ensuremath{\leq} b\\
0 & X>b\end{array}$$show that the mean of this uniform distribution is given by $\ensuremath{\frac{b}{2}}$ and its variance by $\ensuremath{\frac{b^{2}}{12}}$ and find the expected waiting time for an $M/U/1$ queue.\label{example:uniformService}
  

\subsection*{Answer}
2. $M/G/1$ Queues with Vacations
  Consider a server which, when it is free, attends to some other business. For example it could transmit control and record keeping traffic. These periods are sometimes known as vacations (which is an American word that means holidays). The vacation periods are characterised by
3. If a new arrival arrives during a vacation it must wait until the vacation is over before being dealt with.
4. If a vacation ends and the server is idle it immediately goes on a new vacation.
  
  
    
    }

\figure{\includepng{\diagramsDir/npa/vacationMG1}{80%}}{vacationMG1}{vacationMG1}

\notes{
    
  
  We denote the length of these successive vacations to be $V_{1}$, $V_{2}$, $\ensuremath{\dots}$. We assume that $V_{1},$$V_{2}$, $\ensuremath{\dots}$ are independent and identically distributed (i.i.d.) random variables which are also independent of the customer times and the service times. We can then attempt to compute the mean residual service time for this queue for a *Poisson (Markov) arrival* system with *general service times* and *generally distributed vacation times*.
  

\subsection*{Answer}
5. $M/G/1$**with Vacations**. A bar has Poisson arrivals and one member of staff serving. When there are no customers at the bar, the staff member leaves the bar to check on the kitchen. Assuming these checks are exponentially distributed in length, with mean $\ensuremath{\bar{V}}$ and that customer service times are exponentially distributed with mean $\ensuremath{\bar{X}}$ what is the average waiting time in the queue?\label{example:vacationsExample}
  

\subsection*{Answer}}



\notes{\answer{
* For simplicity we consider $\ensuremath{\mu}=\ensuremath{\frac{1}{\left\langle X\right\rangle }}.$ So $\ensuremath{\mu}=\ensuremath{\frac{2}{b}}$ and thus $b=\ensuremath{\frac{2}{\ensuremath{\mu}}}$.
* So we can write the second moment in terms of $\ensuremath{\mu}$. $\left\langle X^{2}\right\rangle =\ensuremath{\frac{b^{2}}{3}}$.
* Substituting in $b=\ensuremath{\frac{2}{\ensuremath{\mu}}}$ we have $\left\langle X^{2}\right\rangle =\ensuremath{\frac{4}{3\ensuremath{\mu^{2}}}}$.
* Substituting in to the Pollaczek-Khinchin formula we recover$$
\ensuremath{\bar{W}}=\ensuremath{\frac{2\ensuremath{\rho}}{3\ensuremath{\mu\left(}1-\ensuremath{\rho\right)}}}.$$
}{0}}





\notes{\answer{
We need to compute residual service time
    For a system with vacations the residual service time is given by  $$
\begin{aligned}
\end{aligned}
$$ where we have introduced the arrival process,  $M\left(t\right)$ , and this time we have also introduced a process which indicates how many vacations there have been,  $L\left(t\right)$ . This means we have to deal with the average number of vacations. On average the proportion of time available for vacations is  $\left(1-\ensuremath{\rho\right)}$ ,  i.e.  that time where the transmission line is not in use. If the average length of a vacation at time  $t$  is  $\ensuremath{\bar{V}_{t}}$  then the number of vacations that will have arrived at that time is  $$
L\left(t\right)=\ensuremath{\frac{t\left(1-\ensuremath{\rho\right)}}{\ensuremath{\bar{V}_{t}}}}.$$ Taking the limit of ( \ref{eq:forVacationResiduals} ) as  $t\ensuremath{\rightarrow\ensuremath{\infty}}$  we can write  $$
\ensuremath{\bar{R}}=\ensuremath{\frac{1}{2}\ensuremath{\lambda\left\langle}} X^{2}\right\rangle +\ensuremath{\frac{\left(1-\ensuremath{\rho\right)\left\langle} V^{2}\right\rangle }{2\ensuremath{\bar{V}}}}.$$ So given that the assumptions that we used to develop the formula  $$
\ensuremath{\bar{W}}=\ensuremath{\frac{\ensuremath{\bar{R}}}{1-\ensuremath{\rho}}}$$ in Section\   \ref{sub:theResidualServiceTime}  are still valid, we may write $$
\ensuremath{\bar{W}}=\ensuremath{\frac{\ensuremath{\lambda\left\langle} X^{2}\right\rangle }{2\left(1-\ensuremath{\rho\right)}}}+\ensuremath{\frac{\left\langle V^{2}\right\rangle }{2\ensuremath{\bar{V}}}}.$$

$$
\begin{aligned}
\ensuremath{\frac{1}{t}\int_{0}^{t}}r\left(\tau\right)d\tau & = & \ensuremath{\frac{1}{t}\sum_{i=1}^{M\left(t\right)}\ensuremath{\frac{1}{2}}}X_{i}^{2}+\ensuremath{\frac{1}{t}\sum_{i=1}^{L\left(t\right)}\ensuremath{\frac{1}{2}}}V_{i}^{2}\nonumber \\
 & = & \ensuremath{\frac{M\left(t\right)}{t}\ensuremath{\frac{1}{2}\frac{\sum_{i=1}^{M\left(t\right)}X_{i}^{2}}{M\left(t\right)}}}+\ensuremath{\frac{L\left(t\right)}{t}\ensuremath{\frac{1}{2}\frac{\sum_{i=1}^{L\left(t\right)}V_{i}^{2}}{L\left(t\right)}}}
\end{aligned}
$$
}{0}}





\notes{\answer{
Exponential standard deviation = $\ensuremath{\frac{1}{\ensuremath{\mu}}}$, mean$=\ensuremath{\frac{1}{\ensuremath{\mu}}}$. So if mean is $\ensuremath{\bar{V}}$, standard deviation is $\ensuremath{\bar{V}}$ and variance is $\ensuremath{\bar{V}^{2}}$. Thus second moment is $\left\langle V^{2}\right\rangle =2\ensuremath{\bar{V}^{2}}$. Similarly for second moment of service time $\left\langle X^{2}\right\rangle =2\ensuremath{\bar{X}^{2}}$. Defining $\ensuremath{\rho}=\ensuremath{\lambda\ensuremath{\bar{X}}}$ we have $$
\ensuremath{\bar{W}}=\ensuremath{\frac{\ensuremath{\lambda\bar{X}}}{\left(1-\ensuremath{\rho\right)}}}+\ensuremath{\bar{V}}=\ensuremath{\frac{\ensuremath{\rho}}{\left(1-\ensuremath{\rho\right)}}}+\ensuremath{\bar{V}}.$$Deterministic vacations would have lead to $$
\ensuremath{\bar{W}}=\ensuremath{\frac{\ensuremath{\lambda\bar{X}}}{\left(1-\ensuremath{\rho\right)}}}+\ensuremath{\frac{\ensuremath{\bar{V}}}{2}}=\ensuremath{\frac{\ensuremath{\rho}}{\left(1-\ensuremath{\rho\right)}}}+\ensuremath{\frac{\ensuremath{\bar{V}}}{2}}.$$
}{0}}

\endif

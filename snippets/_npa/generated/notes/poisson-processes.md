% generated — do not edit; scripts/convert/run.py
\ifndef{npaGenNotesPoissonProcesses}
\define{npaGenNotesPoissonProcesses}

\notes{\section{Stochastic Processes}}

\notes{A probabilistic process, also known as a random process or a stochastic process, can be viewed as a `random function'. A normal function maps a set of inputs to a point value. A probabilistic process maps a set of inputs to a probability distribution over values or a probability density function.
Various systems are modelled with probabilistic processes. For example, the *Wiener process* is the process behind Brownian motion. Stock market data is often modelled as a stochastic process. For example the Black-Scholes formula assumes that the logarithm of the stock market data can be modelled as a Wiener Process.
We will base our definition of a random process on that given by [@Chan:performance00].}

\notes{* **A\** random\  process May be defined as a *random function* which, for a particular value, is a random quantity.}

\notes{\section{Poisson Process\label{sec:poissonProcess}}}

\notes{We've already met the Poisson distribution, there is a simple process which is related to the Poisson distribution: the Poisson process.
The Poisson process gives probabilities of a number of arrivals, $k$, as a function of time, $t$, given a `rate', $\lambda$.}

\notes{\begin{equation}
P\left(k|t,\lambda\right)=\frac{(\lambda t)^{k}}{k!}e^{-\lambda t}.\label{eq:process}\end{equation}Note the similarity between (\ref{eq:poissonDist}) and (\ref{eq:process}). The process is simply the distribution with $\mu$ substituted with $\lambda t$.
Using this substitution the mean of the Poisson process (the first moment of $k$) is given by$$
\left\langle k\right\rangle =\lambda t.$$Which is the expected number of arrivals at a given time $t$. The parameter $\lambda$ is therefore known as the \emph{rate} of the process. This implies that the Poisson process is a form of counting process where the counts are \emph{expected} to increase linearly with time at a rate given by $\lambda$.}

\notes{\section{Properties}}

\notes{In the Chapter\  \ref{cha:markovChainsAndProcesses} we will derive the Poisson process from some simple assumptions about how arrivals occur, for the moment though we will highlight some important properties of the Poisson process. We will describe each in more detail below, to summarise though the fiver properties are:}

\notes{1. Superposition of Poisson processes.
2. Decomposition of Poisson processes.
3. Independence of arrivals.
4. Similarity of arrival distribution.
5. Interarrival time distributions.}

\notes{\subsection{Superposition of Poissons\label{sec:superpositionPoisson}}}

\notes{The first property we will consider is superposition of Poisson flows. It is a property of a Poisson process that if we combine $N$ independent processes with rates $\lambda_{1},\lambda_{2},\dots,\lambda_{N}$ together the resulting process is also a Poisson process with a combined rate, $\lambda$, equal to the sum of each of the input rates: $\lambda=\sum_{n=1}^{N}\lambda_{n}$. This is shown pictorially in Figure\  \ref{cap:poissonSuperposition}.
\footnote{Two variables $x$ and $y$ are independent if their joint distributions are equal to the product of their marginal distributions $P\left(x,y\right)=P\left(x\right)P\left(y\right)$.}}

\figure{\includepng{\diagramsDir/npa/sumPoisson}{60%}}{If independent Poisson processes form a single traffic flow overall process is a Poisson with a rate that s the sum of the rates of the separate processes.}{cap:poissonSuperposition}

\notes{\subsection{Decomposition of Poisson Flow}}

\notes{Just as Poisson processes can be combined to obtain a higher rate Poisson process, they can also be decomposed to obtain lower rate Poisson processes. Assume we have one input channel where arrivals are occurring with a Poisson process with rate $\lambda$. This channel then splits into $N$ separate output channels. Each input arrival is then *independently* assigned to output channel $n$ with probability $P\left(n\right)$. In this case the output channels then behave like Poisson processes with rates given by $\lambda_{n}=P\left(n\right)\lambda$. This is shown in Figure\  \ref{cap:decompositionPoisson}.}

\figure{\includepng{\diagramsDir/npa/decomposePoisson}{80%}}{If a single Poisson process with rate $\lambda$ is switched to different output channels, with each arrival being switched to channel $n$ with probability $P\left(n\right)=\lambda_{n}/\lambda$, each output channel will be a Poisson process with rate $\lambda_{n}$.}{cap:decompositionPoisson}

\notes{\subsection{Independence of Arrivals\label{sub:poissonIndependence}}}

\notes{Consider a single Poisson process, if we look within this process at two *disjoint* time intervals (*i.e. * periods of time that don't overlap). Assume we have $k_{1}$ arrivals in the first interval and $k_{2}$ arrivals in the second interval. The distribution of arrivals in the two intervals are independent of each other, *i.e.\  *$P\left(k_{1},k_{2}\right)=P\left(k_{1}\right)P\left(k_{2}\right)$.}

\notes{\subsection{Similarity of Arrival Distributions for Identical Intervals\label{sub:poissonSimilarities}}}

\notes{Consider a single Poisson process with rate $\lambda$, let the number of arrivals between time $s$ and $s+t$ be given by $k_{1}$. Now consider a second independent Poisson process with the same rate $\lambda$, let the number of arrivals between time $r$ and $r+t$ be given by $k_{2}$. The distribution of $k_{1}$ and $k_{2}$ are then equal, $$
P\left(k_{1}\right)=P\left(k_{2}\right).$$}

\notes{\subsection{Interarrival Times and Poisson Processes}}

\notes{The Poisson process is a simple model of arrivals that is widely used due to its analytical properties. We have already seen how a superpositions and decompositions of Poisson processes also lead to Poisson processes. Another attractive analytical property is the ease with which we can compute the *interarrival time distribution* for the Poisson process.
The interarrival time distribution is the distribution of times between arrivals. Consider waiting for the next bus at a bus stop. If you *just missed a bus* how long will you have to wait for the next bus to arrive? If the buses arrive as a Poisson process, then it is straightforward to work out the distribution of your waiting time.
The interarrival time distribution for the Poisson process turns out to be the *exponential distribution*,$$
p\left(X\right)=\lambda e^{-\lambda X}.$$ This is derived in the examples at the end of this chapter.
Stating that interarrival times are distributed exponentially is equivalent to stating that arrivals occur as a Poisson process. We will therefore use these formulations interchangeably, *i.e. *when we state that the interarrival times for students registering at the Goodwin Sports centre is given by an exponential distribution with parameter $\lambda=2$ we are equivalently stating that these students are arriving according to a Poisson process with rate parameter $\lambda=2$.}

\notes{\section{The Exponential Distribution}}

\notes{In the last section we saw that the exponential distribution gives can be derived by considering the interarrival times of the Poisson distribution. Here we give a few properties of the exponential that will be relevant in this course.}

\notes{\subsection{The Memoryless property}}

\notes{We have already seen in our derivation of the exponential as interarrival time distribution that it is *memoryless*. Formally speaking this means that for exponentially distributed variable $X$$$
P\left(X>s+t|X>t\right)=P\left(X>s\right)$$or in English, the probability of the waiting time being greater than $s+t$ given that the waiting time is already greater than $t$ is the same as the probability of the waiting time being greater than $s$.}

\notes{\subsection{Mean and Variance}}

\notes{Recall the exponential distribution $$
p(X)=\lambda e^{-\lambda X}$$ The mean of an exponential can be found to be, $$
\left\langle X\right\rangle _{p(X)}=\frac{1}{\lambda}$$ and the variance is $$
\left\langle X^{2}\right\rangle _{p(X)}-\left\langle X\right\rangle _{p(X)}^{2}=\frac{1}{\lambda^{2}}.$$ These are easily confirmed --- they are part of Tutorial 1.}

\notes{## Examples}

\notes{{{1. **Superposition of Poisson processes. ** There are three queues for registration of MSc students from different courses at the University of Sheffield. Students for the first course, Physics and Fine Art, arrive with a rate of 4 students per minute. Students for the second course, The Psychology of Sociology, arrive with a rate of 2 students per minute and students for the third course, Computer Science and Aromatherapy arrive with a rate of 5 students a minute.
  Assuming the student arrivals are independent and occur as a Poisson process what is the probability that after 15 minutes there have been **a)** 90 student arrivals? **b) **180 arrivals?
  [0]
    If the arrivals are independent and occur as a Poisson process, the rate of arrivals for all student is the sum of the rates for each course. $\lambda=4+2+5=11$. Now we simply evaluate (\ref{eq:process}) with $t=15$, $\lambda=11$ and **a) **$k=90$ giving 
P\left(k=90|\lambda=11,t=15\right) & = & \frac{\left(11\times15\right)^{90}}{90!}\exp\left(-\left(11\times15\right)\right)\\
 & = & 5.5\times10^{-11}.and **b)**
    
P\left(k=90|\lambda=11,t=15\right) & = & \frac{\left(11\times15\right)^{180}}{180!}\exp\left(-\left(11\times15\right)\right)\\
 & = & ?.
    Now ask someone with a calculator to work this out. Factorial 180 will definitely not work. Explain that it needs to be computed as:
    
P\left(k=90|\lambda=11,t=15\right) & = & \exp\left(180\times\ln\left(11\times15\right)\right.\\
 &  & \left.-\ln\left(180!\right)-\left(11\times15\right)\right)\\
 & = & 0.015.\}{0}
  

\subsubsection*{Answer}
2. **Example of Poisson Decomposition. ** There is one registration for all MSc courses. Students arrive in the hall and are assigned to registration desks according to the first letter of their surname. Desk 1 ($d=1)$takes students with names from A-G, desk 2 ($d=2$) from H-M, desk 3 ($d=3$) from N to S and desk 4 ($d=4$) from R to Z.
  Surnames are distributed amongst these four categories with the following probability distribution:
  {lllll}
    $d$ & 1 & 2 & 3 & 4 \\
    $P\left(d\right)$ & $0.20$ & $0.27$ & $0.25$ & $0.28$ \\
  
  Assuming the students arrive *independently* of their surname as a Poisson process at a rate of 10 students per minute what is the probability that **a) **after 5 minutes 5 students have arrived at desk 1? **b)** after 10 minutes 20 students have arrived at desk 4?
  [0]
    If the splitting is independent of the arrival, then the arrivals at each desks will also occur as a Poisson process. For **a) **arrivals at** **desk 1 will occur as a Poisson process with rate $\lambda_{1}=0.20\times10=2$. The probability that $k=5$ students will have arrived at desk 1 after $t=5$ minutes is given by substituting these values into (\ref{eq:process}): 
P\left(k=5|\lambda_{1}=2,t=5\right) & = & \frac{\left(2\times5\right)^{5}}{5!}\exp\left(-\left(2\times5\right)\right)\\
 & = & 0.038.For **b) **arrivals at** **desk 4 will occur as a Poisson process with rate $\lambda_{4}=0.28\times10=2.8$. The probability that $k=20$ students will have arrived at desk 1 after $t=10$ minutes is again given by substituting these values into (\ref{eq:process}): 
P\left(k=20|\lambda_{4}=2.8,t=10\right) & = & \frac{\left(2.8\times10\right)^{20}}{20!}\exp\left(-\left(2.8\times10\right)\right)\\
 & = & 0.025.\}{0}
  

\subsubsection*{Answer}
3. **Interarrival times for the Poisson process. **In Figure\  \ref{cap:poissonInterArrival} we show different arrival times, $T_{1},\dots,T_{n}$ for the process. You can think of these as the arrival times of the buses.
  [ht]
    \centering
    \figure{\includepng{\diagramsDir/npa/interArrivals}{60%}}{interArrivals}{interArrivals}
    \caption{For a Poisson process, this figure shows the times of the arrivals, $T_{n}$, and the interarrival times, $X_{n}$.}
    \label{cap:poissonInterArrival}
  
  We are interested in computing the distribution of the variables $X_{i}=T_{i}-T_{i-1}$: the times between bus arrivals. In this example you will derive this PDF for the interarrival times.\answer{
  \footnote{The interarrival times, $X_{i}$, are continuous values, so they will be governed by a probability density function rather than a discrete probability distribution.}
  Firstly we define the number of arrivals at time $t$ to be given by the function $N\left(t\right)$. Next we note that the cumulative density function (CDF) of the interarrival time distribution will be given by $P\left(X_{i}\leq t\right)$ (see Section\  \ref{sub:CDFs} for a reminder on CDFs). We can re-write this probability as$$
P\left(X_{i}\leq t\right)=1-P\left(X_{i}>t\right),$$so, rather than focusing on $P\left(X_{i}\leq t\right)$, we can consider the distribution $P\left(X_{i}>t\right)$. Now we rewrite the condition in this distribution as
\left(X_{i}>t\right) & \equiv & \left(T_{i}-T_{i-1}>t\right)\nonumber \\
 & \equiv & \left(T_{i}>T_{i-1}+t\right),\label{eq:conditionInterarrival}where we have simply used the definition of $X_{i}$ and rearranged the inequality. Let's take the time that $T_{i-1}$ occurs to be $t_{i-1}$. This lets us write the condition (\ref{eq:conditionInterarrival}) as $\left(T_{i}>T_{i-1}+t|T_{i-1}=t_{i-1}\right)$. This will be true if and only if the function $N\left(t\right)$ does not change during the interval $\left(t_{i-1},t_{i-1}+t\right)$. We can express this mathematically as $$
\left(X_{i}>t|T_{i-1}=t_{i-1}\right)\equiv\left(N\left(t_{i-1}+t\right)-N\left(t_{i-1}\right)=0\right).$$The right hand side of this statement expresses the condition that no arrivals occur between time $t_{i-1}=T_{i-1}$ and time $t$.
  \footnote{The `$\equiv$' sign should be read as `is equivalent to'.}
  $$
P\left(X_{i}>t|T_{i-1}=t_{i-1}\right)=P\left(N\left(t_{i-1}+t\right)-N\left(t_{i-1}\right)=0\right)$$now, because of the similarity of the arrival distributions for intervals of identical lengths (Section\  \ref{sub:poissonSimilarities}) we can write$$
P\left(N\left(t_{i-1}+t\right)-N\left(t_{i-1}\right)\right)=P\left(N\left(t\right)\right)$$which means that$$
P\left(N\left(t_{i-1}+t\right)-N\left(t_{i-1}\right)=0\right)=P\left(N\left(t\right)=0\right)$$and substituting $N\left(t\right)=k=0$ into (\ref{eq:process}) we find that the probability of their being no arrivals at time $t$, $P\left(N\left(t\right)=0\right)$, is $$
P\left(N\left(t\right)=0\right)=\exp\left(-\lambda t\right)$$so$$
P\left(X_{i}>t\right)=\exp\left(-\lambda t\right)$$and the CDF we are interested in is given by 
P\left(X_{i}\leq t\right) & = & 1-P\left(X_{i}>t\right)\\
 & = & 1-\exp\left(-\lambda t\right).Now to obtain the PDF we simply differentiate the CDF (Section\  \ref{sub:CDFs}) giving$$
p\left(X_{i}\right)=\lambda e^{-\lambda X_{i}}$$which is the interarrival time distribution. The form of the distribution is recognised as an *exponential distribution*. The parameter of the exponential, $\lambda$, is the rate parameter from the Poisson process.\}{0}

\subsubsection*{Answer}}

\endif

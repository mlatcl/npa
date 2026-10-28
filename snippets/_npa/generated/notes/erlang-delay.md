% generated — do not edit; scripts/convert/run.py
\ifndef{npaGenNotesErlangDelay}
\define{npaGenNotesErlangDelay}

\notes{\section{Stationary Distribution}}

\notes{In the context of the Erlang delay system it is usual to refer to the `average holding time', $\tau=\frac{1}{\mu}\equiv\bar{X}$, which, for a network involving telephones, would be the time a call is open.
We give a schematic overview of an Erlang delay system in Figure\  \ref{cap:erlangDelaySchematic}. It shows the offered load, $a=\frac{\lambda}{\mu}$, arriving in the system through a queue. The system is *lossless*, so the carried load (sometimes denoted $a^{\prime}$) is also equal to $a$.}

\figure{\includepng{\diagramsDir/npa/erlangDelayDiagram}{80%}}{Queueing model of the Erlang delay system.}{cap:erlangDelaySchematic}

\notes{\subsection{State Diagram}}

\notes{As with all the Markov based systems we have met so far the first step in their analysis is to write down their state diagram.
The Erlang loss system may be analysed as a birth-death process with birth rate $$
\lambda_{k}=\lambda$$ and death rate $$
\mu_{k}=\left\{ \begin{array}{cc}
k\mu & k=0,1,\dots,m-1\\
m\mu & k>m\end{array}\right.$$we derive the detailed balance equations in Example\  \ref{example:erlangDelayStationary} at the end of the chapter, here we give the result. The overall stationary distribution is$$
P\left(k\right)=\left\{ \begin{array}{cc}
P\left(0\right)\frac{(m\rho)^{k}}{k!}, & k\leq m\\
P\left(0\right)\frac{m^{m}\rho^{k}}{m!} & k>m\end{array}\right.$$where the normalisation constant is given by}}}

\figure{\includepng{\diagramsDir/npa/erlangDelay}{100%}}{State diagram of an Erlang delay system.}{erlangDelay}

\notes{$$
P\left(0\right)=\left[\sum_{k=0}^{m-1}\frac{\left(m\rho\right)^{k}}{k!}+\frac{\left(m\rho\right)^{m}}{m!\left(1-\rho\right)}\right]^{-1}.$$}

\notes{\section{Probability of Waiting}}

\notes{For the $M/M/m$ queue a key quantity of interest is the probability of of a customer queueing, $P_{Q}$. What is the probability, when the system is at steady state, that a customer will arrive and find all the $m$ servers busy? \begin{eqnarray*}
P\left(k\geq m\right) & = & \sum_{k=m}^{\infty}P\left(k\right)\\
 & = & P\left(0\right)\sum_{k=m}^{\infty}\frac{m^{m}\rho^{k}}{m!}\\
 & = & P\left(0\right)\frac{\left(\rho m\right)^{m}}{m!}\sum_{k=m}^{\infty}\rho^{k-m}\doteq C\left(m,a\right),\end{eqnarray*}with a little manipulation (check Example\  \ref{example:erlangDelayStationary}) this expression can be re-written\begin{equation}
C\left(m,a\right)=P\left(0\right)\frac{\left(\rho m\right)^{m}}{m!\left(1-\rho\right)}.\label{eq:ErlangCone}\end{equation}This is known as the *Erlang C formula*, or Erlang's second formula after A.K. Erlang a pioneer of queueing theory. By making use of our definition of $a$ (from Section\  \ref{sub:offeredLoad}), we can rewrite the offered load as$$
a=\frac{\lambda}{\mu}=m\rho$$ and substituting into (\ref{eq:ErlangCone}) we have $$
C(m,a)=\frac{P\left(0\right)a^{m}}{m!\left(1-\frac{a}{m}\right)}.$$The result of this formula can be computed on a computer: but some care must be taken when computing it. In particular when $m$ is large overflow problems will occur for $a^{m}$ and $m!$. If we naively compute the ration $\frac{a^{m}}{m!}$ we will obtain an overflow error. Instead we can compute the formula in log space,$$
\ln C\left(m,a\right)=\ln P\left(0\right)+m\ln a-\ln m!-\ln\left(1-\frac{a}{m}\right).$$Some care still needs to be taken with the $\ln P\left(0\right)$ term, but each of the other terms can be computed with appropriate functions in MATLAB. To compute a log factorial the log of the *gamma function *is used.
When we need to compute the Erlang C curve, for the purposes of exams and exercises, we will use the old fashioned method of curves.}

\notes{\section{Erlang C Curves}}

\notes{We have provided you with two sets of curves in Figure\  \ref{cap:erlangCOne} and \ref{cap:erlangCTwo}. In an exam, if they are needed, curves will be provided with the exam paper. Make sure you mark the curves and hand them in with your paper. To illustrate the use of the curves we will consider a simple telephone trunking example and a customer service centre example, see Examples\  \ref{example:telephoneTrunking}  and\  \ref{example:customerService} at the end of this chapter.}

\figure{\includepng{\diagramsDir/npa/erlangCCurves0to20}{100%}}{Erlang C curves for offered traffic between 0 and 20.}{cap:erlangCOne}

\figure{\includepng{\diagramsDir/npa/erlangCCurves0to100}{100%}}{Erlang C curves for offered traffic between 0 and 100.}{cap:erlangCTwo}

\notes{\subsection{Average number in System.}}

\notes{By computing the expectation of $k$ under the stationary distribution, we can also compute the average number of calls in the Erlang Delay System. The result of this computation is:
$$
\bar{N}=\frac{\rho}{1-\rho}C(m,a)+m\rho.$$ These terms represent the average queue length and the average number of busy lines. The average queue length is given by$$
\bar{N}_{Q}=\frac{\rho}{1-\rho}C(m,a)$$ so using Little's formula the average queueing time is simply $$
\bar{W}=\frac{\bar{N}_{Q}}{\lambda}=\frac{C(m,a)}{m\mu(1-\rho)}.$$(see Example\  \ref{example:erlangDelayWait}) . Note that this is the average queueing time for all customers (whether they queued or not). It might be more informative to compute the average queueing time for those who actually queue. This can be easily done using the fact that the average queueing time for those who don't queue is zero. The average queueing time can be decomposed as
$$
\bar{W}=C\left(m,a\right)\bar{W}_{Q}+\left(1-C\left(m,a\right)\right)\bar{W}_{\sim Q},$$where $\bar{W}_{Q}$ is the average queueing time for those who do queue and $\bar{W}_{\sim Q}$ is the average queueing time for those who don't queue. Since $\bar{W}_{\sim Q}=0$ the second term in this sum is zero, so we can rewrite in terms of $\bar{W}_{Q}$ as $$
\bar{W}_{Q}=\frac{\bar{W}}{C\left(m,a\right)}=\frac{1}{m\mu\left(1-\rho\right)}=\frac{1}{\mu\left(m-a\right)}.$$Note that the result shows that the average queueing time for those who do queue is *independent *of the probability of queueing.}

\notes{## Examples}

\notes{1. **Erlang Delay Stationary Distribution. **Derive the stationary distribution for the Erlang delay system.\label{example:erlangDelayStationary}
  [0]
    The `death rate' $\mu_{k}$ has different definitions for different parts of the state space. To derive the detailed balance equation we need to consider detailed balance for each part in turn,
    When the system's state, $k$, is less than or equal to the number of servers we have boundary flow as in Figure\  \ref{cap:flowAtBoundaryMMma},which leads to the following balance equation $$
\lambda P\left(k-1\right)=k\mu P\left(k\right).$$As a result, for $k=0\dots m$ we may write
P\left(k\right)=\frac{\lambda}{k\mu}P\left(k-1\right).\label{eq:PkForPartA}It will prove convenient to define $$
\rho=\frac{\lambda}{m\mu}$$which in turn gives $$
\frac{\lambda}{k\mu}=\frac{m\rho}{k}$$which we substitute back into (\ref{eq:PkForPartA}) obtaining$$
P\left(k\right)=\frac{m\rho}{k}P\left(k-1\right)$$and as before
P\left(k\right)=\frac{\left(m\rho\right)^{k}}{k!}P\left(0\right) & \textrm{for} & k\leq m\label{eq:probabilities}
    [ht]
      \centering
      \figure{\includepng{\diagramsDir/npa/boundaryFlowMMinf}{40%}}{boundaryFlowMMinf}{boundaryFlowMMinf}
      \caption{Flow rates at a boundary.}
      \label{cap:flowAtBoundaryMMma}
    
    When the system's state is greater than $m$, $k>m$ the flow at the boundary is as in Figure\  \ref{cap:flowAtBoundaryMMmb}, the detailed balance equation is thenwhich leads to $$
\lambda P(k-1)=m\mu P\left(k\right)$$therefore for $k=m+1\dots\infty$ we may write$$
P\left(k\right)=\frac{\lambda}{m\mu}P\left(k-1\right)$$using $\rho=\frac{\lambda}{m\mu}$ we then have$$
P\left(k\right)=\rho P\left(k-1\right)$$leading to $$
P\left(k\right)=\rho^{k-m}P\left(m\right).$$Finally we use (\ref{eq:probabilities}) and substitute $k$ with $m$ to find $P\left(m\right)$ which leads to$$
P\left(m\right)=\frac{\left(m\rho\right)^{m}}{m!}P\left(0\right)$$therefore 
P\left(k\right)=\frac{m^{m}\rho^{k}}{m!}P\left(0\right) & \textrm{for} & k>mthus we can write$$
P\left(k\right)=\left\{ {cc}
P\left(0\right)\frac{(m\rho)^{k}}{k!}, & k\leq m\\
P\left(0\right)\frac{m^{m}\rho^{k}}{m!} & k>m\right.$$
    [ht]
      \centering
      \figure{\includepng{\diagramsDir/npa/boundaryFlowMMm}{40%}}{boundaryFlowMMm}{boundaryFlowMMm}
      \caption{Flow rates at a boundary.}
      \label{cap:flowAtBoundaryMMmb}
    
    Once again we can compute $P\left(0\right)$ through normalisation
\sum_{k=0}^{\infty}P\left(k\right) & = & 1\\
P\left(0\right)\left[\sum_{k=0}^{m-1}\frac{\left(m\rho\right)^{k}}{k!}+\sum_{k=m}^{\infty}\frac{m^{m}\rho^{k}}{m!}\right] & = & 1\\
P\left(0\right) & = & \left[\sum_{k=0}^{m-1}\frac{\left(m\rho\right)^{k}}{k!}+\sum_{k=m}^{\infty}\frac{m^{m}\rho^{k}}{m!}\right]^{-1}.Consider the second term inside the bracket,$$
\sum_{k=m}^{\infty}\frac{m^{m}}{m!}\rho^{k}=\frac{m^{m}\rho^{m}}{m!}\sum_{k=m}^{\infty}\rho^{k-m}$$substitute in $k^{\prime}=k-m$ and we obtain$$
\frac{m^{m}\rho^{m}}{m!}\sum_{k^{\prime}=0}^{\infty}\rho^{k^{\prime}}=\frac{m^{m}\rho^{m}}{m!}\frac{1}{1-\rho}$$because, as we saw in Section\  \ref{sec:MM1Stationary} $$
\sum_{k=0}^{\infty}\rho^{k}=\frac{1}{1-\rho}$$ if $\rho<1$. Thus we have$$
P\left(0\right)=\left[\sum_{k=0}^{m-1}\frac{\left(m\rho\right)^{k}}{k!}+\frac{m^{m}\rho^{m}}{m!\left(1-\rho\right)}\right]^{-1}.$$Note that this relies on $\rho<1$, if $\lambda\geq m\mu$ the system has no stationary distribution.\}{0}}

\notes{### Answer}

\notes{#### $k\leq m$}

\notes{#### $k>m$}

\notes{### Normalisation Condition}

\notes{{1. Consider the telephone trunking problem. A telephone exchange A is to server 10,000 subscribers in a nearby exchange as shown in Figure\  \ref{fig:exchange}. Suppose that during the busy hour, the subscribers generate a Poisson traffic with a rate of 10 calls per minute, which requires trunk lines to exchange B for an average holding time of 3 minutes per call. Determine the number of trunk lines needed for a grade of service (probability of waiting) of 0.01.\label{example:telephoneTrunking}
  [ht]
    \centering
    \figure{\includepng{\diagramsDir/npa/exchange}{80%}}{exchange}{exchange}
    \caption{The telephone exchange.}
    \label{fig:exchange}
  
  [0]
    Average call rate is $\lambda=10$ calls/minute. Average holding time is $\tau=3$ minutes. Offered load $a=\lambda\tau$ is 30 Erlangs. From the Erlang C curves in Figure\  \ref{cap:erlangCOne} it looks to be about 44.\}{0}}

\notes{#### Answer}

\notes{1. A customer service centre has an average holding time, $\tau$, for calls of 8 minutes. In the busy hour, calls arrive at the centre at a rate of one very two minutes. Inter-arrival times and service times are exponentially distributed, how many personnel are required to keep the probability of waiting at 0.1.\label{example:customerService}
  [0]
    Average call rate is $\lambda=0.5$ calls/minute. Average holding time is $\tau=8$ minutes. Offered load is $a=\lambda\tau$ is 4 Erlangs. From the Erlang C curves in Figure\  \ref{cap:erlangCOne} it looks to be about 8.}

\notes{#### Answer}

\notes{{1. What is the average queueing time for Example\  \ref{example:customerService} above? What is the average queueing time for those customers who do queue? \label{example:erlangDelayWait}
  [0]
    The number of servers was $m=8$ and service rate was $\mu=\frac{1}{8}$. The utilization factor was $\rho=\frac{\lambda}{m\mu}=\frac{1}{2}$.
    The delay is $$
\bar{W}=\frac{C(m,a)}{m\mu(1-\rho)}.$$$\frac{0.6}{8\frac{1}{8}\left(1-\frac{1}{2}\right)}=0.2$ minutes, or 12 seconds.
    The queueing time for those who have to queue is $\frac{\bar{W}}{C(m,a)}$. For our example $\frac{\bar{W}}{0.1}=\frac{0.2}{0.1}=2$ minutes.\}{0}}

\notes{#### Answer}

\endif

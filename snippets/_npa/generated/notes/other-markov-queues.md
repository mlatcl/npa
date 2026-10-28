\ifndef{npaGenNotesOtherMarkovQueues}
\define{npaGenNotesOtherMarkovQueues}

\notes{\section{Finite Length $M$/$M$/$1$/$m$}}

\notes{In our analysis of the $M/M/1$ queue so far we have assumed that the queue can have an infinite length, in practice a restricted buffer size may mean that the queue length is also restricted. Let's assume the queue can contain at maximum $m-1$ customers (as shown in Figure\  \ref{cap:stateDiagramMM1m}). This means (because one customer can be under service) there is a maximum of $m$ customers in the system. In the Example\  \ref{example:otherQueuesStationary} at the end of this chapter we derive the stationary distribution for this queue. Then, in Example\  \ref{example:otherQueuesBlocking}, we introduce the concept of blocking probability. The $M/M/1/m$ queue has limited capacity, that means it is a queue with `loss'. The carried load is *not the same* as the offered load because customers are rejected when the queue is full. These customers are assumed not to return.}

\notes{\section{Infinite Serving Capacity --- $M$/$M$/$\ensuremath{\infty}$}}

\notes{In the $M/M/1$ queue we assume that there is only one server. In some cases it can be useful to consider an unlimited number of servers so that there is one server for every customer in the system. The state diagram for this system can be drawn as in Figure\  \ref{cap:stateDiagramMMinf}}

\figure{\includepng{\diagramsDir/npa/stateMMinf}{100%}}{State diagram for the $M/M/\infty$ queue.}{cap:stateDiagramMMinf}

\notes{\subsection{Detailed Balance}}

\notes{We again make use of the standard detailed balance equations for this queue. From the flow rates at the boundary we have, in general,}

\figure{\includepng{\diagramsDir/npa/boundaryFlowMMinf}{60%}}{Flow rates at a boundary for $M/M/\infty$ queue.}{cap:flowAtBoundaryMMinf}

\notes{$$
\lambda_{k-1}P\left(k-1\right)=\mu_{k}P\left(k\right).$$Since there is infinite service capacity in the queue the service rate at state $k$ is simply $\mu_{k}=k\ensuremath{\mu}$. The rate of arrivals stays constant, $\lambda_{k}=\ensuremath{\lambda}$, so for this queue detailed balance gives.$$
\ensuremath{\lambda} P\left(k-1\right)=k\ensuremath{\mu} P\left(k\right)$$Reorganising in terms of $P\left(k\right)$ then gives$$
P\left(k\right)=\ensuremath{\frac{\lambda}{k\mu}}P\left(k-1\right)$$and therefore$$
P\left(k\right)=P\left(0\right)\left(\ensuremath{\frac{\lambda}{\mu}\right)^{k}\frac{1}{k!}}.$$}

\notes{\subsection{Normalisation Condition}}

\notes{Using the normalisation condition for this queue, $$
\sum_{k=0}^{\ensuremath{\infty}}P\left(k\right)=1,$$we obtain $P\left(0\right)$ as $$
P\left(0\right)=\left[\sum_{k=0}^{\ensuremath{\infty}}\left(\ensuremath{\frac{\lambda}{\mu}\right)^{k}\frac{1}{k!}\right]^{-1}}.\label{eq:MMinftyP0}$$}

\notes{\subsubsection{The Offered Load\label{sub:offeredLoad}}}

\notes{It is convenient in this (and later queues) to define the offered load, $a=\ensuremath{\frac{\lambda}{\mu}}$, as arrival rate divided by service rate. This is a dimensionless constant, but has international standard units of Erlangs (after A.\  K.\  Erlang). Substituting this definition back into (\ref{eq:MMinftyP0}) we have, $$
P\left(0\right)=\left[\sum_{k=0}^{\ensuremath{\infty}}\ensuremath{\frac{a^{k}}{k!}\right]^{-1}}.$$Recalling from Section\  \ref{sub:poissonMeanVar} that $$
\sum_{n=0}^{\ensuremath{\infty}}\ensuremath{\frac{x^{n}}{n!}}=\ensuremath{\exp\left(}x\right)$$ we have$$
P\left(0\right)=\ensuremath{\exp\left(}-a\right)$$and the steady state distribution is then$$
P\left(k\right)=\ensuremath{\frac{a^{k}}{k!}\exp\left(}-a\right)$$which is recognised as a Poisson distribution with parameter $a$. Notice that the utilization factor for this queue, $\ensuremath{\rho}$, is *not* equal to $\ensuremath{\frac{\lambda}{\mu}}$ (which is referred to as the offered load). In fact for the $M/M/\ensuremath{\infty}$ queue the offered load can be much larger than 1 but we know that the utilization factor is never greater than $1$. The utilization factor doesn't make much sense for this queue because there are infinite servers: but we can study the probabililty that the system is in use, which is one minus the probability that the queue is empty,$$
1-P\left(0\right),$$The proportion of time that any portion of the system is in use is therefore $$
1-P\left(0\right)=1-\ensuremath{\exp\left(}-a\right).$$}

\notes{## Examples}

\notes{1. Derive the steady state distribution for the $M/M/1/m$ queue.\label{example:otherQueuesStationary}
  
    
    }

\figure{\includepng{\diagramsDir/npa/stateMM1m}{80%}}{stateMM1m}{stateMM1m}

\notes{
    
    \label{cap:stateDiagramMM1m}
  
  [0]
    The balance equation for the $M/M/1/m$ is identical to that for the $M/M/1$ (Section\  \ref{sec:MM1Stationary}). The first step is to draw the flow rates at the boundary (Figure\  \ref{cap:flowAtBoundaryMM1m}).
    At steady state, the expected flow from $k-1$ to $k$ is given by $\ensuremath{\lambda} P\left(k-1\right)$. Flow from $k$ to $k-1$ is given $\ensuremath{\mu} P\left(k-1\right)$. For flow to be balanced we have $$
\ensuremath{\lambda} P\left(k-1\right)=\ensuremath{\mu} P\left(k\right)$$ leading to $$
P\left(k\right)=\ensuremath{\frac{\lambda}{\mu}}P\left(k-1\right).$$Substituting into the detailed balance equation we get$$
P\left(k\right)=\ensuremath{\frac{\lambda}{\mu}}P\left(k-1\right)$$ Thus 
    
      
      }

\figure{\includepng{\diagramsDir/npa/boundaryFlowMM1}{40%}}{boundaryFlowMM1}{boundaryFlowMM1}

\notes{
      
      \label{cap:flowAtBoundaryMM1m}
    
    In the case of the finite length queue the normalisation is computed with a sum over only $m$ states, rather than $\ensuremath{\infty}$ states. This leads to a different value for $P\left(0\right)$. We compute $P\left(0\right)$ by writing the sum across all the $m+1$ states of the distribution, $$
\sum_{k=0}^{m}P\left(0\right)\ensuremath{\rho^{k}}=1.$$This leads us to $$
P\left(0\right)=\sum_{k=0}^{m}\ensuremath{\frac{1}{\rho^{k}}}$$which is recognised as the *finite*sum of a geometric series,$$
\sum_{k=0}^{m}\ensuremath{\frac{1}{\rho^{k}}}=\ensuremath{\frac{1-\rho}{1-\rho^{m+1}}}$$so we have$$
P\left(0\right)=\ensuremath{\frac{1-\rho}{1-\rho^{m+1}}}$$which leads to $$
P\left(k\right)=\ensuremath{\frac{\rho^{k}\left(1-\rho\right)}{1-\rho^{m+1}}}.$$

| P\left(k\right) | = | \left(\ensuremath{\frac{\lambda}{\mu}\right)^{k}}P\left(0\right) |
| --- | --- | --- |
|  | = | \ensuremath{\rho^{k}}P\left(0\right). |}


\notes{### Normalisation}

\notes{1. **Blocking Probabilities.** Given a finite length $M$/$M$/$1$/$m$ queue, what is the probability that an arrival is blocked from joining the queue (and therefore lost). \label{example:otherQueuesBlocking}
  [0]
    This is answered by determining the probability of the queue being full, which means $$
P\left(m\right)=\ensuremath{\frac{\rho^{m}\left(1-\rho\right)}{1-\rho^{m+1}}}$$}

\endif

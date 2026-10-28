\ifndef{npaGenNotesErlangLoss}
\define{npaGenNotesErlangLoss}

\figure{\includepng{\diagramsDir/npa/erlangLossFlowChart}{80%}}{Flow chart of the Erlang Loss System.}{cap:erlangLossFlowChart}

\notes{The system is a limited capacity system. The maximum number in the system is $m$ which means the maximum queue size is zero because there are $m$ servers. In the diagram it shows the offered load is $a$, while the carried load, $a^{\prime}$, is less than $a$ because some packets are rejected, just as they were for the $M/M/1/m$ queue.}

\notes{\section{Stationary Distribution}}

\notes{The system is shown as a flow chart in Figure\  \ref{cap:erlangLossFlowChart}. The Erlang loss system may be analysed as a birth-death process with birth rate $$
\lambda_{k}=\left\{ \begin{array}{cc}
\ensuremath{\lambda} & k=0,1,\ensuremath{\dots},m-1\\
0 & k\ensuremath{\geq} m\end{array}\right.$$ and death rate $$
\mu_{k}=\left\{ \begin{array}{cc}
k\ensuremath{\mu} & k=0,1,\ensuremath{\dots},m\\
0 & k>m\end{array}\right.$$ *Note: when*$k>m$*, it doesn't matter what*$\mu_{k}$*is as we never reach this state.*}}}

\notes{\subsection{State Diagram}}

\figure{\includepng{\diagramsDir/npa/erlangLoss}{100%}}{Markov chain for the Erlang loss system, $M$/$M$/$m$/$m$}{erlangLoss}

\notes{The offered load, $a=\ensuremath{\frac{\lambda}{\mu}}$, is again dimensionless with units of Erlangs, however to compute the carried load we will first have to determine what the probability of a customer being blocked is.}

\notes{\section{Steady State Probabilities}}

\notes{When the system's state, $k$, is less than or equal to the number of servers we have boundary flow as in Figure\  \ref{cap:flowAtBoundaryMMmm}, which leads to the following balance equation
$$
\ensuremath{\lambda} P\left(k-1\right)=k\ensuremath{\mu} P\left(k\right).$$}

\figure{\includepng{\diagramsDir/npa/boundaryFlowMMinf}{40%}}{Flow rates at a boundary.}{cap:flowAtBoundaryMMmm}

\notes{As a result, for $k=0\ensuremath{\dots} m$ we may write$$
P\left(k\right)=\ensuremath{\frac{\lambda}{k\mu}}P\left(k-1\right).\label{eq:PkForkLessThanM}$$
In contrast to the $M/M/m$ queue, the system state cannot go above $m$ so we have no need to consider the region where $k>m$. Substituting in the offered load for $\ensuremath{\frac{\lambda}{\mu}}$ we have,$$
\begin{aligned}
P\left(k\right) & = & \ensuremath{\frac{a}{k}}P(k-1),
\end{aligned}
$$ which means that $$
\begin{aligned}
P\left(k\right) & = & \prod_{n=1}^{k}\ensuremath{\frac{a}{n}}P\left(0\right)\\
 & = & \ensuremath{\frac{a^{k}}{k!}}P\left(0\right).
\end{aligned}
$$}

\notes{\subsection{Normalisation Condition}}

\notes{The normalisation condition gives us $$
P\left(0\right)\sum_{k=0}^{m}\ensuremath{\frac{a^{k}}{k!}}=1$$$$
P\left(0\right)=\ensuremath{\frac{1}{\sum_{k=0}^{m}\frac{a^{k}}{k!}}},$$which leads to the *truncated Poisson distribution*:$$
P\left(k\right)=\ensuremath{\frac{\frac{a^{k}}{k!}}{\sum_{n=0}^{m}\frac{a^{n}}{n!}}}.$$ *Note if*$m\ensuremath{\rightarrow\infty}$*we recover the* $M/M/\ensuremath{\infty}$*queue as we would expect.*}

\notes{\section{Probability of Blocking}}

\notes{For the $M/M/m$ queue we were interested in the probability that a customer would have to wait in the queue for service. In the $M/M/m/m$ system there is no queue because the maximum state of the system is the same as the number of servers. The probability of waiting is therefore zero. Of more interest is the probability of blocking: the probability that when we arrive the system is full and we are denied service. As we discussed for the $M/M/1/m$ queue the blocking probability is given by $P\left(m\right)$, the steady state probability that the system is full. This is given as$$
B(m,a)=P\left(m\right)=\ensuremath{\frac{\frac{a^{m}}{m!}}{\sum_{n=0}^{m}\frac{a^{n}}{n!}}}.$$We have already discussed for the Erlang C system the problems of computing this quantity on a computer. They may be resolved in much the same way through computation in $\ensuremath{\log}$ space. Again we will turn to curves for use in exam questions and exercises. Erlang B curves plot the blocking probability for different numbers of servers as a function of the offered load.}

\figure{\includepng{\diagramsDir/npa/erlangBCurves0to20}{100%}}{Erlang B curves.}{erlangBCurves0to20}

\figure{\includepng{\diagramsDir/npa/erlangBCurves0to100}{100%}}{Erlang B curves.}{erlangBCurves0to100}

\notes{\section{Carried Load and Utilization Factors}}

\notes{Since traffic is lost in $M/M/m/m$ the carried load, $a^{\prime}$, is smaller than the offered load. The carried load is given by the offered load multiplied by the probability that the packet is not blocked. $$
a^{\prime}=a(1-P\left(m\right))=a(1-B(m,a)).$$ The carried load per line is the trunk occupancy, $$
\ensuremath{\rho}=\ensuremath{\frac{a^{\prime}}{m}},$$ also known as the utilization factor. Note the contrast with the lossless systems where the trunk occupancy (or utilization factor) was given by $$
\ensuremath{\rho}=\ensuremath{\frac{a}{m}}$$because the carried load is equal to the offered load $a^{\prime}=a$. When computing utilization factors for lossy systems we have to take this loss into account (for example in the $M/M/1/m$ queue). Also note that the rate of service in the system is no longer given by the arrival rate, $\ensuremath{\lambda}$, we need to consider those packets that are lost. This means the rate of service is given by $$
\dot{\ensuremath{\lambda}}=\ensuremath{\lambda(1-P\left(m\right))}$$where $P\left(m\right)$ is the blocking probability. This has effects when studying the queue using Little's formula. When using Little's formula with a lossy system, the rate we use should be the service rate, *not* the arrival rate. Packets which are blocked by the system do not enter it and therefore have no effect on the system's state.}

\notes{## Examples}

\notes{1. **Load Tripling**\label{example:loadTripling}. In this example we will briefly consider the effect of increasing load in an Erlang Loss system.
2. For a blocking probability of 0.01, what is the number of trunks needed for 6 Erlangs of offered load?
3. For a blocking probability of 0.01, what is the number of trunks needed for 18 Erlangs?
4. Comment on the increase in load compared to the increase in the number of trunks.
  
  [0]
5. 13
6. 28
7. A load increase of 200 % only lead to a trunk increase of 133 %. To understand this further we look at the utilization factors. For the first system the utilisation factor is $$
\rho_{1}=6\left(1-0.005\right)=0.459$$whereas for the second system the utilisation factor is$$
\rho_{2}=18\left(1-0.007\right)=0.6384$$The 30 trunk system is thus more efficient. This explains why it is cheaper to call the U.S.A. than Italy.}


\notes{1. **Example**$M/M/m/n$. This example is from the Exam paper in 2002-3.
  A call centre employs thirty operators selling tickets for a major sporting event. The call centre has sixty lines in total. When all operators are active new calls are placed in a queue for the first available operator. The call centre is to be modelled as an $M/M/m/n$ queue, *i.e.* a queue in which there are $m$ servers and a maximum state of $n$.
2. Draw a state diagram representing the queueing system.
    [0]
      
        
        \includegraphics{}
3. Write down the detailed balance equations for the two cases where the queue state $k<m$ and when $m\ensuremath{\leq} k<n$.
    [0]
      When the system's state, $k$, is less than or equal to the number of servers we have boundary flow as in Figure\  \ref{cap:flowAtBoundaryMMma},which leads to the following balance equation $$
\ensuremath{\lambda} P\left(k-1\right)=k\ensuremath{\mu} P\left(k\right).$$As a result, for $k=0\ensuremath{\dots} m$ we may write
P\left(k\right)=\ensuremath{\frac{\lambda}{k\mu}}P\left(k-1\right).\label{eq:PkForPartAExercise}
      
        
        }

\figure{\includepng{\diagramsDir/npa/boundaryFlowMMinf}{40%}}{boundaryFlowMMinf}{boundaryFlowMMinf}

\notes{
        
        \label{cap:flowAtBoundaryMMma}
      
      The detailed balance for this case is$$
P\left(k\right)=\ensuremath{\frac{\lambda}{m\mu}}P\left(k-1\right)$$
      When the system's state is greater than $m$, $k>m$ the flow at the boundary is as in Figure\  \ref{cap:flowAtBoundaryMMmb}, the detailed balance equation is thenwhich leads to $$
\ensuremath{\lambda} P(k-1)=m\ensuremath{\mu} P\left(k\right)$$
      
        
        }

\figure{\includepng{\diagramsDir/npa/boundaryFlowMMm}{40%}}{boundaryFlowMMm}{boundaryFlowMMm}

\notes{
        
        \label{cap:flowAtBoundaryMMmb}
4. For each of the two cases outlined in the previous part write down the steady state distribution as a function of $P\left(0\right)$, the probability of the system being empty.
    [0]
      From Detailed Balance we may write$$
P\left(k\right)=\ensuremath{\frac{\lambda}{k\mu}}P\left(k-1\right).$$And defining $$
a=\ensuremath{\frac{\lambda}{\mu}}$$which in turn gives $$
\ensuremath{\frac{\lambda}{k\mu}}=\ensuremath{\frac{a}{k}}$$which we substitute back into the detailed balance obtaining$$
P\left(k\right)=\ensuremath{\frac{a}{k}}P\left(k-1\right)$$and as before
P\left(k\right)=\ensuremath{\frac{a^{k}}{k!}}P\left(0\right) & \textrm{for} & k\ensuremath{\leq} m\label{eq:probabilitiesExercise}
      The detailed balance for this case is$$
P\left(k\right)=\ensuremath{\frac{\lambda}{m\mu}}P\left(k-1\right)$$substituting for $a$ gives$$
P\left(k\right)=\ensuremath{\frac{a}{m}}P\left(k-1\right)$$
      leading to $$
P\left(k\right)=\left(\ensuremath{\frac{a}{m}\right)^{k-m}}P\left(m\right).$$Finally we use (\ref{eq:probabilitiesExercise}) and substitute $k$ with $m$ to find $P\left(m\right)$ which leads to$$
P\left(m\right)=\ensuremath{\frac{a^{m}}{m!}}P\left(0\right)$$therefore 
P\left(k\right)=\ensuremath{\frac{a^{k}}{m^{k-m}m!}}P\left(0\right) & \textrm{for} & k>mthus we can write$$
P\left(k\right)=\begin{array}{cc}
P\left(0\right)\ensuremath{\frac{a^{k}}{k!}}, & k\ensuremath{\leq} m\\
P\left(0\right)\ensuremath{\frac{a^{k}}{m^{k-m}m!}} & k>m\end{array}$$
5. Use the fact that the steady state distribution must be normalised to show that $$
P\left(0\right)=\left[\sum_{k=0}^{m}\ensuremath{\frac{a^{k}}{k!}}+\sum_{k=m+1}^{n}\ensuremath{\frac{a^{k}}{m!m^{k-m}}\right]^{-1}}$$where $a=\ensuremath{\frac{\lambda}{\mu}}$, $\ensuremath{\lambda}$ is the arrival rate and $\ensuremath{\mu}$ is the rate of the service time distribution.
    [0]
      Once again we can compute $P\left(0\right)$ through normalisation
\sum_{k=0}^{\ensuremath{\infty}}P\left(k\right) & = & 1\\
P\left(0\right)\left[\sum_{k=0}^{m}\ensuremath{\frac{a^{k}}{k!}}+\sum_{k=m+1}^{n}\ensuremath{\frac{a^{k}}{m!m^{k-m}}\right]} & = & 1\\
P\left(0\right) & = & \left[\sum_{k=0}^{m}\ensuremath{\frac{a^{k}}{k!}}+\sum_{k=m+1}^{n}\ensuremath{\frac{a^{k}}{m!m^{k-m}}\right]^{-1}}.}



\notes{#### Case 1) $k\ensuremath{\leq} m$}

\notes{#### Case 2) $m<k\ensuremath{\leq} n$.}


\notes{#### Case 1) $k\ensuremath{\leq} m$}

\notes{#### Case 2) $m<k\ensuremath{\leq} n$.}

\endif

\ifndef{npaGenSlidesOtherMarkovQueues}
\define{npaGenSlidesOtherMarkovQueues}

\newslide{Other Markov Queues}

\slides{* The $M/M/1$ queue is perhaps the simplest Markov queue.
* We will introduce two related Markov queues and compute their stationary distributions.}

\newslide{Other Markov Queues (continued)}

\slides{* A simple modification to the $M/M/1$ queue: a *finite length*modification $M/M/1/m$
* The *infinite server*queue*,*$M/M/\ensuremath{\infty}$.}

\newslide{Finite Length $M$/$M$/$1$/$m$}

\slides{\figure{\includepng{\diagramsDir/npa/stateMM1m}{100%}}{State diagram for the $M/M/1/m$ queue. Note that there are no transitions to states above the $m$th state.}{cap:stateDiagramMM1m}}

\newslide{Finite Length $M$/$M$/$1$/$m$ (continued)}

\slides{* We have assumed that $M/M/1$ queue can have an infinite length.
* In practice a restricted buffer size --- perhaps queue length is also restricted.
* We assume the system can contain at maximum $m$ customers (*i.e.*the queue can contain $m-1$).}

\newslide{Examples}

\slides{* Example 1: Derive the stationary distribution for this queue.
* Example 2: Blocking probabilities}

\newslide{Infinite Serving Capacity --- $M$/$M$/$\infty$}

\slides{* The $M/M/1/m$ queue covers the case where the queue length is bounded.
* We can also derive when the number of servers is *unbounded*.
* In the $M/M/1$ queue we assume that there is only one server.}

\newslide{Infinite Serving Capacity --- $M$/$M$/$\infty$ (continued)}

\slides{* It can be useful to consider an unlimited number of servers:
* One server for every customer in the system.
* The state diagram for this system can be drawn.
      \label{cap:stateDiagramMMinf}}

\slides{\figure{\includepng{\diagramsDir/npa/stateMMinf}{100%}}{State diagram for the $M/M/\ensuremath{\infty}$ queue.}{cap:stateDiagramMMinf}}

\newslide{Detailed Balance}

\slides{\figure{\includepng{\diagramsDir/npa/boundaryFlowMMinf}{60%}}{Flow rates at a boundary for $M/M/\ensuremath{\infty}$ queue.}{cap:flowAtBoundaryMMinf}}

\newslide{Detailed Balance (continued)}

\slides{* Make use of the standard detailed balance equations for this queue.
* From the flow rates at the boundary we have in general$$
\lambda_{k-1}P\left(k-1\right)=\mu_{k}P\left(k\right)$$
* There is infinite service capacity in the queue the service rate at state $k$ is simply $\mu_{k}=k\ensuremath{\mu}$.
* The rate of arrivals stays constant, $\lambda_{k}=\ensuremath{\lambda}$, so for this queue detailed balance gives.$$
\ensuremath{\lambda} P\left(k-1\right)=k\ensuremath{\mu} P\left(k\right)$$
* Reorganising in terms of $P\left(k\right)$ then gives$$
P\left(k\right)=\ensuremath{\frac{\lambda}{k\mu}}P\left(k-1\right)$$and therefore$$
P\left(k\right)=P\left(0\right)\left(\ensuremath{\frac{\lambda}{\mu}\right)^{k}\frac{1}{k!}}.$$}

\newslide{Normalisation Condition}

\slides{* Using the normalisation condition for this queue, $$
\sum_{k=0}^{\ensuremath{\infty}}P\left(k\right)=1,$$we obtain $P\left(0\right)$ as 
P\left(0\right)=\left[\sum_{k=0}^{\ensuremath{\infty}}\left(\ensuremath{\frac{\lambda}{\mu}\right)^{k}\frac{1}{k!}\right]^{-1}}.\label{eq:MMinftyP0}}

\newslide{The Offered Load\label{sub:offeredLoad}}

\slides{* It is convenient to define the offered load, $$
a=\ensuremath{\frac{\lambda}{\mu}}$$as arrival rate divided by service rate.
* This is a dimensionless constant, but has international standard units of Erlangs (after A.\  K.\  Erlang).}

\newslide{The Offered Load\label{sub:offeredLoad} (continued)}

\slides{* Substituting this definition back into (\ref{eq:MMinftyP0}) we have, $$
P\left(0\right)=\left[\sum_{k=0}^{\ensuremath{\infty}}\ensuremath{\frac{a^{k}}{k!}\right]^{-1}}.$$
* Recalling that $$
\sum_{n=0}^{\ensuremath{\infty}}\ensuremath{\frac{x^{n}}{n!}}=\ensuremath{\exp\left(}x\right)$$ we have$$
P\left(0\right)=\ensuremath{\exp\left(}-a\right)$$and the steady state distribution is then$$
P\left(k\right)=\ensuremath{\frac{a^{k}}{k!}\exp\left(}-a\right)$$
* Which is recognised as a Poisson distribution with parameter $a$.}

\newslide{Utilization Factor}

\slides{* Notice that the utilization factor for this system, $\ensuremath{\rho}$, doesn't really exist.
* For the $M/M/\ensuremath{\infty}$ there is infinite capacity so we can't ask what percentage is in use!
* The proporation of time that some part of the system is in use is$$
1-P\left(0\right)=1-\ensuremath{\exp\left(}-a\right).$$}

\endif

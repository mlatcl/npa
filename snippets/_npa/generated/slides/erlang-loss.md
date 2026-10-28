% generated — do not edit; scripts/convert/run.py
\ifndef{npaGenSlidesErlangLoss}
\define{npaGenSlidesErlangLoss}

<!-- original A4 foil 138: Erlang Loss $M$/$M$/$m$/$m$ -->

\newslide{Erlang Loss $M$/$M$/$m$/$m$}

\figure{\includepng{\diagramsDir/npa/erlangLossFlowChart}{80%}}{Flow chart of the Erlang Loss System.}{cap:erlangLossFlowChart}

<!-- original A4 foil 138: Erlang Loss $M$/$M$/$m$/$m$ -->

\newslide{Erlang Loss $M$/$M$/$m$/$m$ (continued)}

\slides{* The Erlang delay system contained $m$ servers.
* It was assumed that, if all servers were occupied, the customer would be placed on hold until a server became available.
* In the $M/M/m/m$ system there is a maximum number of customers.}

<!-- original A4 foil 139: State Diagram -->

\newslide{State Diagram}

\figure{\includepng{\diagramsDir/npa/erlangLoss}{100%}}{State Diagram for the Erlang loss system, $M$/$M$/$m$/$m$}{erlangLoss}

<!-- original A4 foil 139: State Diagram -->

\newslide{State Diagram (continued)}

\slides{* The offered load, $a=\frac{\lambda}{\mu}$, is again dimensionless with units of Erlangs.
* The Erlang loss system may be analysed as a birth-death process with birth rate \answer{$$
\lambda_{k}=\left\{ {cc}
\lambda & k=0,1,\dots,m-1\\
0 & k\geq m\right.$$\}{4}
* And death rate \answer{$$
\mu_{k}=\left\{ {cc}
k\mu & k=0,1,\dots,m\\
0 & k>m\right.$$\}{4}}}}

<!-- original A4 foil 140: Detailed Balance Equations -->

\newslide{Detailed Balance Equations}

\slides{* When the system's state, $k\leq m$, we have boundary flow as below
    [ht]
      \centering
      \caption{\answer{\}{6}Flow rates at a boundary.}
      \label{cap:flowAtBoundaryMMmm}
* This leads to the following balance equation $$
\lambda P\left(k-1\right)=k\mu P\left(k\right).$$}

\figure{\includepng{\diagramsDir/npa/boundaryFlowMMinf}{60%}}{boundaryFlowMMinf}{boundaryFlowMMinf}

<!-- original A4 foil 140: Detailed Balance Equations -->

\newslide{Detailed Balance Equations (continued)}

\slides{* So for $k=0\dots m$ we may write
P\left(k\right)=\frac{\lambda}{k\mu}P\left(k-1\right).\label{eq:PkForkLessThanM}
* The system state cannot go above $m$ so we have no need to consider the region where $k>m$. Substituting in the offered load we have,
P\left(k\right) & = & \frac{a}{k}P(k-1), which means that 
P\left(k\right) & = & \prod_{n=1}^{k}\frac{a}{n}P\left(0\right)\\
 & = & \frac{a^{k}}{k!}P\left(0\right).}

<!-- original A4 foil 141: Normalisation Condition -->

\newslide{Normalisation Condition}

\slides{* The normalisation condition gives us $$
P\left(0\right)\sum_{k=0}^{m}\frac{a^{k}}{k!}=1$$$$
P\left(0\right)=\frac{1}{\sum_{k=0}^{m}\frac{a^{k}}{k!}},$$
* Which leads to the truncated Poisson distribution $$
P\left(k\right)=\frac{\frac{a^{k}}{k!}}{\sum_{n=0}^{m}\frac{a^{n}}{n!}}$$
* *Note if *$m\rightarrow\infty$* we recover the* $M/M/\infty$* queue as we would expect.*}

<!-- original A4 foil 142: Probability of Blocking -->

\newslide{Probability of Blocking}

\slides{* For the $M/M/m$ queue we were interested in the probability that a customer would have to wait in the queue for service.
* In the $M/M/m/m$ system there is no queue because the maximum state of the system is the same as the number of servers.
* The probability of waiting is therefore zero.}

<!-- original A4 foil 142: Probability of Blocking -->

\newslide{Probability of Blocking (continued)}

\slides{* The probability of blocking is of interest: the probability that when we arrive the system is full and we are denied service.
* As we discussed for the $M/M/1/m$ queue the blocking probability is given by $P\left(m\right)$$$
B(m,a)=P\left(m\right)=\frac{\frac{a^{m}}{m!}}{\sum_{n=0}^{m}\frac{a^{n}}{n!}}.$$
* Use Erlang B curves to compute.}

<!-- original A4 foil 143: Carried Load and Utilization Factors -->

\newslide{Carried Load and Utilization Factors}

\slides{* Since traffic is lost in $M/M/m/m$ the carried load, $a^{\prime}$, is smaller than the offered load.
* The carried load is given by the offered load multiplied by the probability that the packet is not blocked. $$
a^{\prime}=a(1-P\left(m\right))=a(1-B(m,a))$$
* The carried load per line is the trunk occupancy (the utilization facctor), $$
\rho=\frac{a^{\prime}}{m}.$$}

<!-- original A4 foil 143: Carried Load and Utilization Factors -->

\newslide{Carried Load and Utilization Factors (continued)}

\slides{* Note the contrast with the lossless systems where $$
\rho=\frac{a}{m}$$because the carried load is equal to the offered load $a^{\prime}=a$.
* This also applies for the other system with loss we have seen, the $M/M/1/m$ queue.
* The rate of service in the system is no longer given by the arrival rate, $\lambda$, we need to consider those packets that are lost. $$
\dot{\lambda}=\lambda(1-P\left(m\right))$$
* This has effects when studying the queue using Little's formula.}

<!-- original A4 foil 144: Load Tripling -->

\newslide{Load Tripling}

\slides{* **Question**}

<!-- original A4 foil 144: Load Tripling -->

\newslide{Load Tripling (continued)}

\slides{1. For a blocking probability of 0.01, what is the number of trunks needed for 6 Erlangs of offered load?
2. For a blocking probability of 0.01, what is the number of trunks needed for 18 Erlangs?
3. Comment on the increase in load compared to the increase in the number of trunks.}

<!-- original A4 foil 145: Answer -->

\newslide{Answer}

\slides{1. 13
2. 28
3. A tripling in load only leads to a (just over doubling) of the resources required. To understand this further we look at the utilization factors. For the first system the utilisation factor is $$
\rho_{1}=\frac{6}{13}\left(1-0.005\right)=0.459$$whereas for the second system the utilisation factor is$$
\rho_{2}=\frac{18}{28}\left(1-0.007\right)=0.6384$$The 30 trunk system is thus more efficient. This explains why it is cheaper to call the U.S.A. than Italy.}

<!-- original A4 foil 145: Answer -->

\newslide{Answer (continued)}

\slides{* \end{answer}}

<!-- original A4 foil 146: Example $M/M/m/n$ -->

\newslide{Example $M/M/m/n$}

\slides{* This example is from the Exam paper in 2002-3.}

<!-- original A4 foil 146: Example $M/M/m/n$ -->

\newslide{Example $M/M/m/n$ (continued)}

\slides{* Question
1. A call centre employs thirty operators selling tickets for a major sporting event. The call centre has sixty lines in total. When all operators are active new calls are placed in a queue for the first available operator. The call centre is to be modelled as an $M/M/m/n$ queue, *i.e. * a queue in which there are $m$ servers and a maximum state of $n$.
2. Draw a state diagram representing the queueing system.
3. Write down the detailed balance equations for the two cases where the queue state $k<m$ and when $m\leq k<n$.
4. For each of the two cases outlined in the previous part write down the steady state distribution as a function of $P\left(0\right)$, the probability of the system being empty.
5. Use the fact that the steady state distribution must be normalised to show that $$
P\left(0\right)=\left[\sum_{k=0}^{m}\frac{a^{k}}{k!}+\sum_{k=m+1}^{n}\frac{a^{k}}{m!m^{k-m}}\right]^{-1}$$where $a=\frac{\lambda}{\mu}$, $\lambda$ is the arrival rate and $\mu$ is the rate of the service time distribution.}

\endif

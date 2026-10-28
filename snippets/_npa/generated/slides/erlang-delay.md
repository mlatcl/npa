\ifndef{npaGenSlidesErlangDelay}
\define{npaGenSlidesErlangDelay}

\newslide{Erlang Delay $M$/$M$/$m$}

\slides{\figure{\includepng{\diagramsDir/npa/erlangDelayDiagram}{80%}}{Queueing model of the Erlang delay system.}{cap:erlangDelaySchematic}}

\newslide{Erlang Delay $M$/$M$/$m$ (continued)}

\slides{* We have considered the situation were there are as many servers as there are customers.
* More realistic real world situations involve limited numbers of servers.
* For example, call centres.
* The system is known as the *Erlang delay* system. In Kendall's notation it is written $M/M/m$.
* The `average holding time', $\tau=\ensuremath{\frac{1}{\mu}\equiv\bar{X}}$, which, for a network involving telephones is the time a call is open.}

\newslide{State Diagram}

\slides{\figure{\includepng{\diagramsDir/npa/erlangDelay}{100%}}{State diagram of an Erlang delay system.}{erlangDelay}}

\newslide{State Diagram (continued)}

\slides{* The `death rate' $\mu_{k}$ has different definitions in different parts of the state space.
* We need to consider detailed balance for each part in turn.}

\newslide{Detailed Balance}

\slides{* The Erlang delay system may be analysed as a birth-death process with birth rate $$
\lambda_{k}=\ensuremath{\lambda}$$ and death rate $$
\mu_{k}=\begin{array}{cc}
k\ensuremath{\mu} & k=0,1,\ensuremath{\dots},m-1\\
m\ensuremath{\mu} & k>m\end{array}$$}

\newslide{The Two Situations}

\slides{* This means we have to consider two situations in detailed balance
* When the system's state, $k$, is less than or equal to the number of servers.
* When the system's state, $k$, is greater than the number of servers.
    We will cover this as an example.}

\newslide{Stationary Distribution}

\slides{* The overall stationary distribution is then$$
P\left(k\right)=\begin{array}{cc}
P\left(0\right)\ensuremath{\frac{(m\rho)^{k}}{k!}}, & k\ensuremath{\leq} m\\
P\left(0\right)\ensuremath{\frac{m^{m}\rho^{k}}{m!}} & k>m\end{array}$$
    $$
P\left(0\right)=\left[\sum_{k=0}^{m-1}\ensuremath{\frac{\left(m\rho\right)^{k}}{k!}}+\ensuremath{\frac{\left(m\rho\right)^{m}}{m!\left(1-\rho\right)}\right]^{-1}}.$$Note that this relies on $\ensuremath{\rho}<1$, if $\ensuremath{\lambda\geq} m\ensuremath{\mu}$ the system has no stationary distribution.}

\newslide{Probability of Waiting}

\slides{* For the $M/M/m$ queue a key quantity of interest is the probability of of a customer queueing, $P_{Q}$.
* What is the probability, when the system is at steady state, that a customer will arrive and find all the $m$ servers busy? 
P\left(k\ensuremath{\geq} m\right)=P\left(0\right)\sum_{k=m}^{\ensuremath{\infty}}\ensuremath{\frac{m^{m}\rho^{k}}{m!}}$$$$
P\left(k\ensuremath{\geq} m\right)=P\left(0\right)\ensuremath{\frac{\left(\rho m\right)^{m}}{m!}\sum_{k=m}^{\infty}\rho^{k-m}},$$

| P\left(k\ensuremath{\geq} m\right) | = | \sum_{k=m}^{\ensuremath{\infty}}P\left(k\right)$$ |
| --- | --- | --- |}

\newslide{Probability of Waiting contd}

\slides{* Substituting $\dot{k}=k-m$ in the sum gives$$
P\left(k\ensuremath{\geq} m\right)=P\left(0\right)\ensuremath{\frac{\left(\rho m\right)^{m}}{m!}\sum_{\dot{k}=1}^{\infty}\rho^{\dot{k}}},$$
* Making the usual substitution this can be re-written
C\left(m,a\right)=P\left(k\ensuremath{\geq} m\right)=P\left(0\right)\ensuremath{\frac{\left(\rho m\right)^{m}}{m!\left(1-\rho\right)}}.\label{eq:ErlangCone}}

\newslide{Erlang C Formula}

\slides{* This is known as the *Erlang C formula*, or Erlang's second formula after A.K. Erlang. By making use of our definition of $a$ we can rewrite the offered load as$$
a=\ensuremath{\frac{\lambda}{\mu}}=m\ensuremath{\rho}$$ and substituting into (\ref{eq:ErlangCone}) we have $$
C(m,a)=\ensuremath{\frac{P\left(0\right)a^{m}}{m!\left(1-\frac{a}{m}\right)}}.$$}

\newslide{Computing the Erlang C Formula}

\slides{* Can be computed on a computer: but
* some care must be taken when computing it.}

\newslide{Computing the Erlang C Formula (continued)}

\slides{* when $m$ is large overflow problems will occur for $a^{m}$ and $m!$.
* Compute the formula in log space,$$
\ensuremath{\ln} C\left(m,a\right)=\ensuremath{\ln} P\left(0\right)+m\ensuremath{\ln} a-\ensuremath{\ln} m!-\ensuremath{\ln\left(}1-\ensuremath{\frac{a}{m}\right)}.$$Still problems with $\ensuremath{\ln} P\left(0\right)$ term, but each of the other terms can be computed with appropriate functions in Python (`scipy.special.gammaln`).
* When we need to compute the Erlang C curve, for the purposes of exams and exercises, we will use the old fashioned method of curves.}

\newslide{Erlang C Curves}

\slides{* We have provided you with two sets of curves in your notes.
* In an exam, if they are need curves will be provided with the exam paper.
* Make sure you mark the curves and hand them in with your paper.}

\newslide{Examples}

\slides{* Examples 2 and 3 at the end of the chapter cover the Erlang C curves.}

\newslide{Average number in System.}

\slides{* We can also compute the average number of calls in the Erlang Delay system, $$
\ensuremath{\bar{N}}=\ensuremath{\frac{\rho}{1-\rho}}C(m,a)+m\ensuremath{\rho}$$
* These two terms represent the average queue length and the average number of busy lines.
* The average queue length is given by $$
\ensuremath{\bar{N}_{Q}}=\ensuremath{\frac{\rho}{1-\rho}}C(m,a)$$}

\newslide{Average Queueing Time}

\slides{* Using Little's formula the average waiting time is simply $$
\ensuremath{\bar{W}}=\ensuremath{\frac{\bar{N}_{Q}}{\lambda}}=\ensuremath{\frac{C(m,a)}{m\mu(1-\rho)}}.$$
* Note that this is the average queueing time for all customers (whether they queued or not).}

\newslide{Queueing Time for those who Queue}

\slides{* Use the fact that the average queueing time for those who don't queue is zero.
* The average queueing time can be decomposed as$$
\ensuremath{\bar{W}}=C(m,a)\ensuremath{\bar{W}_{Q}}+\left(1-C(m,a)\right)\ensuremath{\bar{W}_{\sim Q}}$$}

\newslide{Queueing Time for those who Queue (continued)}

\slides{* $\ensuremath{\bar{W}_{Q}}$ is the average queueing time for those who do queue
* $\ensuremath{\bar{W}_{\sim Q}}$ is the average queueing time for those who don't queue.
* Since $\ensuremath{\bar{W}_{\sim Q}}=0$ the second term in this sum is zero we can rewrite in terms of $\ensuremath{\bar{W}_{Q}}$ as $$
\ensuremath{\bar{W_{Q}}}=\ensuremath{\frac{\bar{W}}{C(m,a)}}=\ensuremath{\frac{1}{m\mu(1-\rho)}}=\ensuremath{\frac{1}{\mu(m-a)}}$$so the average queueing time for those who do queue is independent of the probability of queueing.}

\newslide{Example}

\slides{* Example 4 at the end of the chapter
* So what is the average waiting time for the telephone service centre example? What is the queueing time for those who have to queue?}

\endif

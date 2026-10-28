% generated — do not edit; scripts/convert/run.py
\ifndef{npaGenSlidesBirthDeathMm1}
\define{npaGenSlidesBirthDeathMm1}

<!-- original A4 foil 52: Markov Chains and Markov Processes\label{cha:markovChainsAndProcesses} -->

\newslide{Markov Chains and Markov Processes\label{cha:markovChainsAndProcesses}}

\slides{* Poisson process in a special case of the more general class of processes known as Markov processes. We will start by considering Markov processes as they operate in *discrete time*, otherwise known as *Markov chains*. Both Markov processes and Markov chains exhibit the *Markov property *which is an assumption about how future values drawn from the process depend on past values. We will first discuss the Markov property in the context of Markov chains, then we will show how a discrete system can be converted to a continuous system.}

<!-- original A4 foil 53: Markov Chains -->

\newslide{Markov Chains}

\slides{* Consider a discrete representation of time $t=0,1,2...$. We associate a state variable, $N$, with this time such that we have values for $N$ at $N(0),\, N(1),\, N(2),\,...$.
* Turns in a board game.
* Markov Property}

<!-- original A4 foil 53: Markov Chains -->

\newslide{Markov Chains (continued)}

\slides{* value at time $t$ is dependent only on its value at time $t-1$.
* The future is conditional independent of the past (the conditioning being on the present).
* State of the system in the future is *not *dependent on what happened in the past if we know the state at the present time.}

<!-- original A4 foil 54: Monopoly -->

\newslide{Monopoly}

\slides{* A real-life example of a Markov chain
* Forty squares on a Monopoly board.
  [ht]
    \centering
    \caption{Image of a monopoly board.}}

\figure{\includepng{\diagramsDir/npa/smallMonopoly}{80%}}{smallMonopoly}{smallMonopoly}

<!-- original A4 foil 55: Markov Chain Monopoly -->

\newslide{Markov Chain Monopoly}

\slides{* Player's state, $N(t)$, square number +40$\times$number of `GO's
  Normally move through two six sided dice and adding them together. Denote the result of this die roll $d(t)$.
* State at time $t$ is
  $$
N(t)=N(t-1)+d(t).$$ Monopoly exhibits the Markov property, future states are independent of your previous states given your current state.}

<!-- original A4 foil 56: State Diagrams -->

\newslide{State Diagrams}

\slides{* A Markov chain can be represented by a state diagram just as finite state machines are often represented in this manner. One important difference is that Markov chains are not necessarily finite, they can have infinity states! A further difference is that the transitions for Markov chains are associated with probabilities (or in the case of Markov processes rates).}

<!-- original A4 foil 57: Poisson Process as a Markov Process -->

\newslide{Poisson Process as a Markov Process}

\slides{* We've introduced the game of Monopoly as a Markov chain. In this next session we shall relate Markov chains, where time is treated as a discrete variable, to Markov processes, where time is a continuous variable. We will show how the Poisson process is a special case of a Markov process where a constrained set of transitions are allowed. To do this we will first introduce a new version of Monopoly that we call `Coin Monopoly'.}

<!-- original A4 foil 58: Coin Monopoly -->

\newslide{Coin Monopoly}

\figure{\includepng{\diagramsDir/npa/stateDiagram}{80%}}{State diagram for coin monopoly. Each node (circle) represents a different possible state value. The state changes (or doesn't change) with each time step according the probabilities associated with the arrows.}{cap:coinMonopolyStateDiagram}

<!-- original A4 foil 58: Coin Monopoly -->

\newslide{Coin Monopoly (continued)}

\slides{* Player tosses the coin when it is their turn.
* We take $d(t)=0$ if a coin is tails and $d(t)=1$ if it is heads. This is depicted as a state diagram in Figure\  \ref{cap:coinMonopolyStateDiagram}.
* Takes a long time to play ... let's speed it up.}

<!-- original A4 foil 59: Fast Coin Monopoly -->

\newslide{Fast Coin Monopoly}

\slides{* Time, $t$, originally changes by $\Delta t=1$.
* Special coin with $P\left(h\right)=\lambda\,\Delta t$ (which must be less than 1), giving $P\left(t\right)=1-\lambda\,\,\Delta t$.
* Use the *binomial distribution* to compute how many heads.}

<!-- original A4 foil 60: Binomial Distribution for $n$ Trials -->

\newslide{Binomial Distribution for $n$ Trials}

\slides{* Example 1, Chapter 5. It is possible to compute a probability distribution for a number of successes given a number of trials. This distribution is known as the binomial. For $n$ trials (equivalent to $n$ coin tosses or $n$ turns for Coin Monopoly) the probability of $k$ successes (equivalent to $k$ moves forward) is given by
P\left(k\right)=\left({c}
n\\
k\right)P\left(h\right)^{k}(1-P\left(h\right))^{n-k}\label{eq:binomialDistirbution}where $\left({c}
n\\
k\right)=\frac{n!}{k!(n-k)!}$ is known as the binomial coefficient.
  By considering the limiting case as the probability of a success (or heads) goes to zero but the number of trials goes to $\infty$ show that a Poisson process can be recovered.
* A probability distribution for a number of successes given a number of trials.
* For $n$ trials (equivalent to $n$ coin tosses or $n$ turns for Coin Monopoly) the probability of $k$ successes (equivalent to $k$ moves forward) is given by
P\left(k\right)=\left({c}
n\\
k\right)P\left(h\right)^{k}(1-P\left(h\right))^{n-k}\label{eq:binomialDistirbution}where $\left({c}
n\\
k\right)=\frac{n!}{k!(n-k)!}$ is known as the binomial coefficient.
      Since each of our turns takes $\Delta t$ time, we know that after $t$ time we will have completed 
n=\frac{t}{\Delta t}\label{eq:nInTermsOfDeltaT} turns. Since we defined $P\left(h\right)=\lambda\Delta t$ we can therefore write$$
P\left(h\right)=\frac{\lambda t}{n}.$$We now substitute this expression for the probability of heads into the binomial distribution (\ref{eq:binomialDistirbution}) giving \answer{
P\left(k|\lambda,t\right) & = & \frac{n!}{k!(n-k)!}\left(\frac{\lambda t}{n}\right)^{k}\left(1-\frac{\lambda t}{n}\right)^{n-k}\\
 & = & \frac{n\left(n-1\right)\dots\left(n-\left(k-1\right)\right)}{n^{k}\left(1-\frac{\lambda t}{n}\right)^{k}}\frac{(\lambda t)^{k}}{k!}\left(1-\frac{\lambda t}{n}\right)^{n}.\}{6}
      The next step is to take the limit as $n\rightarrow\infty$. From (\ref{eq:nInTermsOfDeltaT}) we can see that this is equivalent to taking $\Delta t\rightarrow0$. In this limit we can take advantage of the following $$
\lim_{n\rightarrow\infty}\frac{n\left(n-1\right)\dots\left(n-\left(k-1\right)\right)}{n^{k}\left(1-\frac{\lambda t}{n}\right)^{k}}=1.$$You should recognise this from the fact that the dominant term in the numerator is $n^{k}$ and the dominant term in the denominator is $n^{k}$. Secondly we use the fact that $$
\lim_{m\rightarrow\infty}\left(1+\frac{z}{m}\right)^{m}=\exp\left(z\right).$$Inserting these two limits into the equation gives: 
P\left(k|\lambda,t\right)=\frac{(\lambda t)^{k}}{k!}e^{-\lambda t}.\label{eqn:poisson}which is recognised as a Poisson process. In other words, we have proved that a Poisson process is a particular type of Markov chain, in fact, because we have taken the limit as $\Delta t\rightarrow0$, this system is now continuous time, it is therefore known as a Markov process.}

<!-- original A4 foil 61: Take Limits -->

\newslide{Take Limits}

<!-- original A4 foil 62: Markov Process State Diagrams -->

\newslide{Markov Process State Diagrams}

\figure{\includepng{\diagramsDir/npa/stateDiagramProcess}{80%}}{State diagram for the Markov process given by Coin Monopoly in the limit as $\Delta t\rightarrow0$. This is the state diagram for a Poisson process. Notice in comparison to Figure\  \ref{cap:coinMonopolyStateDiagram}, the probabilities have been replaced by rates and there are no self-transition arrows.}{cap:coinMonopolyProcess}

<!-- original A4 foil 63: Summary -->

\newslide{Summary}

\slides{* You've now seen that a Poisson process can be derived starting from a simple Markov chain. This gives some deeper insight to a Poisson process. In the coin monopoly model there is a fixed (constant) probability of moving forward in every turn and whether a move forward occurs in each turn is completely independent of what happened in previous turns. The Poisson process is the continuous analogue of this stem. There is a constant probability of an arrival occurring at any time which is independent of what has gone before. This gives you an intuitive explanation of the two properties of the Poisson process --- similarity and independence.}

<!-- original A4 foil 64: Steady State\label{sec:steadyState} -->

\newslide{Steady State\label{sec:steadyState}}

\slides{* Steady state behaviour vs the transient dynamics.
* What do we mean by steady state?}

<!-- original A4 foil 64: Steady State\label{sec:steadyState} -->

\newslide{Steady State\label{sec:steadyState} (continued)}

\slides{* A stable condition that does not change over time or in which change in one direction is continually balanced by change in another.
    \footnote{http://www.dictionary.com .}
* A steady state is a dynamic equilibrium.
* A Markov process *can* reach a steady state distribtuion.}

<!-- original A4 foil 65: Steady State contd -->

\newslide{Steady State contd}

\slides{* A probabilistic process $p\left(k|t\right)$ is a `noisy function' of time.
* If process converges to a distribution as time $\rightarrow\infty$ then it has a steady state.$$
\lim_{t\rightarrow\infty}p\left(k|t\right)=p\left(k\right)$$the average value of $k$ at steady state is then given by$$
\left\langle k\right\rangle _{p\left(k\right)}=\sum_{k=0}^{\infty}p\left(k\right)k.$$
* A Poisson process doesn't have a steady state distribution.}

<!-- original A4 foil 66: Coin Monopoly Revisited -->

\newslide{Coin Monopoly Revisited}

\slides{* `Coin Monopoly' Markov chain (as we described it) has no *steady state *distribution
* Over time the value of $k$ will always increase.}

<!-- original A4 foil 66: Coin Monopoly Revisited -->

\newslide{Coin Monopoly Revisited (continued)}

\slides{* In this lecture introduce a (slightly) more complex Markov process: the *birth-death processes*.
* A birth-death process can have a steady state distribution.
* We use detailed balance to discover this distribution.}

<!-- original A4 foil 67: Birth Death Process -->

\newslide{Birth Death Process}

\figure{\includepng{\diagramsDir/npa/birthDeathChain}{100%}}{State diagram for a birth-death chain.}{cap:birthDeathChainState}

<!-- original A4 foil 67: Birth Death Process -->

\newslide{Birth Death Process (continued)}

\slides{* A model for births and deaths in a population.
* Recall the Markov chain underlying `Coin Monopoly'.
* Modify this diagram: allow backwards moves.
* Prevent state from going negative.
* This system is known as a birth-death process.}

\figure{\includepng{\diagramsDir/npa/birthDeathProcess}{100%}}{State diagram for a birth-death process.}{cap:birthDeathChainProcess}

<!-- original A4 foil 68: Kendall's Notation\label{sec:kendall} -->

\newslide{Kendall's Notation\label{sec:kendall}}

\slides{* Simple way of summarising the characteristics of a queue.}

<!-- original A4 foil 68: Kendall's Notation\label{sec:kendall} -->

\newslide{Kendall's Notation\label{sec:kendall} (continued)}

\slides{* / / /
Arrival characteristics
Departure characteristics
number of servers
max number of customers
The arrival and departure characteristics are summarised by
* $M$ --- Markov --- Poisson distributed arrivals, exponentially distributed service times.
* $D$ --- Deterministically distributed times.
* $G$ --- General distribution for inter-arrival/service times.}

<!-- original A4 foil 69: Global Balance -->

\newslide{Global Balance}

\slides{* Seek a stationary distribution through global balance equations.
* At equilibrium the frequency of transitions out of state $k$ equals the frequency of transitions into $k$ [@Bertsekas:data92].
* Markov chain can be defined by a transition probability matrix.
* Gives the probability of transition from any state to any other. $$
\mathbf{P}=\left[{ccccc}
P_{00} & \cdots & P_{i0} & \cdots & P_{N0}\\
\vdots & \ddots &  &  & \vdots\\
P_{0j} &  & P_{ij} &  & P_{Nj}\\
\vdots &  &  & \ddots & \vdots\\
P_{0N} & \cdots & P_{iN} & \cdots & P_{NN}\right].$$where probability of transition from state $i$ to state $j$ is given by $P_{ij}$.}

<!-- original A4 foil 70: Global Balance II -->

\newslide{Global Balance II}

\slides{* If $P\left(j\right)$ is steady state probability for state $j$, global balance says$$
P\left(j\right)\sum_{i=0}^{\infty}P_{ji}=\sum_{i=0}^{\infty}P\left(i\right)P_{ij}$$``the probability of leaving state $j$ should be equal to the probability of arriving in state $j$.''
* Markov Process: rates of transfer.
* Rates of transfer between states are given by a matrix with elements $q_{ij}$ for transfer between $i$ and $j$. Global balance equations give$$
P\left(j\right)\sum_{i=0}^{\infty}q_{ji}=\sum_{i=0}^{\infty}P\left(i\right)q_{ij}.$$}

<!-- original A4 foil 71: Detailed Balance -->

\newslide{Detailed Balance}

\slides{* For the birth death processes transitions only between state $k$ and $k+1$ or $k-1$.
* $P_{ij}=0$ if $i>j+1$ and $i<j-1$.
* Special case of the global balance: detailed balance equations. Looks at the flow between two states.
* For the discrete case$$
P\left(k-1\right)P_{k-1,k}=P\left(k\right)P_{k,k-1}$$
* For the continuous case $$
P\left(k-1\right)q_{k-1,k}=P\left(k\right)q_{k,k-1}.$$
* With our notation rate from $q_{k-1,k}=\lambda_{k-1}$ and $q_{k,k-1}=\mu_{k}$ giving}

<!-- original A4 foil 71: Detailed Balance -->

\newslide{Detailed Balance (continued)}

\slides{* $$
P\left(k-1\right)\lambda_{k-1}=P\left(k\right)\mu_{k}.$$}

<!-- original A4 foil 72: Boundary Flow -->

\newslide{Boundary Flow}

\slides{* Consider the flow rates at a *boundary *between two states, $k-1$ and $k$.
  [ht]
    \centering
    \caption{Flow rates at a Boundary for a birth-death process.}
    \label{cap:flowAtBoundary}
* At steady state
* flow from $k-1$ to $k$ is $\lambda_{k-1}P\left(k-1\right)$,}

\figure{\includepng{\diagramsDir/npa/boundaryFlow}{60%}}{boundaryFlow}{boundaryFlow}

<!-- original A4 foil 72: Boundary Flow -->

\newslide{Boundary Flow (continued)}

\slides{* flow from $k$ to $k-1$ is $\mu_{k}P\left(k\right)$.
* For flow to be balanced we have $$
\lambda_{k-1}P\left(k-1\right)=\mu_{k}P\left(k\right).$$
* For different systems birth rate and death rate will differ. First we consider $M/M/1$ queue.}

<!-- original A4 foil 73: Kendall's Notation --- $M/M/1$ -->

\newslide{Kendall's Notation --- $M/M/1$}

\slides{* / / /
Arrival characteristics
Departure characteristics
number of servers
max number of customers
$M/M/1$}

<!-- original A4 foil 73: Kendall's Notation --- $M/M/1$ -->

\newslide{Kendall's Notation --- $M/M/1$ (continued)}

\slides{* $M$ --- Markov --- Poisson distributed arrivals, exponentially distributed service times.
* $D$ --- Deterministically distributed times.
* $G$ --- General distribution for inter-arrival/service times.}

<!-- original A4 foil 74: $M/M/1$ Queue\label{sec:MM1Stationary} -->

\newslide{$M/M/1$ Queue\label{sec:MM1Stationary}}

\figure{\includepng{\diagramsDir/npa/stateMM1}{100%}}{State diagram for $M/M/1$ queue.}{stateMM1}

<!-- original A4 foil 74: $M/M/1$ Queue\label{sec:MM1Stationary} -->

\newslide{$M/M/1$ Queue\label{sec:MM1Stationary} (continued)}

\slides{* $M/M/1$ arrivals occur as a Poisson process, service times are exponentially distributed.
* A birth-death process
* constant birth rate $\lambda_{k}=\lambda$ (from the Poisson process)
* constant death rate (from the exponentially distributed service times) $\mu_{k}=\mu$.
* State diagram is
* Derive stationary distribution is derived using detailed balance.}

<!-- original A4 foil 75: $M/M/1$ Stationary Distribution -->

\newslide{$M/M/1$ Stationary Distribution}

\slides{* The state diagram highlights several points.
* There are no transitions to a state below 0.
* There is no maximum value for the state shown, this implies that $k$ is unbounded.}

<!-- original A4 foil 75: $M/M/1$ Stationary Distribution -->

\newslide{$M/M/1$ Stationary Distribution (continued)}

\slides{* The birth rates and death rates for each state are indicated.
* Transitions are only possible between neighbouring states.
* Flow at boundary: analyse between $k$ and $k-1$.
  [ht]
    \centering
    \caption{Flow rates at a boundary.}
    \label{cap:flowAtBoundary}
* At steady state, $$
\lambda P\left(k-1\right)=\mu P\left(k\right).$$}

\figure{\includepng{\diagramsDir/npa/boundaryFlowMM1}{60%}}{boundaryFlowMM1}{boundaryFlowMM1}

<!-- original A4 foil 76: $M/M/1$ --- Stationary Distribution II -->

\newslide{$M/M/1$ --- Stationary Distribution II}

\slides{* At steady state, $$
\lambda P\left(k-1\right)=\mu P\left(k\right).$$
* Leading to $$
P\left(k\right)=\frac{\lambda}{\mu}P\left(k-1\right).$$
* Thus
P\left(k\right) & = & \left(\frac{\lambda}{\mu}\right)^{k}P\left(0\right)\\
 & = & \rho^{k}P\left(0\right),
  where we have defined $\rho=\frac{\lambda}{\mu}$, which, for the $M/M/1$ queue, is called the *utilisation factor*.}

<!-- original A4 foil 77: Normalisation\label{sub:normalisationMM1} -->

\newslide{Normalisation\label{sub:normalisationMM1}}

\slides{* To find $P\left(0\right)$ we use the normalisation condition.$$
\sum_{k=0}^{\infty}P\left(k\right)=1$$ and because $P\left(k\right)=\rho^{k}P\left(0\right)$,$$
1=P\left(0\right)\sum_{k=0}^{\infty}\rho^{k}$$ giving 
P\left(0\right)=\frac{1}{\sum_{k=0}^{\infty}\rho^{k}}.\label{eq:MM1Series}
* The infinite series in the denominator converges if $\rho<1$ (when $\lambda<\mu$), $$
\sum_{k=0}^{\infty}\rho^{k}=\frac{1}{1-\rho}\,\,\,\textrm{for\,\,\,$\rho<1$},$$ so $P\left(0\right)=\left(1-\rho\right)$ and the full distribution for the *steady state* probabilities is $$
P\left(k\right)=\rho^{k}\left(1-\rho\right).$$}

<!-- original A4 foil 78: Faster Arrivals than Service -->

\newslide{Faster Arrivals than Service}

\slides{* Notice that if the arrival rate (birth rate) is greater than the service rate (death rate) then $\rho>1$ and the series in (\ref{eq:MM1Series}) doesn't converge. This is indicative of the fact that if the birth rate is greater than the death rate there is no steady state distribution. The queue continues to grow in size.}

<!-- original A4 foil 79: Average Number in System -->

\newslide{Average Number in System}

\slides{* Network design: interested in the average queue length.
* We use the steady state probabilities to compute this quantity.
* The average number of customers in the system *is not* the same as the average queue length
* a customer being served (*e.g. *a packet under transmission) is not in the queue.
* Average number of customers in the system is the expected state of the system.
* $$
\left\langle k\right\rangle _{P\left(k\right)}=\sum_{k=0}^{\infty}kP\left(k\right)$$}

<!-- original A4 foil 80: Average Number in System II -->

\newslide{Average Number in System II}

\slides{* Example 1, Chapter 6. The average number in the system for the $M/M/1$ queue is given by considering the steady state distribution. Compute this value.}

\slides{  \begin{eqnarray*}
\left\langle k\right\rangle _{P\left(k\right)} & = & \sum_{k=0}^{\infty}kP\left(k\right)\\
\\\\\\\\\\\\\end{eqnarray*}
  \begin{eqnarray*}
\left\langle k\right\rangle _{P\left(k\right)} & = & \sum_{k=0}^{\infty}kP\left(k\right)\\
 & = & \left(1-\rho\right)\sum_{k=0}^{\infty}k\rho^{k}\\
\\\\\\\\\\\end{eqnarray*}
  \begin{eqnarray*}
\left\langle k\right\rangle _{P\left(k\right)} & = & \sum_{k=0}^{\infty}kP\left(k\right)\\
 & = & \left(1-\rho\right)\sum_{k=0}^{\infty}k\rho^{k}\\
 & = & \rho\left(1-\rho\right)\sum_{k=0}^{\infty}k\rho^{k-1}\\
\\\\\\\\\end{eqnarray*}
  \begin{eqnarray*}
\left\langle k\right\rangle _{P\left(k\right)} & = & \sum_{k=0}^{\infty}kP\left(k\right)\\
 & = & \left(1-\rho\right)\sum_{k=0}^{\infty}k\rho^{k}\\
 & = & \rho\left(1-\rho\right)\sum_{k=0}^{\infty}k\rho^{k-1}\\
 & = & \rho\left(1-\rho\right)\frac{\partial\sum_{k=0}^{\infty}\rho^{k}}{\partial\rho}\\
\\\\\\\end{eqnarray*}
  \begin{eqnarray*}
\left\langle k\right\rangle _{P\left(k\right)} & = & \sum_{k=0}^{\infty}kP\left(k\right)\\
 & = & \left(1-\rho\right)\sum_{k=0}^{\infty}k\rho^{k}\\
 & = & \rho\left(1-\rho\right)\sum_{k=0}^{\infty}k\rho^{k-1}\\
 & = & \rho\left(1-\rho\right)\frac{\partial\sum_{k=0}^{\infty}\rho^{k}}{\partial\rho}\\
 & = & \rho\left(1-\rho\right)\frac{\partial}{\partial\rho}\left[\frac{1}{1-\rho}\right]\\
\\\\\end{eqnarray*}
  \begin{eqnarray*}
\left\langle k\right\rangle _{P\left(k\right)} & = & \sum_{k=0}^{\infty}kP\left(k\right)\\
 & = & \left(1-\rho\right)\sum_{k=0}^{\infty}k\rho^{k}\\
 & = & \rho\left(1-\rho\right)\sum_{k=0}^{\infty}k\rho^{k-1}\\
 & = & \rho\left(1-\rho\right)\frac{\partial\sum_{k=0}^{\infty}\rho^{k}}{\partial\rho}\\
 & = & \rho\left(1-\rho\right)\frac{\partial}{\partial\rho}\left[\frac{1}{1-\rho}\right]\\
 & = & \rho\left(1-\rho\right)\frac{1}{\left(1-\rho\right)^{2}}\\
\\\end{eqnarray*}
  \begin{eqnarray*}
\left\langle k\right\rangle _{P\left(k\right)} & = & \sum_{k=0}^{\infty}kP\left(k\right)\\
 & = & \left(1-\rho\right)\sum_{k=0}^{\infty}k\rho^{k}\\
 & = & \rho\left(1-\rho\right)\sum_{k=0}^{\infty}k\rho^{k-1}\\
 & = & \rho\left(1-\rho\right)\frac{\partial\sum_{k=0}^{\infty}\rho^{k}}{\partial\rho}\\
 & = & \rho\left(1-\rho\right)\frac{\partial}{\partial\rho}\left[\frac{1}{1-\rho}\right]\\
 & = & \rho\left(1-\rho\right)\frac{1}{\left(1-\rho\right)^{2}}\\
 & = & \frac{\rho}{1-\rho}\end{eqnarray*}
  \begin{eqnarray*}
\left\langle k\right\rangle _{P\left(k\right)} & = & \sum_{k=0}^{\infty}kP\left(k\right)\\
 & = & \left(1-\rho\right)\sum_{k=0}^{\infty}k\rho^{k}\\
 & = & \rho\left(1-\rho\right)\sum_{k=0}^{\infty}k\rho^{k-1}\\
 & = & \rho\left(1-\rho\right)\frac{\partial\sum_{k=0}^{\infty}\rho^{k}}{\partial\rho}\\
 & = & \rho\left(1-\rho\right)\frac{\partial}{\partial\rho}\left[\frac{1}{1-\rho}\right]\\
 & = & \rho\left(1-\rho\right)\frac{1}{\left(1-\rho\right)^{2}}\\
 & = & \frac{\rho}{1-\rho}\\
 & = & \frac{\lambda}{\mu-\lambda}\end{eqnarray*}
  As an exercise on the tutorial sheet, you will show that the variance of the number in the system is given by}

<!-- original A4 foil 81: Average Number in System II -->

\newslide{Average Number in System II}

<!-- original A4 foil 82: Average Number in System II -->

\newslide{Average Number in System II}

<!-- original A4 foil 83: Average Number in System II -->

\newslide{Average Number in System II}

<!-- original A4 foil 84: Average Number in System II -->

\newslide{Average Number in System II}

<!-- original A4 foil 85: Average Number in System II -->

\newslide{Average Number in System II}

<!-- original A4 foil 86: Average Number in System II -->

\newslide{Average Number in System II}

<!-- original A4 foil 87: Average Number in System II -->

\newslide{Average Number in System II}

<!-- original A4 foil 88: Variance -->

\newslide{Variance}

\slides{* The variance is computed as an excercise in the Tutorial Sheet.
$$
\textrm{var}\left[k\right]=\left\langle k^{2}\right\rangle -\left\langle k\right\rangle ^{2}=\frac{\rho}{\left(1-\rho\right)^{2}}.$$}

<!-- original A4 foil 89: Discrete Simulation of $M/M/1$ -->

\newslide{Discrete Simulation of $M/M/1$}

\slides{* Next week: first lab class.
* Discrete simulation of an $M/M/1$ queue: easy to run because it takes the form of a Markov chain.
* State diagram for this system.
  [ht]
    \centering
    \caption{State diagram for the discrete version of the $M/M/1$ queue.}}

\figure{\includepng{\diagramsDir/npa/discreteMM1State}{100%}}{discreteMM1State}{discreteMM1State}

<!-- original A4 foil 90: Hints for the Simulation -->

\newslide{Hints for the Simulation}

\slides{* Use a loop over discrete time steps.
* At each time step there are three possible events:
* the state of the system increases by one;}

<!-- original A4 foil 90: Hints for the Simulation -->

\newslide{Hints for the Simulation (continued)}

\slides{* the state of the system decreases by one and
* the state of the system stays the same.
* Modelling the queue is therefore a simple matter of testing which of these outcomes is true.
  [ht]
    \centering
    \caption{Testing for one of three outcomes. Generate a random number and see where it lands.}}

\figure{\includepng{\diagramsDir/npa/probOutcome}{80%}}{probOutcome}{probOutcome}

<!-- original A4 foil 91: Approximating a Continuous $M/M/1$ Queue -->

\newslide{Approximating a Continuous $M/M/1$ Queue}

\slides{* We know from last week that a Poisson process can be derived by considering the limit of a simple Markov chain.
* A continuous $M/M/1$ queue is the limit of the discrete model we are using for simulation}

<!-- original A4 foil 91: Approximating a Continuous $M/M/1$ Queue -->

\newslide{Approximating a Continuous $M/M/1$ Queue (continued)}

\slides{* In your lab class you can make ths approximation by taking $\Delta t$ to be much smaller than $\lambda$ or $\mu$.
* Then you may set $P\left(b\right)=\lambda\Delta t$ and $P\left(d\right)=\mu\Delta t$.}

<!-- original A4 foil 92: Demonstration -->

\newslide{Demonstration}

\slides{* Lab class: run a simulation of the discrete queue.
* Answer questions on the analysis of that queue.}

<!-- original A4 foil 92: Demonstration -->

\newslide{Demonstration (continued)}

\slides{* Now we demonstrate a simulation in the lecture.
* We also give you histograms that are similar to those you should be producing in the lab class.}

<!-- original A4 foil 93: Histograms -->

\newslide{Histograms}

\figure{\includepng{\diagramsDir/npa/rho_half_1000_arrivals}{45%}}{Left figure: steady state probabilities after the first 100 seconds for $\rho=0.5$. Right figure: steady state probabilities after the first 1000 seconds for $\rho=0.5$.}{rho-half-1000-arrivals}

<!-- original A4 foil 93: Histograms -->

\newslide{Histograms (continued)}

\figure{\includepng{\diagramsDir/npa/rho_point95_1000_arrivals}{45%}}{Left figure: steady state probabilities after the first 100 seconds for $\rho=0.95$. Right figure: steady state probabilities after the first 1000 seconds for $\rho=0.95$.}{rho-point95-1000-arrivals}

\endif

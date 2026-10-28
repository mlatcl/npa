\ifndef{npaGenSlidesBirthDeathMm1}
\define{npaGenSlidesBirthDeathMm1}

\newslide{Markov Chains and Markov Processes\label{cha:markovChainsAndProcesses}}

\slides{* Poisson process in a special case of the more general class of processes known as Markov processes. We will start by considering Markov processes as they operate in *discrete time*, otherwise known as *Markov chains*. Both Markov processes and Markov chains exhibit the *Markov property*which is an assumption about how future values drawn from the process depend on past values. We will first discuss the Markov property in the context of Markov chains, then we will show how a discrete system can be converted to a continuous system.}

\newslide{Markov Chains}

\slides{* Consider a discrete representation of time $t=0,1,2...$. We associate a state variable, $N$, with this time such that we have values for $N$ at $N(0),\, N(1),\, N(2),\,...$.
* Turns in a board game.
* Markov Property}

\newslide{Markov Chains (continued)}

\slides{* value at time $t$ is dependent only on its value at time $t-1$.
* The future is conditional independent of the past (the conditioning being on the present).
* State of the system in the future is *not*dependent on what happened in the past if we know the state at the present time.}

\newslide{Monopoly}

\slides{* A real-life example of a Markov chain
* Forty squares on a Monopoly board.}

\slides{\figure{\includepng{\diagramsDir/npa/smallMonopoly}{80%}}{Image of a monopoly board.}{smallMonopoly}}

\newslide{Markov Chain Monopoly}

\slides{* Player's state, $N(t)$, square number +40$\ensuremath{\times}$number of `GO's
  Normally move through two six sided dice and adding them together. Denote the result of this die roll $d(t)$.
* State at time $t$ is
  $$
N(t)=N(t-1)+d(t).$$ Monopoly exhibits the Markov property, future states are independent of your previous states given your current state.}

\newslide{State Diagrams}

\slides{* A Markov chain can be represented by a state diagram just as finite state machines are often represented in this manner. One important difference is that Markov chains are not necessarily finite, they can have infinity states! A further difference is that the transitions for Markov chains are associated with probabilities (or in the case of Markov processes rates).}

\newslide{Poisson Process as a Markov Process}

\slides{* We've introduced the game of Monopoly as a Markov chain. In this next session we shall relate Markov chains, where time is treated as a discrete variable, to Markov processes, where time is a continuous variable. We will show how the Poisson process is a special case of a Markov process where a constrained set of transitions are allowed. To do this we will first introduce a new version of Monopoly that we call `Coin Monopoly'.}

\newslide{Coin Monopoly}

\slides{\figure{\includepng{\diagramsDir/npa/stateDiagram}{80%}}{State diagram for coin monopoly. Each node (circle) represents a different possible state value. The state changes (or doesn't change) with each time step according the probabilities associated with the arrows.}{cap:coinMonopolyStateDiagram}}

\newslide{Coin Monopoly (continued)}

\slides{* Player tosses the coin when it is their turn.
* We take $d(t)=0$ if a coin is tails and $d(t)=1$ if it is heads. This is depicted as a state diagram in Figure\  \ref{cap:coinMonopolyStateDiagram}.
* Takes a long time to play ... let's speed it up.}

\newslide{Fast Coin Monopoly}

\slides{* Time, $t$, originally changes by $\ensuremath{\Delta} t=1$.
* Special coin with $P\left(h\right)=\ensuremath{\lambda},\ensuremath{\Delta} t$ (which must be less than 1), giving $P\left(t\right)=1-\ensuremath{\lambda},\,\ensuremath{\Delta} t$.
* Use the *binomial distribution* to compute how many heads.}

\newslide{Binomial Distribution for $n$ Trials}

\slides{* Example 1, Chapter 5. It is possible to compute a probability distribution for a number of successes given a number of trials. This distribution is known as the binomial. For $n$ trials (equivalent to $n$ coin tosses or $n$ turns for Coin Monopoly) the probability of $k$ successes (equivalent to $k$ moves forward) is given by
P\left(k\right)=\begin{array}{c}
n\\
k\right)P\left(h\right)^{k}(1-P\left(h\right))^{n-k}\label{eq:binomialDistirbution}where $\begin{array}{c}
n\\
k\right)=\ensuremath{\frac{n!}{k!(n-k)!}}$ is known as the binomial coefficient.
  By considering the limiting case as the probability of a success (or heads) goes to zero but the number of trials goes to $\ensuremath{\infty}$ show that a Poisson process can be recovered.
* A probability distribution for a number of successes given a number of trials.
* For $n$ trials (equivalent to $n$ coin tosses or $n$ turns for Coin Monopoly) the probability of $k$ successes (equivalent to $k$ moves forward) is given by
P\left(k\right)=\begin{array}{c}
n\\
k\right)P\left(h\right)^{k}(1-P\left(h\right))^{n-k}\label{eq:binomialDistirbution}where $\begin{array}{c}
n\\
k\right)=\ensuremath{\frac{n!}{k!(n-k)!}}$ is known as the binomial coefficient.
      Since each of our turns takes $\ensuremath{\Delta} t$ time, we know that after $t$ time we will have completed 
n=\ensuremath{\frac{t}{\Delta t}\label{eq:nInTermsOfDeltaT}} turns. Since we defined $P\left(h\right)=\ensuremath{\lambda\Delta} t$ we can therefore write$$
P\left(h\right)=\ensuremath{\frac{\lambda t}{n}}.$$We now substitute this expression for the probability of heads into the binomial distribution (\ref{eq:binomialDistirbution}) giving 
P\left(k|\ensuremath{\lambda},t\right) & = & \ensuremath{\frac{n!}{k!(n-k)!}\left(\frac{\lambda t}{n}\right)^{k}\left(}1-\ensuremath{\frac{\lambda t}{n}\right)^{n-k}\\}
 & = & \ensuremath{\frac{n\left(n-1\right)\dots\left(n-\left(k-1\right)\right)}{n^{k}\left(1-\frac{\lambda t}{n}\right)^{k}}\frac{(\lambda t)^{k}}{k!}\left(}1-\ensuremath{\frac{\lambda t}{n}\right)^{n}}.
      The next step is to take the limit as $n\ensuremath{\rightarrow\infty}$. From (\ref{eq:nInTermsOfDeltaT}) we can see that this is equivalent to taking $\ensuremath{\Delta} t\rightarrow0$. In this limit we can take advantage of the following $$
\lim_{n\ensuremath{\rightarrow\infty}}\ensuremath{\frac{n\left(n-1\right)\dots\left(n-\left(k-1\right)\right)}{n^{k}\left(1-\frac{\lambda t}{n}\right)^{k}}}=1.$$You should recognise this from the fact that the dominant term in the numerator is $n^{k}$ and the dominant term in the denominator is $n^{k}$. Secondly we use the fact that $$
\lim_{m\ensuremath{\rightarrow\infty}}\left(1+\ensuremath{\frac{z}{m}\right)^{m}}=\ensuremath{\exp\left(}z\right).$$Inserting these two limits into the equation gives: 
P\left(k|\ensuremath{\lambda},t\right)=\ensuremath{\frac{(\lambda t)^{k}}{k!}}e^{-\ensuremath{\lambda} t}.\label{eqn:poisson}which is recognised as a Poisson process. In other words, we have proved that a Poisson process is a particular type of Markov chain, in fact, because we have taken the limit as $\ensuremath{\Delta} t\rightarrow0$, this system is now continuous time, it is therefore known as a Markov process.\end{array}}

\newslide{Take Limits}

\newslide{Markov Process State Diagrams}

\slides{\figure{\includepng{\diagramsDir/npa/stateDiagramProcess}{80%}}{State diagram for the Markov process given by Coin Monopoly in the limit as $\ensuremath{\Delta} t\rightarrow0$. This is the state diagram for a Poisson process. Notice in comparison to Figure\  \ref{cap:coinMonopolyStateDiagram}, the probabilities have been replaced by rates and there are no self-transition arrows.}{cap:coinMonopolyProcess}}

\newslide{Summary}

\slides{* You've now seen that a Poisson process can be derived starting from a simple Markov chain. This gives some deeper insight to a Poisson process. In the coin monopoly model there is a fixed (constant) probability of moving forward in every turn and whether a move forward occurs in each turn is completely independent of what happened in previous turns. The Poisson process is the continuous analogue of this stem. There is a constant probability of an arrival occurring at any time which is independent of what has gone before. This gives you an intuitive explanation of the two properties of the Poisson process --- similarity and independence.}

\newslide{Steady State\label{sec:steadyState}}

\slides{* Steady state behaviour vs the transient dynamics.
* What do we mean by steady state?}

\newslide{Steady State\label{sec:steadyState} (continued)}

\slides{* A stable condition that does not change over time or in which change in one direction is continually balanced by change in another.
    \footnote{http://www.dictionary.com .}
* A steady state is a dynamic equilibrium.
* A Markov process *can* reach a steady state distribtuion.}

\newslide{Steady State contd}

\slides{* A probabilistic process $p\left(k|t\right)$ is a `noisy function' of time.
* If process converges to a distribution as time $\ensuremath{\rightarrow\infty}$ then it has a steady state.$$
\lim_{t\ensuremath{\rightarrow\infty}}p\left(k|t\right)=p\left(k\right)$$the average value of $k$ at steady state is then given by$$
\left\langle k\right\rangle _{p\left(k\right)}=\sum_{k=0}^{\ensuremath{\infty}}p\left(k\right)k.$$
* A Poisson process doesn't have a steady state distribution.}

\newslide{Coin Monopoly Revisited}

\slides{* `Coin Monopoly' Markov chain (as we described it) has no *steady state*distribution
* Over time the value of $k$ will always increase.}

\newslide{Coin Monopoly Revisited (continued)}

\slides{* In this lecture introduce a (slightly) more complex Markov process: the *birth-death processes*.
* A birth-death process can have a steady state distribution.
* We use detailed balance to discover this distribution.}

\newslide{Birth Death Process}

\slides{\figure{\includepng{\diagramsDir/npa/birthDeathChain}{100%}}{State diagram for a birth-death chain.}{cap:birthDeathChainState}}

\newslide{Birth Death Process (continued)}

\slides{* A model for births and deaths in a population.
* Recall the Markov chain underlying `Coin Monopoly'.
* Modify this diagram: allow backwards moves.
* Prevent state from going negative.
* This system is known as a birth-death process.}

\slides{\figure{\includepng{\diagramsDir/npa/birthDeathProcess}{100%}}{State diagram for a birth-death process.}{cap:birthDeathChainProcess}}

\newslide{Kendall's Notation\label{sec:kendall}}

\slides{* Simple way of summarising the characteristics of a queue.}

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

\newslide{Global Balance}

\slides{* Seek a stationary distribution through global balance equations.
* At equilibrium the frequency of transitions out of state $k$ equals the frequency of transitions into $k$ [@Bertsekas:data92].
* Markov chain can be defined by a transition probability matrix.
* Gives the probability of transition from any state to any other. $$
\mathbf{P}=\left[{ccccc}

| P_{00} | \ensuremath{\cdots} | P_{i0} | \ensuremath{\cdots} | P_{N0} |
| --- | --- | --- | --- | --- |
| \vdots | \ddots |  |  | \vdots |
| P_{0j} |  | P_{ij} |  | P_{Nj} |
| \vdots |  |  | \ddots | \vdots |
| P_{0N} | \ensuremath{\cdots} | P_{iN} | \ensuremath{\cdots} | P_{NN}\right].$$where probability of transition from state $i$ to state $j$ is given by $P_{ij}$. |}

\newslide{Global Balance II}

\slides{* If $P\left(j\right)$ is steady state probability for state $j$, global balance says$$
P\left(j\right)\sum_{i=0}^{\ensuremath{\infty}}P_{ji}=\sum_{i=0}^{\ensuremath{\infty}}P\left(i\right)P_{ij}$$``the probability of leaving state $j$ should be equal to the probability of arriving in state $j$.''
* Markov Process: rates of transfer.
* Rates of transfer between states are given by a matrix with elements $q_{ij}$ for transfer between $i$ and $j$. Global balance equations give$$
P\left(j\right)\sum_{i=0}^{\ensuremath{\infty}}q_{ji}=\sum_{i=0}^{\ensuremath{\infty}}P\left(i\right)q_{ij}.$$}

\newslide{Detailed Balance}

\slides{* For the birth death processes transitions only between state $k$ and $k+1$ or $k-1$.
* $P_{ij}=0$ if $i>j+1$ and $i<j-1$.
* Special case of the global balance: detailed balance equations. Looks at the flow between two states.
* For the discrete case$$
P\left(k-1\right)P_{k-1,k}=P\left(k\right)P_{k,k-1}$$
* For the continuous case $$
P\left(k-1\right)q_{k-1,k}=P\left(k\right)q_{k,k-1}.$$
* With our notation rate from $q_{k-1,k}=\lambda_{k-1}$ and $q_{k,k-1}=\mu_{k}$ giving}

\newslide{Detailed Balance (continued)}

\slides{* $$
P\left(k-1\right)\lambda_{k-1}=P\left(k\right)\mu_{k}.$$}

\newslide{Boundary Flow}

\slides{* Consider the flow rates at a *boundary*between two states, $k-1$ and $k$.
    \label{cap:flowAtBoundary}
* At steady state
* flow from $k-1$ to $k$ is $\lambda_{k-1}P\left(k-1\right)$,}

\slides{\figure{\includepng{\diagramsDir/npa/boundaryFlow}{60%}}{Flow rates at a Boundary for a birth-death process.}{cap:flowAtBoundary}}

\newslide{Boundary Flow (continued)}

\slides{* flow from $k$ to $k-1$ is $\mu_{k}P\left(k\right)$.
* For flow to be balanced we have $$
\lambda_{k-1}P\left(k-1\right)=\mu_{k}P\left(k\right).$$
* For different systems birth rate and death rate will differ. First we consider $M/M/1$ queue.}

\newslide{Kendall's Notation --- $M/M/1$}

\slides{* / / /
Arrival characteristics
Departure characteristics
number of servers
max number of customers
$M/M/1$}

\newslide{Kendall's Notation --- $M/M/1$ (continued)}

\slides{* $M$ --- Markov --- Poisson distributed arrivals, exponentially distributed service times.
* $D$ --- Deterministically distributed times.
* $G$ --- General distribution for inter-arrival/service times.}

\newslide{$M/M/1$ Queue\label{sec:MM1Stationary}}

\slides{\figure{\includepng{\diagramsDir/npa/stateMM1}{100%}}{State diagram for $M/M/1$ queue.}{stateMM1}}

\newslide{$M/M/1$ Queue\label{sec:MM1Stationary} (continued)}

\slides{* $M/M/1$ arrivals occur as a Poisson process, service times are exponentially distributed.
* A birth-death process
* constant birth rate $\lambda_{k}=\ensuremath{\lambda}$ (from the Poisson process)
* constant death rate (from the exponentially distributed service times) $\mu_{k}=\ensuremath{\mu}$.
* State diagram is
* Derive stationary distribution is derived using detailed balance.}

\newslide{$M/M/1$ Stationary Distribution}

\slides{* The state diagram highlights several points.
* There are no transitions to a state below 0.
* There is no maximum value for the state shown, this implies that $k$ is unbounded.}

\newslide{$M/M/1$ Stationary Distribution (continued)}

\slides{* The birth rates and death rates for each state are indicated.
* Transitions are only possible between neighbouring states.
* Flow at boundary: analyse between $k$ and $k-1$.
    \label{cap:flowAtBoundary}
* At steady state, $$
\ensuremath{\lambda} P\left(k-1\right)=\ensuremath{\mu} P\left(k\right).$$}

\slides{\figure{\includepng{\diagramsDir/npa/boundaryFlowMM1}{60%}}{Flow rates at a boundary.}{cap:flowAtBoundary}}

\newslide{$M/M/1$ --- Stationary Distribution II}

\slides{* At steady state, $$
\ensuremath{\lambda} P\left(k-1\right)=\ensuremath{\mu} P\left(k\right).$$
* Leading to $$
P\left(k\right)=\ensuremath{\frac{\lambda}{\mu}}P\left(k-1\right).$$
* Thus
  where we have defined $\ensuremath{\rho}=\ensuremath{\frac{\lambda}{\mu}}$, which, for the $M/M/1$ queue, is called the *utilisation factor*.

| P\left(k\right) | = | \left(\ensuremath{\frac{\lambda}{\mu}\right)^{k}}P\left(0\right) |
| --- | --- | --- |
|  | = | \ensuremath{\rho^{k}}P\left(0\right), |}

\newslide{Normalisation\label{sub:normalisationMM1}}

\slides{* To find $P\left(0\right)$ we use the normalisation condition.$$
\sum_{k=0}^{\ensuremath{\infty}}P\left(k\right)=1$$ and because $P\left(k\right)=\ensuremath{\rho^{k}}P\left(0\right)$,$$
1=P\left(0\right)\sum_{k=0}^{\ensuremath{\infty}}\ensuremath{\rho^{k}}$$ giving 
P\left(0\right)=\ensuremath{\frac{1}{\sum_{k=0}^{\infty}\rho^{k}}}.\label{eq:MM1Series}
* The infinite series in the denominator converges if $\ensuremath{\rho}<1$ (when $\ensuremath{\lambda}<\ensuremath{\mu}$), $$
\sum_{k=0}^{\ensuremath{\infty}}\ensuremath{\rho^{k}}=\ensuremath{\frac{1}{1-\rho}\},\,\,\textrm{for\,\,\,$\ensuremath{\rho}<1$},$$ so $P\left(0\right)=\left(1-\ensuremath{\rho\right)}$ and the full distribution for the *steady state* probabilities is $$
P\left(k\right)=\ensuremath{\rho^{k}\left(}1-\ensuremath{\rho\right)}.$$}

\newslide{Faster Arrivals than Service}

\slides{* Notice that if the arrival rate (birth rate) is greater than the service rate (death rate) then $\ensuremath{\rho}>1$ and the series in (\ref{eq:MM1Series}) doesn't converge. This is indicative of the fact that if the birth rate is greater than the death rate there is no steady state distribution. The queue continues to grow in size.}

\newslide{Average Number in System}

\slides{* Network design: interested in the average queue length.
* We use the steady state probabilities to compute this quantity.
* The average number of customers in the system *is not* the same as the average queue length
* a customer being served (*e.g.*a packet under transmission) is not in the queue.
* Average number of customers in the system is the expected state of the system.
* $$
\left\langle k\right\rangle _{P\left(k\right)}=\sum_{k=0}^{\ensuremath{\infty}}kP\left(k\right)$$}

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

\newslide{Average Number in System II}

\newslide{Average Number in System II}

\newslide{Average Number in System II}

\newslide{Average Number in System II}

\newslide{Average Number in System II}

\newslide{Average Number in System II}

\newslide{Average Number in System II}

\newslide{Variance}

\slides{* The variance is computed as an excercise in the Tutorial Sheet.
$$
\textrm{var}\left[k\right]=\left\langle k^{2}\right\rangle -\left\langle k\right\rangle ^{2}=\ensuremath{\frac{\rho}{\left(1-\rho\right)^{2}}}.$$}

\newslide{Discrete Simulation of $M/M/1$}

\slides{* Next week: first lab class.
* Discrete simulation of an $M/M/1$ queue: easy to run because it takes the form of a Markov chain.
* State diagram for this system.}

\slides{\figure{\includepng{\diagramsDir/npa/discreteMM1State}{100%}}{State diagram for the discrete version of the $M/M/1$ queue.}{discreteMM1State}}

\newslide{Hints for the Simulation}

\slides{* Use a loop over discrete time steps.
* At each time step there are three possible events:
* the state of the system increases by one;}

\newslide{Hints for the Simulation (continued)}

\slides{* the state of the system decreases by one and
* the state of the system stays the same.
* Modelling the queue is therefore a simple matter of testing which of these outcomes is true.}

\slides{\figure{\includepng{\diagramsDir/npa/probOutcome}{80%}}{Testing for one of three outcomes. Generate a random number and see where it lands.}{probOutcome}}

\newslide{Approximating a Continuous $M/M/1$ Queue}

\slides{* We know from last week that a Poisson process can be derived by considering the limit of a simple Markov chain.
* A continuous $M/M/1$ queue is the limit of the discrete model we are using for simulation}

\newslide{Approximating a Continuous $M/M/1$ Queue (continued)}

\slides{* In your lab class you can make ths approximation by taking $\ensuremath{\Delta} t$ to be much smaller than $\ensuremath{\lambda}$ or $\ensuremath{\mu}$.
* Then you may set $P\left(b\right)=\ensuremath{\lambda\Delta} t$ and $P\left(d\right)=\ensuremath{\mu\Delta} t$.}

\newslide{Demonstration}

\slides{* Lab class: run a simulation of the discrete queue.
* Answer questions on the analysis of that queue.}

\newslide{Demonstration (continued)}

\slides{* Now we demonstrate a simulation in the lecture.
* We also give you histograms that are similar to those you should be producing in the lab class.}

\newslide{Histograms}

\slides{\figure{\includepng{\diagramsDir/npa/rho_half_1000_arrivals}{45%}}{Left figure: steady state probabilities after the first 100 seconds for $\ensuremath{\rho}=0.5$. Right figure: steady state probabilities after the first 1000 seconds for $\ensuremath{\rho}=0.5$.}{rho-half-1000-arrivals}}

\newslide{Histograms (continued)}

\slides{\figure{\includepng{\diagramsDir/npa/rho_point95_1000_arrivals}{45%}}{Left figure: steady state probabilities after the first 100 seconds for $\ensuremath{\rho}=0.95$. Right figure: steady state probabilities after the first 1000 seconds for $\ensuremath{\rho}=0.95$.}{rho-point95-1000-arrivals}}

\endif

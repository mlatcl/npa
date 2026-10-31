\ifndef{npaGenNotesBirthDeathMm1}
\define{npaGenNotesBirthDeathMm1}

\notes{\section{Markov Chains}}

\notes{Time is a continuous variable, but sometimes it is convenient, or natural, to discretise time. One example of a form of discretised time would be turns in a board game. As the turns progress this discretised form of time progresses.
Consider a discrete representation of time $t=0,1,2...$. We associate a state variable, $N$, with this time such that we have values for $N$ at $N(0),\, N(1),\, N(2),\,...$.}

\notes{\subsection{Markov Property}}

\notes{If this state variable exhibits the Markov property its value at time $t$ is dependent only on its value at time $t-1$. The common way of putting this property is that the future is conditional independent of the past. The conditioning being on the present. In other words, the state of the system in the future is *not*dependent on what happened in the past if we know the state at the present time.
Let's consider a real-life example of a Markov chain, that of the board game of Monopoly.}

\notes{\subsection{Monopoly Board}}

\notes{There are forty squares on a Monopoly board. We assume that there is only one player. That player's state, $N(t)$, will be the number of the square his/her counter is on $+40$ for every time he/she has reached GO. For example if you have circled the board twice and are currently on GO then $N(t)=80$. Or if you have circled the board once and are on King's Cross then $N(t)=45$. The time $t$ is now clearly discrete and associated with the number of turns the player has had.
In Monopoly you move your counter through rolling two six sided dice and adding them together. We will denote the result of this die roll at time $t$ with $d(t)$. Notice that your state after turn $t$, $N(t)$ depends only on your die role, $d(t)$, and your state before turn $t$, $N(t-1)$. We write this as: 

$$
N(t)=N(t-1)+d(t).
$$

 This means that Monopoly exhibits the Markov property, as your future states are independent of your previous states given your current state.}

\notes{\subsection{State Diagrams}}

\notes{A Markov chain can be represented by a state diagram just as finite state machines are often represented. One important difference is that Markov chains are not necessarily finite, they can have infinite states! A further difference is that the transitions for Markov chains are associated with probabilities (or in the case of Markov processes rates).}

\figure{\includepng{\diagramsDir/npa/smallMonopoly}{100%}}{Image of a monopoly board.}{smallMonopoly}

\notes{\section{Poisson Process as a Markov Process\label{sec:poissonAsMarkov}}}

\notes{We've introduced the game of Monopoly as a Markov chain. In this next session we shall relate Markov chains, where time is treated as a discrete variable, to Markov processes, where time is a continuous variable. We will show how the Poisson process is a special case of a Markov process where a constrained set of transitions are allowed. To do this we will first introduce a new version of Monopoly that we call `Coin Monopoly'.}

\notes{\subsection{Coin Monopoly}}

\notes{In regular Monopoly each jump, $d(t)$, is given by the sum of two die rolls. Let's assume that we a Monopoly addict Anne who has lost the dice for her set of Monopoly. In danger of going into withdrawal and, finding a coin in her pocket, she comes up with the following way of playing the game.
In the coin version of Monopoly each player tosses the coin when it is their turn. Then, instead of $d(t)$ being the sum of two die roles, we take $d(t)=0$ if a coin is tails and $d(t)=1$ if it is heads. This is depicted as a state diagram in Figure\  \ref{cap:coinMonopolyStateDiagram}.
There is a drawback to playing `Coin Monopoly': it takes rather a long time. However, Anne is a keen mathematician and tries to find a way of speeding it up.
Currently, with each turn, we consider time, $t$, to change by $\Delta t=1$. Let's pretend we have a special coin where we can change the probability that it will be heads. We denote this probability, $P\left(h\right)=\lambda\,\Delta t$ (which must be less than 1), giving $P\left(t\right)=1-\lambda\,\,\Delta t$.}

\figure{\includepng{\diagramsDir/npa/stateDiagram}{80%}}{State diagram for coin monopoly. Each node (circle) represents a different possible state value. The state changes (or doesn't change) with each time step according the probabilities associated with the arrows.}{cap:coinMonopolyStateDiagram}

\notes{Anne can compute the probability that, after $n$ turns, the state of the system will be $k$ using the *binomial distribution*.}

\notes{\subsection{Binomial Distribution for $n$ Trials}}

\notes{Consider a system with two states (such as a coin). Let's assume that one of those states is associated with `success' and one is associated with `failure'. In our Coin Monopoly example heads might be considered success (because it is associated with a move forward) and tails might be associated with failure (because it is associated with no move). This distribution is known as the binomial. For $n$ trials (equivalent to $n$ coin tosses or $n$ turns for Coin Monopoly) the probability of $k$ successes (equivalent to $k$ moves forward) is given by}

\notes{

$$
P\left(k\right)=\left(\begin{array}{c}
n\\
k\end{array}\right)P\left(h\right)^{k}(1-P\left(h\right))^{n-k}\label{eq:binomialDistirbution}
$$

where $\left(\begin{array}{c}
n\\
k\end{array}\right)=\frac{n!}{k!(n-k)!}$ is known as the binomial coefficient. In the examples at the end of this chapter we show that as the number of trials, $n\rightarrow\infty$, is taken to $\infty$ and the probability of success is driven to zero, $P\left(h\right)=\frac{\lambda}{n}$, this system becomes a Poisson process. Inserting these two limits into the equation gives: 

$$
P\left(k|\lambda,t\right)=\frac{(\lambda t)^{k}}{k!}e^{-\lambda t}.\label{eqn:poisson}
$$

 In other words, we have proved that a Poisson process is a particular type of Markov chain, in fact, taking the number of trials to $\infty$ is equivalent to taking the limit as $\Delta t\rightarrow0$, this system is now continuous time, it is therefore known as a Markov process rather than a Markov chain. A Poisson process is therefore also a particular instance of a Markov process.
\subsection{Markov Process State Diagrams}
When drawing state diagrams for continuous systems there a couple of small differences to the Markov chain state diagram given in Figure\~ \ref{cap:coinMonopolyStateDiagram}. We no longer include the arrows that point to the same state and we replace the probability of state transfer with a rate of transfer between states (see Figure\~ \ref{cap:coinMonopolyProcess}).
You've now seen that a Poisson process can be derived starting from a simple Markov chain. This gives some deeper insight to a Poisson process. In the coin monopoly model there is a fixed (constant) probability of moving forward in every turn and whether a move forward occurs in each turn is completely independent of what happened in previous turns. The Poisson process is the continuous analogue of this stem. There is a constant probability of an arrival occurring at any time which is independent of what has gone before. This gives you an intuitive explanation of the two properties of the Poisson process given in Sections\~ \ref{sub:poissonIndependence}~ and\~ \ref{sub:poissonSimilarities}.

  
  }

\figure{\includepng{\diagramsDir/npa/stateDiagramProcess}{80%}}{stateDiagramProcess}{stateDiagramProcess}

\notes{
  
  \label{cap:coinMonopolyProcess}
}

\notes{## Examples}

\notes{1. It is possible to compute a probability distribution for a number of successes given a number of trials. This distribution is known as the binomial. For $n$ trials (equivalent to $n$ coin tosses or $n$ turns for Coin Monopoly) the probability of $k$ successes (equivalent to $k$ moves forward) is given by
  

$$
P\left(k\right)=\left(\begin{array}{c}
n\\
k\end{array}\right)P\left(h\right)^{k}(1-P\left(h\right))^{n-k}\label{eq:binomialDistirbution}
$$

where $\left(\begin{array}{c}
n\\
k\end{array}\right)=\frac{n!}{k!(n-k)!}$ is known as the binomial coefficient.
  By considering the limiting case as the probability of a success (or heads) goes to zero but the number of trials goes to $\infty$ show that a Poisson process can be recovered.}

\notes{\answer{
Since each of our turns takes  $\Delta t$  time, we know that after  $t$  time we will have completed  

$$
n=\frac{t}{\Delta t}\label{eq:nInTermsOfDeltaT}
$$

  turns. Since we defined  $P\left(h\right)=\lambda\Delta t$  we can therefore write 

$$
P\left(h\right)=\frac{\lambda t}{n}.
$$

 We now substitute this expression for the probability of heads into the binomial distribution ( \ref{eq:binomialDistirbution} ) giving  

$$
\begin{aligned}
P\left(k|\lambda,t\right) & = & \frac{n!}{k!(n-k)!}\left(\frac{\lambda t}{n}\right)^{k}\left(1-\frac{\lambda t}{n}\right)^{n-k}\\
 & = & \frac{n\left(n-1\right)\dots\left(n-\left(k-1\right)\right)}{n^{k}\left(1-\frac{\lambda t}{n}\right)^{k}}\frac{(\lambda t)^{k}}{k!}\left(1-\frac{\lambda t}{n}\right)^{n}.
\end{aligned}
$$

 The next step is to take the limit as  $n\rightarrow\infty$ . From ( \ref{eq:nInTermsOfDeltaT} ) we can see that this is equivalent to taking  $\Delta t\rightarrow0$ . In this limit we can take advantage of the following  

$$
\lim_{n\rightarrow\infty}\frac{n\left(n-1\right)\dots\left(n-\left(k-1\right)\right)}{n^{k}\left(1-\frac{\lambda t}{n}\right)^{k}}=1.
$$

 You should recognise this from the fact that the dominant term in the numerator is  $n^{k}$  and the dominant term in the denominator is  $n^{k}$ . Secondly we use the fact that  

$$
\lim_{m\rightarrow\infty}\left(1+\frac{z}{m}\right)^{m}=\exp\left(z\right).
$$

 Inserting these two limits into the equation gives:  

$$
P\left(k|\lambda,t\right)=\frac{(\lambda t)^{k}}{k!}e^{-\lambda t}.\label{eqn:poisson}
$$

 which is recognised as a Poisson process. In other words, we have proved that a Poisson process is a particular type of Markov chain, in fact, because we have taken the limit as  $\Delta t\rightarrow0$ , this system is now continuous time, it is therefore known as a Markov process.
}{0}}

\notes{\section{Steady State\label{sec:steadyState}}}

\notes{Often we are interested in the steady state behaviour of a system, rather than the transient dynamics. We might ask the question: what is the average network delay when the system has reached steady state? What do we mean by steady state?}

\notes{1. A stable condition that does not change over time or in which change in one direction is continually balanced by change in another.
  \footnote{http://www.dictionary.com .}
2. A steady state is a dynamic equilibrium.}

\notes{A Markov process, under certain conditions, will reach a steady state distribution over $k$. Recall that a probabilistic process $p\left(k|t\right)$ is a `noisy function' of time. Some probabilistic processes will converge to a probability distribution when we look at them in the limit as time $\rightarrow\infty$. Not all will though, for example a Poisson *won't*.
The steady state distribution is taken to be

$$
\lim_{t\rightarrow\infty}p\left(k|t\right)=p\left(k\right)
$$

the average value of $k$ at steady state is then given by

$$
\left\langle k\right\rangle _{p\left(k\right)}=\sum_{k=0}^{\infty}p\left(k\right)k.
$$

}

\notes{\subsection{Coin Monopoly Revisited}}

\notes{The Markov chain underlying `Coin Monopoly' (as presented in the previous chapter) has no associated *steady state*distribution, over time the value of $k$ will always increase. In this chapter we will introduce a slightly more complex Markov process called a birth-death processes. A birth-death process does have a steady state distribution. We will use a condition known as detailed balance to discover this distribution.}

\speakernotes{In `Coin Monopoly' Anne moved forward at each time step by tossing a coin, if it came up heads she moved forward, otherwise she stayed on the same square. Anne's friend Bob suggests a variation of this game. At each of Anne's turns Bob tosses a second coin. If Bob's coin comes up heads then Anne has to move backwards one step. Anne likes this idea, but is concerned that she doesn't want to go back from the start so she suggests an additional, and final rule, that if she haven't been around the board yet and she is at GO (*i.e.* state $N\left(t\right)=0$) then Bob is not allowed to toss his coin.
  At each time step we now have to consider Let's represent the outcomes of this system If we assume, as before}

\notes{\section{Birth Death Process}}

\notes{Let's consider a model for births and deaths in a population. Recall the Markov chain underlying `Coin Monopoly' (Figure\  \ref{cap:coinMonopolyStateDiagram}). Consider a modification to this diagram whereby as well as moving forward in state space (a transition from state equalling $k$ to state equalling $k+1$) you can also move backwards (a transition from state equalling $k$ and state equalling $k-1$). The only restriction we impose is that the state cannot go negative. This system is known as a birth-death process. A birth is an increase in the state $k$ and a death is a decrease.
We represent the discrete version of this system with a state diagrams in Figure\  \ref{cap:birthDeathChainState} is with a state diagram as follows.and the continuous version with that in Figure\  \ref{cap:birthDeathChainProcess}.}

\figure{\includepng{\diagramsDir/npa/birthDeathChain}{100%}}{State diagram for a birth-death chain.}{cap:birthDeathChainState}

\notes{Such processes form the basic model for many different queues. The various different queues are often summarised by a simple notation known as Kendall's notation.}

\figure{\includepng{\diagramsDir/npa/birthDeathProcess}{100%}}{State diagram for a birth-death process.}{cap:birthDeathChainProcess}

\notes{\section{Kendall's Notation\label{sec:kendall}}}

\notes{Kendall's notation provides a simple way of summarising the characteristics of the arrivals and service times of a queue, as well as the number of `servers' and maximum number of customers. In its simplest form it represents
/ / /
Arrival characteristics
Departure characteristics
number of servers
max number of customers
The arrival and departure characteristics are summarised by}

\notes{* $M$ --- Markov --- Poisson distributed arrivals, exponentially distributed service times.
* $D$ --- Deterministically distributed times.
* $G$ --- General distribution for inter-arrival/service times.}

\notes{\section{Global Balance}}

\notes{We seek a stationary distribution by looking for global balance equations. Global balance equations state that at equilibrium the frequency of transitions out of state $k$ equals the frequency of transitions into $k$. (pg 260-262 of [@Bertsekas:data92]).}

\notes{\subsection{Discrete Time Markov Chain}}

\notes{In its most general form a Markov chain can be defined by a transition probability matrix, this gives the probability of transition from any state to any other. If the probability of transition from state $i$ to state $j$ is given by $P_{ij}$ then the transition probability matrix is given by

$$
\mathbf{P}=\left[\begin{array}{ccccc}
P_{00} & \cdots & P_{i0} & \cdots & P_{N0}\\
\vdots & \ddots &  &  & \vdots\\
P_{0j} &  & P_{ij} &  & P_{Nj}\\
\vdots &  &  & \ddots & \vdots\\
P_{0N} & \cdots & P_{iN} & \cdots & P_{NN}\end{array}\right].
$$

Under global balance, if the steady state probability of being in state $j$ is $P\left(j\right)$, then we must have

$$
P\left(j\right)\sum_{i=0}^{\infty}P_{ji}=\sum_{i=0}^{\infty}P\left(i\right)P_{ij}
$$

which in English says the probability of leaving state $j$ should be equal to the probability of arriving in state $j$. If this is true then the system is in global balance and there is an associated steady state distribution.}

\notes{\subsection{Continuous Time Markov Process}}

\notes{In Markov processes we are interested in rates of transfer rather than probabilities if the rates of transfer between states are given by a matrix whose elements $q_{ij}$ give the rate of transfer between state $i$ and state $j$, then the global balance equations give

$$
P\left(j\right)\sum_{i=0}^{\infty}q_{ji}=\sum_{i=0}^{\infty}P\left(i\right)q_{ij}.
$$

}

\notes{\section{Detailed Balance}}

\notes{For the birth death processes we are considering transitions only occur between state $k$ and $k+1$ or $k-1$. In other words $P_{ij}=0$ if $i>j+1$ and $i<j-1$. This leads us to a special case of the global balance equations known as the detailed balance equations which look at the flow between two states. For the discrete case

$$
P\left(k-1\right)P_{k-1,k}=P\left(k\right)P_{k,k-1}
$$

and for the continuous case 

$$
P\left(k-1\right)q_{k-1,k}=P\left(k\right)q_{k,k-1}.
$$

In our notation rate from $k$ to state $k-1$is given by $\mu_{k}$ and the rate from $k-1$ to $k$ is given by $\lambda_{k-1}$so we have

$$
P\left(k-1\right)\lambda_{k-1}=P\left(k\right)\mu_{k}.
$$

 To understand what this represents it is easier to consider the flow rates at a *boundary*between two states, $k-1$ and $k$. This is shown in Figure\  \ref{cap:flowAtBoundary}.
At steady state, flow from $k-1$ to $k$ is given by $\lambda_{k-1}P\left(k-1\right)$. Flow from $k$ to $k-1$ is given $\mu_{k}P\left(k\right)$. For flow to be balanced we have 

$$
\lambda_{k-1}P\left(k-1\right)=\mu_{k}P\left(k\right)
$$

 leading to 

$$
P\left(k\right)=\frac{\lambda_{k-1}}{\mu_{k}}P\left(k-1\right).
$$

For different systems, the birth rate and death rate will differ. We will first study the $M/M/1$ queue which is a birth-death process where the birth rate and death rate are constant regardless of the state of the queue.}

\figure{\includepng{\diagramsDir/npa/boundaryFlow}{40%}}{Flow rates at a Boundary for a birth-death process.}{cap:flowAtBoundary}

\notes{\section{$M/M/1$ Queue\label{sec:MM1Stationary}}}

\notes{From Kendall's notation (Section\  \ref{sec:kendall}) we know that in an $M/M/1$ that the arrivals occur as a Poisson process, and service times are exponentially distributed. This implies a birth death process with constant birth rate $\lambda_{k}=\lambda$ (from the Poisson process) and constant death rate (from the exponentially distributed service times) $\mu_{k}=\mu$. We now give a worked example showing how the stationary distribution is derived using detailed balance. The first step is to draw the state diagram.
The state diagram highlights several points.}

\figure{\includepng{\diagramsDir/npa/stateMM1}{100%}}{State diagram for $M/M/1$ queue.}{stateMM1}

\notes{1. There are no transitions to a state below 0.
2. There is no maximum value for the state shown, this implies that $k$ is unbounded.
3. The birth rates and death rates for each state are indicated.
4. Transitions are only possible between neighbouring states.}

\notes{Having drawn the state diagram the next step is to analyse the flow rates at a boundary. We analyse between $k$ and $k-1$.
At steady state, the expected flow from $k-1$ to $k$ is given by $\lambda P\left(k-1\right)$. Flow from $k$ to $k-1$ is given $\mu P\left(k-1\right)$. For flow to be balanced we have 

$$
\lambda P\left(k-1\right)=\mu P\left(k\right)
$$

 leading to 

$$
P\left(k\right)=\frac{\lambda}{\mu}P\left(k-1\right).
$$

 Thus 

$$
\begin{aligned}
P\left(k\right) & = & \left(\frac{\lambda}{\mu}\right)^{k}P\left(0\right)\\
 & = & \rho^{k}P\left(0\right),
\end{aligned}
$$

 where we have defined $\rho=\frac{\lambda}{\mu}$, which for the $M/M/1$ queue will turn out to be a useful ratio called the *utilisation factor*.}

\figure{\includepng{\diagramsDir/npa/boundaryFlowMM1}{40%}}{Flow rates at a boundary.}{cap:flowAtBoundary}

\notes{\subsection{Normalisation\label{sub:normalisationMM1}}}

\notes{To find $P\left(0\right)$ we exploit our knowledge that, for the $M/M/1$ queue $0\leq k<\infty$. Given that the steady state distribution *must*be normalised, we can write 

$$
\sum_{k=0}^{\infty}P\left(k\right)=1
$$

 and therefore 

$$
1=P\left(0\right)\sum_{k=0}^{\infty}\rho^{k}
$$

 giving 

$$
P\left(0\right)=\frac{1}{\sum_{k=0}^{\infty}\rho^{k}}.\label{eq:MM1Series}
$$

 We are once again faced with an infinite series in the denominator of (\ref{eq:MM1Series}). This series converges if $\rho<1$ (when the birth rate is less than the death rate), 

$$
\sum_{k=0}^{\infty}\rho^{k}=\frac{1}{1-\rho}\,\,\,\textrm{for\,\,\,$\rho<1$},
$$

 meaning that 

$$
P\left(0\right)=\left(1-\rho\right).\label{eq:MM1emptyProb}
$$

 We can now write down the full distribution for the *steady state* probabilities 

$$
P\left(k\right)=\rho^{k}\left(1-\rho\right).
$$

}

\notes{\subsection{Faster Arrivals than Service}}

\notes{Notice that if the arrival rate (birth rate) is greater than the service rate (death rate) then $\rho>1$ and the series in (\ref{eq:MM1Series}) doesn't converge. This is indicative of the fact that if the birth rate is greater than the death rate there is no steady state distribution: the queue simply continues to grow in size.}

\notes{\subsection{Average Number in System}}

\notes{For network design we might be interested in the average queue length. We can use the steady state probabilities to compute this quantity.
The average number of customers in the system *is not* the same as the average queue length because a customer being served (*e.g.*a packet under transmission) is not in the queue.
The average number of customers in the system is given by the expected state of the system,

$$
\left\langle k\right\rangle _{P\left(k\right)}=\sum_{k=0}^{\infty}kP\left(k\right)
$$

in the examples section at the end of this chapter we show how this average can be computed as

$$
\begin{aligned}
\left\langle k\right\rangle _{P\left(k\right)} & = & \frac{\rho}{1-\rho}\\
 & = & \frac{\lambda}{\mu-\lambda}.
\end{aligned}
$$

The variance can also be computed, it is given by

$$
\textrm{var}\left[k\right]=\left\langle k^{2}\right\rangle -\left\langle k\right\rangle ^{2}=\frac{\rho}{\left(1-\rho\right)^{2}}.
$$

Computation of the variance is an exercise in Tutorial Sheet 2.
As an exercise on the tutorial sheet, you will show that the variance of the number in the system is given by

$$
\textrm{var}\left[k\right]=\left\langle k^{2}\right\rangle -\left\langle k\right\rangle ^{2}=\frac{\rho}{\left(1-\rho\right)^{2}}.
$$

}

\notes{\section{Discrete Simulation of $M/M/1$}}

\notes{In the first lab you will run a discrete simulation of an $M/M/1$ queue. A discrete simulation for these queues is easy to run because it takes the form of a Markov chain. The state diagram for this chain is shown in Figure\  \ref{cap:discreteMM1}.The simulation consists of a loop over discrete time steps. For each time step there are three possible events: the state of the system increases by one; the state of the system decreases by one and the state of the system stays the same. Modelling the queue is therefore a simple matter of testing which of these outcomes is true.}

\figure{\includepng{\diagramsDir/npa/discreteMM1State}{100%}}{State diagram for the discrete version of the $M/M/1$ queue.}{cap:discreteMM1}

\figure{\includepng{\diagramsDir/npa/probOutcome}{80%}}{Testing for one of three outcomes. Generate a random number between 0 and 1 (in Python, `numpy.random.random()`), see where the result lies on the line above. If it is less than $P\left(b\right)$ then state of queue increases by 1, if it is greater than $P\left(b\right)$ but less than $P\left(b\right)+P\left(d\right)$ *and the queue is not empty* then state of queue decreases by one, otherwise queue state stays the same.}{probOutcome}

\notes{\subsection{Approximating a Continuous $M/M/1$ Queue}}

\notes{We know from our derivation in Section\  \ref{sec:poissonAsMarkov} that a Poisson process can be derived by considering the limit, as the discrete time intervals go to zero, of a simple Markov chain. A continuous $M/M/1$ queue is also the limit of the discrete model we are using for simulation. In your lab class you can make this approximation by taking $\Delta t$ to be much smaller than $\lambda$ or $\mu$. Then you may set $P\left(b\right)=\lambda\Delta t$ and $P\left(d\right)=\mu\Delta t$.}

\notes{\subsection{Demonstration}}

\notes{In your lab class you will run a simulation of the discrete queue and answer questions on the analysis of that queue. To help you understand the simulation process we will demonstrate a simulation in the lecture. We also give you (below) histograms that are similar to those you should be producing in the lab class.}

\speakernotes{In lecture show demo for high $\rho$ ($\lambda=1.9$,$\mu=2$) and low $\rho$ ($\lambda=1$, $\mu=2$) exhibiting high $N$ and $T$ and low $N$ and $T$. Talk about how the probabilities converge to the steady-state values, mention issues of heavy tails *etc*..}

\figure{\includepng{\diagramsDir/npa/rho_half_1000_arrivals}{45%}}{Left figure: steady state probabilities after the first 100 seconds for $\rho=0.5$. Right figure: steady state probabilities after the first 1000 seconds for $\rho=0.5$.}{rho-half-1000-arrivals}

\figure{\includepng{\diagramsDir/npa/rho_point95_1000_arrivals}{45%}}{Left figure: steady state probabilities after the first 100 seconds for $\rho=0.95$. Right figure: steady state probabilities after the first 1000 seconds for $\rho=0.95$.}{rho-point95-1000-arrivals}

\notes{## Examples}

\notes{1. The mean number in the system for the $M/M/1$ queue is given by considering the expectation under the steady state distribution. Compute this value.}

\notes{\answer{
\subsection*{Answer}

$$
\begin{aligned}
\left\langle k\right\rangle _{P\left(k\right)} & = & \sum_{k=0}^{\infty}kP\left(k\right)\\
 & = & \left(1-\rho\right)\sum_{k=0}^{\infty}k\rho^{k}\\
 & = & \rho\left(1-\rho\right)\sum_{k=0}^{\infty}k\rho^{k-1}\\
 & = & \rho\left(1-\rho\right)\frac{\partial\sum_{k=0}^{\infty}\rho^{k}}{\partial\rho}\\
 & = & \rho\left(1-\rho\right)\frac{\partial}{\partial\rho}\left[\frac{1}{1-\rho}\right]\\
 & = & \rho\left(1-\rho\right)\frac{1}{\left(1-\rho\right)^{2}}\\
 & = & \frac{\rho}{1-\rho}\\
 & = & \frac{\lambda}{\mu-\lambda}
\end{aligned}
$$

}{0}}

\endif

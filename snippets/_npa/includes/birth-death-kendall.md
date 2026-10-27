\ifndef{birthDeathKendall}
\define{birthDeathKendall}

\section{Steady State}

\notes{Once the Poisson process sits inside the Markov family, the next objects are birth-death processes and the $M/M/1$ queue. We first need *steady state*: a condition that does not change with time, or in which change in one direction is continually balanced by change in the other. Network delay, once the transient has died, is a steady-state question.}

\slides{* Steady state: no net change, or balanced flows
* We ask for delay and occupancy *after* the transient}

\section{Birth-Death Processes}

\notes{Start from the Coin Monopoly chain and allow a step *backwards* as well as forwards: $k\to k+1$ (a birth) and $k\to k-1$ (a death), with the state forbidden from going negative. That is a birth-death process. Discrete and continuous versions have the state diagrams below.}

\figure{\includepng{\diagramsDir/npa/birthDeathChain}{70%}}{State diagram for a discrete-time birth-death chain.}{birth-death-chain}

\figure{\includepng{\diagramsDir/npa/birthDeathProcess}{70%}}{State diagram for a continuous-time birth-death process. Births increase $k$; deaths decrease it.}{birth-death-process}

\slides{* Birth: $k\to k+1$; death: $k\to k-1$
* $k$ cannot go negative
* Many queues are birth-death processes}

\section{Kendall's Notation}

\notes{Kendall's notation summarises a queue as
$$
A/S/m/K,
$$
arrival process / service process / number of servers / capacity (optional). The letters for $A$ and $S$ are $M$ (Markov: Poisson arrivals or exponential service), $D$ (deterministic), and $G$ (general).}

\slides{* $A/S/m/K$: arrivals / service / servers / capacity
* $M$: Poisson or exponential
* $D$: deterministic; $G$: general}

\endif

\ifndef{markovChainsMonopoly}
\define{markovChainsMonopoly}

\section{Markov Chains}

\notes{The Poisson process is a special case of a Markov process. We start in discrete time, with *Markov chains*, then take a continuum limit. Both chains and processes obey the Markov property: the future is conditionally independent of the past given the present.}

\slides{* Markov chain: discrete time
* Markov process: continuous time
* Markov property: future $\perp$ past $\mid$ present}

\subsection{The Markov Property}

\notes{Let time be discrete, $t=0,1,2,\ldots$, and let $N(t)$ be a state. The chain has the Markov property if $N(t)$ depends on the history only through $N(t-1)$.}

\subsection{Monopoly}

\notes{A single-player Monopoly board has forty squares. Let $N(t)$ be the square index plus $40$ for each completed circuit: twice round and on GO gives $N(t)=80$; once round and on King's Cross gives $N(t)=45$. Time $t$ counts turns.}

\notes{Each turn the player rolls two six-sided dice. Write $d(t)$ for the total. Then
$$
N(t)=N(t-1)+d(t).
$$
The next square depends only on the current square and the current roll, so the walk has the Markov property.}

\figure{\includepng{\diagramsDir/npa/smallMonopoly}{45%}}{A Monopoly board. The token's square after a turn depends only on the square before the turn and the dice.}{small-monopoly}

\slides{* Forty squares; $N(t)$ counts circuits as well as the square
* $N(t)=N(t-1)+d(t)$
* Markov: the next square does not depend on the path that led here}

\subsection{State Diagrams}

\notes{A Markov chain has a state diagram in the same spirit as a finite-state machine, with two differences. The state space need not be finite. Transitions carry probabilities (or, for a process, rates) rather than deterministic labels.}

\slides{* State diagrams: nodes are values of $N$
* Transitions carry probabilities or rates
* The state space may be infinite}

\endif

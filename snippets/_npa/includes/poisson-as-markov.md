\ifndef{poissonAsMarkov}
\define{poissonAsMarkov}

\section{The Poisson Process as a Markov Process}

\notes{We now pass from a discrete-time chain to a continuous-time process, and recover the Poisson process as a Markov process with a restricted set of transitions. The device is a one-dimensional walk we call Coin Monopoly.}

\subsection{Coin Monopoly}

\notes{Anne has lost the dice. She tosses a coin instead: $d(t)=0$ on tails and $d(t)=1$ on heads. The state either stays put or advances by one square.}

\figure{\includepng{\diagramsDir/npa/stateDiagram}{70%}}{State diagram for Coin Monopoly. Each node is a square index. With each turn the token stays or moves one step, with the probabilities on the arrows.}{coin-monopoly-chain}

\notes{The game is slow. Speed it up by shrinking the turn length $\Delta t$ and using a coin whose heads probability is $P(h)=\lambda\Delta t<1$, so $P(\text{tails})=1-\lambda\Delta t$.}

\slides{* Coin Monopoly: $d(t)\in\{0,1\}$
* $P(h)=\lambda\Delta t$, turn length $\Delta t$
* After $n$ turns the occupancy is binomial}

\subsection{Binomial Trials to a Poisson Process}

\notes{After $n$ turns the number of heads $k$ is binomial,
$$
P(k)=\binom{n}{k}P(h)^k\bigl(1-P(h)\bigr)^{n-k},\qquad \binom{n}{k}=\frac{n!}{k!(n-k)!}.
$$
In time $t$ there are $n=t/\Delta t$ turns, so $P(h)=\lambda t/n$. Substitute and take $n\to\infty$, which is $\Delta t\to 0$:
$$
\lim_{n\to\infty}\frac{n(n-1)\cdots(n-k+1)}{n^k\bigl(1-\lambda t/n\bigr)^k}=1,
\qquad
\lim_{n\to\infty}\Bigl(1-\frac{\lambda t}{n}\Bigr)^{n}=e^{-\lambda t}.
$$
The occupancy becomes
$$
P(k\mid\lambda,t)=\frac{(\lambda t)^k}{k!}e^{-\lambda t}.
$$
That is a Poisson process: a Markov *process*, because time is now continuous.}

\slides{* $n=t/\Delta t$, $P(h)=\lambda t/n$
* $n\to\infty$ recovers $P(k\mid\lambda,t)=(\lambda t)^k e^{-\lambda t}/k!$
* Poisson process $=$ Markov process with only $k\to k+1$}

\subsection{Process State Diagrams}

\notes{On a continuous-time diagram we drop the self-transition arrows and replace transition probabilities by rates.}

\figure{\includepng{\diagramsDir/npa/stateDiagramProcess}{70%}}{Coin Monopoly in the limit $\Delta t\to 0$: a Poisson process. Rates replace probabilities, and there are no self-loops.}{poisson-as-markov-process}

\notes{The construction explains two Poisson properties from the last lecture. At every instant the probability of an arrival is constant, and it does not depend on what has already happened. That is the Markov property in continuous time.}

\endif

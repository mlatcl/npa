\ifndef{tandemAndBurke}
\define{tandemAndBurke}

\section{Queues in Tandem}

\notes{So far every model has been a single queue. Two transmission lines in series are the smallest network. Packet length does not change from hop to hop, and service time is proportional to length. Arrivals at the first queue are Poisson; lengths are exponential.}

\notes{The first hop is $M/M/1$. The second is not. A long packet occupies the first server for a long time, during which the second queue can drain. A long packet therefore tends to arrive at the second hop when that queue is shorter, and waits *less* there than a short packet would. The analogy is a slow vehicle on a road: from that driver's seat the road looks empty, because they never catch anyone. The first queue has destroyed independence between a packet's length and the state of the second queue.}

\notes{That correlation is hard to treat exactly. The way through is to *break* it: pretend service times at the two hops are statistically independent, even though they are the same length. Lab 2 asked you to look at whether the simulated occupancies still match isolated $M/M/1$ formulae. Kleinrock's independence assumption, below, is that pretence made systematic.}

\slides{* Tandem: first hop $M/M/1$, second is not
* Long packet sees a drained second queue
* Independence of service across hops is an assumption, not a fact}

\section{Time Reversibility and Burke}

\notes{Birth-death chains (every Markov queue in the course except $M/G/1$) satisfy detailed balance. They are also *time-reversible* in steady state: the arrival process is Poisson at rate $\lambda$, and so is the *departure* process. The service rate $\mu$ is not the departure rate, because a departure can occur only when $k>0$. That happens a fraction $\rho$ of the time, so the departure rate is $\mu\rho=\lambda$.}

\notes{Burke's theorem: an $M/M/1$, $M/M/m$, or $M/M/\infty$ queue in steady state with Poisson arrivals at rate $\lambda$ has a Poisson departure process at rate $\lambda$, *and* the occupancy at time $t$ is independent of the departure times before $t$. Loss systems are excluded: blocked customers never enter, so the process that does enter is not rate $\lambda$.}

\notes{The second claim is the surprising one. A burst of departures might seem to leave the queue short. Burke says it does not. The only way both can be true is that the occupancy *before* the burst was abnormally high.}

\notes{If we grant independent service at the second hop, Burke says the input to that hop is Poisson at $\lambda$. Two $M/M/1$ queues in series then have occupancies
$$
P_1(k)=(1-\rho_1)\rho_1^k,\qquad P_2(\ell)=(1-\rho_2)\rho_2^\ell,
$$
and the joint distribution factors. Mean delay is the sum of the two sojourn times.}

\slides{* Time-reversible birth-death: departures Poisson at $\lambda$
* Burke: occupancy independent of past departures
* Independent service $\Rightarrow$ tandem is two $M/M/1$}

\endif

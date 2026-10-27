\ifndef{multiaccessAndAloha}
\define{multiaccessAndAloha}

\section{Multiaccess Channels}

\notes{A multiaccess system is one channel shared by many stations: a satellite and its ground terminals, packet radio, a multitapped bus, a LAN. Typical LAN rates in 2006 were 10 Mbps to 1 Gbps, distances from metres to kilometres, target error rates $10^{-8}$ to $10^{-11}$. Throughput --- messages per second --- is approximately the utilisation $\rho$ when overhead bits are few.}

\notes{Before ALOHA, the standard split was multiplexing. $m$ independent Poisson streams each of rate $\lambda/m$, exponential packet lengths giving service rate $\mu$ on the full line. Statistical multiplexing superposes them to Poisson rate $\lambda$ and delay $1/(\mu-\lambda)$. Splitting the line into $m$ circuits of rate $\mu/m$ multiplies that delay by $m$: when only one station is transmitting, statistical multiplexing uses the whole bandwidth; TDM/FDM wastes a fraction $(m-1)/m$. This is Bertsekas and Gallager, Example 3.9.}

\notes{On a multiaccess channel the same split is called TDMA or FDMA (CDMA is not treated here). Statistical multiplexing assumed a *single* $M/M/1$ queue. Stations on a LAN are distributed; there is no single queue without a central controller. TDMA/FDMA can still dedicate a transmit channel per station. How to do statistical multiplexing without a centre is the random-access question.}

\slides{* One channel, many stations
* Statistical multiplexing beats TDM/FDM by factor $m$
* No central queue $\Rightarrow$ random access}

\section{Pure ALOHA}

\notes{ALOHA was a University of Hawaii packet-radio network among the islands; Ethernet inherited the collision-and-retry idea. All stations share one channel. A transmission that overlaps another is a *collision*; the station becomes *backlogged* and retries after a random delay (a fixed delay would collide again immediately).}

\figure{\includepng{\diagramsDir/npa/pureALOHA}{80%}}{Pure ALOHA: a packet sent at $t$ collides with any other packet sent in $(t-1,t+1)$.}{pure-aloha-vulnerable}

\notes{Each packet takes one time unit. A packet sent at $t$ collides with any other sent in $(t-1,t+1)$: a vulnerable period of length $2$. New arrivals at all stations are Poisson at rate $\lambda$, with infinitely many stations so that no one station is a finite fraction of $\lambda$. A backlogged station waits an exponential time of rate $\mu$ before retry. If $n$ stations are backlogged, retries are Poisson at rate $n\mu$, and the channel sees attempts at
$$
G(n)=\lambda+n\mu.
$$
(Bertsekas and Gallager write $x$ for our $\mu$.)}

\notes{The probability of no other attempt in two time units is $e^{-2G}$. Throughput --- successful transmissions per unit time --- is
$$
S=G e^{-2G}.
$$}

\figure{\includepng{\diagramsDir/npa/pureALOHAThroughput}{70%}}{Pure ALOHA throughput $S=Ge^{-2G}$. The maximum is $1/(2e)\approx 0.184$ at $G=1/2$.}{pure-aloha-throughput}

\notes{Stationary points of $S$ solve $(1-2G)e^{-2G}=0$, so $G=1/2$ (the maximum) or $G\to\infty$ (a minimum). At best the channel is busy about 18\% of the time. With $X=1$, utilisation equals $\lambda$.}

\slides{* Vulnerable period of length 2
* $G=\lambda+n\mu$, $S=Ge^{-2G}$
* $\max S=1/(2e)$ at $G=1/2$}

\section{Slotted ALOHA}

\notes{Force stations to wait for a slot boundary, slots of length one synchronised across the network. A collision now requires another attempt in the *same* slot: the vulnerable period is half as long. Throughput becomes
$$
S=G e^{-G},
$$
with maximum $1/e$ at $G=1$, twice pure ALOHA.}

\figure{\includepng{\diagramsDir/npa/slottedALOHAThroughput}{70%}}{Slotted ALOHA throughput $S=Ge^{-G}$. The maximum is $1/e$ at $G=1$.}{slotted-aloha-throughput}

\notes{The wait through $k$ exponential retries is Erlang. Averaging over the geometric number of attempts, the backlog wait is exponential with rate $\mu'=\mu e^{-2G}$. For fixed $\lambda$ and $n$ the delay is minimised at $\mu=1/(2n)$, and that minimum grows linearly in $n$ and exponentially in $\lambda$. In practice $\mu$ cannot depend on $n$ unless stations announce their backlog on the very channel we are analysing. Compare the ARQ geometric service time: there $p=1-q$ was an error probability; here $q=e^{-2G}$ is a success probability.}

\slides{* Slotted: vulnerable period 1, $S=Ge^{-G}$
* $\max S=1/e$ at $G=1$
* Backlog wait exponential; best $\mu=1/(2n)$}

\endif

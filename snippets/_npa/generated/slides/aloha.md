\ifndef{npaGenSlidesAloha}
\define{npaGenSlidesAloha}

\newslide{Multiaccess Systems}

\slides{* Finally we briefly review multiaccess systems.
* These are systems where there is one communication channel and multiple stations (or nodes) making use of it.
* Examples of multiaccess systems include: Satellite systems; packet radio networks; a multitapped bus.}

\newslide{LANs}

\slides{* A very common example of multi-access channels is the local area network.
* In a local area network transmission rates are around 10Mbps to 1Gbps.
* Transmission distances range from a few meters to several kilometres.}

\newslide{LANs (continued)}

\slides{* The required error rates are low: typically from $10^{-8}$ to $10^{-11}$, that's about 1 error every Gigabyte.
* Typically we are interested in the throughput of the network --- the amount of data or messages passing through the network each second.
* If the number of overhead bits (associated with network administration *etc*.) is low then this is approximately equal to the utilization factor $\rho$.}

\newslide{Channel Multiplexing}

\slides{* Until the introduction of the ALOHA network the standard approach to splitting a channel was through multiplexing.
* We will now briefly review this approach to multiplexing using Example  3.9 from Bertsekas and Gallagher.
* Assume we have $m$ statistically independent Poisson streams.}

\newslide{Channel Multiplexing (continued)}

\slides{* Each has arrival rate $\frac{\lambda}{m}$.
* The packets to be transmitted are assumed to have an exponentially distributed length.
* For a given bandwidth this leads to a service time distribution for the whole transmission line which is an exponential with a rate parameter $\mu$.}

\newslide{Statistical Multiplexing}

\slides{* System 1: merge the Poisson streams together, through statistical multiplexing.
* The superposition property of the Poisson distribution tells us that they become a Poisson stream with rate $\lambda$.
* If the transmission times are exponentially distributed the average delay, from the $M/M/1$ queue, will be

$$
\bar{T}=\frac{1}{\mu-\lambda}.
$$

}

\newslide{Time or Frequency Division Multiplexing}

\slides{* System 2: provide each communication channel with a separate `circuit'.
* The transmission line needs to be split into $m$ separate channels.}

\newslide{Time or Frequency Division Multiplexing (continued)}

\slides{* Each of these separate channels will now have service time distributions with a reduced rated $\frac{\mu}{m}$.
* Delay in this system will now be

$$
\bar{T}=\frac{1}{\frac{\mu}{m}-\frac{\lambda}{m}}=\frac{m}{\mu-\lambda}
$$

which is $m$ times larger than that for statistical multiplexing.}

\newslide{Why does this happen?}

\slides{* The reduction in delay arises from the fact that when only one of the $m$ channels is transmitting with statistical multiplexing it can use the entire bandwidth of the channel but with time or frequency division multiplexing $\frac{m-1}{m}$ of the bandwidth is wasted.}

\newslide{Multiaccess Systems}

\slides{* In multiaccess systems splitting the channel using time division multiplexing is known as time division multiple access (TDMA).
* Similarly splitting the channel using frequency division multiplexing is known as frequency division multiple access (FDMA).}

\newslide{Multiaccess Systems (continued)}

\slides{* We have already shown that statistical multiplexing can make more efficient use of bandwidth than time or frequency based multiplexing.
* However in a multiaccess system it can be difficult to implement in the manner discussed above.}

\newslide{Multiplexing for Multiaccess}

\slides{* We assumed that the all the transmissions could be queued in a single $M/M/1$ queue.
* In a local area network the transmitting stations (or nodes) are distributed across different portions of the network as are the receiving nodes.}

\newslide{Multiplexing for Multiaccess (continued)}

\slides{* Forming a single queue is not possible without some form of centralised control.
* TDMA and FDMA can be implemented by by dedicating one channel for each station to transmit on, but allowing each station to receive on any channel.
* This allows for an analysis of the type we described above. However, it is not clear how to perform statistical multiplexing in these circumstances.}

\newslide{Random Access}

\slides{* When we have stations distributed across a single communication channel would be to have a centralised computer attempting to control which computer is able to access our transmission lines at what times.
* However, we may wish communication to occur without centralised control. In this case we may choose a *random access* solution.}

\newslide{Random Access (continued)}

\slides{* We will consider random access networks where there is one communication channel on which all the nodes communicate.
  \footnote{It could be the case that only a subset of the nodes have access to the channel.}
* Each station sends a packet immediately whenever it has a packet to send. This means that packets can collide and may have to be resent.}

\newslide{Pure ALOHA Networks}

\slides{* ALOHA network was developed at the University of Hawaii.
* Packet radio network which communicated between different stations on the Hawaiian islands.
* For the ALOHA network
* all stations attempt to communicate on the same channel.}

\newslide{Pure ALOHA Networks (continued)}

\slides{* When a station attempts to transmit, it detects if its transmission has interfered with an existing transmission: this is known as a *collision*.
* If a collision occurs the station becomes *backlogged*and attempts to transmit at a later time.
* If both stations attempted to retransmit after the same period of time they would simply collide again.
* To avoid this problem the stations normally wait for a random period of time before retransmitting.}

\newslide{ALOHA}

\slides{\figure{\includepng{\diagramsDir/npa/pureALOHA}{100%}}{pureALOHA}{pureALOHA}}

\newslide{ALOHA (continued)}

\slides{* For this network we assume that each station can tell whether the transmitted packets were correctly received.
* Furthermore, we assume that each packet requires 1 `time unit' for transmission. This means that if a packet of interest is sent at time $t$, then any other packet sent between time $t-1$ and time $t+1$ will collide with our packet.}

\newslide{Simple Analysis}

\slides{* The arrival rate for packets at all stations is a Poisson process with rate $\lambda.$
* We assume that the number of stations is very large (infinite) so that an individual station's packet rate is an insignificant proportion of $\lambda$, *i.e.* 

$$
\frac{\lambda_{n}}{\lambda}=\lim_{\delta\rightarrow0}\delta=0.
$$

* We denote the number of backlogged stations at any particular time as $n$.}

\newslide{Backlogged Stations}

\slides{* A station is considered backlogged between the time that it became aware that its previous transmission failed and the time of a successful transmission.
* Once a station is aware that a transmission was unsuccessful it waits for $T_{i}$ time units to retransmit where the distribution over these waits is given by

$$
p\left(T_{i}\right)=\mu\exp\left(-\mu T_{i}\right).
$$

}

\newslide{Backlogged Stations (continued)}

\slides{* If $n$ nodes are backlogged then the arrivals from backlogged nodes is a Poisson process with rate $n\mu$.
* The overall `arrival process' for the system is Poisson with a rate $G\left(n\right)=\lambda+n\mu$.}

\newslide{Pure ALOHA}

\slides{* The probability that there are no arrivals in an interval of 2 time units for a Poisson process with rate $G\left(n\right)$ is given by 

$$
p\left(k=0|G\left(n\right),2\right)=\exp\left(-2G\left(n\right)\right).
$$

* Therefore this is the probability that there is no collision between the packet of interest and any other packets in the network.
* It is therefore the probability of a successful transmission.}

\newslide{Throughput}

\slides{\figure{\includepng{\diagramsDir/npa/pureALOHAThroughput}{60%}}{pureALOHAThroughput}{pureALOHAThroughput}}

\newslide{Throughput (continued)}

\slides{* The rate of attempted transmissions is $G\left(n\right)$ so the rate of successful transmissions is given by

$$
G^{\prime}\left(n\right)=G\left(n\right)\exp\left(-2G\left(n\right)\right),
$$

* This is known as the throughput.
* It is the number of packets that successfully reach their destination. The throughput is plotted as a function of $G$ .
* \label{cap:pureALOHAThroughput}}

\newslide{Maximum Throughput}

\slides{* The curve goes up to a maximum point and drops down thereafter.
* We can find the maximum of the throughput by looking for points where the gradient of the throughput is zero.
* Taking the gradient of $G^{\prime}$ with respect to $G$ gives

$$
\frac{dG^{\prime}}{dG}=\exp\left(-2G\right)-2G\exp\left(-2G\right).
$$

}

\newslide{Stationary Points}

\slides{* To find the stationary points we set this equation to zero and solve for $G$. The equation becomes

$$
\exp\left(-2G\right)-2G\exp\left(-2G\right)=0
$$

$$
\left(1-2G\right)\exp\left(-2G\right)=0
$$

* So either $\exp\left(-2G\right)=0$, which in turn implies that $G\rightarrow\infty$ or}

\newslide{Stationary Points (continued)}

\slides{* $1-2G=0$ which implies $G=\frac{1}{2}$.
* The first solution is a minimum (and the throughput is zero) and the second solution is a maximum.
* The maximum is the maximum possible throughput for the system and is given when $G=\frac{1}{2}$.}

\newslide{Maximum Throughput}

\slides{* Substituting into the equation for the throughput we find that the maximum is $\frac{1}{2}\exp\left(-1\right)=\frac{1}{2e}\approx0.184$. This maximum throughput shows that at best the channel is in use only about 18% of the time.
  \footnote{Note that since the service time is fixed at $X_{n}=1$ for all $n$ then the utilisation for this system is given by $\rho=\lambda\bar{X}=\lambda.$}
* The system will be in equilibrium if the throughput equals $\lambda$.}

\newslide{Analysis of Backlog Delay}

\slides{* Recall our assumption that a backlogged node waits for a time, $T_{i}$, before attempting to retransmit, 

$$
p\left(T_{i}\right)=\mu\exp\left(-\mu T_{i}\right).
$$

* Given this assumption, can we compute the delay associated with this backlogged node?
* Since the node may experience several collisions, the wait associated with the backlog will involve a sum over the random variable $T_{i}$. It turns out to be an *Erlang distribution*.}

\newslide{Sums of Exponential Variables and the Erlang Distribution\label{sub:erlang}}

\slides{* If a random variable, $x$, is exponentially distributed with rate parameter $b$. The sum of $a$ random variables, each of which is exponentially distributed with rate parameter $b$ is distributed as an *Erlang distribution.*
* Consider variables a set of $a$ variables$\left(x_{1}\dots x_{a}\right)$ ,

$$
p\left(x_{i}|b\right)=b\exp\left(-bx_{i}\right).
$$

}

\newslide{Sums of Exponential Variables and the Erlang Distribution\label{sub:erlang} (continued)}

\slides{* We define the sum of the values to be, $z=\sum_{i=1}^{a}x_{i}$.
* The distribution governing $z$ is then an *Erlang distribution*, given by 

$$
p\left(z|a,b\right)=\frac{b^{a}}{\left(a-1\right)!}z^{a-1}\exp\left(-bz\right).
$$

}

\newslide{Notes on Erlang}

\slides{* Note that this distribution is a generalisation of the exponential distribution because the exponential is the special case where $a=1$.
* This clearly should be the case because if $a=1$ then the `sum' of that variable will simply be the variable itself.}

\newslide{Erlang Distribution Mean and Variance}

\slides{* The mean of the Erlang distribution is given by 

$$
\left\langle z\right\rangle _{p\left(z|a,b\right)}=\frac{a}{b}
$$

 and the variance is 

$$
\textrm{var}\left(z\right)=\frac{a}{b^{2}}.
$$

}

\newslide{Delay Associated with Backlogs}

\slides{* If the node retransmits $k$ times then the distribution over the total time required, $W=\sum_{i=1}^{k}T_{i}$, comes from the sum of $k$ independent exponentially distributed variables.
* We know that the resulting variable $X$ is Erlang distributed with parameters $\mu$ and $k$, 

$$
p\left(W|k,\mu\right)=\frac{\mu^{k}}{\left(a-1\right)!}W^{k-1}\exp\left(-\mu W\right).
$$

* The probability of transmitting after $k$ attempts is given by 

$$
p\left(k\right)=q\left(1-q\right)^{k-1}.
$$

where $q$ is the probability of a successful transmission. For pure ALOHA $q=\exp\left(-2G\right)$.
  \footnote{Compare this with the ARQ system we analysed in the chapter on $M/G/1$ queues. There we were considering errors (unsuccessful transmissions) so $p=\left(1-q\right)$.}}

\newslide{Distribution for $W$}

\slides{* From the product rule and the sum rule we know that the probability distribution for $W$ is given by

$$
\begin{aligned}
p\left(W|\mu\right) & = & \sum_{k=1}^{\infty}p\left(W|k,\mu\right)p\left(k\right),
\end{aligned}
$$

 

$$
p\left(W|\mu\right)=\sum_{k=1}^{\infty}q\left(1-q\right)^{k-1}\frac{\mu^{k}}{\left(k-1\right)!}W^{k-1}\exp\left(-\mu W\right),
$$

substituting $\dot{k}=k-1$

$$
p\left(W|\mu\right)=\sum_{k=0}^{\infty}q\left(1-q\right)^{\dot{k}}\frac{\mu^{\dot{k}+1}}{\dot{k}!}X^{\dot{k}}\exp\left(-\mu W\right),
$$

extracting the $q$, the exponential term and one of the $\mu$s from the product we rewrite as,

$$
p\left(X|\mu\right)=q\mu\exp\left(-\mu W\right)\sum_{k=0}^{\infty}\frac{\left(\mu\left(1-q\right)W\right)^{\dot{k}}}{\dot{k}!},\label{eq:pXgivenMuWithSum}
$$

The term inside the sum is then recognised as being of the form

$$
\exp\left(x\right)=\sum_{k=0}^{\infty}\frac{x^{\dot{k}}}{\dot{k}!}
$$

$$
\sum_{k=0}^{\infty}\frac{\left(\mu\left(1-q\right)W\right)^{\dot{k}}}{\dot{k}!}=\exp\left(\mu\left(1-q\right)W\right),
$$

which can be substituted back into (\ref{eq:pXgivenMuWithSum}) to obtain

$$
\begin{aligned}
p\left(W|\mu\right) & = & q\mu\exp\left(-\mu W\right)\exp\left(\mu\left(1-q\right)W\right),\\
 & = & q\mu\exp\left(-q\mu W\right)
\end{aligned}
$$

which is recognised as an exponential distribution with rate parameter $\mu^{\prime}=q\mu=\mu\exp\left(-2G\right)$.
* Using the fact that $G$ is a function of $\mu$ we can write

$$
\mu^{\prime}=\mu\exp\left(-2\left(\lambda+n\mu\right)\right).\label{eq:rateFunctionALOHA}
$$

* So the service rate is a function of $\lambda$, $n$ and $\mu$.}

\newslide{Optimum value of $\mu$}

\slides{* For a given value of $\lambda$ and $n$ there is a optimal value for $\mu$.
* This value of $\mu$ can be found by seeking the maximum rate, this is done by differentiating with respect to $\mu$ 

$$
\frac{d\mu^{\prime}}{d\mu}=\exp\left(-2\left(\lambda+n\mu\right)\right)-2n\mu\exp\left(-2\left(\lambda+n\mu\right)\right)
$$

and setting the result to zero to find the stationary points,

$$
\exp\left(-2\left(\lambda+n\mu\right)\right)-2n\mu\exp\left(-2\left(\lambda+n\mu\right)\right)=0,
$$

$$
\left(1-2n\mu\right)\exp\left(-2\left(\lambda+n\mu\right)\right)=0.
$$

}

\newslide{Solutions for $\mu$}

\slides{* There are two solutions to this equation. The first is $\exp\left(-2\left(\lambda+n\mu\right)\right)=0$, meaning that $\lambda+n\mu\rightarrow\infty$. This solution is a minimiser . The other solution is given when 

$$
0=1-2n\mu
$$

or

$$
\mu=\frac{1}{2n},
$$

 this turns out to be a maximum of (\ref{eq:rateFunctionALOHA}).}

\newslide{Notes on Optimum}

\slides{* By maximising the `rate' parameter $\mu^{\prime}$ we minimise the average delay associated with the backlog, which is given by $\bar{W}=\frac{1}{\mu^{\prime}}$.
* By setting $\mu=\frac{1}{2n}$ we find a minimum for the average delay: 

$$
\bar{W}_{\textrm{min}}=2n\exp\left(2\lambda+1\right)
$$

.}

\newslide{Notes on Optimum (continued)}

\slides{* In practice it may be difficult to set the rate $\mu$ to something that is dependent on the number of backlogged nodes.
* This is because the number of backlogged nodes can only be known by nodes communicating their status over the network, we have not allowed for such a mechanism in our analysis.
* Note that the minimum average delay goes up linearly with the number of backlogged nodes and *exponentially* with the rate of arrivals for the system, $\lambda$.}

\newslide{Slotted ALOHA}

\slides{* A simple improvement to the ALOHA system comes from constraining when packets can be sent.
* Instead of allowing stations to transmit immediately they receive a packet each station waits for the beginning of a `slot' to start transmitting.
* These slots are synchronised across the entire network.
* In this system a collision occurs if another station attempts to transmit in the same slot.
* This happens if another station received a packet for transmission in the preceding slot.
* If each slot is one time unit in length the probability of this event is given by

$$
p\left(k=0|G\left(n\right),2\right)=\exp\left(-G\left(n\right)\right).
$$

}

\newslide{Slotted ALOHA}

\slides{* The probability is smaller than for pure ALOHA because the `vulnerable period' for a collision is smaller (half the length of before).
* A collision now only occurs if another station attempts to transmit in the same slot. As a result the rate of successful transmissions is given by

$$
G^{\prime}\left(n\right)=G\left(n\right)\exp\left(-G\left(n\right)\right),
$$

* \label{cap:slottedALOHAThroughput}}

\slides{\figure{\includepng{\diagramsDir/npa/slottedALOHAThroughput}{60%}}{slottedALOHAThroughput}{slottedALOHAThroughput}}

\newslide{Smaller Vulnerable period}

\slides{* The smaller vulnerable period leads to a greater maximum throughput which is now found at $G=1$. The maximum throughput is $\frac{1}{e}$. Slotted ALOHA therefore can be twice as efficient as pure ALOHA.}

\newslide{References}

\slides{* \bibliographystyle{abbrvnat}
\bibliography{lawrence,other,zbooks}}

\endif

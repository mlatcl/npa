\ifndef{npaGenNotesAloha}
\define{npaGenNotesAloha}

\notes{\section{Channel Multiplexing}}

\notes{Let's assume we have $m$ statistically independent Poisson streams. Each has arrival rate $\ensuremath{\frac{\lambda}{m}}$. The packets to be transmitted are assumed to have an exponentially distributed length which, for a given bandwidth leads to a service time distribution for the whole transmission line which is an exponential with a rate parameter $\ensuremath{\mu}$.}

\notes{\subsection{Statistical Multiplexing}}

\notes{If we merge the Poisson streams together, through statistical multiplexing the superposition property of the Poisson distribution (from Section\  \ref{sec:superpositionPoisson}) tells us that they become a Poisson stream with rate $\ensuremath{\lambda}$. If the transmission times are exponentially distributed the average delay, from the $M/M/1$ queue, will be
$$
\ensuremath{\bar{T}}=\ensuremath{\frac{1}{\mu-\lambda}}.$$}

\notes{\subsection{Time or Frequency Division Multiplexing}}

\notes{With the alternative approach of providing each communication channel with a separate circuit the transmission line needs to be split into $m$ separate channels. Each of these separate channels will now have service time distributions with a reduced rate $\ensuremath{\frac{\mu}{m}}$.
Delay in this system will now be $m$ times larger than that for statistical multiplexing$$
\ensuremath{\bar{T}}=\ensuremath{\frac{1}{\frac{\mu}{m}-\frac{\lambda}{m}}}=\ensuremath{\frac{m}{\mu-\lambda}}.$$}

\notes{\subsection{Why does this happen?}}

\notes{The reduction in delay arises from the fact that when only one of the $m$ channels is transmitting with statistical multiplexing it can use the entire bandwidth of the channel. With time or frequency multiplexing $\ensuremath{\frac{m-1}{m}}$ of the bandwidth is wasted.}

\notes{\section{Multiaccess Systems}}

\notes{In multiaccess systems splitting the channel using time division multiplexing is known as time division multiple access (TDMA). Similarly splitting the channel using frequency division multiplexing is known as frequency division multiple access (FDMA). A further technique is known as code division multiple access (CDMA) but we will not discuss that here.
We have already shown that statistical multiplexing can make more efficient use of bandwidth than time or frequency based multiplexing. However in a multiaccess system it can be difficult to implement in the manner discussed above. We assumed that all the transmissions could be queued in a single $M/M/1$ queue. In a local area network the transmitting stations (or nodes) are distributed across different portions of the network as are the receiving nodes. Forming a single queue is therefore not possible without some form of centralised control. TDMA and FDMA can be implanted by dedicating one channel for each station to transmit on, but allowing each station to receive on any channel. This then allows for an analysis of the type we described above. However, it is not clear how to perform statistical multiplexing in these circumstances.}

\notes{\section{Random Access}}

\notes{One way of performing statistical multiplexing when we have stations distributed across a single communication channel would be to have a centralised computer attempting to control which computer is able to access our transmission lines at what times. However, we may wish communication to occur without centralised control. In this case we may choose a random access solution.
We will consider random access networks where there is one communication channel on which all the nodes communicate. Each station sends a packet immediately whenever it receives a packet to send. this means that packets can *collide* and may have to be resent.
\footnote{It could be the case that only a subset of the nodes have access to the channel. For example in a packet radio network the range between stations may mean that only a subset of nodes are able to receive from any particular node. However this complicates analysis so we will ignore this possibility.}}

\notes{\subsection{Pure ALOHA Networks}}

\notes{The ALOHA network was developed at the University of Hawaii, it was a packet radio network which communicated between different stations on the Hawaiian islands. For the ALOHA network (and Ethernet, the modern LAN protocol that was inspired by ALOHA) all stations attempt to communicate on the same channel. When a station attempts to transmit, it detects if its transmission has interfered with an existing transmission: this is known as a collision. If a collision occurs the station becomes *backlogged*and attempts to transmit at a later time. If both stations attempted to retransmit after the *same*period of time they would simply collide again after retransmission. To avoid this problem the stations normally wait for a random period of time before retransmitting.
For this network we assume that each station, after a given propagation delay, can tell whether the transmitted packets were correctly received. Furthermore, we assume that each packet requires 1 `time unit' for transmission. This means that if a packet of interest is sent at time $t$, then any other packet sent between time $t-1$ and time $t+1$ will collide with our packet.}

\figure{\includepng{\diagramsDir/npa/pureALOHA}{100%}}{Pure ALOHA, packets collide with any other packet transmitted within one time unit of their transmission. The diagram shows a packet sent at $t$ and packets sent at $t+1$ and $t-1$. Any packet sent after $t-1$ and before $t+1$ will collide with the packet sent at $t$.}{pureALOHA}

\notes{We will now look at a simple analysis of the ALOHA system. Let's assume that the total arrival rate for packets at all stations is a Poisson process with rate $\ensuremath{\lambda}$. We assume that the number of stations is very large (infinite) so that an individual station's packet rate is an insignificant proportion of $\ensuremath{\lambda}$, *i.e.*$$
\ensuremath{\frac{\lambda_{n}}{\lambda}}=\lim_{\delta\rightarrow0}=0.$$A station is considered backlogged between the time that it became aware that its previous transmission failed and the time of a successful transmission. We denote the number of backlogged stations at any particular time as $n$. Once a station is aware that a transmission was unsuccessful it waits for $T_{i}$ time units to retransmit. The waiting time is sampled from a probability density function given by$$
p\left(T_{i}\right)=\ensuremath{\mu\exp\left(}-\ensuremath{\mu} T_{i}\right).$$So if $n$ nodes are backlogged then (from superposition of Poissons) the arrivals from the backlogged nodes are a Poisson process with rate $n\ensuremath{\mu}$. So the overall arrival process, from the perspective of the channel, is Poisson with a rate that is a function of $n$, $G\left(n\right)=\ensuremath{\lambda}+n\ensuremath{\mu}$.
\footnote{In [@Bertsekas:data92] they use $x$ as the parameter instead of $\ensuremath{\mu}$.}
The probability that there are no arrivals in an interval of 2 time units for a Poisson process with rate $G\left(n\right)$ is given by$$
p\left(k=0|G\left(n\right),2\right)=\ensuremath{\exp\left(}-2G\left(n\right)\right)$$as we derived in Section\  \ref{sec:poissonProcess}. This is the probability that there is no collision between the packet of interest and any other packets in the network, thus it is the probability of a successful transmission. The rate of attempted transmissions is $G\left(n\right)$ so the rate of successful transmissions is given by$$
G^{\prime}\left(n\right)=G\left(n\right)\ensuremath{\exp\left(}-2G\left(n\right)\right),$$this is known as the throughput. It is the number of packets that successfully reach their destination. The throughput is plotted as a function of $G$ in Figure\  \ref{cap:pureALOHAThroughput}.}

\figure{\includepng{\diagramsDir/npa/pureALOHAThroughput}{60%}}{Throughput for pure ALOHA as a function of $G$.}{cap:pureALOHAThroughput}

\notes{Note that the curve goes up to a maximum point and drops down thereafter. We can find the maximum of the throughput by looking for points where the gradient of the throughput is zero. In the examples below we find that the maximum throughput for the system occurs when $G=1$. The throughput at this point is $\ensuremath{\frac{1}{2e}\approx}0.184$. This maximum throughput shows that at best the channel is in use only about 18% of the time. The system will be in equilibrium if the throughput equals $\ensuremath{\lambda}.$ In other words if the throughput is equal to the arrival rate of the packets.
\footnote{Note that since the service time is fixed at $X_{n}=1$ for all $n$ then the utilization for this system is given by $\ensuremath{\rho}=\ensuremath{\lambda\bar{X}}=\ensuremath{\lambda}$.}}

\notes{\subsection{Slotted ALOHA}}

\notes{A simple improvement to the ALOHA system comes from constraining when packets can be sent. Instead of allowing stations to transmit immediately they receive a packet each station waits for the beginning of a `slot' to start transmitting. These slots are synchronised across the entire network. In this system a collision occurs if another station attempts to transmit in the same slot. This happens if another station received a packet for transmission in the preceding slot. If each slot is one time unit in length the probability of this event is given by$$
p\left(k=0|G\left(n\right),2\right)=\ensuremath{\exp\left(}-G\left(n\right)\right).$$The probability is smaller than for pure ALOHA because the `vulnerable period' for a collision is smaller (half the length of before). A collision now only occurs if another station attempts to transmit in the same slot. As a result the rate of successful transmissions is given by$$
G^{\prime}\left(n\right)=G\left(n\right)\ensuremath{\exp\left(}-G\left(n\right)\right),$$this is known as the throughput. It is the number of packets that successfully reach their destination. The throughput is plotted as a function of $G$ in Figure\  \ref{cap:slottedALOHAThroughput}.
The smaller vulnerable period leads to a greater maximum throughput which is now found at $G=1$. The maximum throughput is $\ensuremath{\frac{1}{e}}$. Slotted ALOHA therefore can be twice as efficient as pure ALOHA.}

\figure{\includepng{\diagramsDir/npa/slottedALOHAThroughput}{60%}}{Throughput for slotted ALOHA as a function of $G$.}{cap:slottedALOHAThroughput}

\notes{\subsection{Analysis of Backlog Delay in Pure ALOHA}}

\notes{Recall our assumption that a backlogged node waits for a time, $T_{i}$, before attempting to retransmit, $$
p\left(T_{i}\right)=\ensuremath{\mu\exp\left(}-\ensuremath{\mu} T_{i}\right).$$
Given this assumption, can we compute the delay associated with this backlogged node? Since the node may experience several collisions, the wait associated with the backlog will involve a sum over the random variable $T_{i}$. It turns out to be an *Erlang distribution*.}

\notes{\subsection{Sums of Exponential Variables and the Erlang Distribution\label{sub:erlang}}}

\notes{If a random variable, $x$, is exponentially distributed with rate parameter $b$. The sum of $a$ random variables, each of which is exponentially distributed with rate parameter $b$ is distributed as an *Erlang distribution.*Consider variables a set of $a$ variables$\left(x_{1}\ensuremath{\dots} x_{a}\right)$ which are each governed by the same exponential distribution, $$
p\left(x_{i}|b\right)=b\ensuremath{\exp\left(}-bx_{i}\right).$$We define the sum of the values to be, $z=\sum_{i=1}^{a}x_{i}$. The distribution governing $z$ is then an *Erlang distribution*, given by $$
p\left(z|a,b\right)=\ensuremath{\frac{b^{a}}{\left(a-1\right)!}}z^{a-1}\ensuremath{\exp\left(}-bz\right).$$Note that this distribution is a generalisation of the exponential distribution because the exponential is the special case where $a=1$. This clearly should be the case because if $a=1$ then the `sum' of that variable will simply be the variable itself.}

\notes{\subsection{Erlang Distribution Mean and Variance}}

\notes{The mean of the Erlang distribution is given by $$
\left\langle z\right\rangle _{p\left(z|a,b\right)}=\ensuremath{\frac{a}{b}}$$ and the variance is $$
\textrm{var}\left(z\right)=\ensuremath{\frac{a}{b^{2}}}.$$}

\notes{\subsection{Delay Associated with Backlogs}}

\notes{If the node retransmits $k$ times then the distribution over the total time required, $W=\sum_{i=1}^{k}T_{i}$, comes from the sum of $k$ independent exponentially distributed variables. From the property of the exponential distribution given in Section\  \ref{sub:erlang} we know that the resulting variable $X$ is Erlang distributed with parameters $\ensuremath{\mu}$ and $k$, $$
p\left(W|k,\ensuremath{\mu\right)}=\ensuremath{\frac{\mu^{k}}{\left(a-1\right)!}}W^{k-1}\ensuremath{\exp\left(}-\ensuremath{\mu} W\right).$$
The probability of transmitting after $k$ attempts is given by $$
p\left(k\right)=q\left(1-q\right)^{k-1}.$$where $q$ is the probability of a successful transmission. For the pure ALOHA system we have, from above, $$
q=\ensuremath{\exp\left(}-2G\right).$$.
\footnote{Compare this with the ARQ system we analysed in the chapter on $M/G/1$ queues. There we were considering errors (unsuccessful transmissions) so $p=\left(1-q\right)$.}
We are now interested in the distribution of the waiting time, using the product rule and the sum rule of probability we know that the probability distribution for $W$ is given by$$
\begin{aligned}
p\left(W|\ensuremath{\mu\right)} & = & \sum_{k=1}^{\ensuremath{\infty}}p\left(W|k,\ensuremath{\mu\right)}p\left(k\right),
\end{aligned}
$$substituting in our distributions gives,$$
p\left(W|\ensuremath{\mu\right)}=\sum_{k=1}^{\ensuremath{\infty}}q\left(1-q\right)^{k-1}\ensuremath{\frac{\mu^{k}}{\left(k-1\right)!}}W^{k-1}\ensuremath{\exp\left(}-\ensuremath{\mu} W\right),$$now substituting $\dot{k}=k-1$$$
p\left(W|\ensuremath{\mu\right)}=\sum_{k=0}^{\ensuremath{\infty}}q\left(1-q\right)^{\dot{k}}\ensuremath{\frac{\mu^{\dot{k}+1}}{\dot{k}!}}X^{\dot{k}}\ensuremath{\exp\left(}-\ensuremath{\mu} W\right),$$extracting the $q$, the exponential term and one of the $\ensuremath{\mu}$s from the product we rewrite as,$$
p\left(X|\ensuremath{\mu\right)}=q\ensuremath{\mu\exp\left(}-\ensuremath{\mu} W\right)\sum_{k=0}^{\ensuremath{\infty}}\ensuremath{\frac{\left(\mu\left(1-q\right)W\right)^{\dot{k}}}{\dot{k}!}},\label{eq:pXgivenMuWithSum}$$Recalling the following equality,$$
\ensuremath{\exp\left(}x\right)=\sum_{k=0}^{\ensuremath{\infty}}\ensuremath{\frac{x^{\dot{k}}}{\dot{k}!}},$$we know we can write$$
\sum_{k=0}^{\ensuremath{\infty}}\ensuremath{\frac{\left(\mu\left(1-q\right)W\right)^{\dot{k}}}{\dot{k}!}}=\ensuremath{\exp\left(\mu\left(}1-q\right)W\right),$$which can be substituted back into (\ref{eq:pXgivenMuWithSum}) to obtain$$
\begin{aligned}
p\left(W|\ensuremath{\mu\right)} & = & q\ensuremath{\mu\exp\left(}-\ensuremath{\mu} W\right)\ensuremath{\exp\left(\mu\left(}1-q\right)W\right),\\
 & = & q\ensuremath{\mu\exp\left(}-q\ensuremath{\mu} W\right)
\end{aligned}
$$which is recognised as an exponential distribution with rate parameter $\ensuremath{\mu^{\prime}}=q\ensuremath{\mu}=\ensuremath{\mu\exp\left(}-2G\right)$.
Using the fact that $G$ is a function of $\ensuremath{\mu}$ we can write$$
\ensuremath{\mu^{\prime}}=\ensuremath{\mu\exp\left(}-2\left(\ensuremath{\lambda}+n\ensuremath{\mu\right)\right)}.\label{eq:rateFunctionALOHA}$$This means that for a given value of $\ensuremath{\lambda}$ and $n$ there is an optimal value for $\ensuremath{\mu}$. This value of $\ensuremath{\mu}$ can be found by seeking the maximum rate, this is done by differentiating with respect to $\ensuremath{\mu}$,$$
\ensuremath{\frac{d\mu^{\prime}}{d\mu}}=\left(1-2n\ensuremath{\mu\right)\exp\left(}-2\left(\ensuremath{\lambda}+n\ensuremath{\mu\right)\right)}$$and setting the result to zero to find the stationary points we have
$$
\left(1-2n\ensuremath{\mu\right)\exp\left(}-2\left(\ensuremath{\lambda}+n\ensuremath{\mu\right)\right)}=0.$$There are two solutions to this equation. The first is $\ensuremath{\exp\left(}-2\left(\ensuremath{\lambda}+n\ensuremath{\mu\right)\right)}=0$, meaning that $\ensuremath{\lambda}+n\ensuremath{\mu\rightarrow\infty}$. This solution is a minimiser . The other solution is given when $$
0=1-2n\ensuremath{\mu}$$or$$
\ensuremath{\mu}=\ensuremath{\frac{1}{2n}},$$ this turns out to be a maximum of (\ref{eq:rateFunctionALOHA}). A maximum is what we want because by maximising the `rate' parameter $\ensuremath{\mu^{\prime}}$ we minimise the average delay associated with the backlog, which is given by $\ensuremath{\bar{W}}=\ensuremath{\frac{1}{\mu}}$, so by setting $\ensuremath{\mu}=\ensuremath{\frac{1}{2n}}$ we find a minimum for the average delay which is given by $$
\ensuremath{\bar{W}_{\textrm{min}}}=2n\ensuremath{\exp\left(}2\ensuremath{\lambda}+1\right).$$ In practice it may be difficult to set the rate $\ensuremath{\mu}$ to something that is dependent on the number of backlogged nodes. this is because the number of backlogged nodes can only be known by nodes communicating their status over the network and we have not allowed for such a mechanism in our analysis. Note that the minimum average delay goes up linearly with the number of backlogged nodes and *exponentially*with the rate of arrivals for the system, $\ensuremath{\lambda}$.}

\notes{## Examples}

\notes{1. Throughput for pure ALOHA system. Find the maximum throughput for the pure ALOHA system by seeking the stationary point of the throughput curve.
  [0]
    To find stationary points we seek the gradient of the throughput.$$
G^{\prime}=G\ensuremath{\exp\left(}-2G\right)$$differentiating with respect to $G$ we obtain
\left(1-2G\right)\ensuremath{\exp\left(}-2G\right)=0$$which implies that either $\ensuremath{\exp\left(}-2G\right)=0$, this happens when $G\ensuremath{\rightarrow\infty}$ and $G^{\prime}\rightarrow0$; or $\left(1-2G\right)=0$ which implies that $G=1$. The first of these stationary points is a minimum, the second is a maximum. To find the value of the maximum we insert $G=1$ into our throughput equation giving$$
G^{\prime}=1\ensuremath{\exp\left(}-1\right)\approx0.184.$$

| \ensuremath{\frac{dG^{\prime}}{dG}} | = | \ensuremath{\exp\left(}-2G\right)-2G\ensuremath{\exp\left(}-2G\right) |
| --- | --- | --- |
|  | = | \left(1-2G\right)\ensuremath{\exp\left(}-2G\right)to find stationary points we solve for points where the gradient is zero,$$ |}


\notes{\bibtex[abbrvnat]{lawrence,other,zbooks}}

\endif

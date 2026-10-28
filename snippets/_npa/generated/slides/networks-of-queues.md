% generated — do not edit; scripts/convert/run.py
\ifndef{npaGenSlidesNetworksOfQueues}
\define{npaGenSlidesNetworksOfQueues}

<!-- original A4 foil 190: Networks of Queues and Simulation -->

\newslide{Networks of Queues and Simulation}

\slides{* So far in the course we have looked at queueing models in isolation.
* We will now turn briefly to some of the issues that arise when they are combined.
* We will start by considering a simple combination of two $M/M/1$ queues.}

<!-- original A4 foil 191: `$M/M/1$' Queues in Tandem\label{sec:tandemQueuesOne} -->

\newslide{`$M/M/1$' Queues in Tandem\label{sec:tandemQueuesOne}}

\figure{\includepng{\diagramsDir/npa/MM1tandem}{100%}}{Two queues in tandem}{MM1tandem}

<!-- original A4 foil 191: `$M/M/1$' Queues in Tandem\label{sec:tandemQueuesOne} -->

\newslide{`$M/M/1$' Queues in Tandem\label{sec:tandemQueuesOne} (continued)}

\slides{* Consider a simple system involving two transmission lines in tandem.
* Packets have a fixed length and their transmission times are proportional to their length.
* Packet lengths are exponentially distributed and arrivals occur at the first queue as a Poisson process.}

<!-- original A4 foil 192: Implications -->

\newslide{Implications}

\slides{* The first queue may be modelled as $M/M/1$, but the second queue cannot be.
* A packet which is large will take a long time in the first queue. During this time the second queue will have a chance to clear.}

<!-- original A4 foil 192: Implications -->

\newslide{Implications (continued)}

\slides{* The result will be that for the second queue larger packets are likely to arrive when the queue is smaller.
* This means that a large packet will typically experience less delay at the second queue than a small one.}

<!-- original A4 foil 193: Analogy -->

\newslide{Analogy}

\slides{* One analogy for this situation is a slow moving vehicle on a road.
* From this vehicle's driver's perception there is very little traffic on the road because the slow moving vehicle never catches up with any.}

<!-- original A4 foil 193: Analogy -->

\newslide{Analogy (continued)}

\slides{* A similar thing occurs with $M/M/1$ queues in tandem.
* A large packet arrives at the second queue to find it has less packets because the smaller packets have had time to be processed.}

<!-- original A4 foil 194: Lack of Independence -->

\newslide{Lack of Independence}

\slides{* The first queue destroys the independence of the packet length and the state of the second queue.
* This problem is difficult to deal with analytically.}

<!-- original A4 foil 194: Lack of Independence -->

\newslide{Lack of Independence (continued)}

\slides{* To proceed with our analysis we will need to break this dependency.
* This can be achieved by considering service times for each packet to be statistically independent at each queue.}

<!-- original A4 foil 195: Time Reversibility --- Burke's Theorem -->

\newslide{Time Reversibility --- Burke's Theorem}

\slides{* In the analysis of the Markov chain systems we have seen so far we relied on detailed balance.
* Detailed balance equations are a special case of global balance equations which arise when transitions only occur between neighbouring states in the Markov chain.}

<!-- original A4 foil 195: Time Reversibility --- Burke's Theorem -->

\newslide{Time Reversibility --- Burke's Theorem (continued)}

\slides{* Detailed balance can be applied to find the stationary distribution in any birth-death processes.
* Burke's theorem leads to an additional special property of birth-death processes known as *time reversibility*.}

<!-- original A4 foil 196: Time Reversibility -->

\newslide{Time Reversibility}

\slides{* The principle with time reversibility is as follows:
* for a birth-death process at steady state the arrival process is Poisson with rate $\lambda$. Time reversibility states that the *departure process* will also be Poisson with rate $\lambda$.
* A proof is given in Section\  3.7 of Bertsekas and Gallager.}

<!-- original A4 foil 197: Time Revesibility Intuition -->

\newslide{Time Revesibility Intuition}

\slides{* Consider the following `intuition' for the $M/M/1$ queue.
* The service rate for the system is given by $\mu$.}

<!-- original A4 foil 197: Time Revesibility Intuition -->

\newslide{Time Revesibility Intuition (continued)}

\slides{* The service rate is *not* the departure rate because a departure can only occur when the system has a state $k>0$.
* This condition is satisfied for a fraction of the time which is given by the utilization factor $\rho$.
* The departure rate is therefore given by $$
\mu\rho=\mu\frac{\lambda}{\mu}=\lambda$$.}

<!-- original A4 foil 198: Burke's Theorem -->

\newslide{Burke's Theorem}

\slides{* Burke's theorem follows on from time reversibility. It states that
* if an $M/M/1$, an $M/M/m$ or an $M/M/\infty$ queue at its stationary distribution has a Poisson arrival process with a rate $\lambda$
* then the departure process is also Poisson with rate $\lambda$.
* Furthermore the number of the customers in the system at time $t$ is *independent* of the sequence of departure times prior to $t$.
* Queues with loss are slightly more complex because the arrival process does not have rate $\lambda$ due to blocked packets.}

<!-- original A4 foil 199: Burke's Theorem -->

\newslide{Burke's Theorem}

\slides{* The second property is worthy of comment as it seems counterintuitive.
* You might expect that if there were a rapid series of departures from the queue then the queue would be shorter than normal,
* Burke's theorem tells us that this is not the case.
* From this we can infer that the state of a queue *before *a rapid series of departures is about to occur must be abnormally high.
* Otherwise it *would* be abnormally low after the departures which Burke's theorem tells us is not the case.}

<!-- original A4 foil 200: $M/M/1$ Queues in Tandem Revisited -->

\newslide{$M/M/1$ Queues in Tandem Revisited}

\slides{* Lets return to the $M/M/1$ queues in tandem. --- Example 2 in notes.
* Burke's theorem tells us that the departure process from the first queue will be a Poisson with rate $\lambda$.}

<!-- original A4 foil 200: $M/M/1$ Queues in Tandem Revisited -->

\newslide{$M/M/1$ Queues in Tandem Revisited (continued)}

\slides{* We allow service times at the second queue to be independent of service times at the first queue.
* This breaks the dependence of the queue length at the second queue on the service time at the second queue.
* In this case the system can be modelled as two $M/M/1$ queues.}

<!-- original A4 foil 201: M/M/1 in Tandem -->

\newslide{M/M/1 in Tandem}

\slides{* If the service time distributions at the two queues are governed by exponential distributions with rate parameters $\mu_{1}$ and $\mu_{2}$.
* This leads to utilization factors for each queue as $\rho_{1}=\frac{\lambda}{\mu_{1}}$ and $\rho_{2}=\frac{\lambda}{\mu_{2}}$ .}

<!-- original A4 foil 201: M/M/1 in Tandem -->

\newslide{M/M/1 in Tandem (continued)}

\slides{* The distributions for the states of the systems are given by$$
p\left(k_{1}\right)=\rho_{1}^{k_{1}}\left(1-\rho_{1}\right)$$$$
p\left(k_{2}\right)=\rho_{2}^{k_{2}}\left(1-\rho_{2}\right).$$
* The joint distribution for both systems is then
p\left(k_{1},k_{2}\right) & = & p\left(k_{1}\right)p\left(k_{2}\right)\\
 & = & \rho_{1}^{k_{1}}\left(1-\rho_{1}\right)\rho_{2}^{k_{2}}\left(1-\rho_{2}\right)because the two queues can be viewed independently.
* As a result the average delay in the system can be computed as the sum of the average delays in each queue$$
\bar{T}=\bar{T}_{1}+\bar{T}_{2}=\frac{1}{\mu_{1}-\lambda}+\frac{1}{\mu_{2}-\lambda}.$$}

<!-- original A4 foil 202: Relation to Reality -->

\newslide{Relation to Reality}

\slides{* This will typically be larger than the actual delay because
* when the queue length is correlated with packet size}

<!-- original A4 foil 202: Relation to Reality -->

\newslide{Relation to Reality (continued)}

\slides{* a large packet will find the second queue to be smaller than normal
* and would therefore spend less time than might be expected in the system.}

<!-- original A4 foil 203: Kleinrock's Independence Approximation -->

\newslide{Kleinrock's Independence Approximation}

\slides{* Kleinrock's independence approximation suggests assuming independence for every node in the network.
* The approximation is good if if large numbers of packets from outside the network are introduced at every queue.
* Consider a general network with labelled nodes and links between these nodes.
* There are several packet streams in the network, each stream has a rate of $x_{s}$.
* We define $f_{ij}\left(s\right)$ as the fraction of packets from stream $s$ that cross the link between $i$ and $j$.
* The rate associated with a link between node $i$ and $j$ is then 
\lambda_{ij} & = & \sum_{s\textrm{ }}f_{ij}\left(s\right)x_{s}.}

<!-- original A4 foil 204: Kleinrock's Independence Approximation -->

\newslide{Kleinrock's Independence Approximation}

\slides{* Kleinrock suggested that merging traffic streams on a transmission line has the effect of restoring independence of arrival and service times.
* The approach is to assume that each link can be treated as an $M/M/1$ queue. This is a good approximation for
* arrivals which occur as a Poisson process
* exponentially distributed packets
* densely connected networks
* moderate-heavy traffic.
* Given this assumption, from the $M/M/1$ queue, we know that the average number at each link is $$
\bar{N}_{ij}=\frac{\lambda_{ij}}{\mu_{ij}-\lambda_{ij}}$$}

<!-- original A4 foil 205: The Average in the System -->

\newslide{The Average in the System}

\slides{* Thus the average number in the entire system is
\bar{N} & = & \sum_{ij}\bar{N}_{ij}\\
 & = & \sum_{ij}\frac{\lambda_{ij}}{\mu_{ij}-\lambda_{ij}}
* Average delay at each link is given by Little's theorem$$
\bar{T}_{ij}=\frac{1}{\mu_{ij}-\lambda_{ij}}.$$}

<!-- original A4 foil 206: Example --- A Simple Network -->

\newslide{Example --- A Simple Network}

\figure{\includepng{\diagramsDir/npa/kleinrockNetwork}{80%}}{A small network with five nodes.}{cap:fiveNodeNetwork}

<!-- original A4 foil 206: Example --- A Simple Network -->

\newslide{Example --- A Simple Network (continued)}

\slides{* **Question**
  Figure\  \ref{cap:fiveNodeNetwork} shows a simple five node network. In the network flow only occurs from lower numbered nodes to higher numbered nodes. The connections in the network have average service times in milliseconds as follows:
* Different routes through the network are indicated with thick lines. Each route has a rate associated with it as follows
* According to the Kleinrock independence assumption, what is the most congested link? What is the quickest route between node 1 & 5?}

| $\bar{X}$ | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| 1 | - | - | - | - | - |
| 2 | 0.05 | - | - | - | - |
| 3 | 0.05 | - | - | - | - |
| 4 | 0.0333 | - | - | - | - |
| 5 | - | 0.05 | 0.05 | 0.033 | - |

|  | $x_{1}$ | $x_{2}$ | $x_{3}$ | $x_{4}$ | $x_{5}$ | $x_{6}$ | $x_{7}$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $\lambda$ | 5 | 10 | 7 | 12 | 4 | 8 | 4 |

<!-- original A4 foil 207: Answer -->

\newslide{Answer}

\slides{* \tiny    \normalsize}

| $\lambda$ | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| 1 | - | - | - | - | - |
| 2 | $x_{1}+x_{2}=15$ | - | - | - | - |
| 3 | $x_{3}=7$ | - | - | - | - |
| 4 | $x_{4}+x_{5}=16$ | - | - | - | - |
| 5 | - | $x_{2}=10$ | $x_{3}+x_{6}=15$ | $x_{4}+x_{7}=16$ | - |

| $\rho=\lambda\bar{X}$ | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| 1 | - | - | - | - | - |
| 2 | $15\times0.05=\frac{3}{4}$ | - | - | - | - |
| 3 | $7\times0.05=\frac{7}{20}$ | - | - | - | - |
| 4 | $16\times0.0333=\frac{8}{15}$ | - | - | - | - |
| 5 | - | $10\times0.05=\frac{1}{2}$ | $15\times0.05=\frac{3}{4}$ | $16\times0.033=\frac{8}{15}$ | - |

<!-- original A4 foil 208: Answer Contd -->

\newslide{Answer Contd}

\slides{* \normalsize
* **The most congested links are from 1 to 2 and 3 to 5.**}

| $1-\rho$ | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| 1 | - | - | - | - | - |
| 2 | $\frac{1}{4}$ | - | - | - | - |
| 3 | $\frac{13}{20}$ | - | - | - | - |
| 4 | $\frac{7}{15}$ | - | - | - | - |
| 5 | - | $\frac{1}{2}$ | $\frac{1}{4}$ | $\frac{7}{15}$ | - |

| $N=\frac{\rho}{1-\rho}$ | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| 1 | - | - | - | - | - |
| 2 | $3$ | - | - | - | - |
| 3 | $\frac{7}{13}$ | - | - | - | - |
| 4 | $\frac{8}{7}$ | - | - | - | - |
| 5 | - | 1 | 3 | $\frac{8}{7}$ | - |

<!-- original A4 foil 209: Answer Contd -->

\newslide{Answer Contd}

\slides{{* To compute the answer to the second part we need the average delay at each link
    \tiny\normalsize
* This means that to go via node 2 takes $\frac{1}{5}+\frac{1}{10}=0.3$ via node 3 takes $\frac{1}{13}+\frac{1}{5}=0.277$ via node 4 it takes $\frac{1}{14}+\frac{1}{14}=\frac{1}{7}=0.1429$ according to Kleinrock's independence assumption.\}{20}
    Here we have assumed that there is no further delay associated with each link (propagation, processing). In practice such delays may arise however we shall not consider them. See Bertsekas & Gallager Section 3.6.1 for more details.}

| $\bar{T}=\frac{\bar{X}}{1-\rho}$ | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| 1 | - | - | - | - | - |
| 2 | $4\times0.05=\frac{1}{5}$ | - | - | - | - |
| 3 | $\frac{20}{13}\times0.05=\frac{1}{13}$ | - | - | - | - |
| 4 | $\frac{15}{7}\times0.033=\frac{1}{14}$ | - | - | - | - |
| 5 | - | $2\times0.05=\frac{1}{10}$ | $4\times0.05=\frac{1}{5}$ | $\frac{15}{7}\times0.033=\frac{1}{14}$ | - |

<!-- original A4 foil 210: Jackson's Theorem -->

\newslide{Jackson's Theorem}

\slides{* While Kleinrock's independence assumption approximates the activities at each queue as $M/M/1$ queues, Jackson's theorem provides a result for the number in the queueing system as a whole.
* Some analysis of the system is given in Section\  3.8 of Bertsekas and Gallager.
* For our purposes it is sufficient to give the assumptions and the result.}

<!-- original A4 foil 210: Jackson's Theorem -->

\newslide{Jackson's Theorem (continued)}

\slides{* there is no correlation between service times and queue lengths.
* randomisation is used to divide the traffic along different routes through the network.
* Given these assumptions the average number of packets in the network is given by$$
N=\sum_{i,j}\frac{\lambda_{ij}}{\mu_{ij}-\lambda_{ij}}.$$}

<!-- original A4 foil 211: Network Simulation -->

\newslide{Network Simulation}

\slides{* The approximations we have outlined so far may be useful for `back of the envelope' style calculations.
* In practice though it is highly likely that you will wish to simulate the system.
* There are a range of simulation packages available.
* We will introduce a simple one based on the Tcl scripting language called `The Network Simulator' or ns-2 ([http://www.isi.edu/nsnam/ns/](http://www.isi.edu/nsnam/ns/).}

<!-- original A4 foil 211: Network Simulation -->

\newslide{Network Simulation (continued)}

\slides{* It is a discrete event simulator aimed at networking research.
* It supports a range of protocols including TCP and multicast protocols and it is straightforward to extend using C++.
* It is a powerful research tool which has the added advantage of being freely available.
* It is installed in the Lewin Laboratory on the Linux systems.
* If you require a personal installation, it can be installed through the Cygwin ([http://www.cygwin.com](http://www.cygwin.com)) API.}

<!-- original A4 foil 212: Network Simulation with NS2 -->

\newslide{Network Simulation with NS2}

\slides{* As a lab class in week 9 you will simulate some simple queues in NS2 and compare the simulations with some results obtained using Kleinrock's independence assumption.
* The lab class will be completed in Linux so please make sure you know your Unix password for the DCS system before the lab start.}

<!-- original A4 foil 212: Network Simulation with NS2 -->

\newslide{Network Simulation with NS2 (continued)}

\slides{* The lab sheet has some notes on simple commands you will need.
* If you are unfamiliar with Linux it is suggested that you try them out before starting the lab.}

\endif

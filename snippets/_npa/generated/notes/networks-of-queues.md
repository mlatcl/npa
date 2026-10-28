% generated — do not edit; scripts/convert/run.py
\ifndef{npaGenNotesNetworksOfQueues}
\define{npaGenNotesNetworksOfQueues}

\notes{\section{$M/M/1$ Queues in Tandem}}

\notes{Consider a simple system involving two transmission lines in tandem. The packet length doesn't change during transmission and transmission times are proportional to packet length. The packet lengths are exponentially distributed and arrivals occur at the first queue as a Poisson process.
The first queue may be modelled as $M/M/1$, but the second queue cannot be. A packet which is large will take a long time in the first queue. During this time the second queue will have a chance to clear. The result will be that for the second queue larger packets are likely to arrive when the queue is smaller. This means that a large packet will typically experience less delay at the second queue than a small one. One analogy for this situation is a slow moving vehicle on a road. From this vehicle's driver's perspective there is very little traffic on the road because the slow moving vehicle never catches up with any. A similar thing occurs with $M/M/1$ queues in tandem. A large packet arrives at the second queue to find it has less packets because the smaller packets have had time to be processed. The effect of the first queue is to destroy the independence of the packet length and the state of the second queue. This problem is difficult to deal with analytically. To proceed with our analysis we will need to break this dependency. This can be achieved by considering service times for each packet to be statistically independent at each queue. We will now look at the consequences of this assumption for our simple pairing of two queues, but first we must introduce the concept of time reversibility.}

\notes{\section{Time Reversibility --- Burke's Theorem}}

\notes{In the analysis of the Markov chain systems we have seen so far ($M/M/1$, $M/M/1/m$, $M/M/\infty$, $M/M/m$ and $M/M/m/m$) we relied on detailed balance to find the steady state distribution. Detailed balance equations are a special case of global balance equations which arise when transitions only occur between neighbouring states in the Markov chain. Detailed balance can be applied to find the stationary distribution in any birth-death processes.
In this section we will briefly mention an additional special property of birth-death processes (and other Markov systems for which detailed balance applies) known as *time reversibility. * The principle with time reversibility is as follows: for a birth-death process at steady state the arrival process is Poisson with rate $\lambda$. Time reversibility states that the departure process will also be Poisson with rate $\lambda$.
We will now give some motivation for this statement, a proof is Given in Section 3.7 of [@Bertsekas:data92]. Consider the following `intuition' for the $M/M/1$ queue. The service rate for the system is given by $\mu$. However this is not the departure rate because a departure can only occur when the system has a state $k>0$. This condition is satisfied for a fraction of the time which is given by the utilization factor $\rho$. the departure rate is therefore given by $\mu\rho=\mu\frac{\lambda}{\mu}=\lambda$.}

\notes{\section{Burke's Theorem}}

\notes{Burke's theorem follows on from time reversibility. It states that if an $M/M/1$, an $M/M/m$ or an $M/M/\infty$ queue at its stationary distribution has a Poisson arrival process with a rate $\lambda$ then the departure process is also Poisson with rate $\lambda$. Furthermore the number of the customers in the system at time $t$ is *independent *of the sequence of the departure times prior to $t$.
\footnote{Queues with loss are slightly more complex because the arrival process does not have rate $\lambda$ due to blocked packets.}
The second property is worthy of comment as it sounds counterintuitive. You might expect that if there were a rapid series of departures from the queue then the queue would be shorter than normal, but Burke's theorem tells us that this is not the case. From this we can infer that the state of a queue *before *a rapid series of departures is about to occur must be abnormally high. Otherwise it *would* be abnormally low after the departures, but Burke's theorem tells us that this is not the case.}

\notes{\section{Kleinrock's Independence Approximation}}

\notes{Kleinrock's independence approximation suggests assuming independence for every node in the network. The approximation is good if large numbers of packets from outside the network are introduced at every queue.
Consider a general network with labelled nodes and links between these nodes. There are several packet streams in the network, each stream has a rate of $x_{s}$. We define $f_{ij}\left(s\right)$ as the fraction of packets from stream $s$ that cross the link between $i$ and j. The rate associated with a link between node $i$and $ $j is then $$
\lambda_{ij}=\sum_{s}f_{ij}\left(s\right)x_{s}.$$Kleinrock suggested that merging traffic streams on a transmission line has the effect of restoring independence of arrival and service times. The approach is to assume that each link can be treated as an $M/M/1$ queue. This is a good approximation for:}

\notes{1. Arrivals which occur as a Poisson process.
2. Exponentially distributed packets.
3. Densely connected networks.
4. Moderate to heavy traffic.}

\notes{Given this assumption, from the $M/M/1$ queue, we know that the average number at each link is$$
\bar{N}_{ij}=\frac{\lambda_{ij}}{\mu_{ij}-\lambda_{ij}}$$thus the average number in the entire system is\begin{eqnarray*}
\bar{N} & = & \sum_{ij}\bar{N}_{ij}\\
 & = & \sum_{ij}\frac{\lambda_{ij}}{\mu_{ij}-\lambda_{ij}},\end{eqnarray*}average delay at each link is given by Little's theorem$$
\bar{T}_{ij}=\frac{1}{\mu_{ij}-\lambda_{ij}}.$$In our studies we will assume that there is no further delay associated with each link (propagation, processing). In practice such delays may arise however we shall not consider them. See [@Bertsekas:data92] Section 3.6.1 for more details.}

\notes{\section{Jackson's Theorem}}

\notes{While Kleinrock's independence assumption approximates the activities at each queue as $M/M/1$ queues, Jackson's theorem provides a result for the number in the queueing system as a whole. Some analysis of the system is given in Section 3.8 of [@Bertsekas:data92], but for our purposes it is sufficient to give the assumptions and the result. The first assumption is the premise of Kleinrock's independence assumption: there is no correlation between service times and queue lengths. The second assumption is that randomisation is used to divide the traffic along different routes through the network. Given these assumptions the average number of packets in the network is given by$$
\bar{N}=\sum_{i,j}\frac{\lambda_{ij}}{\mu_{ij}-\lambda_{ij}}.$$}

\notes{\section{Network Simulation}}

\notes{The approximations we have outlined so far may be useful for `back of the envelope' style calculations. In practice though it is highly likely that you will wish to simulate the system. There are a range of simulation packages available, we will introduce a simple one based on the Tcl scripting language called `The Network Simulator' or ns-2 ([http://www.isi.edu/nsnam/ns/](http://www.isi.edu/nsnam/ns/)). It is a discrete event simulator aimed at networking research. It supports a range of protocols including TCP and multicast protocols and is straightforward to extend using C++. It is a powerful research tool that has the added advantage of being freely available. It is installed in the Lewin Laboratory on the Linux systems and, if you require a personal installation, it can be installed through the Cygwin API ([http://www.cygwin.com](http://www.cygwin.com)).}

\notes{\section{Network Simulation with NS-2}}

\notes{At the second lab class you will simulate some simple queues in NS2 and compare the simulations with approximate results obtained using Kleinrock's independence assumption. The lab class will be completed in Linux so please make sure you know your Unix password for the DCS system before the lab starts. The lab sheet has some notes on simple commands you will need. If you are unfamiliar with Linux it is suggested that you try them out before starting the lab.}

\notes{## Examples}

\notes{{1. Figure\  \ref{cap:fiveNodeNetwork} shows a small network with five nodes. In the network flow only occurs from lower numbered nodes to higher numbered nodes. The connections in the network have average service times in milliseconds as follows:
  {llllll}
    $\bar{X}$ & 1 & 2 & 3 & 4 & 5 \\
    1 & - & - & - & - & - \\
    2 & 0.05 & - & - & - & - \\
    3 & 0.05 & - & - & - & - \\
    4 & 0.0333 & - & - & - & - \\
    5 & - & 0.05 & 0.05 & 0.033 & - \\
  
  [ht]
    \centering
    \figure{\includepng{\diagramsDir/npa/kleinrockNetwork}{80%}}{kleinrockNetwork}{kleinrockNetwork}
    \caption{A small network with five nodes.}
    \label{cap:fiveNodeNetwork}
  
  Different routes through the network are indicated with thick lines. Each route has a rate associated with it as follows
  {llllllll}
     & $x_{1}$ & $x_{2}$ & $x_{3}$ & $x_{4}$ & $x_{5}$ & $x_{6}$ & $x_{7}$ \\
    $\lambda$ & 5 & 10 & 7 & 12 & 4 & 8 & 4 \\
  
  According to the Kleinrock independence assumption, what is the most congested link? What is the quickest route between node 1 & 5? In your answers you should consider propagation or processing delays at each node to be negligible.
  [0]
    From the diagram we can see which links traffic flows down. Let us take each link in turn. Using the superposition of Poisson flows we have
    \tiny
    {llllll}
      $\lambda$ & 1 & 2 & 3 & 4 & 5 \\
      1 & - & - & - & - & - \\
      2 & $x_{1}+x_{2}=15$ & - & - & - & - \\
      3 & $x_{3}=7$ & - & - & - & - \\
      4 & $x_{4}+x_{5}=16$ & - & - & - & - \\
      5 & - & $x_{2}=10$ & $x_{3}+x_{6}=15$ & $x_{4}+x_{7}=16$ & - \\
    
    \tiny    \normalsize
    {llllll}
      $\rho=\lambda\bar{X}$ & 1 & 2 & 3 & 4 & 5 \\
      1 & - & - & - & - & - \\
      2 & $15\times0.05=\frac{3}{4}$ & - & - & - & - \\
      3 & $7\times0.05=\frac{7}{20}$ & - & - & - & - \\
      4 & $16\times0.0333=\frac{8}{15}$ & - & - & - & - \\
      5 & - & $10\times0.05=\frac{1}{2}$ & $15\times0.05=\frac{3}{4}$ & $16\times0.033=\frac{8}{15}$ & - \\
    
    {llllll}
      $1-\rho$ & 1 & 2 & 3 & 4 & 5 \\
      1 & - & - & - & - & - \\
      2 & $\frac{1}{4}$ & - & - & - & - \\
      3 & $\frac{13}{20}$ & - & - & - & - \\
      4 & $\frac{7}{15}$ & - & - & - & - \\
      5 & - & $\frac{1}{2}$ & $\frac{1}{4}$ & $\frac{7}{15}$ & - \\
    
    \normalsize
    {llllll}
      $N=\frac{\rho}{1-\rho}$ & 1 & 2 & 3 & 4 & 5 \\
      1 & - & - & - & - & - \\
      2 & $3$ & - & - & - & - \\
      3 & $\frac{7}{13}$ & - & - & - & - \\
      4 & $\frac{8}{7}$ & - & - & - & - \\
      5 & - & 1 & 3 & $\frac{8}{7}$ & - \\
    
    **The most congested links are from 1 to 2 and 3 to 5.**
    To compute the answer to the second part we need the average delay at each link
    \tiny\normalsize
    {llllll}
      $\bar{T}=\frac{\bar{X}}{1-\rho}$ & 1 & 2 & 3 & 4 & 5 \\
      1 & - & - & - & - & - \\
      2 & $4\times0.05=\frac{1}{5}$ & - & - & - & - \\
      3 & $\frac{20}{13}\times0.05=\frac{1}{13}$ & - & - & - & - \\
      4 & $\frac{15}{7}\times0.033=\frac{1}{14}$ & - & - & - & - \\
      5 & - & $2\times0.05=\frac{1}{10}$ & $4\times0.05=\frac{1}{5}$ & $\frac{15}{7}\times0.033=\frac{1}{14}$ & - \\
    
    This means that to go via node 2 takes $\frac{1}{5}+\frac{1}{10}=0.3$ via node 3 takes $\frac{1}{13}+\frac{1}{5}=0.277$ via node 4 it takes $\frac{1}{14}+\frac{1}{14}=\frac{1}{7}=0.1429$ according to Kleinrock's independence assumption.\}{0}}

\notes{### Answer}

\notes{{1. $M/M/1$ Queues in Tandem Revisited
  Let's return to the $M/M/1$ queues in tandem. Burke's theorem tells us that the departure process from the first queue will be a Poisson with rate $\lambda.$ Now if we allow service times at the second queue to be independent of service times at the first queue we can break the dependence of the queue length at the second queue on the service time at the second queue. In this case the system can be modelled as two $M/M/1$ queues. What are the distributions for the states of the two systems?
  [0]
    If the service time distributions at the two queues are governed by exponential distributions with rate parameters $\mu_{1}$ and $\mu_{2}$ leading to utilization factors for each queue as $\rho_{1}=\frac{\lambda}{\mu_{1}}$ and $\rho_{2}=\frac{\lambda}{\mu_{2}}$. then the distributions for the states of the systems are given by$$
P\left(k_{1}\right)=\rho_{1}^{k_{1}}\left(1-\rho_{1}\right)$$$$
P\left(k_{2}\right)=\rho_{2}^{k_{2}}\left(1-\rho_{2}\right).$$The joint distribution for both systems is then 
P\left(k_{1},k_{2}\right) & = & P\left(k_{1}\right)P\left(k_{2}\right)\\
 & = & \rho_{1}^{k_{1}}\left(1-\rho_{1}\right)\rho_{2}^{k_{2}}\left(1-\rho_{2}\right)because the two queues can be considered independently. As a result the average delay in the system can be computed as the sum of the average delays in each queue,$$
\bar{T}=\bar{T}_{1}+\bar{T}_{2}=\frac{1}{\mu_{1}-\lambda}+\frac{1}{\mu_{2}-\lambda}.$$\}{0}}

\notes{### Answer}

\endif

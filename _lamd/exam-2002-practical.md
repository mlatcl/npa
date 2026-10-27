---
title: "Exam 2002--03"
practical: 7
layout: practical
assignment: False
notespdf: False
tex_template: exercise
posts: True
ipynb: False
reveal: False
docx: False
pptx: False
date: 2003-01-01
abstract: >
  COM6131/COM3270, autumn semester 2002--2003, two hours. Residual service
  time and Pollaczek--Khinchin; ns-2 multipath and Kleinrock; Erlang C
  call centres; $M/M/m/n$. Questions only.
---

\section{Paper}

\notes{Network Performance Analysis. Autumn semester 2002--2003. Two hours. Press mark COM6131 (masters) / COM3270 (undergraduate).}

\notes{This paper examines $M/G/1$ residual time (lectures 11--13), ns-2 and Kleinrock (Lab 2; lectures 14--15), Erlang C and Little (lectures 6 and 9), and a finite multi-server birth-death chain (lectures 5, 8--10).}

\section{Question 1}

\notes{In an $M/G/1$ queue inter-arrival times are exponentially distributed and service times are generally distributed.}

\notes{**(a)** [50%] Use the concept of residual service time to show that, assuming customers are served in the order that they arrive, the average waiting time is
$$
\bar{W}=\frac{\bar{R}}{1-\rho},
$$
where $\bar{R}$ is the average residual service time and $\rho$ is the utilisation. Use diagrams where necessary, and state your assumptions clearly.}

\notes{**(b)** [40%] Use a graphical argument to derive a formula for the residual service time, then combine it with (a) to show that
$$
\bar{W}=\frac{\lambda\langle X^2\rangle}{2(1-\rho)},
$$
where $\lambda$ is the arrival rate and $\langle X^2\rangle$ is the second moment of service time.}

\notes{**(c)** [10%] This is the Pollaczek--Khinchin formula. Use it to derive the average waiting time in an $M/D/1$ queue.}

\section{Question 2}

\notes{You are presented with the following portion of Tcl designed for ns-2.}

\notes{`set node1 [$ns node]`
`set node2 [$ns node]`
`set node3 [$ns node]`
`set node4 [$ns node]`

`$node1 set multiPath_ 1`

`set link1 [$ns duplex-link $node1 $node2 1Kb 0ms DropTail]`
`set link2 [$ns duplex-link $node1 $node3 1Kb 0ms DropTail]`
`set link3 [$ns duplex-link $node2 $node4 1Kb 0ms DropTail]`
`set link4 [$ns duplex-link $node3 $node4 1Kb 0ms DropTail]`

`set src [new Agent/UDP]`
`$ns attach-agent $node1 $src`
`set sink [new Agent/Null]`
`$ns attach-agent $node4 $sink`}

\notes{**(a)** [25%] Assuming that only the specified nodes exist, draw the network topology showing the associated routes.}

\notes{**(b)** [35%] State the assumptions behind the Kleinrock independence approximation. Discuss to what extent they are valid for this topology.}

\notes{**(c)** [25%] Packet arrivals at `node1` are Poisson at rate 2 per second. Packet lengths are exponential with mean 0.5 Kb. Packets are sent randomly along all possible routes with equal probability. Use Kleinrock's independence assumption to estimate the steady-state average number of packets at each link.}

\notes{**(d)** [15%] What is the expected delay for each route through the network?}

\section{Question 3}

\notes{*Hand in the Erlang C curves provided with your answer to this question.*}

\notes{Northern Telecom has purchased several local telecommunications companies, each with their own regional support team. There are three regional teams. Calls arrive as a Poisson process; service times are exponential. Region A has $m=10$ and 120 customers per hour; region B has $m=13$ and 160 customers per hour; region C has $m=10$ and 100 customers per hour.}

\figure{\includepng{\diagramsDir/npa/erlangCCurves0to20}{80%}}{Erlang C curves issued with the paper (offered traffic 0 to 20).}{exam2002-erlang-c}

\notes{**(a)** [30%] Average holding time $\tau$ is 3 minutes. Use the Erlang C curves to give, for each region, the probability of queueing $C(m,a)$.}

\notes{**(b)** [30%] The mean queue length in $M/M/m$ is $\bar{N}_Q=\rho C(m,a)/(1-\rho)$. Use Little's formula to obtain the mean queueing time, and compute it for each centre.}

\notes{**(c)** [20%] The mean queueing time for customers who do *not* queue is zero. What is the mean queueing time for customers who *do* queue?}

\notes{**(d)** [20%] The company merges the centres to one location. Total traffic, holding time, and staff numbers stay the same. What is the average queueing time for the new centre?}

\section{Question 4}

\notes{A call centre employs thirty operators selling tickets. It has sixty lines in total. When all operators are active, new calls join a queue for the first free operator. Model the centre as $M/M/m/n$: $m$ servers and maximum occupancy $n$.}

\notes{**(a)** [30%] Draw a state diagram for the system.}

\notes{**(b)** [20%] Write down the detailed balance equations for $k<m$ and for $m\le k<n$.}

\notes{**(c)** [30%] For each of those two regions, write the steady-state distribution as a function of $P(0)$.}

\notes{**(d)** [20%] Using normalisation, show that
$$
P(0)=\left[\sum_{k=0}^{m}\frac{a^k}{k!}+\sum_{k=m+1}^{n}\frac{a^k}{m!\,m^{k-m}}\right]^{-1},
$$
where $a=\lambda/\mu$.}

\thanks

\references

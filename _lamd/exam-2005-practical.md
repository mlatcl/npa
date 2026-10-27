---
title: "Exam 2005--06"
practical: 9
layout: practical
assignment: False
notespdf: False
tex_template: exercise
posts: True
ipynb: False
reveal: False
docx: False
pptx: False
date: 2006-01-01
abstract: >
  COM6131/COM3270, autumn semester 2005--2006, two hours. Section A is
  Pollaczek--Khinchin; Section B offers Erlang B, an Erlang C call-centre
  merger, or ns-2 with Kleinrock. Questions only.
---

\section{Paper}

\notes{Network Performance Analysis. Autumn semester 2005--2006. Two hours. Press mark COM6131 / COM3270.}

\notes{Section A is $M/G/1$ residual time (lectures 11--13). Section B is a choice: Erlang B (Q2; lecture 10), Erlang C with issued curves (Q3; lecture 9), or ns-2, Kleinrock, and the Lab 1 warning about sample averages (Q4).}

\section{Section A}

\subsection{Question 1}

\notes{In an $M/G/1$ queue, inter-arrivals are exponential and service times are general. The mean wait may be written
$$
\bar{W}=\frac{\bar{R}}{1-\rho},
$$
where $\bar{R}$ is mean residual service time and $\rho$ is utilisation.}

\notes{**(a)** [30%] Describe, using diagrams where necessary, residual service time. State the assumptions used in deriving the formula above.}

\notes{**(b)** [40%] Use a graphical argument to derive a formula for residual service time. Combine it with (a) to show
$$
\bar{W}=\frac{\lambda\langle X^2\rangle}{2(1-\rho)}.
$$}

\notes{**(c)** [15%] This is the Pollaczek--Khinchin formula. Use it to derive the mean wait in an $M/M/1$ queue.}

\notes{**(d)** [15%] Which service-time distribution leads to the lowest delay for a given mean? What characteristic of that distribution ensures it?}

\section{Section B}

\subsection{Question 2}

\notes{This question focuses on the Erlang loss system.}

\notes{**(a)** [20%] Consider
$$
B(m,a)=\frac{a^m/m!}{\sum_{n=0}^{m}a^n/n!}.
$$
What is the significance of this formula? What do $a$ and $m$ stand for?}

\notes{**(b)** [25%] What problems arise when computing it on a calculator or a computer? How would you resolve them?}

\notes{**(c)** [25%] The steady-state distribution is the truncated Poisson
$$
P(k)=\frac{a^k/k!}{\sum_{n=0}^{m}a^n/n!}.
$$
If the number of servers is very large ($m\gg a$), what is the average number of customers in the system? *Hint:* consider $m\to\infty$.}

\notes{**(d)** [30%] Under what conditions does the steady-state distribution exist? What is the form of that distribution when $a$ becomes much larger than $m$, and what is the effect on carried load?}

\subsection{Question 3}

\notes{*Annotate and hand in the Erlang C curves with your answer.*}

\notes{United Telecom has purchased several local companies, each with a regional support team. Model the centres as Erlang delay systems. Region X has $m=12$ and 50 customers per hour; region Y has $m=15$ and 70 customers per hour; region Z has $m=8$ and 25 customers per hour.}

\figure{\includepng{\diagramsDir/npa/erlangDelayCurves06}{80%}}{Erlang C curves issued with the 2005--06 paper.}{exam2005-erlang-c-1}

\figure{\includepng{\diagramsDir/npa/erlangDelayCurves06_2}{80%}}{Second sheet of Erlang C curves issued with the paper.}{exam2005-erlang-c-2}

\notes{**(a)** [30%] Average holding time $\tau$ is 6 minutes. Use the curves to give $C(m,a)$ for each region.}

\notes{**(b)** [20%] Mean queue length is $\bar{N}_Q=\rho C(m,a)/(1-\rho)$. Use Little's formula to derive $\bar{W}$ and compute it for each centre.}

\notes{**(c)** [25%] Show that the mean wait among customers who queue is $\bar{W}_Q=1/(\mu(1-\rho))$, and compute it for each centre.}

\notes{**(d)** [5%] The company merges the centres. Total traffic and holding time stay the same. How many staff are needed to keep the probability of waiting at $0.006$ or below?}

\notes{**(e)** [20%] Explain the difference in staffing between the centralised centre and the three originals, focusing on utilisation.}

\subsection{Question 4}

\notes{You are presented with the following portion of Tcl designed for ns-2.}

\notes{`set node1 [$ns node]`
`set node2 [$ns node]`
`set node3 [$ns node]`

`$node1 set multiPath_ 1`

`set link1 [$ns duplex-link $node1 $node2 2Kb 0ms DropTail]`
`set link2 [$ns duplex-link $node2 $node3 2Kb 0ms DropTail]`
`set link3 [$ns duplex-link $node1 $node3 2Kb 0ms DropTail]`

`set src [new Agent/UDP]`
`$ns attach-agent $node1 $src`
`set sink [new Agent/Null]`
`$ns attach-agent $node3 $sink`}

\notes{**(a)** [25%] Draw the network topology showing the associated routes.}

\notes{**(b)** [25%] Arrivals at `node1` are Poisson at rate 2 per second. Packet lengths are exponential with mean 0.5 Kb. Packets are sent randomly along all routes with equal probability. Use Kleinrock's independence assumption to estimate the mean number of packets at each link and the mean delay for each route.}

\notes{**(c)** [20%] One route contains two queues. Explain how the second queue's size, as perceived by an arriving packet, relates to that packet's length, and how waiting time is affected for longer packets at the second queue.}

\notes{**(d)** [20%] For each route, consider Kleinrock's independence assumption. For which route would you expect it to be more accurate, and why?}

\notes{**(e)** [10%] In a large network, analytical modelling is often impossible and we simulate. Why might sample-based approximations from those simulations be misleading? (Lab 1 asked the same question of the discrete $M/M/1$ chain.)}

\thanks

\references

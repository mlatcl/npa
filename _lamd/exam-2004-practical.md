---
title: "Exam 2004--05"
practical: 8
layout: practical
assignment: False
notespdf: False
tex_template: exercise
posts: True
ipynb: False
reveal: False
docx: False
pptx: False
date: 2005-01-01
abstract: >
  COM6131/COM3270, autumn semester 2004--2005, two hours. Section A is a
  birth-death survey; Section B offers discrete $M/M/1$ simulation, ARQ as
  $M/G/1$, or Kleinrock and Jackson. Questions only.
---

\section{Paper}

\notes{Network Performance Analysis. Autumn semester 2004--2005. Two hours. Press mark COM6131 / COM3270.}

\notes{Section A is a compulsory survey of utilisation, blocking, and steady state on the Markov queues from lectures 5--10. Section B is a choice: Lab 1's discrete simulator (Q2), an ARQ delay that is $M/G/1$ (Q3; lectures 11--13), or Kleinrock and Jackson on tandem queues (Q4; lectures 14--15).}

\section{Section A}

\subsection{Question 1}

\notes{This question concerns queueing models based around birth-death processes: Markov arrivals and Markov departures.}

\notes{**(a)** [25%] Explain what you understand by the term utilisation factor. What are the advantages and disadvantages of utilisation factors that are close to one?}

\notes{**(b)** [20%] Give the utilisation factors for $M/M/1$, $M/M/1/m$, $M/M/m$, and $M/M/\infty$.}

\notes{**(c)** [20%] What do you understand by blocking probability? Give it for $M/M/m/m$ and $M/M/1/m$.}

\notes{**(d)** [15%] Describe what you understand by the steady-state distribution of a queueing system.}

\notes{**(e)** [20%] For $M/M/1$, $M/M/m$, $M/M/m/m$, and $M/M/\infty$, give the conditions under which the steady-state distribution exists.}

\section{Section B}

\subsection{Question 2}

\notes{The diagram below is the state diagram for a discrete-time $M/M/1$ queue.}

\figure{\includepng{\diagramsDir/npa/discreteMM1State}{70%}}{Discrete-time $M/M/1$: from occupancy $k$ the next occupancy is $k+1$, $k-1$, or $k$.}{exam2004-discrete-mm1}

\notes{Take $P(b)=\lambda\,\delta t$ and $P(d)=\mu\,\delta t$, with $(\mu+\lambda)\delta t<1$.}

\notes{**(a)** [30%] Derive the steady-state distribution in terms of the utilisation factor.}

\notes{**(b)** [20%] Derive the mean of this distribution.}

\notes{**(c)** [30%] Write down an algorithm for computer simulation of this queue. MATLAB notation or pseudocode is acceptable.}

\notes{**(d)** [20%] When designing networks we usually want the steady-state behaviour. For this chain we can compute it analytically; otherwise we simulate. What problems with the simulation in (c) might mean you do not accurately estimate the steady-state distribution? You may wish to distinguish distribution means, sample means, and time averages. This is the same warning Lab 1 asked you to summarise.}

\subsection{Question 3}

\notes{*Delay analysis of an ARQ system.* Packets are transmitted in frames $1$ millisecond long. An acknowledgement is sent if a packet is received without error. The system waits at most $n-1$ milliseconds for the acknowledgement, then transmits the next packet. Arrivals are Poisson at rate $\lambda$. Packet errors occur independently with probability $p$.}

\figure{\includepng{\diagramsDir/npa/ARQ}{70%}}{Schematic of the ARQ system from the 2004 paper.}{exam2004-arq}

\notes{**(a)** [15%] Explain why the service-time distribution (time from the start of a given packet's transmission to the end of the previous transmission) is
$$
P(X=1+kn)=(1-p)p^k.
$$}

\notes{**(b)** [25%] What is the mean of this distribution?}

\notes{**(c)** [10%] What is the utilisation factor for this queue?}

\notes{**(d)** [30%] What is the second moment of the service-time distribution?}

\notes{**(e)** [20%] Comment on the validity of the independence assumption for packet errors.}

\notes{You may use $\sum_{k=0}^{\infty}k^2 p^k=(p+p^2)/(1-p)^3$.}

\subsection{Question 4}

\notes{When simulating networks of queues we have to resort to approximations.}

\notes{**(a)** [25%] A small system is modelled as two queues. Packets arrive at the first as a Poisson stream with exponentially distributed lengths. After leaving the first queue they enter a second. Service time at both queues is proportional to packet length. Explain how the second queue's size, as perceived by an arriving packet, is related to that packet's length, and how that affects waiting time at the second queue.}

\notes{**(b)** [25%] Explain Kleinrock's independence assumption. Given that assumption, what is the delay for a transmission line with traffic rate $\lambda$ and mean transmission time $\bar{X}$?}

\notes{**(c)** [25%] Give conditions under which Kleinrock's assumption yields a reasonable approximation for a network of queues.}

\notes{**(d)** [25%] What does Jackson's theorem state, and what are its assumptions? What is the average number of packets in a system according to Jackson's theorem?}

\thanks

\references

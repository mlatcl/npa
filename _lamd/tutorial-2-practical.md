---
title: "Tutorial 2: $M/M/1$ Queue and Little's Formula"
practical: 2
layout: practical
assignment: True
notespdf: False
tex_template: exercise
posts: True
ipynb: False
reveal: False
docx: False
pptx: False
date: 2006-10-03
abstract: >
  Exponential interarrivals, the occupancy variance of $M/M/1$, delay as
  utilisation approaches one, a cash-machine $M/M/1$, and why utilisation
  for $M/M/1/m$ is not $\lambda/\mu$. Originally COM6131 Tutorial 2
  (18 October 2001), carried into the 2006 notes.
---

\section{Tutorial 2}

\notes{Network Performance Analysis. $M/M/1$, Little's formula, and the exponential distribution.}

\section{The exponential density}

\notes{The $M/M/1$ queue uses exponential densities for interarrival times and service times. The interarrival density with parameter $\lambda$ is
$$
p(t)=\lambda e^{-\lambda t},\qquad t\ge 0.
$$}

\notes{1. Sketch this density function.}

\notes{2. Show that both the mean and the standard deviation are $1/\lambda$.}

\notes{3. Briefly explain what these two properties of a density represent.}

\notes{4. What is meant by the *memoryless* property of the exponential distribution?}

\section{Occupancy variance}

\notes{In the notes the mean number of customers in an $M/M/1$ system is
$$
\langle k\rangle=\frac{\rho}{1-\rho}.
$$
Show that the variance of $k$ is
$$
\langle k^2\rangle-\langle k\rangle^2=\frac{\rho}{(1-\rho)^2}.
$$}

\section{Delay versus utilisation}

\notes{For an $M/M/1$ queue, sketch the following quantities against the utilisation $\rho$.}

\notes{1. The average number of customers in the system.}

\notes{2. The average time delay of the system.}

\notes{3. Using these plots, comment on the consequences of allowing $\rho$ to approach 1.}

\section{A cash machine}

\notes{Students arrive as a Poisson process at a cash-dispensing machine with average interarrival time 5 minutes. The time a student spends on the machine is exponential with mean 2 minutes.}

\notes{1. What is the probability that a student arriving at the machine will have to wait?}

\notes{2. What is the average waiting (queueing) time for a student?}

\notes{3. The bank plans to install a second machine when the average waiting time is 5 minutes or longer. At what average arrival rate will this occur? For that arrival rate, what is the *total* average delay that students spend at the machine?}

\notes{4. What is the average queue length at that arrival rate?}

\section{Finite waiting room}

\notes{For a single server ($M/M/1$ or $M/M/1/m$) the utilisation $\rho$ is the probability that the occupancy is not zero. For a lossless system, Little's formula (valid for $M/G/1$) gave $\rho=\lambda/\mu$. Use the stationary distribution of the $M/M/1/m$ queue to compute the utilisation, and explain why it is not $\lambda/\mu$.}

\thanks

\references

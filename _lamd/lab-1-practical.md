---
title: "Lab 1: Discrete Simulation of the $M/M/1$ Queue"
week: 3
practical: 4
layout: practical
assignment: True
notespdf: False
tex_template: exercise
posts: True
ipynb: True
reveal: False
docx: False
pptx: False
date: 2006-10-09
abstract: >
  Week 3 lab. Build a discrete-time birth-death simulation of $M/M/1$
  and compare the time-average occupancy with the geometric steady state
  from lectures 4--6. Originally MATLAB (`hist`, `bar`, `rand`); rewritten
  in Python.
---

\section{How this lab sits in the course}

\notes{This is the Monday of week 3, immediately after *Birth-Death Processes and the $M/M/1$ Queue* (lectures 4 and 5) and *Little's Formula* (lecture 6). The lectures derived $P(k)=(1-\rho)\rho^k$ from detailed balance and showed a discrete-time chain with $\Delta t$ as a computational stand-in for the continuous process. This lab asks you to *write* that chain, sample it, and see when the sample mean is a trustworthy estimate of $\bar{N}=\rho/(1-\rho)$. Tutorial 2, later the same week, returns to occupancy variance and Little on paper.}

\slides{* After lectures 4--6: implement the discrete $M/M/1$ chain
* Compare histogram and sample mean with $(1-\rho)\rho^k$ and $\rho/(1-\rho)$}

\section{The task}

\notes{Originally COM6131/4290 Lab Sheet 1. All lab classes in this course compare simulation with analysis. Here the simulator is a discrete Markov model based on a birth-death process. Use time steps $\Delta t=0.01$. In 2001--02 this same task was Coursework 1, worth 30\% of the module; students handed in the write-up on 21 November 2002 and left MATLAB in a DCS directory named `COM6131a1y1` or `COM3270a1y1`.}

\notes{The 2006 machine-room sheet (`labsheet.lyx`) asked students to reboot into Red Hat Linux, log in through Gnome, open a terminal, `mkdir ~/npalab`, fetch `http://www.dcs.shef.ac.uk/~neil/NPA/source.zip` in Netscape, and `unzip source.zip`. Those steps are archive colour. The simulation itself is below.}

\figure{\includepng{\diagramsDir/npa/mmOneBirthDeathProcess}{70%}}{Birth-death rates for the lab: birth $\lambda$ in every state, death $\mu$ for $k\ge 1$, and $\mu_0=0$ so the occupancy cannot go negative.}{lab1-birth-death}

\figure{\includepng{\diagramsDir/npa/discreteMM1State}{70%}}{The same chain as in the lecture: from occupancy $k$ the next occupancy is $k+1$, $k-1$, or $k$.}{lab1-discrete-state}

\include{snippets/_npa/includes/npa-python-setup.md}

\notes{The 2006 sheet used MATLAB (`hist`, `bar`, `rand`, and the demo `simulateQueue.m`). Write the loop yourself first. `npa_plots.simulate_mm1` is the same algorithm, for checking.}

\section{1. Run the chain}

\notes{Code a simulation with birth rate $\lambda=1$ for all $k=0,1,\ldots$ and death rate $\mu=2$ for $k=1,1,\ldots$ (with $\mu_0=0$). At each step the probability of $+1$ is $\lambda\Delta t$, of $-1$ is $\mu\Delta t$, and of no change is $1-(\lambda+\mu)\Delta t$. Run for $1000$ seconds ($100{,}000$ iterations). Store the occupancy at every step: those stored values are samples from the model the queue represents.}

\notes{*While you wait for simulations to run you might like to start looking at the questions below.*}

\code{occupancy = npa_plots.simulate_mm1(1.0, 2.0, delta_t=0.01, n_iters=100_000, rng=1)
print(occupancy[:20], occupancy.mean())}

\section{2. Normalized histogram}

\notes{Produce a normalized histogram of the samples (the area of the bars adds up to one, not to the number of counts).}

\section{3. Sample mean}

\notes{Compute the mean of the samples.}

\section{4. Steady-state probabilities}

\notes{Use the detailed balance equations to derive the steady-state probabilities for each state in your queueing system. Comment on the similarities between those equations and those of the $M/M/1$ queue from the lecture.}

\section{5. Analytical mean}

\notes{Use these steady-state probabilities to derive the distribution's mean.}

\section{6. Compare}

\notes{Plot the computed probabilities from (4) against the normalized histogram from (2). Compare the sample mean from (3) with the analytical mean from (5). Comment on differences between the analytically computed values and those computed from the samples.}

\code{fig, ax = npa_plots.plot_mm1_occupancy(1.0, 2.0, n_iters=100_000, rng=1)
ax.set_title(r"$\lambda=1$, $\mu=2$, $\rho=0.5$, 1000 seconds")
plt.show()}

\section{7. High utilisation}

\notes{Run the model again with $\lambda=1.9$, keeping $\mu=2$. Repeat (2) and (3). Are the sample-based estimates more or less accurate for this system? Comment on why.}

\code{fig, ax = npa_plots.plot_mm1_occupancy(1.9, 2.0, n_iters=100_000, rng=1)
ax.set_title(r"$\lambda=1.9$, $\mu=2$, $\rho=0.95$, 1000 seconds")
plt.show()}

\section{8. What simulation can hide}

\notes{Real networks are more complex than this chain. Many cannot be studied analytically, so their statistics must be determined through simulation. Summarise what you have learned from the simple example above about the possible dangers of such simulations.}

\thanks

\references

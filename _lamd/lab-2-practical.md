---
title: "Lab 2: Simulation of Networks of Queues in ns-2"
week: 8
practical: 5
layout: practical
assignment: True
notespdf: False
tex_template: exercise
posts: True
ipynb: True
reveal: False
docx: False
pptx: False
date: 2006-11-13
abstract: >
  Week 8 lab. Revisit $M/M/1$ inside the ns-2 packet simulator, then build
  a tandem pair and a multipath network and compare occupancy with
  Kleinrock's independence assumption. Analysis originally in MATLAB;
  the Tcl scripts remain as historical listings.
---

\section{How this lab sits in the course}

\notes{This is the Monday of week 8, after Erlang delay and loss and (in the 2006 timetable) after the lectures on networks of queues and Jackson's theorem. It has three layers of dependence on earlier material.}

\notes{1. *Lab 1 and lectures 4--6.* Part 1 is again an $M/M/1$ queue, now as packets on a link rather than a birth-death chain on $\Delta t$. Arrival rate $\lambda$ and exponential packet length with rate $\mu$ are the same pair you simulated in week 3. The theoretical mean occupancy is still $\rho/(1-\rho)$ with $\rho=\lambda/\mu$, provided the link is stable.}

\notes{2. *Little (lecture 6) and Erlang (lectures 7--10).* You already know that time averages need a long enough run, and that high $\rho$ mixes slowly. That is why the sheet asks for $\lambda=1$ and then $\lambda=1.9$ with $\mu=2$, the same two operating points as Lab 1.}

\notes{3. *Networks of queues (lectures 14--15, week 7).* The tandem and multipath parts are the first time two queues share a packet. Kleinrock's independence assumption --- treat each link as if it saw Poisson arrivals with independent service --- is the analytical tool those lectures justify. This lab asks you to *test* it on ns-2 traces.}

\notes{A Python packet-level stand-in for ns-2 is deliberately not provided here. The Tcl in `labs/ns2/` is the 2006 artefact. Occupancy *analysis* is rewritten in Python, as in Lab 1.}

\slides{* Part 1: ns-2 $M/M/1$ = Lab 1 in a packet simulator
* Same $(\lambda,\mu)=(1,2)$ and $(1.9,2)$ as week 3
* Tandem and multipath: preview of Kleinrock / Jackson}

\include{snippets/_npa/includes/npa-python-setup.md}

\section{The 2006 lab environment}

\notes{As taught, students rebooted departmental PCs into Red Hat Linux, logged in through Gnome, opened a terminal, fetched `http://www.dcs.shef.ac.uk/~neil/NPA/source.zip` in Netscape, and ran `ns mm1.tcl`. Those machine-room steps are archive colour. The scripts that mattered are in this repository as `labs/ns2/mm1.tcl` and `labs/ns2/multipath.tcl`.}

\section{1. An $M/M/1$ link in ns-2}

\notes{Open `labs/ns2/mm1.tcl`. At the top, `lamda` is the packet arrival rate and `mu` parametrises an exponential packet length in kilobytes. The topology section is marked `# Set up the network structure`: two nodes and a simplex link
$$
\texttt{set link [\$ns simplex-link \$node1 \$node2 8Kb 0ms DropTail]}.
$$
What do the arguments of `simplex-link` do? What does simplex mean?}

\notes{Run `ns mm1.tcl`. Queue length is printed to the screen; `ns mm1.tcl > qlength.dat` writes it to a file. The 2006 sheet then loaded that file in MATLAB (`load qlength.dat`) and plotted the running average `cumsum(qlength)./(1:length(qlength))'`. In Python, if `qlength` is a one-dimensional array of occupancies,}

\code{qlength = npa_plots.simulate_mm1(1.0, 2.0, n_iters=100_000, rng=1)
t = np.arange(1, len(qlength) + 1)
plt.plot(t, np.cumsum(qlength) / t)
plt.xlabel("step")
plt.ylabel(r"running mean occupancy")
plt.show()
print("sample mean", qlength.mean())}

\notes{Run the ns-2 script (or the discrete stand-in above) for $\lambda=1$, $\mu=2$, then again for $\lambda=1.9$, $\mu=2$. Compute the theoretical average queue length in each case from the $M/M/1$ formula in lectures 5--6, and compare with the plotted running mean. The helper `simulate_mm1` is *not* ns-2: it is Lab 1's chain. Use it only as a numerical check on the formula while the historic Tcl is what the 2006 class ran.}

\section{2. Tandem $M/M/1$}

\notes{Extend the simulation by adding a third node and a second queue. The topology is two links in series.}

\figure{\includepng{\diagramsDir/npa/ns2mm2Tandem}{55%}}{Tandem pair: node 1 to node 2 to node 3, each hop an 8 Kb DropTail link.}{lab2-tandem}

\notes{Save `mm1.tcl` as `tandemMM1.tcl`, then:}

\notes{* After `set node2 [$ns node]`, add `set node3 [$ns node]`.}

\notes{* After the first `simplex-link`, add `set link2 [$ns simplex-link $node2 $node3 8Kb 0ms DropTail]`.}

\notes{* Associate a queue with the new link: `set qu2 [[$ns link $node2 $node3] set queue_]` and `$qu2 set limit_ $m`.}

\notes{* Attach the sink to `node3` instead of `node2`.}

\notes{* Monitor the new queue, `set qmon2 [$ns monitor-queue $node2 $node3 ""]`, and print both occupancies from `outputdata`.}

\notes{This is the smallest network in which a packet's length is *reused* at the second server: service times on the two hops are proportional to the same $L$. That correlation is exactly what Kleinrock's independence assumption discards. The networks-of-queues lecture (week 7) is the justification; here, look at whether the two running means still match isolated $M/M/1$ formulae.}

\section{3. Multipath and Kleinrock}

\notes{A more complex architecture is prepared in `labs/ns2/multipath.tcl`. Read the code (the duplex links are required by the multipath routing protocol; traffic still travels one way). Draw the architecture: source `node1`, two parallel two-hop paths to sink `node4`. The routing command sends traffic equally down all available paths.}

\notes{1. Use Kleinrock's independence assumption to approximate the expected queue length at each link.}

\notes{2. How does that approximation compare with the simulated occupancy for light load $\mu=2$, $\lambda=2$; moderate load $\mu=2$, $\lambda=3$; and heavier load $\mu=2$, $\lambda=3.8$?}

\notes{3. Reduce each link bandwidth to 4 Kb. How does average queue length compare with the original example?}

\notes{4. Modify the multipath script to include a direct route from `node1` to `node4`, and to include another node on the way to `node4`.}

\notes{*End of lab.* The ns-2 scripts stay in `labs/ns2/` until a Python packet-level equivalent is added.}

\thanks

\references

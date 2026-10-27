\ifndef{networkSimulationNs2}
\define{networkSimulationNs2}

\section{Simulation}

\notes{Kleinrock and Jackson are back-of-envelope tools. A real network is usually simulated. The 2006 lab used ns-2, a discrete-event network simulator driven by Tcl, supporting TCP and multicast, extensible in C++, and installed on the departmental Linux machines (Cygwin for a personal copy). Lab 2 is that comparison: occupancy from ns-2 against isolated $M/M/1$ formulae on a tandem pair and a multipath diamond.}

\notes{The approximations are useful *before* the simulator, and as a check on it. Lab 1 already showed that a sample mean from a short run at high $\rho$ is not the steady-state mean. The same warning applies to packet traces.}

\slides{* ns-2: discrete-event, Tcl, Lab 2
* Kleinrock as a check, not a replacement
* Sample averages at high $\rho$ still lie}

\endif

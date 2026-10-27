\ifndef{databaseBottleneckExample}
\define{databaseBottleneckExample}

\subsection{Example: Matching Disk and CPU}

\notes{A simple design question. We are building database servers from existing parts: two CPU/motherboard systems and two disk systems.}

CPU system | Expected service time (ms) | Disk system | Expected service time (ms)
-----------|----------------------------|-------------|----------------------------
A | 423 | 1 | 215
B | 210 | 2 | 390

\notes{Which should we match with which? One fast system and one slow system, or two similar systems?}

\slides{* Match A with disk 2 and B with disk 1
* That avoids a bottleneck: disk 1 would wait for CPU A about half the time, and CPU B would wait for disk 2 about half the time}

\notes{Match A with 2 and B with 1. Pairing the slow CPU with the slow disk and the fast CPU with the fast disk avoids a one-sided wait: disk 1 would otherwise wait for CPU A on about half the jobs, and CPU B would wait for disk 2 on about half the jobs.}

\endif

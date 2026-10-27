---
title: "Tutorial 3: Erlang Delay and Loss, and $M/G/1$"
week: 7
practical: 3
layout: practical
assignment: True
notespdf: False
tex_template: exercise
posts: True
ipynb: False
reveal: False
docx: False
pptx: False
date: 2006-10-17
abstract: >
  An Erlang-C call centre, an Erlang-B trunk group, and a triangular
  service time in the Pollaczek–Khinchin formula. Originally Network
  Performance Analysis Tutorial 3.
---

\section{Tutorial 3}

\notes{Erlang delay and loss, and the $M/G/1$ queue. Assume Poisson arrivals and exponential service in the first two questions.}

\section{A complaints call centre}

\notes{A telephone call centre handles complaints from bank customers. In the busy hour, calls arrive at 120 customers per hour. Dealing with each customer takes 3 minutes on average. When all assistants are occupied, customers are placed in a holding system.}

\notes{1. The centre has 10 assistants. What is the probability that a customer has to join the queue?}

\notes{2. What is the expected queueing time for each customer?}

\notes{3. Customers who do not queue have waiting time 0. What is the average waiting time for those who *do* queue?}

\notes{4. The bank wishes to combine two such centres. Both have busy-hour arrival rate 120 customers per hour. How many staff does the combined centre need to keep the queueing probability at least as low as in (1)?}

\notes{5. Answer (2) and (3) for the new system.}

\section{Trunk lines}

\notes{A telephone company plans to rent trunk lines between Birmingham and London for \$1{,}000 per year. They expect a demand of 20 calls per hour and an average holding time of 15 minutes. They can charge \$0.01 per minute per customer. There is no holding facility.}

\notes{1. How many trunk lines are needed to keep the blocking probability below 0.01?}

\notes{2. How much profit will they make?}

\section{A triangular service time}

\notes{A service-time distribution is
$$
P(X)=\begin{cases}
\frac{2}{b}-\frac{2}{b^2}X & 0<X\le b,\\
0 & X>b.
\end{cases}
$$}

\notes{1. Sketch this distribution.}

\notes{2. The Pollaczek–Khinchin formula gives the mean waiting time
$$
\bar{W}=\frac{\lambda\langle X^2\rangle}{2(1-\rho)}.
$$}

\notes{3. By determining the first two moments $\langle X\rangle$ and $\langle X^2\rangle$, derive the average waiting time for the queue.}

\thanks

\references

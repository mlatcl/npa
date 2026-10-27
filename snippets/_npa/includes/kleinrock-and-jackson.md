\ifndef{kleinrockAndJackson}
\define{kleinrockAndJackson}

\section{Kleinrock's Independence Assumption}

\notes{Kleinrock's independence assumption treats every link as if it saw Poisson arrivals and independent service --- as if merging streams restored the independence that tandem service destroys. It is a good approximation when many packets from outside the network enter at every queue, on densely connected networks, with exponential packet lengths, Poisson exogenous arrivals, and moderate to heavy traffic.}

\notes{Label nodes and links. Stream $s$ has rate $x_s$; $f_{ij}(s)$ is the fraction of that stream that uses the link from $i$ to $j$. The link rate is
$$
\lambda_{ij}=\sum_s f_{ij}(s)\,x_s.
$$
Each link is then an $M/M/1$ queue with mean occupancy and delay
$$
\bar{N}_{ij}=\frac{\lambda_{ij}}{\mu_{ij}-\lambda_{ij}},\qquad
\bar{T}_{ij}=\frac{1}{\mu_{ij}-\lambda_{ij}}.
$$
The mean number in the network is the sum over links. We ignore propagation and processing delay; see Bertsekas and Gallager, Section 3.6.1.}

\slides{* Each link $\approx$ $M/M/1$ after merging
* $\lambda_{ij}=\sum_s f_{ij}(s)x_s$
* $\bar{N}_{ij}=\lambda_{ij}/(\mu_{ij}-\lambda_{ij})$
* Best when the network is dense and traffic is mixed}

\section{Jackson's Theorem}

\notes{Kleinrock approximates each *link*. Jackson's theorem is a statement about the *network*. Assumptions: no correlation between service times and queue lengths (Kleinrock's premise), and routing that randomises among paths. Then the mean number of packets in the network is
$$
\bar{N}=\sum_{i,j}\frac{\lambda_{ij}}{\mu_{ij}-\lambda_{ij}}.
$$
The product-form occupancy is the deeper result; for this course the mean and the two assumptions are enough. Analysis is in Bertsekas and Gallager, Section 3.8. This is Question 4 of the 2004--05 paper.}

\slides{* Jackson: product form under Kleinrock + random routing
* $\bar{N}=\sum_{ij}\lambda_{ij}/(\mu_{ij}-\lambda_{ij})$}

\section{A Five-Node Example}

\figure{\includepng{\diagramsDir/npa/kleinrockNetwork}{80%}}{Five-node network used with Kleinrock's assumption. Flow is from lower-numbered nodes to higher; thick routes carry the streams $x_s$.}{kleinrock-five-node}

\notes{Mean transmission times in milliseconds: $\bar{X}_{12}=\bar{X}_{13}=\bar{X}_{25}=\bar{X}_{35}=0.05$, $\bar{X}_{14}=\bar{X}_{45}=0.033$. Stream rates $x_1=5$, $x_2=10$, $x_3=7$, $x_4=12$, $x_5=4$, $x_6=8$, $x_7=4$. Superposition on each link gives $\lambda_{12}=15$, $\lambda_{13}=7$, $\lambda_{14}=16$, $\lambda_{25}=10$, $\lambda_{35}=15$, $\lambda_{45}=16$. The most congested links under Kleinrock are $1\to 2$ and $3\to 5$ ($\rho=3/4$, $\bar{N}=3$). Mean delays $\bar{T}=\bar{X}/(1-\rho)$ make the route $1\to 4\to 5$ the shortest ($1/7$), then $1\to 3\to 5$, then $1\to 2\to 5$.}

\slides{* Worked five-node Kleinrock example
* Most congested: $1\to 2$ and $3\to 5$
* Fastest $1\to 5$: via node 4}

\endif

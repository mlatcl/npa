\ifndef{npaIndependence}
\define{npaIndependence}

\subsection{Independence}

\notes{We will often assume that two or more variables are independent. That means knowledge of one does not change the distribution of the other,
$$
P(x)=P(x\mid y),
$$
so the joint factorises,
$$
P(x,y)=P(x)P(y).
$$
Factorisation is what makes so much of the later analysis tractable: superposition of Poisson processes, Kleinrock’s independence assumption, and the product-form results for networks of queues all start here.}

\slides{* Independent: $P(x\mid y)=P(x)$, hence $P(x,y)=P(x)P(y)$
* This factorisation is why Poisson superposition and product-form networks work}

\endif

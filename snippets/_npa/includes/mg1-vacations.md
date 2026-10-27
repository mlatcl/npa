\ifndef{mg1Vacations}
\define{mg1Vacations}

\section{$M/G/1$ with Vacations}

\notes{When the server is free it may attend to other work --- control traffic, a kitchen check --- a *vacation*. An arrival that finds the server on vacation waits until the vacation ends. If a vacation ends and the server is still idle, it takes another. Vacation lengths $V_1,V_2,\ldots$ are i.i.d. and independent of arrivals and service.}

\figure{\includepng{\diagramsDir/npa/vacationMG1}{70%}}{An $M/G/1$ server that takes a vacation whenever the queue is empty.}{mg1-vacation-schematic}

\figure{\includepng{\diagramsDir/npa/vacationResidual}{70%}}{Residual time now includes vacation triangles as well as service triangles.}{mg1-vacation-residual}

\notes{The residual-time integral now has two families of triangles. With $M(t)$ service completions and $L(t)$ vacations in $[0,t]$,
$$
\frac1t\int_0^t r(\tau)\,d\tau
=\frac{M(t)}{t}\frac12\frac{\sum X_i^2}{M(t)}
+\frac{L(t)}{t}\frac12\frac{\sum V_i^2}{L(t)}.
$$
The fraction of time available for vacations is $1-\rho$, so $L(t)=t(1-\rho)/\bar{V}_t$. The limit is
$$
\bar{R}=\frac12\lambda\langle X^2\rangle+\frac{(1-\rho)\langle V^2\rangle}{2\bar{V}},
$$
and therefore
$$
\bar{W}=\frac{\lambda\langle X^2\rangle}{2(1-\rho)}+\frac{\langle V^2\rangle}{2\bar{V}}.
$$
Pollaczek--Khinchin plus a vacation residual that does *not* depend on $\rho$.}

\notes{A bar with Poisson arrivals, exponential service of mean $\bar{X}$, and exponential kitchen checks of mean $\bar{V}$ has $\langle X^2\rangle=2\bar{X}^2$ and $\langle V^2\rangle=2\bar{V}^2$, so
$$
\bar{W}=\frac{\rho\bar{X}}{1-\rho}+\bar{V}.
$$
Deterministic vacations of the same mean would add only $\bar{V}/2$.}

\slides{* Vacation whenever idle; i.i.d. $V_i$
* $\bar{W}=\lambda\langle X^2\rangle/(2(1-\rho))+\langle V^2\rangle/(2\bar{V})$
* Exponential vacation adds $\bar{V}$; deterministic adds $\bar{V}/2$}

\endif

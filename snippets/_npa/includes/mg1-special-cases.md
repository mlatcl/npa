\ifndef{mg1SpecialCases}
\define{mg1SpecialCases}

\section{Special Cases}

\notes{Second moment $\langle X^2\rangle=\mathrm{Var}(X)+\bar{X}^2$. For exponential service, $\bar{X}=1/\mu$ and $\mathrm{Var}(X)=1/\mu^2$, so $\langle X^2\rangle=2/\mu^2$ and Pollaczek--Khinchin collapses to the $M/M/1$ wait $\bar{W}=\rho/(\mu(1-\rho))$.}

\notes{Deterministic service ($M/D/1$, fixed-length packets on a fixed-bandwidth line) has $\mathrm{Var}(X)=0$, so $\langle X^2\rangle=1/\mu^2$ and
$$
\bar{W}=\frac{\rho}{2\mu(1-\rho)},
$$
half the $M/M/1$ wait. Among distributions with a given mean, deterministic service gives the lowest delay: the residual sawtooth has the smallest area.}

\notes{Uniform service on $[0,b]$ has mean $b/2$ and variance $b^2/12$. With $\mu=2/b$, the second moment is $4/(3\mu^2)$ and
$$
\bar{W}=\frac{2\rho}{3\mu(1-\rho)}.
$$}

\notes{Writing $\mu=1/\bar{X}$: exponential wait $\rho/(\mu(1-\rho))$, sojourn $1/(\mu(1-\rho))$, $\bar{N}=\rho/(1-\rho)$; deterministic wait half of that, sojourn $(2-\rho)/(2\mu(1-\rho))$, $\bar{N}=\rho(2-\rho)/(2(1-\rho))$.}

\slides{* $M/M/1$: PK recovers $\bar{W}=\rho/(\mu(1-\rho))$
* $M/D/1$: half that wait; lowest delay at fixed mean
* $M/U/1$ on $[0,b]$: $\langle X^2\rangle=4/(3\mu^2)$}

\endif

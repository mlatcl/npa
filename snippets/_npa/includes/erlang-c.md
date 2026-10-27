\ifndef{erlangC}
\define{erlangC}

\section{Probability of Waiting}

\notes{The operational question for $M/M/m$ is the probability that an arrival finds every server busy and must wait,
$$
P_Q=P(k\ge m)=\sum_{k=m}^{\infty}P(k)=P(0)\frac{(m\rho)^m}{m!(1-\rho)}\doteq C(m,a).
$$
This is *Erlang's second formula*, or Erlang C. In offered-load form $a=m\rho$,
$$
C(m,a)=\frac{P(0)\,a^m}{m!(1-a/m)}.
$$}

\notes{Direct evaluation of $a^m/m!$ overflows for large $m$. Compute in log space,
$$
\ln C(m,a)=\ln P(0)+m\ln a-\ln m!-\ln(1-a/m),
$$
with $\ln m!=\ln\Gamma(m+1)$. The original MATLAB helpers `erlangC.m` / `plotErlang.m` do that; `npa_plots.erlang_c` and `npa_plots.plot_erlang_curves` are the same calculation.}

\slides{* $C(m,a)=P(k\ge m)$: Erlang C, probability of waiting
* Log-space: $\ln m!$ via $\ln\Gamma(m+1)$
* Exams used paper curves of $C$ against $a$}

\include{snippets/_npa/includes/npa-python-setup.md}

\code{fig, ax = npa_plots.plot_erlang_curves(
    range(1, 13), np.linspace(0.05, 20, 400), kind="C")
ax.set_title("Erlang C, offered traffic 0 to 20")
plt.show()}

\figure{\includepng{\diagramsDir/npa/erlangCCurves0to20}{80%}}{Historic Erlang C curves for offered traffic between 0 and 20. In an exam the curves were issued with the paper.}{erlang-c-curves-20}

\figure{\includepng{\diagramsDir/npa/erlangCCurves0to100}{80%}}{Historic Erlang C curves for offered traffic between 0 and 100.}{erlang-c-curves-100}

\section{Mean Occupancy and Waiting Time}

\notes{The mean number in the system splits into the mean queue length and the mean number of busy servers $a=m\rho$,
$$
\bar{N}=\frac{\rho}{1-\rho}C(m,a)+m\rho,\qquad
\bar{N}_Q=\frac{\rho}{1-\rho}C(m,a).
$$
Little's formula on the waiting line, with arrival rate $\lambda$ (nothing is lost), gives the mean wait for *all* customers,
$$
\bar{W}=\frac{\bar{N}_Q}{\lambda}=\frac{C(m,a)}{m\mu(1-\rho)}.
$$
Customers who do not queue have $\bar{W}_{\sim Q}=0$, so the mean wait among those who *do* queue is
$$
\bar{W}=C(m,a)\,\bar{W}_Q\qquad\Rightarrow\qquad
\bar{W}_Q=\frac{1}{m\mu(1-\rho)}=\frac{1}{\mu(m-a)}.
$$
That conditional wait does not depend on $C(m,a)$.}

\slides{* $\bar{N}_Q=\rho C(m,a)/(1-\rho)$, $\bar{W}=C(m,a)/(m\mu(1-\rho))$
* Conditional wait $\bar{W}_Q=1/(\mu(m-a))$, independent of $C$}

\endif

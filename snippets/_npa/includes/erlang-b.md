\ifndef{erlangB}
\define{erlangB}

\section{Probability of Blocking}

\notes{Waiting probability is zero: the chain never enters $k>m$. The quantity of interest is the blocking probability, which by PASTA is $P(m)$,
$$
B(m,a)=P(m)=\frac{a^m/m!}{\sum_{n=0}^{m}a^n/n!}.
$$
This is *Erlang's first formula*, or Erlang B. The same overflow caution as Erlang C applies; `npa_plots.erlang_b` evaluates it in log space, matching `erlangB.m`.}

\include{snippets/_npa/includes/npa-python-setup.md}

\code{fig, ax = npa_plots.plot_erlang_curves(
    range(1, 13), np.linspace(0.05, 20, 400), kind="B")
ax.set_title("Erlang B, offered traffic 0 to 20")
plt.show()}

\figure{\includepng{\diagramsDir/npa/erlangBCurves0to20}{80%}}{Historic Erlang B curves for offered traffic between 0 and 20.}{erlang-b-curves-20}

\figure{\includepng{\diagramsDir/npa/erlangBCurves0to100}{80%}}{Historic Erlang B curves for offered traffic between 0 and 100.}{erlang-b-curves-100}

\slides{* $B(m,a)=P(m)$: Erlang B, fraction of arrivals lost
* No queue, so $P_Q=0$
* Log-space evaluation; exams used paper curves}

\section{Carried Load and Utilisation}

\notes{Carried load is offered load times the probability of not being blocked,
$$
a'=a\bigl(1-B(m,a)\bigr).
$$
Trunk occupancy --- utilisation of a line --- is then $\rho=a'/m$, not $a/m$. In a lossless system $a'=a$ and the two coincide. The throughput of the system, the rate at which customers actually enter service, is
$$
\dot{\lambda}=\lambda\bigl(1-P(m)\bigr).
$$
Little's formula on a lossy system must use this carried rate, not the offered arrival rate: blocked customers never enter, so they do not contribute to occupancy.}

\slides{* $a'=a(1-B(m,a))$, $\rho=a'/m$
* Throughput $\dot{\lambda}=\lambda(1-P(m))$
* Little: use carried rate, not offered $\lambda$}

\endif

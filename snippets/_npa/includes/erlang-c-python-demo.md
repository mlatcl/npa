\ifndef{npaErlangCPythonDemo}
\define{npaErlangCPythonDemo}

\include{snippets/_npa/includes/npa-python-setup.md}

\notes{The MATLAB helpers `erlangC.m` / `plotErlang.m` are `npa_plots.erlang_c` and `npa_plots.plot_erlang_curves`. $\ln m!$ is $\ln\Gamma(m+1)$.}

\code{fig, ax = npa_plots.plot_erlang_curves(
    range(1, 13), np.linspace(0.05, 20, 400), kind="C")
ax.set_title("Erlang C, offered traffic 0 to 20")
plt.show()}

\endif

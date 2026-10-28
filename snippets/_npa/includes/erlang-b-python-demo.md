\ifndef{npaErlangBPythonDemo}
\define{npaErlangBPythonDemo}

\include{snippets/_npa/includes/npa-python-setup.md}

\notes{`npa_plots.erlang_b` evaluates Erlang B in log space, matching `erlangB.m`.}

\code{fig, ax = npa_plots.plot_erlang_curves(
    range(1, 13), np.linspace(0.05, 20, 400), kind="B")
ax.set_title("Erlang B, offered traffic 0 to 20")
plt.show()}

\endif

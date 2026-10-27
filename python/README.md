# NPA Python helpers

Replacements for the MATLAB demos in `matlab/` and `labs/matlab/`. Import from
lecture snippets via `_npa/includes/npa-python-setup.md`.

| MATLAB | Python |
| --- | --- |
| `exponentialSamp.m` | `npa_plots.exponential_sample` |
| `erlangB.m` | `npa_plots.erlang_b` |
| `erlangC.m` | `npa_plots.erlang_c` |
| `plotErlang.m` | `npa_plots.plot_erlang_curves` |
| `demo/simulateQueue.m` | `npa_plots.simulate_mm1` |
| occupancy histograms | `npa_plots.plot_mm1_occupancy` |

Lab 1 uses `simulate_mm1`. Lab 2 still runs the historic ns-2 Tcl
(`labs/ns2/mm1.tcl`, `multipath.tcl`); occupancy *analysis* is Python.
A packet-level Python stand-in is not added yet.

Notebook smoke tests (`scripts/smoke_notebooks.py`) execute the compiled
`_notebooks/*.ipynb` files, including the cells that import this module.

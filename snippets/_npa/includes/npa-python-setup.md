\ifndef{npaPythonSetup}
\define{npaPythonSetup}

\setupcode{import sys
import os
_root = os.path.abspath(os.path.join(os.getcwd(), '..'))
_py = os.path.join(_root, 'python')
if os.path.isdir(_py) and _py not in sys.path:
    sys.path.insert(0, _py)
import numpy as np
import matplotlib.pyplot as plt
import npa_plots}

\endif

# Environmental noise analysis in Python (Py_Env_Noise)

[![Build Status](https://travis-ci.org/EconForge/interpolation.py.svg?branch=master)](https://travis-ci.org/EconForge/interpolation.py)

The library contains:

- `utils.*`: comprehensive sets of functions for pre- and post-signal processing


## install

Install latest version:

- from PyPI: `pip install pyenvnoise`

Latest development version from git:

```
pip install poetry # if not already installed
pip install git+https://github.com/econforge/interpolation.py.git/
```

## Read *.pti files

Preferred interface for multilinear interpolation. It can interpolate on uniform
and nonuniform cartesian grids. Several extrapolation options are available.


```python
import pyenvnoise
from pyenvnoise.utils import ptiread

# read .pti files
# output:
# signal: array(lengh samples, numbers of channels)
# fs: sampling frequency
# t: time of files
# d: date of file
signal, fs, t, d = ptiread('Recording-1.1.pti')


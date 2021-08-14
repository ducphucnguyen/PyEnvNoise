Environmental noise analysis in Python
=====================

[![Language](https://img.shields.io/badge/python-v3.7-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/ducphucnguyen/PyEnvNoise/blob/master/LICENSE)

The library contains:

- `utils.*`: comprehensive sets of functions for pre- and post-signal processing


## install

Install latest version:

- `pip install pyenvnoise==0.1.1`

Latest development version from git:

```
pip install poetry # if not already installed
pip install git+https://github.com/ducphucnguyen/PyEnvNoise.git
```

## Read *.pti files

A fastest method to read acoustic files with *.pti extension

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


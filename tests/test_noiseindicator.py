# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 13:02:47 2021

@author: nguy0936
"""

from pyenvnoise.utils import ptiread
from pyenvnoise.utils import noise_indicator
#from pyenvnoise.utils import weighting_network


data = ptiread('R:\CMPH-Windfarm Field Study\Hornsdale\set2\Recording-1.1.pti')
x = data[0][:,0]
Fs = data[1]

Leq = noise_indicator.Leq(x)
LAeq = noise_indicator.LAeq(x, Fs)

LCeq = noise_indicator.LCeq(x, Fs)

LZeq = noise_indicator.LZeq(x, Fs)

LGeq = noise_indicator.LGeq(x, Fs)

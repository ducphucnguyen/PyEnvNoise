# -*- coding: utf-8 -*-
import numpy as np
from scipy.signal.filter_design import bilinear
from scipy.signal import lfilter, zpk2tf, decimate



#---- Annex E - Analytical expressions for frequency-weightings C, A, and Z.-#

_POLE_FREQUENCIES = {
    1: 20.60,
    2: 107.7,
    3: 737.9,
    4: 12194.0,
}
"""Approximate values for pole frequencies f_1, f_2, f_3 and f_4.

See section E.4.1 of the standard.
"""

_NORMALIZATION_CONSTANTS = {
    'A': -2.000,
    'C': -0.062,
}
"""Normalization constants :math:`C_{1000}` and :math:`A_{1000}`.

See section E.4.2 of the standard.
"""

def A_weighting(x, Fs):
    """A-weighting filter represented as polynomial transfer function.

    :returns: Tuple of `num` and `den`.

    See equation E.6 of the standard.

    """
    f1 = _POLE_FREQUENCIES[1]
    f2 = _POLE_FREQUENCIES[2]
    f3 = _POLE_FREQUENCIES[3]
    f4 = _POLE_FREQUENCIES[4]
    offset = _NORMALIZATION_CONSTANTS['A']
    numerator = np.array([(2.0 * np.pi * f4)**2.0 * (10**(-offset / 20.0)), 0.0, 0.0, 0.0, 0.0])
    part1 = [1.0, 4.0 * np.pi * f4, (2.0 * np.pi * f4)**2.0]
    part2 = [1.0, 4.0 * np.pi * f1, (2.0 * np.pi * f1)**2.0]
    part3 = [1.0, 2.0 * np.pi * f3]
    part4 = [1.0, 2.0 * np.pi * f2]
    denomenator = np.convolve(np.convolve(np.convolve(part1, part2), part3), part4)
    B, A = bilinear(numerator, denomenator, Fs)
    
    return lfilter(B, A, x)


def C_weighting(x, Fs):
    """C-weighting filter represented as polynomial transfer function.

    :returns: Tuple of `num` and `den`.

    See equation E.1 of the standard.

    """
    f1 = _POLE_FREQUENCIES[1]
    f4 = _POLE_FREQUENCIES[4]
    offset = _NORMALIZATION_CONSTANTS['C']
    numerator = np.array([(2.0 * np.pi * f4)**2.0 * (10**(-offset / 20.0)), 0.0, 0.0])
    part1 = [1.0, 4.0 * np.pi * f4, (2.0 * np.pi * f4)**2.0]
    part2 = [1.0, 4.0 * np.pi * f1, (2.0 * np.pi * f1)**2.0]
    denomenator = np.convolve(part1, part2)
    B, A = bilinear(numerator, denomenator, Fs)
    
    return lfilter(B, A, x)



def Z_weighting(x, Fs):
    """Z-weighting filter represented as polynomial transfer function.

    :returns: Tuple of `num` and `den`.

    Z-weighting is 0.0 dB for all frequencies and therefore corresponds to a
    multiplication of 1.

    """
    numerator = [1]
    denomenator = [1]
    B, A = bilinear(numerator, denomenator, Fs)
    
    return lfilter(B, A, x)


def G_weighting(x,Fs):
    
    q = round(Fs/1024)
    if q<1:
        q = 1
    
    Fs_q = round(Fs/q) # downsample
    x_q = decimate(x, q)
             
             
    z = [0+0j, 0+0j, 0+0j, 0+0j]
    
    p = [2j*(-0.707 + 0.707j), 2*np.pi*(-0.707 - 0.707j),
         2*np.pi*(-19.27 + 5.16j), 2*np.pi*(-19.27 - 5.16j),
         2*np.pi*(-14.11 + 14.11j), 2*np.pi*(-14.11 - 14.11j),
         2*np.pi*(-5.16 + 19.27j), 2*np.pi*(-5.16 - 19.27j)]
    
    k = 9.825e8
    
    bc, ac = zpk2tf(z,p,k)
    B, A = bilinear(bc, ac, Fs_q)
    
    return lfilter(B, A, x_q)






WEIGHTING_SYSTEMS = {
    'A': A_weighting,
    'C': C_weighting,
    'Z': Z_weighting,
    'G': G_weighting,
}
"""Weighting systems.
"""
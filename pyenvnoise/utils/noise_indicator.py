# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 12:57:24 2021

@author: nguy0936
"""

import numpy as np
from pyenvnoise.utils import weighting_network

REFERENCE_PRESSURE = 2.0e-5
"""
Reference value of the sound pressure :math:`p_0` is :math:`2 \cdot 10^{-5}` Pa.
"""

def Leq(pressure, reference_pressure=REFERENCE_PRESSURE, axis=-1):
    """
    Time-averaged sound pressure level :math:`L_{p,T}` or equivalent-continious sound pressure level :math:`L_{p,eqT}` in dB.

    :param pressure: Instantaneous sound pressure :math:`p`.
    :param reference_pressure: Reference value :math:`p_0`.
    :param axis: Axis.

    .. math:: L_{p,T} = L_{p,eqT} = 10.0 \\log_{10}{ \\left( \\frac{\\frac{1}{T} \\int_{t_1}^{t_2} p^2 (t) \\mathrm{d} t  }{p_0^2} \\right)}

    See section 2.3.
    """
    return 10.0 * np.log10((pressure**2.0).mean(axis=axis) / reference_pressure**2.0)



def LAeq(pressure, Fs, reference_pressure=REFERENCE_PRESSURE, axis=-1):
    """
    Time-averaged sound pressure level :math:`L_{p,T}` or equivalent-continious sound pressure level :math:`L_{p,eqT}` in dB.

    :param pressure: Instantaneous sound pressure :math:`p`.
    :param reference_pressure: Reference value :math:`p_0`.
    :param axis: Axis.

    .. math:: L_{p,T} = L_{p,eqT} = 10.0 \\log_{10}{ \\left( \\frac{\\frac{1}{T} \\int_{t_1}^{t_2} p^2 (t) \\mathrm{d} t  }{p_0^2} \\right)}

    See section 2.3.
    """
    
    y_A = weighting_network.WEIGHTING_SYSTEMS['A'](pressure, Fs)
    
    return 10.0 * np.log10((y_A**2.0).mean(axis=axis) / reference_pressure**2.0)



def LCeq(pressure, Fs, reference_pressure=REFERENCE_PRESSURE, axis=-1):
    """
    Time-averaged sound pressure level :math:`L_{p,T}` or equivalent-continious sound pressure level :math:`L_{p,eqT}` in dB.

    :param pressure: Instantaneous sound pressure :math:`p`.
    :param reference_pressure: Reference value :math:`p_0`.
    :param axis: Axis.

    .. math:: L_{p,T} = L_{p,eqT} = 10.0 \\log_{10}{ \\left( \\frac{\\frac{1}{T} \\int_{t_1}^{t_2} p^2 (t) \\mathrm{d} t  }{p_0^2} \\right)}

    See section 2.3.
    """
    
    y_C = weighting_network.WEIGHTING_SYSTEMS['C'](pressure, Fs)
    
    return 10.0 * np.log10((y_C**2.0).mean(axis=axis) / reference_pressure**2.0)



def LZeq(pressure, Fs, reference_pressure=REFERENCE_PRESSURE, axis=-1):
    """
    Time-averaged sound pressure level :math:`L_{p,T}` or equivalent-continious sound pressure level :math:`L_{p,eqT}` in dB.

    :param pressure: Instantaneous sound pressure :math:`p`.
    :param reference_pressure: Reference value :math:`p_0`.
    :param axis: Axis.

    .. math:: L_{p,T} = L_{p,eqT} = 10.0 \\log_{10}{ \\left( \\frac{\\frac{1}{T} \\int_{t_1}^{t_2} p^2 (t) \\mathrm{d} t  }{p_0^2} \\right)}

    See section 2.3.
    """
    
    y_Z = weighting_network.WEIGHTING_SYSTEMS['Z'](pressure, Fs)
    
    return 10.0 * np.log10((y_Z**2.0).mean(axis=axis) / reference_pressure**2.0)



def LGeq(pressure, Fs, reference_pressure=REFERENCE_PRESSURE, axis=-1):
    """
    Time-averaged sound pressure level :math:`L_{p,T}` or equivalent-continious sound pressure level :math:`L_{p,eqT}` in dB.

    :param pressure: Instantaneous sound pressure :math:`p`.
    :param reference_pressure: Reference value :math:`p_0`.
    :param axis: Axis.

    .. math:: L_{p,T} = L_{p,eqT} = 10.0 \\log_{10}{ \\left( \\frac{\\frac{1}{T} \\int_{t_1}^{t_2} p^2 (t) \\mathrm{d} t  }{p_0^2} \\right)}

    See section 2.3.
    """
    
    y_G = weighting_network.WEIGHTING_SYSTEMS['G'](pressure, Fs)
    
    return 10.0 * np.log10((y_G**2.0).mean(axis=axis) / reference_pressure**2.0)





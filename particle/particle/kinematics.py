# Copyright (c) 2018-2019, Eduardo Rodrigues and Henry Schreiner.
#
# Distributed under the 3-clause BSD license, see accompanying file LICENSE
# or https://github.com/scikit-hep/particle for details.

"""
Functions relevant to particle kinematics.
"""

from __future__ import absolute_import, division, print_function

from hepunits.units import MeV, ns
from hepunits.constants import hbar


def width_to_lifetime(Gamma):
    """
    Convert from a particle decay width to a lifetime.

    Parameters
    ----------
    Gamma : float > 0
        Particle decay width, in the HEP standard energy unit MeV.

    Returns
    -------
    Gamma > 0: particle lifetime, in the HEP standard time unit ns.
    Gamma = 0: Infinity (float("inf")).
    Gamma < 0: an exception ValueError is raised.

    Examples
    --------
    Manipulation with no explicit usage of units:

    >>> width_to_lifetime(4.33e-10)   # result returned in ns
    0.001520119980246514

    Manipulations with explicit units defined in the HEP system of units:

    >>> from hepunits.units import MeV, eV, ps   # handy module with units in the HEP system of units
    >>>
    >>> width_to_lifetime(4.33e-10*MeV)
    0.001520119980246514          # result returned in ns
    >>>
    >>> width_to_lifetime(4.33e-4*eV)
    0.001520119980246514          # result again returned in ns
    >>>
    >>> width_to_lifetime(4.33e-10*MeV)/ps   # result converted to ps
    1.520119980246514
    """

    if Gamma < 0.:
        raise ValueError( 'Input provided, {0} <= 0!'.format(Gamma) )
    elif Gamma == 0:
        return float('inf')

    # Just need to first make sure that the width is in the standard unit MeV
    return hbar / float(Gamma / MeV)


def lifetime_to_width(tau):
    """
    Convert from a particle lifetime to a decay width.

    Parameters
    -----------
    tau : float > 0
        Particle lifetime, in the HEP standard time unit ns.

    Returns
    -------
    Particle decay width, in the HEP standard energy unit MeV.
    tau > 0: particle lifetime, in the HEP standard time unit ns.
    tau = 0: Infinity (float("inf")).
    tau < 0: an exception ValueError is raised.

    Examples
    --------
    Manipulation with no explicit usage of units:

    >>> lifetime_to_width(0.001520119980246514)   # result returned in MeV
    4.33e-10

    Manipulations with explicit units defined in the HEP system of units:

    >>> from hepunits.units import MeV, eV, ps   # handy module with units in the HEP system of units
    >>>
    >>> lifetime_to_width(0.001520119980246514*ns)
    4.33e-10          # result returned in MeV
    >>>
    >>> lifetime_to_width(1.520119980246514*ps)
    4.33e-10          # result again returned in MeV
    >>>
    >>> lifetime_to_width(1.520119980246514*ps)/eV   # result converted to eV
    0.000433
    """

    if tau < 0:
        raise ValueError( 'Input provided, {0} <= 0!'.format(tau) )
    elif tau == 0:
        return float('inf')

    # Just need to first make sure that the lifetime is in the standard unit ns
    return hbar / float(tau / ns)

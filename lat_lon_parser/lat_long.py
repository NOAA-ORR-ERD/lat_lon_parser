#!/usr/bin/env python

"""
Utilities for converting to/from floats to Sexagesimal:

degrees, minutes, seconds ...

"""
from __future__ import (unicode_literals,
                        absolute_import,
                        division,
                        print_function)

import math


def to_dec_deg(d=0, m=0, s=0, max=180):
    """
    DecDegrees = to_dec_deg(d=0, m=0, s=0)

    converts degrees, minutes, seconds to decimal degrees
    (returned as a float).
    """
    if not (0 <= m <= 60 and 0 <= s <= 60):
        raise ValueError("Minutes and seconds have to be between 0 and 60")

    if abs(d) > max:
        raise ValueError("Degrees have to be between -180 and 180")

    if d != int(d) and (m != 0 or s != 0):
        raise ValueError("degrees cannot have fraction unless both minutes"
                         "and seconds are zero")

    if m != int(m) and s != 0:
        raise ValueError("minutes cannot have fraction unless seconds "
                         "are zero")

    return math.copysign(abs(d) + m / 60 + s / 3600, d)


def to_deg_min(DecDegrees):
    """
    Converts from decimal (binary float) degrees to:
      Degrees, Minutes
    """
    degrees, remainder = divmod(abs(DecDegrees), 1)

    # float to preserve -0.0
    return math.copysign(degrees, DecDegrees), remainder * 60


def to_deg_min_sec(DecDegrees):
    """
    Converts from decimal (binary float) degrees to:
      Degrees, Minutes, Seconds
    """
    degrees, remainder = divmod(round(abs(DecDegrees), 9), 1)
    minutes, remainder = divmod(round(remainder * 60, 9), 1)

    # float to preserve -0.0
    return math.copysign(degrees, DecDegrees), minutes, remainder * 60


def to_str_dec_deg(d=0, m=0, s=0):
    Degrees = to_dec_deg(d, m, s)
    return to_str(Degrees)


def to_str_deg_min(DecDegrees):
    (Degrees, Minutes) = to_deg_min(DecDegrees)
    return to_str(Degrees, Minutes)


def to_str_deg_min_sec(DecDegrees):
    (deg, min, sec) = to_deg_min_sec(DecDegrees)
    return to_str(deg, min, sec)


def to_str(deg, min=None, sec=None):
    """
    Convert to string form

    :param deg: degrees value
    :param min=None: minutes value
    :param sec=None: seconds value
    """
    if min is None and sec is None:
        s = "{:.6f}\xb0".format(deg)
    elif sec is None:
        s = "{:.0f}\xb0 {:.3f}'".format(deg, min)
    else:
        s = "{:.0f}\xb0 {:.0f}' {:.2f}\"".format(deg, min, sec)
    return s

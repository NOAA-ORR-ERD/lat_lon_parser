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
import struct

# These specialzed float functions (and others)
# are to distinguish between -0 and 0.
# Needed to avoid results like: 20degrees, 60 minutes


def signbit(value):
    """
    Test whether the sign bit of the given floating-point value is
    set.  If it is set, this generally means the given value is
    negative.  However, this is not the same as comparing the value
    to C{0.0}.  For example:

    >>> NEGATIVE_ZERO < 0.0
    False

    since negative zero is numerically equal to positive zero.  But
    the sign bit of negative zero is indeed set:

    >>> signbit(NEGATIVE_ZERO)
    True
    >>> signbit(0.0)
    False

    @type  value: float
    @param value: a Python (double-precision) float value

    @rtype:  bool
    @return: C{True} if the sign bit of C{value} is set;
             C{False} if it is not set.

    signbit and doubleToRawLongBits
    are from Martin Jansche:

    http://symptotic.com/mj/code.html  (MIT license).

    This is required to capture the difference between -0.0 and 0.0, which is
    useful if someone wants to convert a latitude or longitude like:
    -0.0degrees, 34minutes to  0d34'00"S

    """
    return (doubleToRawLongBits(value) >> 63) == 1


def doubleToRawLongBits(value):
    """
    @type  value: float
    @param value: a Python (double-precision) float value

    @rtype: long
    @return: the IEEE 754 bit representation (64 bits as a long integer)
             of the given double-precision floating-point value.
    """
    # pack double into 64 bits, then unpack as long int
    return struct.unpack(b'Q', struct.pack(b'd', value))[0]


def to_dec_deg(d=0, m=0, s=0, ustring=False, max=180):
    """
    DecDegrees = to_dec_deg(d=0, m=0, s=0)

    converts degrees, minutes, seconds to decimal degrees
    (returned as a float).
    """
    if m < 0 or s < 0:
        raise ValueError("Minutes and Seconds have to be positive")

    if m > 60.0 or s > 60.0:
        raise ValueError("Minutes and Seconds have to be between "
                         "-180 and 180")

    if abs(d) > max:
        raise ValueError("Degrees have to be between -180 and 180")

    if signbit(d):
        Sign = -1
        d = abs(d)
    else:
        Sign = 1

    deg_has_fract = bool(math.modf(d)[0])
    min_has_fract = bool(math.modf(m)[0])

    if deg_has_fract and (m != 0.0 or s != 0.0):
        raise ValueError("degrees cannot have fraction unless both minutes"
                         "and seconds are zero")

    if min_has_fract and s != 0.0:
        raise ValueError("minutes cannot have fraction unless seconds "
                         "are zero")

    DecDegrees = Sign * (d + m / 60.0 + s / 3600.0)

    if ustring:
        return u"%.6f\xb0" % (DecDegrees)
    else:
        return DecDegrees


def to_deg_min(DecDegrees, ustring=False):
    """
    Converts from decimal (binary float) degrees to:
      Degrees, Minutes

    If the optional parameter: "ustring" is True,
    a Unicode string is returned

    """
    if signbit(DecDegrees):
        Sign = -1
        DecDegrees = abs(DecDegrees)
    else:
        Sign = 1

    Degrees = int(DecDegrees)

    # add a tiny bit then round to avoid binary rounding issues
    DecMinutes = round((DecDegrees - Degrees + 1e-14) * 60, 10)

    if ustring:
        if Sign == 1:
            return u"%i\xb0 %.3f'" % (Degrees, DecMinutes)
        else:
            return u"-%i\xb0 %.3f'" % (Degrees, DecMinutes)
    else:
        # float to preserve -0.0
        return (Sign * float(Degrees), DecMinutes)


def to_deg_min_sec(DecDegrees, ustring=False):
    """
    Converts from decimal (binary float) degrees to:
      Degrees, Minutes, Seconds

    If the optional parameter: "ustring" is True,
    a unicode string is returned

    """
    if signbit(DecDegrees):
        Sign = -1
        DecDegrees = abs(DecDegrees)
    else:
        Sign = 1

    Degrees = int(DecDegrees)

    # add a tiny bit to avoid rounding issues
    DecMinutes = (DecDegrees - Degrees + 1e-14) * 60

    Minutes = int(DecMinutes)
    Seconds = round(((DecMinutes - Minutes) * 60), 10)

    if ustring:
        if Sign == 1:
            return u"%i\xb0 %i' %.2f\"" % (Degrees, Minutes, Seconds)
        else:
            return u"-%i\xb0 %i' %.2f\"" % (Degrees, Minutes, Seconds)
    else:
        return (Sign * float(Degrees), Minutes, Seconds)

.. image:: https://github.com/NOAA-ORR-ERD/lat_lon_parser/workflows/CI/badge.svg
  :target: https://github.com/NOAA-ORR-ERD/lat_lon_parser/actions?query=workflow%3ACI

.. image:: https://img.shields.io/pypi/v/lat-lon-parser.svg
  :target: https://pypi.org/project/lat-lon-parser/

.. image:: https://img.shields.io/pypi/pyversions/lat-lon-parser.svg
  :target: https://pypi.org/project/lat-lon-parser/

.. image:: https://img.shields.io/github/license/NOAA-ORR-ERD/lat_lon_parser
  :target: https://github.com/NOAA-ORR-ERD/lat_lon_parser/




##############
lat_lon_parser
##############

Code for parsing lat-long coordinates in "various" formats, and for converting between lat-long formats (e.g. decimal degrees to degrees-minutes-seconds)

Note: perhaps it would be better to integrate this with a more full featured lib like:

https://pypi.python.org/pypi/LatLon23

But that one does not seem to support parsing unknown formats at this point -- and it's GPL, and perhaps a little more complex and structured than it needs to be.

Parsing Latitude and Longitude strings
=======================================

Usage:
------

from lat_lon_parser import parse

.. code-block::

    In [12]: from lat_lon_parser import parse

    In [13]: parse("45° 12.6' W")
    Out[13]: -45.21


Formats supported:
------------------

Decimal degrees (easy)::

   23.43
   -45.21

Decimal Degrees with quadrant::

   23.43 N
   45.21 W

Or with spelled out::

   23.43 North
   45.21 West

(note that all of the cardinal directions are not case-sensitive)

Degrees, decimal minutes: (now it starts getting tricky!)::

  23° 25.800'
  -45° 12.600'

or::

  23 25.800'
  -45 12.600'

or::

  23° 25.8' N
  45° 12.6' West

Degrees, Minutes, Seconds: (really fun!!!)::

   23° 25' 48.0"
  -45° 12' 36.0"

or::

   23d 25' 48.0"
  -45d 12' 36.0"

or::

  23° 25' 48.0" North
  45° 12' 36.0" S

or -- lots of other combinations!

For a more complete list, see the tests

How it works:
-------------

This uses a pretty "stupid" algorithm -- it assumes that all formats will be something like:

[-][space] degrees [separator] minutes [separator] seconds [separator] [N[orth]|S[outh|E[ast]|W[est]]

But that actually is pretty darn robust!

If you have other formats you want to be able to parse, please contribute tests! -- And ideally a patch if the current code doesn't work.


Conversion to Latitude Longitude Formats
========================================

Also included is code to convert to other formats used for latitude and longitude:

- degrees
- degrees minutes
- degrees minutes seconds

Converting to numbers:
----------------------

Functions for returning tuples of numbers::

  >>> to_dec_deg(23, 12, 3)
  23.200833333333332
  >>> to_deg_min(34.1234)
  (34.0, 7.404)
  >>> to_deg_min_sec(34.1234)
  (34.0, 7, 24.24)


Converting to strings:
----------------------

Functions for converting to various string formats::

  >>> to_str_dec_deg(23, 12, 3)
  '23.200833°'
  >>> to_str_deg_min(2.345)
  "2° 20.700'"
  >>> to_str_deg_min_sec(-23.1234)
  '-23° 7\' 24.24"'

  >>> to_str(23.45)
  '23.450000°'
  >>> to_str(23, 45)
  "23° 45.000'"
  >>> to_str(23, 45, 6.7)
  '23° 45\' 6.70"'




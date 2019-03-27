##############
lat_lon_parser
##############

Code for parsing lat-long coordinates in "various" formats

Note: perhaps it would be better to integrate this with a more full featured lib like:

https://pypi.python.org/pypi/LatLon23

But that one does not seem to support parsing unknown formats at this point -- and it's GPL, and perhaps a littel more complex and structured than it needs to be.

Formats supported:
==================

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

Adding to the options:
======================

This uses a pretty "stupid" algorithm -- it assumes that all formats will be something like:

[-][space] degrees [separator] minutes [separator] seconds [separator] [N[orth]|S[outh|E[ast]|W[est]]

But that actually is pretty darn robust!

If you have other formats you want to be able to parse, please contribute tests! -- And ideally a patch if the current code doesn't work.




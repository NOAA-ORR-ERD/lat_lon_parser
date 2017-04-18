##############
lat_lon_parser
##############

Experimental code for parsing lat-long coordinates in "various" formats

Note: perhaps it would be better to integarte this with a more full featured lib like:

https://pypi.python.org/pypi/LatLon23

But that one does not seem to support parsing unknown formats

Formats supported:
==================

Decimal degrees (easy)::

   23.43
   -45.21

Decimal Degrees with quadrant::

   23.43 N
   45.21 W

Degrees, decimal minutes: (now it starts getting tricky!)::

  23° 25.800'
  -45° 12.600'

or::

  23 25.800'
  -45 12.600'

or::

  23° 25.8' N
  45° 12.6' W

Degrees, Minutes, Seconds: (really fun!!!)::

   23° 25' 48.0"
  -45° 12' 36.0"

or::

   23d 25' 48.0"
  -45d 12' 36.0"

or::

  23° 25' 48.0" N
  45° 12' 36.0" S

or -- lots of other combinations!

Adding to the options:
======================

This uses a pretty "stupid" algorithm -- it assumes that all formats will be something like:

degrees [separator] minutes [separator] seconds [separtor] [N|S|E|W]






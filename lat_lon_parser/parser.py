#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Code for parsing lat-long coordinates in "various" formats

formats supported:

Decimal degrees (easy):
   23.43
   -45.21

Decimal Degrees with quadrant:
   23.43 N
   45.21 W

Degrees, decimal minutes: (now it starts getting tricky!)
  23° 25.800'
  -45° 12.600'

  or

  23 25.800'
  -45 12.600'

  or

  23° 25.8' N
  45° 12.6' W

Degrees, Minutes, Seconds: (really fun!!!)

   23° 25' 48.0"
  -45° 12' 36.0"

  or

   23d 25' 48.0"
  -45d 12' 36.0"

  or

   23° 25' 48.0" N
  45° 12' 36.0" S

  or -- lots of other combinations!

  Warning: this is not testing for non-compliant strings
  -- it will let anything pass that follows one of the patterns:

  [-]num<any symbol>[W or E or N or S] :: decimal degrees

  [-]num<any symbol>num<any symbol>[W or E or N or S]:: degrees, decimal minutes

  [-]num <any symbol> num <any symbol> num <any symbol>[W or E or N or S]:: degrees, minutes, decimal seconds

  W or S will return a negative result
  W,E,N,S are not case-sensitive.

  "north, south, east, west" also work -- also not case sensitive.

  <any symbol> can be literally anything

"""
from __future__ import unicode_literals, absolute_import, division, print_function
from . import lat_long

# unit_conversion  # from: https://github.com/NOAA-ORR-ERD/PyNUCOS



# new test version -- much simpler
import re

def parse(string):
    """
    Attempts to parse a latitude or longitude string

    Returns the value in floating point degrees

    If parsing fails, it raises a ValueError

    NOTE: This is a naive brute-force approach. And it's quite accepting of
          non-compliant strings. But that may be a good thing
    """

    print("starting with:", string)
    orig_string = string

    string = string.strip().lower()
    # replace full cardinatl directions:
    string = string.replace('north', 'n')
    string = string.replace('south', 's')
    string = string.replace('east', 'e')
    string = string.replace('west', 'w')

    # change W and S to a negative value
    if string.endswith('w') or string.endswith('s'):
        negative = -1
    else:
        negative = 1
    negative = -1 if string.startswith("-") else negative
    string = string.lstrip("- ")

    # print("after sign stripping", string, negative)
    # get rid of everything that is not numbers
    string = re.sub(r"[^0-9.]", " ", string).strip()
    # print("after stripping non-numbers", string)

    try:
        parts = [float(part) for part in string.split()]
        # print("parts", parts)
        if parts:
            return negative * lat_long.to_dec_deg(*parts)
        else:
            raise ValueError()
    except ValueError:
        raise ValueError("%s is not a valid coordinate string" % orig_string)

# ######################
# below is the "old" version -- more complex and less excepting of random junk.
# still not totally sure which is the better way to go.

# # Some are multiple characters, can't be done with translate
# replace_list = [('DEG', "°"),
#                 ('D', "°"),
#                 ('\N{MASCULINE ORDINAL INDICATOR}', "°"),
#                 ('N', ""),  # these don't change anything
#                 ('E', ""),
#                 ('\N{PRIME}', "'"),  # the "proper" symbol for minutes
#                 ('\N{DOUBLE PRIME}', '"'),  # the "proper" symbol for seconds
#                 ]

# def parse(string):
#     """
#     Attempts to parse a latitude or longitude string

#     Returns the value in floating point degrees

#     If parsing fails, it raises a ValueError

#     NOTE: This is a naive brute-force approach.
#           I imagine someone that can make regular expressions dance could do better..
#     """
#     orig_string = string
#     # clean up the string:
#     string = string.strip().upper()  # uppercase everything, then fewer replace options
#     for swap in replace_list:
#         string = string.replace(*swap)

#     # change W and S to a negative value
#     if 'W' in string:
#         string = '-' + string.replace('W', '')
#     if 'S' in string:
#         string = '-' + string.replace('S', '')
#     try:  # are we done?
#         val = float(string)
#         return val
#     except ValueError:  # that didn't work, keep going.
#         pass

#     # not very robust in the face of multiple degree symbols, etc
#     # but very flexible and easy!

#     # All "legitimate" symbols replaced with space
#     string = string.replace('°', ' ')
#     string = string.replace('"', ' ')
#     string = string.replace("'", ' ')
#     try:
#         parts = [float(part) for part in string.split()]
#         return unit_conversion.LatLongConverter.ToDecDeg(*parts)
#     except ValueError:
#         raise

#     raise ValueError("%s is not a valid coordinate string" % orig_string)


if __name__ == "__main__":
    # print out all the forms that work
    print("All these forms work:")
    for string, val in test_values:
        print(string)
    print("And these don't:")
    for string in invalid_values:
        print(string)


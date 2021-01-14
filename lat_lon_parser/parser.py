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

  - num<any symbol>[W or E or N or S] :: decimal degrees

  - num<any symbol>num<any symbol>[W or E or N or S]:: degrees, decimal minutes

  - num <any symbol> num <any symbol> num <any symbol>[W or E or N or S]::
    degrees, minutes, decimal seconds

  W or S will return a negative result
  W,E,N,S are not case-sensitive.

  "north, south, east, west" also work -- also not case sensitive.

  <any symbol> can be literally anything

"""
from __future__ import (unicode_literals,
                        absolute_import,
                        division,
                        print_function)
from . import lat_long

import re


def parse(string):
    """
    Attempts to parse a latitude or longitude string

    Returns the value in floating point degrees

    If parsing fails, it raises a ValueError

    :param string: The string to parse
    "type string": str

    :returns: A float value representing degrees.
              negative for southern or western hemisphere or

    NOTE: This is a naive brute-force approach. And it's quite accepting of
          non-compliant strings. But that may be a good thing
    """

    # print("starting with:", string)
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

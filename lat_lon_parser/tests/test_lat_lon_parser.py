#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_lat_lon_parser
----------------------------------

Tests for `lat_lon_parser` module.
"""

from __future__ import unicode_literals, absolute_import, division, print_function

import pytest

from lat_lon_parser import parse

# note: tripple quotes strings to support both ' and " in the string
# test code
test_values = [# decimal degrees
               ('23.43', 23.43),
               ('-45.21', -45.21),
               ('23.43 N', 23.43),
               ('45.21 W', -45.21),
               ('23.43 E', 23.43),
               ('45.21 S', -45.21),
               ('23.43 n', 23.43),
               ('45.21 w', -45.21),
               ('23.43 e', 23.43),
               ('45.21 s', -45.21),

               # degrees, minutes
               ("""23° 25.800'""", 23.43),
               ("""-45° 12.600'""", -45.21),

               ("""23° 25.800""", 23.43),
               ("""-45° 12.600""", -45.21),

               ("""23° 25.800""", 23.43),
               ("""-45° 12.600'""", -45.21),

               ("""23°25.800\N{PRIME}""", 23.43),
               ("""-45°12.600\N{PRIME}""", -45.21),

               ("""23d25.800'""", 23.43),
               ("""-45deg12.600'""", -45.21),

               ("""23Deg25.800'""", 23.43),
               ("""-45D12.600'""", -45.21),

               # degrees, minutes, just space
               ("""23 25.0""", 23.416666666667),
               ("""-45 12.0""", -45.2),

               ("""23 25""", 23.416666666667),
               ("""-45 12""", -45.2),

               ("""23 25 N""", 23.416666666667),
               ("""45 12W""", -45.2),


               # degrees, minutes, seconds
               ("""23° 25' 48.0" N""", 23.43),
               ("""45° 12' 36.0" S""", -45.21),

               ("""23 25 48.0 N""", 23.43),
               ("""45 12 36.0 S""", -45.21),

               ("""23 25 48.0""", 23.43),
               ("""-45 12 36.0""", -45.21),
               ]

@pytest.mark.parametrize("string, value", test_values)
def test_parse(string, value):
    tol = 12
    assert round(parse(string), tol) == round(value, tol)

invalid_values = ["some_crap",
                  "23.43.2",
                  "23.43t",
                  "23.4 14.2",  # decimal in more than one field
                  """23.2d 14' 12.22" """,  # decimal in more than one field
                  ]

@pytest.mark.parametrize("string", invalid_values)
def test_parse_invalid(string):
    with pytest.raises(ValueError):
        parse(string)


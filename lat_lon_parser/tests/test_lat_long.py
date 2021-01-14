"""
tests for lat_long.py

This can be tricky to make sure the FP issues are addressed correctly
"""

from __future__ import (unicode_literals,
                        absolute_import,
                        division,
                        print_function)

from lat_lon_parser import lat_long

import pytest


class Test_SignBit():

    def test_Neg(self):
        assert lat_long.signbit(-5.0) is True

    def test_NegZero(self):
        assert lat_long.signbit(-0.0) is True

    def test_IntegerNeg(self):
        assert lat_long.signbit(-5) is True

    def test_Pos(self):
        assert lat_long.signbit(5.0) is False

    def test_PosZero(self):
        assert lat_long.signbit(0.0) is False

    def test_IntegerPos(self):
        assert lat_long.signbit(5) is False


class Test_LatLongErrors():

    def test_NegativeMinutes(self):
        with pytest.raises(ValueError):
            lat_long.to_dec_deg(30, -30)

    def test_NegativeSeconds(self):
        with pytest.raises(ValueError):
            lat_long.to_dec_deg(30, 30, -1)

    def test_TooBig(self):
        with pytest.raises(ValueError):
            lat_long.to_dec_deg(d=200)

    def test_TooNegative(self):
        with pytest.raises(ValueError):
            lat_long.to_dec_deg(d=-181)

    def test_TooBigMin(self):
        with pytest.raises(ValueError):
            lat_long.to_dec_deg(d=20, m=61)

    def test_TooBigSec(self):
        with pytest.raises(ValueError):
            lat_long.to_dec_deg(d=30, m=42, s=61)

    def test_DegFractAndMin(self):
        with pytest.raises(ValueError):
            lat_long.to_dec_deg(d=30.2, m=5, s=0)

    def test_DegFractAndSec(self):
        with pytest.raises(ValueError):
            lat_long.to_dec_deg(d=30.2, m=0, s=6.3)

    def test_MinFractAndSec(self):
        with pytest.raises(ValueError):
            lat_long.to_dec_deg(d=30, m=4.5, s=6)


class Test_LatLong:

    def test_DecDegrees(self):
        assert lat_long.to_dec_deg(30, 30) == 30.5

    def test_DecDegrees2(self):
        assert lat_long.to_dec_deg(30, 30, 30) == 30.508333333333333

    def test_DegMin(self):
        assert lat_long.to_deg_min(30.5)[0] == 30
        assert lat_long.to_deg_min(30.5)[1] == 30.0

    def test_MinusZeroDeg(self):
        assert lat_long.to_dec_deg(d=-0.0, m=20, s=20 == -0.33888888888888885)

    def test_BinaryProblem(self):
        assert lat_long.to_deg_min_sec(45.05) == (45, 3, 0.0)

    def test_DDString(self):
        d, m, s = 120, 30, 5
        assert lat_long.to_str_dec_deg(d, m, s) == "120.501389\xb0"

    def test_DDString2(self):
        d, m, s = -50, 30, 5
        assert lat_long.to_str_dec_deg(d, m, s) == "-50.501389\xb0"

    def test_DDString3(self):
        d, m, s = 0, 30, 0
        assert lat_long.to_str_dec_deg(d, m, s) == "0.500000\xb0"

    def test_DMString(self):
        d, m = 120, 45.5
        DecDeg = lat_long.to_dec_deg(d, m)
        assert lat_long.to_str_deg_min(DecDeg) == "120\xb0 45.500'"

    def test_DMString2(self):
        d, m = -120, 3
        DecDeg = lat_long.to_dec_deg(d, m)
        assert lat_long.to_str_deg_min(DecDeg) == "-120\xb0 3.000'"

    def test_DMSString(self):
        d, m, s = 120, 45, 15
        DecDeg = lat_long.to_dec_deg(d, m, s)
        assert lat_long.to_str_deg_min_sec(DecDeg) == "120\xb0 45' 15.00\""

    def test_DMSString2(self):
        d, m, s = -120, 3, 15
        DecDeg = lat_long.to_dec_deg(d, m, s)
        assert lat_long.to_str_deg_min_sec(DecDeg) == "-120\xb0 3' 15.00\""

    def test_DMtringZero(self):
        d, m, s = -0.0, 3, 0
        DecDeg = lat_long.to_dec_deg(d, m, s)
        assert lat_long.to_str_deg_min(DecDeg) == """-0\xb0 3.000'"""

    def test_DMSStringZero(self):
        d, m, s = -0.0, 3, 15
        DecDeg = lat_long.to_dec_deg(d, m, s)
        assert lat_long.to_str_deg_min_sec(DecDeg) == '''-0\xb0 3' 15.00"'''

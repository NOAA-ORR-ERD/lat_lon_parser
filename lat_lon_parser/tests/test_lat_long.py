"""
tests for lat_long.py

This can be tricky to make sure the FP issues are addressed

fixme -- convert to pur pytest some day...
"""
import unittest
from lat_lon_parser import lat_long


class testSignBit():

    def testNeg(self):
        lat_long.signbit(-5.0) is True

    def testNegZero(self):
        lat_long.signbit(-0.0) is True

    def testIntegerNeg(self):
        lat_long.signbit(-5) is True

    def testPos(self):
        lat_long.signbit(5.0) is False

    def testPosZero(self):
        lat_long.signbit(0.0) is False

    def testIntegerPos(self):
        lat_long.signbit(5) is False


class testLatLongErrors():

    def testNegativeMinutes(self):
        self.assertRaises(ValueError, lat_long.to_dec_deg, 30, -30)

    def testNegativeSeconds(self):
        self.assertRaises(ValueError, lat_long.to_dec_deg, 30, 30, -1)

    def testTooBig(self):
        self.assertRaises(ValueError, lat_long.to_dec_deg, d=200)

    def testTooNegative(self):
        self.assertRaises(ValueError, lat_long.to_dec_deg, d=-181)

    def testTooBigMin(self):
        self.assertRaises(ValueError, lat_long.to_dec_deg, d=20, m=61)

    def testTooBigSec(self):
        self.assertRaises(ValueError, lat_long.to_dec_deg, d=30, m=42, s=61)

    def testDegFractAndMin(self):
        self.assertRaises(ValueError, lat_long.to_dec_deg, d=30.2, m=5, s=0)

    def testDegFractAndSec(self):
        self.assertRaises(ValueError, lat_long.to_dec_deg, d=30.2, m=0, s=6.3)

    def testMinFractAndSec(self):
        self.assertRaises(ValueError, lat_long.to_dec_deg, d=30, m=4.5, s=6)


class testLatLong(unittest.TestCase):

    def testDecDegrees(self):
        self.assertEqual(lat_long.to_dec_deg(30, 30), 30.5)

    def testDecDegrees2(self):
        self.assertAlmostEqual(lat_long.to_dec_deg(30, 30, 30), 30.50833333333)

    def testDegMin(self):
        self.assertEqual(lat_long.to_deg_min(30.5)[0], 30)
        self.assertEqual(lat_long.to_deg_min(30.5)[1], 30.0)

    def testMinusZeroDeg(self):
        self.assertEqual(lat_long.to_dec_deg(d=-0.0, m=20, s=20), -0.33888888888888885)

    def testBinaryProblem(self):
        self.assertEqual(lat_long.to_deg_min_sec(45.05), (45, 3, 0.0))

    def testDDString(self):
        d, m, s = 120, 30, 5
        self.assertEqual(lat_long.to_dec_deg(d, m, s, ustring=True),
                         u"120.501389\xb0")

    def testDDString2(self):
        d, m, s = -50, 30, 5
        self.assertEqual(lat_long.to_dec_deg(d, m, s, ustring=True),
                         u"-50.501389\xb0")

    def testDDString3(self):
        d, m, s = 0, 30, 0
        self.assertEqual(lat_long.to_dec_deg(d, m, s, ustring=True),
                         u"0.500000\xb0")

    def testDMString(self):
        d, m = 120, 45.5
        DecDeg = lat_long.to_dec_deg(d, m)
        self.assertEqual(lat_long.to_deg_min(DecDeg, True),
                         u"120\xb0 45.500'")

    def testDMString2(self):
        d, m = -120, 3
        DecDeg = lat_long.to_dec_deg(d, m)
        self.assertEqual(lat_long.to_deg_min(DecDeg, True),
                         u"-120\xb0 3.000'")

    def testDMSString(self):
        d, m, s = 120, 45, 15
        DecDeg = lat_long.to_dec_deg(d, m, s)
        self.assertEqual(lat_long.to_deg_min_sec(DecDeg, True),
                         u"120\xb0 45' 15.00\"")

    def testDMSString2(self):
        d, m, s = -120, 3, 15
        DecDeg = lat_long.to_dec_deg(d, m, s)
        self.assertEqual(lat_long.to_deg_min_sec(DecDeg, True),
                         u"-120\xb0 3' 15.00\"")

    def testDMtringZero(self):
        d, m, s = -0.0, 3, 0
        DecDeg = lat_long.to_dec_deg(d, m, s)
        self.assertEqual(lat_long.to_deg_min(DecDeg, True),
                         u"""-0\xb0 3.000'""")

    def testDMSStringZero(self):
        d, m, s = -0.0, 3, 15
        DecDeg = lat_long.to_dec_deg(d, m, s)
        self.assertEqual(lat_long.to_deg_min_sec(DecDeg, True),
                         u'''-0\xb0 3' 15.00"''')

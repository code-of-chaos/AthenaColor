# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library

# Custom Packages
import AthenaColor.Objects.Color.ColorObjectConversion
from AthenaColor import *

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ColorObjects_RGB(unittest.TestCase):
    @staticmethod
    def CreateColor(r=127,g=127,b=127) -> RGB:
        return RGB(r,g,b)

    def dunder_tests(self,equal,notEqual,greater,less,greaterEqual,lessEqual):
        color = self.CreateColor()
        self.assertEqual(       color, equal)       # color == equal
        self.assertNotEqual(    color, notEqual)    # color != notEqual
        self.assertGreater(     color, greater)     # color >  greater
        self.assertLess(        color, less)        # color <  less
        self.assertGreaterEqual(color, greaterEqual)# color >= greaterEqual
        self.assertLessEqual(   color, lessEqual)   # color <= lessEqual

    # ------------------------------------------------------------------------------------------------------------------
    # - BASIC Color Object Testing -
    # ------------------------------------------------------------------------------------------------------------------
    def test_repr(self):
        self.assertEqual(repr(self.CreateColor()),"RGB(r=127,g=127,b=127)")

    def test_str(self):
        self.assertEqual(str(self.CreateColor()),"127;127;127")

    def test_dunder_comparison_tuples(self):
        self.dunder_tests(
            equal=(127,127,127),
            notEqual=(0,0,0),
            greater=(0,0,0),
            less=(200,200,200),
            greaterEqual=(0,0,127),
            lessEqual=(127,128,129)
        )

    def test_dunder_comparison_integers(self):
        self.dunder_tests(
            equal=127,
            notEqual=0,
            greater=0,
            less=200,
            greaterEqual=0,
            lessEqual=128
        )

    def test_dunder_comparison_RGB(self):
        self.dunder_tests(
            equal=          RGB(127,127,127),
            notEqual=       RGB(0,0,0),
            greater=        RGB(0,0,0),
            less=           RGB(200,200,200),
            greaterEqual=   RGB(0,0,127),
            lessEqual=      RGB(127,128,129)
        )

    def test_dunder_comparison_HEX(self):
        self.dunder_tests(
            equal=          HEX("#7F7F7F"),
            notEqual=       HEX("#000000"),
            greater=        HEX("#000000"),
            less=           HEX("#C8C8C8"),
            greaterEqual=   HEX("#00007F"),
            lessEqual=      HEX("#7F8081")
        )

    def test_dunder_comparison_HSL(self):
        self.dunder_tests(
            equal=          HSL(0,0,.498),
            notEqual=       HSL(0,0,0),
            greater=        HSL(0,0,0),
            less=           HSL(0,0,.784),
            greaterEqual=   HSL(240,1,.249),
            lessEqual=      HSL(210,.008,.502)
        )

    def test_dunder_comparison_HSV(self):
        self.dunder_tests(
            equal=          HSV(0,0,.498),
            notEqual=       HSV(0,0,0),
            greater=        HSV(0,0,0),
            less=           HSV(0,0,.784),
            greaterEqual=   HSV(240,1,.498),
            lessEqual=      HSV(210,.016,.506),
        )

    def test_dunder_comparison_CMYK(self):
        self.dunder_tests(
            equal=          CMYK(0,0,0,.502),
            notEqual=       CMYK(0,0,0,0),
            greater=        CMYK(0,0,0,.9),
            less=           CMYK(0,0,0,0),
            greaterEqual=   CMYK(1,1,0,.505),
            lessEqual=      CMYK(.02,.01,0,.49),
        )

    def test_dunder_math_tuple(self):
        self.assertEqual(
            self.CreateColor() - (500,500,500),
            RGB(r=0, g=0, b=0)
        )
        self.assertEqual(
            self.CreateColor() + (500,500,500),
            RGB(r=255, g=255, b=255)
        )
        self.assertEqual(
            self.CreateColor() / (3,3,3),
            RGB(r=42, g=42, b=42)
        )
        self.assertEqual(
            self.CreateColor() // (4,4,4),
            RGB(r=31, g=31, b=31)
        )
        self.assertEqual(
            self.CreateColor() * (2,2,2),
            RGB(r=254, g=254, b=254)
        )
        self.assertEqual(
            self.CreateColor(3,3,3) ** (4,4,4),
            RGB(r=81, g=81, b=81)
        )
        self.assertEqual(
            self.CreateColor() % (4,4,4),
            RGB(r=3, g=3, b=3)
        )
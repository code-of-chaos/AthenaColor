# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library
from AthenaColor import *

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ColorObjects_HEX(unittest.TestCase):
    @staticmethod
    def CreateColor(hex_str = "#204080") -> HEX:
        return HEX(hex_str)

    # ------------------------------------------------------------------------------------------------------------------
    # - BASIC Color Object Testing -
    # ------------------------------------------------------------------------------------------------------------------
    # noinspection PyTypeChecker
    def test_input(self):
        with self.assertRaises(AssertionError):
            HEX(1)
        with self.assertRaises(AssertionError):
            HEX(b"#123456")
        with self.assertRaises(ValueError):
            HEX("#123456789")
        with self.assertRaises(AssertionError):
            HEX(**{"hex_value":1})
        with self.assertRaises(TypeError):
            HEX(**{"hex_value":"#123456","a":1})

    def test_repr(self):
        self.assertEqual(repr(self.CreateColor()),"HEX(r=32,g=64,b=128)")

    def test_str(self):
        self.assertEqual(str(self.CreateColor()),"#204080")

    def test_dunder_tuples(self):
        color = self.CreateColor()
        # Comparison
        self.assertEqual(       color, (32,64,128))
        self.assertNotEqual(    color, (0,0,0))
        self.assertGreater(     color, (0,0,0))
        self.assertLess(        color, (255,255,255))
        self.assertGreaterEqual(color, (0,0,128))
        self.assertLessEqual(   color, (255,255,128))

        # math
        self.assertEqual(
            color + (32,64,128),
            HEX("#4080FF")
        )
        self.assertEqual(
            color - (32,64,128),
            HEX("#000000")
        )
        self.assertEqual(
            color * (4,3,2),
            HEX("#80C0FF")
        )
        self.assertEqual(
            color / (4,3,2),
            HEX("#081540")
        )
        self.assertEqual(
            color // (9,7,5),
            HEX("#030919")
        )
        self.assertEqual(
            color ** (2,2.5,1),
            HEX("#FFFF80")
        )
        self.assertEqual(
            color % (9,7,5),
            HEX("#050103")
        )

    def test_dunder_RGB(self):
        color = self.CreateColor()
        # Comparison
        self.assertEqual(       color, RGB(32,64,128))
        self.assertNotEqual(    color, RGB(0,0,0))
        self.assertGreater(     color, RGB(0,0,0))
        self.assertLess(        color, RGB(255,255,255))
        self.assertGreaterEqual(color, RGB(0,0,128))
        self.assertLessEqual(   color, RGB(255,255,128))

        # math
        self.assertEqual(
            color + RGB(32, 64, 128),
            RGB(64, 128, 255)
        )
        self.assertEqual(
            color - RGB(32, 64, 128),
            RGB(0, 0, 0)
        )
        self.assertEqual(
            color * RGB(4, 3, 2),
            RGB(128, 192, 255)
        )
        self.assertEqual(
            color / RGB(4, 3, 2),
            RGB(8, 21, 64)
        )
        self.assertEqual(
            color // RGB(9, 7, 5),
            RGB(3, 9, 25)
        )
        self.assertEqual(
            color ** RGB(2, 2, 1),
            RGB(255, 255, 128)
        )
        self.assertEqual(
            color % RGB(9, 7, 5),
            RGB(5, 1, 3)
        )

    def test_dunder_HEX(self):
        color = self.CreateColor()
        # Comparison
        self.assertEqual(       color, HEX("#204080"))
        self.assertNotEqual(    color, HEX("#000000"))
        self.assertGreater(     color, HEX("#000000"))
        self.assertLess(        color, HEX("#FFFFFF"))
        self.assertGreaterEqual(color, HEX("#000000"))
        self.assertLessEqual(   color, HEX("#FFFF80"))

        # math
        self.assertEqual(
            color + HEX("#abcdef"),
            RGB(203,255,255)
        )
        self.assertEqual(
            color - HEX("#00bb55"),
            RGB(32,0,43)
        )
        self.assertEqual(
            color * HEX("#020302"),
            RGB(64,192,255)
        )
        self.assertEqual(
            color / HEX("#020302"),
            RGB(16,21,64)
        )
        self.assertEqual(
            color // HEX("#050709"),
            RGB(6,9,14)
        )
        self.assertEqual(
            color ** HEX("#020101"),
            RGB(255,64,128)
        )
        self.assertEqual(
            color % HEX("#121664"),
            RGB(14,20,28)
        )

    def test_dunder_HSL(self):
        color = self.CreateColor()
        # Comparison
        self.assertEqual(       color, HSL(220,0.6,.314))
        self.assertNotEqual(    color, HSL(0,0,0))
        self.assertGreater(     color, HSL(0,0,0))
        self.assertLess(        color, HSL(359,1,1))
        self.assertGreaterEqual(color, HSL(220,0,0))
        self.assertLessEqual(   color, HSL(180.0,1.0,0.563))

        # math
        self.assertEqual(
            color + HSL(0.125,0.5,0.1),
            RGB(70,77,141)
        )
        self.assertEqual(
            color - HSL(0.125,0.5,0.1),
            RGB(0,51,115)
        )
        self.assertEqual(
            color * HSL(0,0,0.01),
            RGB(96,192,255)
        )
        self.assertEqual(
            color / HSL(0,0,0.01),
            RGB(10,21,42)
        )
        self.assertEqual(
            color // HSL(0,0,0.01),
            RGB(10,21,42)
        )
        self.assertEqual(
            color ** HSL(0,0,0.006),
            RGB(255,255,255)
        )
        self.assertEqual(
            color % HSL(0,0.2,0.1),
            RGB(1,4,8)
        )

    def test_dunder_HSV(self):
        color = self.CreateColor()
        # Comparison
        self.assertEqual(       color, HSV(220,0.75,.502))
        self.assertNotEqual(    color, HSV(0,0,0))
        self.assertGreater(     color, HSV(0,0.0,0.063))
        self.assertLess(        color, HSV(0,0.0,1.0))
        self.assertGreaterEqual(color, HSV(0.0,0.5,0.125))
        self.assertLessEqual(   color, HSV(180.0,0.875,1.0))

        # math
        self.assertEqual(
            color + HSV(0,0.2,0.1),
            RGB(58,84,148)
        )
        self.assertEqual(
            color - HSV(0,0.2,0.1),
            RGB(6,44,108)
        )
        self.assertEqual(
            color * HSV(0,0,0.01),
            RGB(96,192,255)
        )
        self.assertEqual(
            color / HSV(0,0,0.01),
            RGB(10,21,42)
        )
        self.assertEqual(
            color // HSV(0,0,0.01),
            RGB(10,21,42)
        )
        self.assertEqual(
            color ** HSV(0,0,0.006),
            RGB(255,255,255)
        )
        self.assertEqual(
            color % HSV(0,0.2,0.1),
            RGB(6,4,8)
        )

    def test_dunder_CMYK(self):
        color = self.CreateColor()
        # Comparison
        self.assertEqual(       color, CMYK(0.75,0.5,0.0,0.498))
        self.assertNotEqual(    color, CMYK(1.0,1.0,1.0,1.0))
        self.assertGreater(     color, CMYK(1.0,1.0,1.0,1.0))
        self.assertLess(        color, CMYK(0.0,0.0,0.0,0.0))
        self.assertGreaterEqual(color, CMYK(0.0,0.0,0.0,0.875))
        self.assertLessEqual(   color, CMYK(0.5,0.0,0.0,0.498))

        # math
        self.assertEqual(
            color + CMYK(.9,.9,.75,.1),
            RGB(55,87,185)
        )
        self.assertEqual(
            color - CMYK(.9,.9,.75,.1),
            RGB(9,41,71)
        )
        self.assertEqual(
            color * CMYK(.9,.9,.75,.9),
            RGB(96,192,255)
        )
        self.assertEqual(
            color / CMYK(.9,.9,.75,.9),
            RGB(10,21,21)
        )
        self.assertEqual(
            color // CMYK(.9,.9,.75,.9),
            RGB(10,21,21)
        )
        self.assertEqual(
            color ** CMYK(1,0,0,0),
            RGB(1,255,255)
        )
        self.assertEqual(
            color % CMYK(0.5,0.5,0.5,0),
            RGB(32,64,0)
        )
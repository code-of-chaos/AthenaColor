# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library
from AthenaColor import *

# Custom Packages
from AthenaColor.AthenaLib.StrictAnnotated import StrictError

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ColorObjects_HSV(unittest.TestCase):
    @staticmethod
    def CreateColor(h=.25,s=.5,v=.75) -> HSV:
        return HSV(h,s,v)

    # ------------------------------------------------------------------------------------------------------------------
    # - BASIC Color Object Testing -
    # ------------------------------------------------------------------------------------------------------------------
    # noinspection PyTypeChecker
    def test_input(self):
        with self.assertRaises(StrictError):
            HSV("a","b","c")
        with self.assertRaises(StrictError):
            HSV(b"a",b"b",b"c")
        with self.assertRaises(StrictError):
            HSV(**{"h":"a","s":"b","v":"c"})
        with self.assertRaises(TypeError):
            HSV(**{"h":1,"s":2,"v":3,"x":"n"})

    def test_repr(self):
        self.assertEqual(repr(self.CreateColor()),"HSV(h=0.25,s=0.5,v=0.75)")

    def test_str(self):
        self.assertEqual(str(self.CreateColor()),"0.25;0.5;0.75")

    def test_dunder_tuples(self):
        color = self.CreateColor()
        # Comparison
        self.assertEqual(       color, (.25,.5,0.75))
        self.assertNotEqual(    color, (0,0,0))
        self.assertGreater(     color, (0,0,0))
        self.assertLess(        color, (1,1,1))
        self.assertGreaterEqual(color, (0,0,0.75))
        self.assertLessEqual(   color, (.25,1,1))

        # math
        self.assertEqual(
            color + (.25,.25,.25),
            HSV(.5,.75,1.0)
        )
        self.assertEqual(
            color - (.25,.5,0.75),
            HSV(0.0,0.0,0.0)
        )
        self.assertEqual(
            color * (.1,.5,0.75),
            HSV(0.025,0.25,0.562)
        )
        self.assertEqual(
            color / (.1,.5,0.75),
            HSV(2.5,1.0,1.0)
        )
        self.assertEqual(
            color // (.1,.5,0.75),
            HSV(2.0,1.0,1.0)
        )
        self.assertEqual(
            color ** (.1,.5,0.75),
            HSV(0.871,0.707,0.806)
        )
        self.assertEqual(
            color % (.1,.5,0.75),
            HSV(0.05,0.0,0.0)
        )

    def test_dunder_RGB(self):
        color = self.CreateColor()

        # Comparison
        self.assertEqual(       HSV(0.0, 0.497, 0.749), RGB(191,96,96))
        self.assertNotEqual(    color, RGB(0,0,0))
        self.assertGreater(     color, RGB(0,0,0))
        self.assertLess(        color, RGB(255, 4, 0))
        self.assertGreaterEqual(color, RGB(191,191,191))
        self.assertLessEqual(   color, RGB(204,4,0))

        # math
        self.assertEqual(
            color + RGB(32, 64, 128),
            HSV(220.25,1,1)
        )
        self.assertEqual(
            color - RGB(32, 64, 128),
            HSV(0,0,0.248)
        )
        self.assertEqual(
            color * RGB(4, 3, 2),
            HSV(7.5,0.25,0.012)
        )
        self.assertEqual(
            color / RGB(4, 3, 2),
            HSV(0.008,1.0,1)
        )
        self.assertEqual(
            color // RGB(9, 7, 5),
            HSV(0.0,1.0,1)
        )
        self.assertEqual(
            color ** RGB(2, 2, 1),
            HSV(0.0,0.707,0.998)
        )
        self.assertEqual(
            color % RGB(9, 7, 5),
            HSV(0.25,0.056,0.015)
        )

    def test_dunder_HEX(self):
        color = self.CreateColor()
        # Comparison
        self.assertEqual(       HSV(0.0, 0.497, 0.749), HEX("#bf6060"))
        self.assertNotEqual(    color, HEX("#000000"))
        self.assertGreater(     color, HEX("#000000"))
        self.assertLess(        color, HEX("#ff0400"))
        self.assertGreaterEqual(color, HEX("#bfbfbf"))
        self.assertLessEqual(   color, HEX("#cc0400"))

        # math
        self.assertEqual(
            color + HEX("#abcdef"),
            HSV(210.25,0.785,1)
        )
        self.assertEqual(
            color - HEX("#00bb55"),
            HSV(0,0,0.017)
        )
        self.assertEqual(
            color * HEX("#020302"),
            HSV(30.0,0.167,0.009)
        )
        self.assertEqual(
            color / HEX("#020302"),
            HSV(0.002,1,1)
        )
        self.assertEqual(
            color // HEX("#050709"),
            HSV(0.0,1.0,1)
        )
        self.assertEqual(
            color ** HEX("#020101"),
            HSV(1.0,0.707,0.998)
        )
        self.assertEqual(
            color % HEX("#121664"),
            HSV(0.25,0.5,0.358)
        )

    def test_dunder_HSL(self):
        color = self.CreateColor()
        # Comparison
        self.assertEqual(       HSV(0.0, 0.497, 0.749), HSL(0.0, 0.426, 0.563))
        self.assertNotEqual(    color, HSL(0,0,0))
        self.assertGreater(     color, HSL(0,0,0))
        self.assertLess(        color, HSL(180.0, 1.0, 0.5))
        self.assertGreaterEqual(color, HSL(220,0,0))
        self.assertLessEqual(   color, HSL(180.0,1.0,0.563))

        # math
        self.assertEqual(
            color + HSL(0.125,0.5,0.1),
            HSV(0.25,1,0.899)
        )
        self.assertEqual(
            color - HSL(0.125,0.5,0.1),
            HSV(0.25,0,0.601)
        )
        self.assertEqual(
            color * HSL(0,0,0.01),
            HSV(0.0,0.0,0.009)
        )
        self.assertEqual(
            color / HSL(180,1,.01),
            HSV(0.001,0.5,1)
        )
        self.assertEqual(
            color // HSL(180,1,.01),
            HSV(0.0,0.0,1)
        )
        self.assertEqual(
            color ** HSL(0,0,0.006),
            HSV(1.0, 1.0, 0.998)
        )
        self.assertEqual(
            color % HSL(180,0.2,0.1),
            HSV(0.25,0.145,0.018)
        )

    def test_dunder_HSV(self):
        color = self.CreateColor()
        # Comparison
        self.assertEqual(       color, HSV(.25, .5, 0.75))
        self.assertNotEqual(    color, HSV(0, 0, 0))
        self.assertGreater(     color, HSV(0, 0, 0))
        self.assertLess(        color, HSV(1, 1, 1))
        self.assertGreaterEqual(color, HSV(0, 0, 0.75))
        self.assertLessEqual(   color, HSV(.25, 1, 1))

        # math
        self.assertEqual(
            color + HSV(.25, .25, .25),
            HSV(.5, .75, 1.0)
        )
        self.assertEqual(
            color - HSV(.25, .5, 0.75),
            HSV(0.0, 0.0, 0.0)
        )
        self.assertEqual(
            color * HSV(.1, .5, 0.75),
            HSV(0.025, 0.25, 0.562)
        )
        self.assertEqual(
            color / HSV(.1, .5, 0.75),
            HSV(2.5, 1.0, 1.0)
        )
        self.assertEqual(
            color // HSV(.1, .5, 0.75),
            HSV(2.0, 1.0, 1.0)
        )
        self.assertEqual(
            color ** HSV(.1, .5, 0.75),
            HSV(0.871, 0.707, 0.806)
        )
        self.assertEqual(
            color % HSV(.1, .5, 0.75),
            HSV(0.05, 0.0, 0.0)
        )

    def test_dunder_CMYK(self):
        color = self.CreateColor()
        # Comparison
        self.assertEqual(       HSV(0.0, 0.497, 0.749), CMYK(0.0, 0.497, 0.497, 0.251))
        self.assertNotEqual(    color, CMYK(1.0,1.0,1.0,1.0))
        self.assertGreater(     color, CMYK(1.0,1.0,1.0,1.0))
        self.assertLess(        color, CMYK(1.0, 0.0, 0.0, 0.0))
        self.assertGreaterEqual(color, CMYK(0.0,0.0,0.0,0.875))
        self.assertLessEqual(   color, CMYK(1.0, 0.0, 0.0, 0.0))

        # math
        self.assertEqual(
            color + CMYK(.9,.9,.75,.1),
            HSV(240.25,1,0.974)
        )
        self.assertEqual(
            color - CMYK(.9,.9,.75,.1),
            HSV(0,0,0.526)
        )
        self.assertEqual(
            color * CMYK(.9,.9,.75,.9),
            HSV(60.0,0.25,0.018)
        )
        self.assertEqual(
            color / CMYK(.9,.9,.75,.9),
            HSV(0.001,1.0,1)
        )
        self.assertEqual(
            color // CMYK(.9,.9,.75,.9),
            HSV(0.0,1.0,1)
        )
        self.assertEqual(
            color ** CMYK(1,0,0,0),
            HSV(0.0,0.5,0.75)
        )
        self.assertEqual(
            color % CMYK(0.75,0.25,0.25,0.15),
            HSV(0.25,0.5,0.111)
        )
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
# noinspection PyTypeChecker
class ColorObjects_HSL(unittest.TestCase):
    @staticmethod
    def CreateColor(h=60,s=.5,l=.75) -> HSL:
        return HSL(h,s,l)

    # ------------------------------------------------------------------------------------------------------------------
    # - BASIC Color Object Testing -
    # ------------------------------------------------------------------------------------------------------------------
    # noinspection PyTypeChecker
    def test_input(self):
        with self.assertRaises(TypeError):
            HSL(**{"h":1,"s":2,"l":3,"x":"n"})

    def test_repr(self):
        self.assertEqual(repr(self.CreateColor()),"HSL(h=60,s=0.5,l=0.75)")

    def test_str(self):
        self.assertEqual(str(self.CreateColor()),"60;0.5;0.75")

    # noinspection PyTypeChecker
    def test_dunder_tuples(self):
        color = self.CreateColor()
        # Comparison
        self.assertEqual(       color, (60,.5,0.75))
        self.assertNotEqual(    color, (0,0,0))
        self.assertGreater(     color, (0,0,0))
        self.assertLess(        color, (180,1,1))
        self.assertGreaterEqual(color, (0,0,0.75))
        self.assertLessEqual(   color, (180,.5,1))

        # math
        self.assertEqual(
            round(color + (.25,.25,.25),3),
            HSL(60.25,0.75,1.0)
        )
        self.assertEqual(
            round(color - (.25,.5,0.75),3),
            HSL(59.75,0.0,0.0)
        )
        self.assertEqual(
            round(color * (.1,.5,0.75),3),
            HSL(6.0,0.25,0.562)
        )
        self.assertEqual(
            round(color / (.1,.5,0.75),3),
            HSL(360,1.0,1.0)
        )
        self.assertEqual(
            round(color // (.1,.5,0.75),3),
            HSL(360,1.0,1.0)
        )
        self.assertEqual(
            round(color ** (.1,.5,0.75),3),
            HSL(1.506,0.707,0.806)
        )
        self.assertEqual(
            round(color % (.1,.5,0.75),3),
            HSL(0.1, 0.0, 0.0)
        )

    def test_dunder_RGB(self):
        color = self.CreateColor()

        # Comparison
        self.assertEqual(       HSL(60.0, 0.5, 0.749), RGB(223, 223, 159))
        self.assertNotEqual(    color, RGB(0,0,0))
        self.assertGreater(     color, RGB(0,0,0))
        self.assertLess(        color, RGB(153, 255, 255))
        self.assertGreaterEqual(color, RGB(153, 153, 102))
        self.assertLessEqual(   color, RGB(179, 230, 230))

        # math
        self.assertEqual(
            round(color + RGB(32, 64, 128),3),
            HSL(280.0,1,1)
        )
        self.assertEqual(
            round(color - RGB(32, 64, 128),3),
            HSL(0,0,0.436)
        )
        self.assertEqual(
            round(color * RGB(4, 3, 2),3),
            HSL(360,0.167,0.009)
        )
        self.assertEqual(
            round(color / RGB(4, 3, 2),3),
            HSL(2.0,1,1)
        )
        self.assertEqual(
            round(color // RGB(9, 7, 5),3),
            HSL(2.0,1.0,1)
        )
        self.assertEqual(
            round(color ** RGB(2, 2, 1),3),
            HSL(360, 0.794, 0.998)
        )
        self.assertEqual(
            round(color % RGB(9, 7, 5),3),
            HSL(0.0, 0.214, 0.021)
        )

    def test_dunder_HEX(self):
        color = self.CreateColor()
        # Comparison
        self.assertEqual(       HSL(60.0, 0.5, 0.749), HEX("#dfdf9f"))
        self.assertNotEqual(    color, HEX("#000000"))
        self.assertGreater(     color, HEX("#000000"))
        self.assertLess(        color, HEX("#99ffff"))
        self.assertGreaterEqual(color, HEX("#999966"))
        self.assertLessEqual(   color, HEX("#b3e6e6"))

        # math
        self.assertEqual(
            round(color + HEX("#204080"),3),
            HSL(280.0, 1, 1)
        )
        self.assertEqual(
            round(color - HEX("#204080"),3),
            HSL(0, 0, 0.436)
        )
        self.assertEqual(
            round(color * HEX("#040302"),3),
            HSL(360, 0.167, 0.009)
        )
        self.assertEqual(
            round(color / HEX("#040302"),3),
            HSL(2.0, 1, 1)
        )
        self.assertEqual(
            round(color // HEX("#090705"),3),
            HSL(2.0, 1.0, 1)
        )
        self.assertEqual(
            round(color ** HEX("#020201"),3),
            HSL(360, 0.794, 0.998)
        )
        self.assertEqual(
            round(color % HEX("#090705"),3),
            HSL(0.0, 0.214, 0.021)
        )

    def test_dunder_HSL(self):
        color = self.CreateColor()
        # Comparison
        self.assertEqual(       color, HSL(60,.5,0.75))
        self.assertNotEqual(    color, HSL(0,0,0))
        self.assertGreater(     color, HSL(0,0,0))
        self.assertLess(        color, HSL(180,1,1))
        self.assertGreaterEqual(color, HSL(0,0,0.75))
        self.assertLessEqual(   color, HSL(180,.5,1))

        # math
        self.assertEqual(
            round(color + HSL(.25,.25,.25),3),
            HSL(60.25,0.75,1.0)
        )
        self.assertEqual(
            round(color - HSL(.25,.5,0.75),3),
            HSL(59.75,0.0,0.0)
        )
        self.assertEqual(
            round(color * HSL(.1,.5,0.75),3),
            HSL(6.0,0.25,0.562)
        )
        self.assertEqual(
            round(color / HSL(.1,.5,0.75),3),
            HSL(360,1.0,1.0)
        )
        self.assertEqual(
            round(color // HSL(.1,.5,0.75),3),
            HSL(360,1.0,1.0)
        )
        self.assertEqual(
            round(color ** HSL(.1,.5,0.75),3),
            HSL(1.506,0.707,0.806)
        )
        self.assertEqual(
            round(color % HSL(.1,.5,0.75),3),
            HSL(0.1, 0.0, 0.0)
        )

    def test_dunder_HSV(self):
        color = self.CreateColor()
        # Comparison
        self.assertEqual(       HSL(60.0, 0.5, 0.749), HSV(60.0, 0.287, 0.875))
        self.assertNotEqual(    color, HSV(0, 0, 0))
        self.assertGreater(     color, HSV(36.0, 0.179, 0.11))
        self.assertLess(        color, HSV(247.895, 0.314, 0.949))
        self.assertGreaterEqual(color, HSV(0, 0.0, 0.251))
        self.assertLessEqual(   color, HSV(60.0, 0.314, 0.949))

        # math
        self.assertEqual(
            round(color + HSV(.25, .25, .25),3),
            HSL(60.0,0.643,0.97)
        )
        self.assertEqual(
            round(color - HSV(.25, .5, 0.75),3),
            HSL(60.0,0.074,0.187)
        )
        self.assertEqual(
            round(color * HSV(.1, .5, 0.75),3),
            HSL(0.0,0.213,0.422)
        )
        self.assertEqual(
            round(color / HSV(30, .5, 0.75),3),
            HSL(2,1,1)
        )
        self.assertEqual(
            round(color // HSV(30, .5, 0.75),3),
            HSL(2.0,1.0,1.0)
        )
        self.assertEqual(
            round(color ** HSV(.1, .5, 0.75),3),
            HSL(1.0, 0.744, 0.85)
        )
        self.assertEqual(
            round(color % HSV(30, .5, 0.75),3),
            HSL(0,0.074,0.187)
        )

    def test_dunder_CMYK(self):
        color = self.CreateColor()
        # Comparison
        self.assertEqual(       HSL(60.0, 0.5, 0.749), CMYK(0.0, 0.0, 0.287, 0.125))
        self.assertNotEqual(    color, CMYK(1.0,1.0,1.0,1.0))
        self.assertGreater(     color, CMYK(0.0, 0.077, 0.16, 0.239))
        self.assertLess(        color, CMYK(0.069, 0.0, 0.142, 0.031))
        self.assertGreaterEqual(color, CMYK(0.0, 0.0, 0.16, 0.239))
        self.assertLessEqual(   color, CMYK(0.0, 0.0, 0.142, 0.031))

        # math
        self.assertEqual(
            round(color + CMYK(.9,.9,.75,.1),3),
            HSL(300.0,0.925,0.907)
        )
        self.assertEqual(
            round(color - CMYK(.9,.9,.75,.1),3),
            HSL(0,0.075,0.593)
        )
        self.assertEqual(
            round(color * CMYK(.9,.9,.75,.9),3),
            HSL(360,0.167,0.013)
        )
        self.assertEqual(
            round(color / CMYK(.9,.9,.75,.9),3),
            HSL(0.25,1,1)
        )
        self.assertEqual(
            round(color // CMYK(.9,.9,.75,.9),3),
            HSL(0.0,1.0,1)
        )
        self.assertEqual(
            round(color ** CMYK(.01,.1,.1,.2),3),
            HSL(1.0,0.904,0.804)
        )
        self.assertEqual(
            round(color % CMYK(0.75,0.25,0.25,0.15),3),
            HSL(60.0,0.5,0.325)
        )
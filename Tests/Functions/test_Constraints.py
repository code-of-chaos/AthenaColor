# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library
from AthenaColor.Functions.Constraints import *

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Functions_Constraints(unittest.TestCase):
    def test_Constrain(self):
        # Keyworded arguments
        self.assertEqual(Constrain(value=125,maximum=100),100)
        self.assertEqual(Constrain(value=85,maximum=100),85)
        self.assertEqual(Constrain(value=85,maximum=100,minimum=90),90)
        self.assertEqual(Constrain(value=-1000,maximum=100,minimum=-100),-100)

    def test_Constrain_Fail(self):
        with self.assertRaises(TypeError):
            # noinspection PyTypeChecker
            Constrain(value="a", maximum=100)
        with self.assertRaises(TypeError):
            # noinspection PyTypeChecker
            Constrain(value=100, maximum="a")
        with self.assertRaises(TypeError):
            # noinspection PyTypeChecker
            Constrain(100, 100,"a")

    def test_Constrain_HSV(self):
        self.assertEqual(ConstrainHSV(1000,2,2),(360,1,1))
        self.assertEqual(ConstrainHSV(-360,-1,-1),(0,0,0))

    def test_Constrain_HSL(self):
        self.assertEqual(ConstrainHSL(1000,2,2),(360,1,1))
        self.assertEqual(ConstrainHSL(-360,-1,-1),(0,0,0))

    def test_Constrain_RGB(self):
        self.assertEqual(ConstrainRGB(500,500,500),(255,255,255))
        self.assertEqual(ConstrainRGB(-500,-500,-500),(0,0,0))

    def test_Constrain_CMYK(self):
        self.assertEqual(ConstrainCMYK(2,2,2,2),(1,1,1,1))
        self.assertEqual(ConstrainCMYK(-1,-1,-1,-1),(0,0,0,0))

    def test_Constrain_RGBA(self):
        self.assertEqual(ConstrainRGBA(500,500,500,500),(255,255,255,255))
        self.assertEqual(ConstrainRGBA(-500,-500,-500,-500),(0,0,0,0))
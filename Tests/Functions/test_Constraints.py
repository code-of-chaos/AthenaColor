# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library
from AthenaColor.functions.constrains import *

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Functions_Constraints(unittest.TestCase):
    def test_Constrain(self):
        # Keyword arguments
        self.assertEqual(constrain(value=125, maximum=100), 100)
        self.assertEqual(constrain(value=85, maximum=100), 85)
        self.assertEqual(constrain(value=85, maximum=100, minimum=90), 90)
        self.assertEqual(constrain(value=-1000, maximum=100, minimum=-100), -100)

    def test_Constrain_Fail(self):
        with self.assertRaises(TypeError):
            # noinspection PyTypeChecker
            constrain(value="a", maximum=100)
        with self.assertRaises(TypeError):
            # noinspection PyTypeChecker
            constrain(value=100, maximum="a")
        with self.assertRaises(TypeError):
            # noinspection PyTypeChecker
            constrain(100, 100, "a")

    def test_Constrain_HSV(self):
        self.assertEqual(constrain_hsv(1000, 2, 2), (360, 1, 1))
        self.assertEqual(constrain_hsv(-360, -1, -1), (0, 0, 0))

    def test_Constrain_HSL(self):
        self.assertEqual(constrain_hsl(1000, 2, 2), (360, 1, 1))
        self.assertEqual(constrain_hsl(-360, -1, -1), (0, 0, 0))

    def test_Constrain_RGB(self):
        self.assertEqual(constrain_rgb(500, 500, 500), (255, 255, 255))
        self.assertEqual(constrain_rgb(-500, -500, -500), (0, 0, 0))

    def test_Constrain_CMYK(self):
        self.assertEqual(constrain_cmyk(2, 2, 2, 2), (1, 1, 1, 1))
        self.assertEqual(constrain_cmyk(-1, -1, -1, -1), (0, 0, 0, 0))

    def test_Constrain_RGBA(self):
        self.assertEqual(constrain_rgba(500, 500, 500, 500), (255, 255, 255, 255))
        self.assertEqual(constrain_rgba(-500, -500, -500, -500), (0, 0, 0, 0))
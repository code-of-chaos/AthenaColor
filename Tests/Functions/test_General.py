# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library
from AthenaColor.Functions.General import *
from AthenaColor import init

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Functions_General(unittest.TestCase):
    def test_Normalize(self):
        for i in range(1,100):
            with self.subTest(i=i):
                self.assertEqual(Normalize(i), i/100)

    def test_Normalize_Factor(self):
        for i, f in zip(range(1,100),range(100,200)):
            with self.subTest(i=i):
                self.assertEqual(Normalize(i, factor=f), i/f)

    def test_RoundToDecimals(self):
        for i, f in zip(range(1,24),range(24,56)):
            with self.subTest(i=i, f=f):
                self.assertEqual(RoundToDecimals(i/f), round(i/f , init.decimalPlaces))

    # noinspection PyTypeChecker
    def test_RoundToDecimals_Fail(self):
        with self.assertRaises(TypeError):
            RoundToDecimals(100,"a")
        with self.assertRaises(TypeError):
            RoundToDecimals("a",1)

    def test_RoundHalfUp(self):
        for i, e in ((0.5,1),(0.4,0),(1.1,1),(.8,1),):
            with self.subTest(i=i,e=e):
                self.assertEqual(
                    RoundHalfUp(i),
                    e
                )

    # noinspection PyTypeChecker
    def test_RoundHalfUp_Fail(self):
        with self.assertRaises(TypeError):
            RoundHalfUp("a")
        with self.assertRaises(TypeError):
            RoundHalfUp((1,))
        with self.assertRaises(TypeError):
            RoundHalfUp([1,])
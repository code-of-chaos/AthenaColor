# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library
from AthenaColor.functions.functions import *

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Functions_General(unittest.TestCase):
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
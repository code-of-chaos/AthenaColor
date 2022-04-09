# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library

# Custom Packages
from AthenaColor import *

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class AthenaColorTest(unittest.TestCase):
    # ------------------------------------------------------------------------------------------------------------------
    # - BASIC Color Object Testing -
    # ------------------------------------------------------------------------------------------------------------------
    def test_ColorObjects_RGB(self):
        self.assertEqual(
            repr(RGB(1,2,3)),
            "RGB(r=1,g=2,b=3)"
        )
        self.assertEqual(
            repr(RGB(321,654,987)),
            "RGB(r=255,g=255,b=255)"
        )
    def test_ColorObjects_RGBA(self):
        self.assertEqual(
            repr(RGBA(1,2,3,4)),
            "RGBA(r=1,g=2,b=3,a=4)"
        )
        self.assertEqual(
            repr(RGBA(321,654,987, -1)),
            "RGBA(r=255,g=255,b=255,a=0)"
        )

    def test_ColorObjects_HEX(self):
        self.assertEqual(
            repr(HEX("#001122")),
            "HEX(r=0,g=17,b=34)"
        )
        self.assertEqual(
            repr(HEX("#FFAABB")),
            "HEX(r=255,g=170,b=187)"
        )
    def test_ColorObjects_HEXA(self):
        self.assertEqual(
            repr(HEXA("#00112233")),
            "HEXA(r=0,g=17,b=34,a=51)"
        )
        self.assertEqual(
            repr(HEXA("#BBCCAAFF")),
            "HEXA(r=187,g=204,b=170,a=255)"
        )

if __name__ == '__main__':
    unittest.main()
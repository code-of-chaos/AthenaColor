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
class ColorObjects_RGB(unittest.TestCase):
    @staticmethod
    def CreateColor(r=127,g=127,b=127) -> RGB:
        return RGB(r,g,b)
    # ------------------------------------------------------------------------------------------------------------------
    # - BASIC Color Object Testing -
    # ------------------------------------------------------------------------------------------------------------------
    def test_repr(self):
        self.assertEqual(repr(self.CreateColor()),"RGB(r=127,g=127,b=127)")

    def test_str(self):
        self.assertEqual(repr(self.CreateColor()),"127;127;127")

    def test_dunder_comparison_tuples(self):
        self.assertTrue(self.CreateColor() == (127,127,127))
        self.assertTrue(self.CreateColor() != (0,0,0))
        self.assertTrue(self.CreateColor() < (200,200,200))
        self.assertTrue(self.CreateColor() > (0,0,0))
        self.assertTrue(self.CreateColor() <= (127,128,129))
        self.assertTrue(self.CreateColor() >= (0,0,127))

    def test_dunder_comparison_objects(self):
        self.assertTrue(self.CreateColor() == RGB(127,127,127))
        self.assertTrue(self.CreateColor() != RGB(0,0,0))
        self.assertTrue(self.CreateColor() <  RGB(200,200,200))
        self.assertTrue(self.CreateColor() >  RGB(0,0,0))
        self.assertTrue(self.CreateColor() <= RGB(127,128,129))
        self.assertTrue(self.CreateColor() >= RGB(0,0,127))

        self.assertTrue(self.CreateColor() == HEX("#7F7F7F"))
        self.assertTrue(self.CreateColor() != HEX("#000000"))
        self.assertTrue(self.CreateColor() <  HEX("#C8C8C8"))
        self.assertTrue(self.CreateColor() >  HEX("#000000"))
        self.assertTrue(self.CreateColor() <= HEX("#7F8081"))
        self.assertTrue(self.CreateColor() >= HEX("#00007F"))

        self.assertTrue(self.CreateColor() == HSL(0,0,.498))
        self.assertTrue(self.CreateColor() != HSL(0,0,0))
        self.assertTrue(self.CreateColor() <  HSL(0,0,.784))
        self.assertTrue(self.CreateColor() >  HSL(0,0,0))
        self.assertTrue(self.CreateColor() <= HSL(210,.008,.502))
        self.assertTrue(self.CreateColor() >= HSL(240,1,.249))

        self.assertTrue(self.CreateColor() == HSV(0,0,.498))
        self.assertTrue(self.CreateColor() != HSV(0,0,0))
        self.assertTrue(self.CreateColor() <  HSV(0,0,.784))
        self.assertTrue(self.CreateColor() >  HSV(0,0,0))
        self.assertTrue(self.CreateColor() <= HSV(210,.016,.506))
        self.assertTrue(self.CreateColor() >= HSV(240,1,.498))

        self.assertTrue(self.CreateColor() == CMYK(0,0,0,.502))
        self.assertTrue(self.CreateColor() != CMYK(0,0,0,0))
        self.assertTrue(self.CreateColor() <  CMYK(0,0,0,0.22))
        self.assertTrue(self.CreateColor() >  CMYK(0,0,0,1))
        self.assertTrue(self.CreateColor() <= CMYK(.02,.01,0,.49))
        self.assertTrue(self.CreateColor() >= CMYK(1,1,0,.505))

    def test_dunder_math_tuple(self):
        self.assertEqual(self.CreateColor()-(500,500,500), RGB(r=0, g=0, b=0))
        self.assertEqual(self.CreateColor()+(500,500,500), RGB(r=255, g=255, b=255))
        self.assertEqual(self.CreateColor()/(3,3,3), RGB(r=42, g=42, b=42))
        self.assertEqual(self.CreateColor()//(4,4,4), RGB(r=31, g=31, b=31))
        self.assertEqual(self.CreateColor()*(2,2,2), RGB(r=254, g=254, b=254))
        self.assertEqual(self.CreateColor(3,3,3)**(4,4,4), RGB(r=81, g=81, b=81))
        self.assertEqual(self.CreateColor()%(4,4,4), RGB(r=3, g=3, b=3))

if __name__ == '__main__':
    unittest.main()
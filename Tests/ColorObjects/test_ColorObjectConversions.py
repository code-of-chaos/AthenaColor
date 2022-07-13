# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library
from AthenaColor import *
from AthenaColor.func.color_object_conversion import *

# Custom Packages
# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ColorObject_ObjectConversion(unittest.TestCase):

    def test_to_rgb(self):
        cases = (
            # VALUE             # RGB
            (RGB(125,22,124),   RGB(r=125,g=22,b=124)),
            (HEX("#ffa1b8"),    RGB(r=255,g=161,b=184)),
            (RGBA(125,22,124,1),RGB(r=125,g=22,b=124)),
            (HEXA("#ffa1b8ff"), RGB(r=255,g=161,b=184)),
            (HSL(152,.9,.4),    RGB(r=10,g=194,b=108)),
            (HSV(152,.9,.4),    RGB(r=10,g=102,b=59)),
            (CMYK(0,.1,.87,.2), RGB(r=204,g=184,b=27)),
        )
        for value, output_value in cases:
            with self.subTest(value=value,output_value=output_value):
                self.assertEqual(
                    to_RGB(value),
                    output_value
                )

    def test_to_hex(self):
        cases = (
            # VALUE             # RGB
            (RGB(125,22,124),   HEX("#7D167C")),
            (HEX("#ffa1b8"),    HEX("#ffa1b8")),
            (RGBA(125,22,124,1),HEX("#7D167C")),
            (HEXA("#ffa1b8ff"), HEX("#ffa1b8")),
            (HSL(152,.9,.4),    HEX("#0AC26C")),
            (HSV(152,.9,.4),    HEX("#0A663B")),
            (CMYK(0,.1,.87,.2), HEX("#CCB81B")),
        )
        for value, output_value in cases:
            with self.subTest(value=value,output_value=output_value):
                self.assertEqual(
                    to_HEX(value),
                    output_value
                )

    def test_to_hexa(self):
        cases = (
            # VALUE             # HEXA
            (RGB(125,22,124),   HEXA("#7D167Cff")),
            (HEX("#ffa1b8"),    HEXA("#ffa1b8ff")),
            (RGBA(125,22,124,1),HEXA("#7D167C01")),
            (HEXA("#ffa1b8ff"), HEXA("#ffa1b8ff")),
            (HSL(152,.9,.4),    HEXA("#0AC26Cff")),
            (HSV(152,.9,.4),    HEXA("#0A663Bff")),
            (CMYK(0,.1,.87,.2), HEXA("#CCB81Bff")),
        )
        for value, output_value in cases:
            with self.subTest(value=value,output_value=output_value):
                self.assertEqual(
                    to_HEXA(value),
                    output_value
                )

    def test_to_rgba(self):
        cases = (
            # VALUE             # RGB
            (RGB(125,22,124),   RGBA(r=125,g=22,b=124,a=255)),
            (HEX("#ffa1b8"),    RGBA(r=255,g=161,b=184,a=255)),
            (RGBA(125,22,124,1),RGBA(r=125,g=22,b=124,a=1)),
            (HEXA("#ffa1b8ff"), RGBA(r=255,g=161,b=184,a=255)),
            (HSL(152,.9,.4),    RGBA(r=10,g=194,b=108,a=255)),
            (HSV(152,.9,.4),    RGBA(r=10,g=102,b=59,a=255)),
            (CMYK(0,.1,.87,.2), RGBA(r=204,g=184,b=27,a=255)),
        )
        for value, output_value in cases:
            with self.subTest(value=value,output_value=output_value):
                self.assertEqual(
                    to_RGBA(value),
                    output_value
                )

    def test_to_hsv(self):
        cases = (
            # VALUE                 # HSV
            (RGB(125, 22, 124),     HSV(h=0,s=0.824,v=0.49)),
            (HEX("#ffa1b8"),        HSV(h=0,s=0.369,v=1.0)),
            (RGBA(125, 22, 124, 1), HSV(h=0,s=0.824,v=0.49)),
            (HEXA("#ffa1b8ff"),     HSV(h=0,s=0.369,v=1.0)),
            (HSL(152, .9, .4),      HSV(h=152,s=0.948,v=0.761)),
            (HSV(152, .9, .4),      HSV(h=152,s=0.9,v=0.4)),
            (CMYK(0, .1, .87, .2),  HSV(h=53,s=0.868,v=0.8)),
        )
        for value, output_value in cases:
            with self.subTest(value=value, output_value=output_value):
                self.assertEqual(
                    HSV(*(round(n, 3) for n in to_HSV(value))),
                    output_value
                )

    def test_to_hsl(self):
        cases = (
            # VALUE                 # HSV
            (RGB(125, 22, 124),     HSL(h=301,s=0.701,l=0.288)),
            (HEX("#ffa1b8"),        HSL(h=345,s=1.0,l=0.816)),
            (RGBA(125, 22, 124, 1), HSL(h=301,s=0.701,l=0.288)),
            (HEXA("#ffa1b8ff"),     HSL(h=345,s=1.0,l=0.816)),
            (HSL(152, .9, .4),      HSL(h=152,s=0.9,l=0.4)),
            (HSV(152, .9, .4),      HSL(h=152,s=0.821,l=0.22)),
            (CMYK(0, .1, .87, .2),  HSL(h=53,s=0.766,l=0.453)),
        )
        for value, output_value in cases:
            with self.subTest(value=value, output_value=output_value):
                self.assertEqual(
                    HSL(*(round(n, 3) for n in to_HSL(value))),
                    output_value
                )

    def test_to_cmyk(self):
        cases = (
            # VALUE                 # CMYK
            (RGB(125, 22, 124),     CMYK(c=0.0,m=0.824,y=0.008,k=0.51)),
            (HEX("#ffa1b8"),        CMYK(c=0.0,m=0.369,y=0.278,k=0.0)),
            (RGBA(125, 22, 124, 1), CMYK(c=0.0,m=0.824,y=0.008,k=0.51)),
            (HEXA("#ffa1b8ff"),     CMYK(c=0.0,m=0.369,y=0.278,k=0.0)),
            (HSL(152, .9, .4),      CMYK(c=0.948,m=0.0,y=0.443,k=0.239)),
            (HSV(152, .9, .4),      CMYK(c=0.902,m=0.0,y=0.422,k=0.6)),
            (CMYK(0, .1, .87, .2),  CMYK(c=0,m=0.1,y=0.87,k=0.2)),
        )
        for value, output_value in cases:
            with self.subTest(value=value, output_value=output_value):
                self.assertEqual(
                    CMYK(*(round(n, 3) for n in to_CMYK(value))),
                    output_value
                )


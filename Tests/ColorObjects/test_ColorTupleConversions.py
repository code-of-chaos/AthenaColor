# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library
from AthenaColor.models.Color.ColorTupleConversion import *

# Custom Packages
# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ColorObject_TupleConversion(unittest.TestCase):
    def test_NormalizeRgb(self):
        for i in range(256):
            with self.subTest(i=i):
                NormalizeRgb(i,i,i)

    def test_hex_to_rgb(self):
        cases = (
            # HEX       # RGB
            ("#ffffff", (255,255,255)),
            ("719146",  (113, 145, 70)),
            ("#574c87", (87, 76, 135)),
            ("#a34d95", (163, 77, 149)),
            ("a19633",  (161, 150, 51)),
        )
        for hex_value, rgb_value in cases:
            with self.subTest(hex_value=hex_value,rgb_value=rgb_value):
                self.assertEqual(
                    hex_to_rgb(hex_value),
                    rgb_value
                )

    def test_hsv_to_rgb(self):
        cases = (
            # HSV           # RGB
            ((54,.68,.63),  (161, 150, 51)),
            ((54,.33,.73),  (186, 180, 125)),
            ((300,.19,.8),  (204, 165, 204)),
            ((54,0,0),      (0, 0, 0)),
            ((199,0,1),     (255, 255, 255)),
        )
        for hsv_value, rgb_value in cases:
            with self.subTest(hsv_value=hsv_value,rgb_value=rgb_value):
                self.assertEqual(
                    hsv_to_rgb(*hsv_value),
                    rgb_value
                )

    def cmyk_to_rgb(self):
        cases = (
            # CMYK              # RGB
            ((0,0,0,0),         (255, 255, 255)),
            ((0,0,0,1),         (0,0,0)),
            ((.5,.5,0,.39),     (78,78,156)),
            ((0,.78,.28,.2),    (204, 45, 146)),
            ((.05,0,.52,.22),   (190, 199, 95)),
        )
        for cmyk_value, rgb_value in cases:
            with self.subTest(cmyk_value=cmyk_value,rgb_value=rgb_value):
                self.assertEqual(
                    cmyk_to_rgb(*cmyk_value),
                    rgb_value
                )

    def test_hsl_to_rgb(self):
        cases = (
            # HSL               # RGB
            ((62,0,1),          (255, 255, 255)),
            ((176,0,0),         (0,0,0)),
            ((259,.728,.553),   (111, 58, 224)),
            ((136,.38,.47),     (74, 165, 99)),
        )
        for hsl_value, rgb_value in cases:
            with self.subTest(hsl_value=hsl_value,rgb_value=rgb_value):
                self.assertEqual(
                    hsl_to_rgb(*hsl_value),
                    rgb_value
                )

    def test_rgb_to_hex(self):
        cases = (
            # RGB               # HEX
            ((137, 176, 147),   "#89b093"),
            ((255,255,255),     "#ffffff"),
            ((0,0,0),           "#000000"),
            ((106, 150, 176),   "#6a96b0"),
            ((106, 150, 176),   "#6a96b0"),
            ((173, 127, 71),    "#ad7f47"),
        )
        for rgb_value, hex_value in cases:
            with self.subTest(rgb_value=rgb_value,hex_value=hex_value):
                self.assertEqual(
                    rgb_to_hex(*rgb_value),
                    hex_value
                )

    def test_hsv_to_hex(self):
        cases = (
            # HSV               # HEX
            ((33, .59, .68),    "#ad7f47"),
            ((33, 0, 1),        "#ffffff"),
            ((33, 0, 0),        "#000000"),
            ((234, .92, .93),   "#1329ed"),
            ((56, .86, .62),    "#9e9516"),
        )
        for hsv_value, hex_value in cases:
            with self.subTest(hsv_value=hsv_value,hex_value=hex_value):
                self.assertEqual(
                    hsv_to_hex(*hsv_value),
                    hex_value
                )

    def test_cmyk_to_hex(self):
        cases = (
            # CMYK              # HEX
            ((0,.06,.86,.38),   "#9e9516"),
            ((0,0,0,0),         "#ffffff"),
            ((0,0,0,1),         "#000000"),
            ((0.09,0.78,0,.17), "#c12fd4"),
        )
        for cmyk_value, hex_value in cases:
            with self.subTest(cmyk_value=cmyk_value,hex_value=hex_value):
                self.assertEqual(
                    cmyk_to_hex(*cmyk_value),
                    hex_value
                )

    def test_hsl_to_hex(self):
        cases = (
            # HSL               # HEX
            ((293, .66, .51),   "#c130d5"),
            ((33, 0, 1),        "#ffffff"),
            ((33, 0, 0),        "#000000"),
            ((84, 1, .33),      "#65a800"),
            ((333, .63, .48),   "#c82d73"),
        )
        for hsl_value, hex_value in cases:
            with self.subTest(hsl_value=hsl_value,hex_value=hex_value):
                self.assertEqual(
                    hsl_to_hex(*hsl_value),
                    hex_value
                )

    def test_rgb_to_hsv(self):
        cases = (
            # RGB               # HSV
            ((255, 255, 255),   (0,0,1.0)),
            ((0, 0, 0),         (0,0,0)),
            ((67, 48, 110),     (258,.564,.431)),
            ((3, 238, 255),     (184,.988,1)),
            ((139, 171, 22),    (73,.871,.671)),
        )
        for rgb_value, hsv_value in cases:
            with self.subTest(rgb_value=rgb_value, hsv_value=hsv_value):
                self.assertEqual(
                    rgb_to_hsv(*rgb_value),
                    hsv_value
                )

    def test_hex_to_hsv(self):
        cases = (
            # HEX       # HSV
            ("#ffffff", (0,0,1.0)),
            ("#000000", (0,0,0)),
            ("#43306e", (258,.564,.431)),
            ("#03eeff", (184,.988,1)),
            ("#8bab16", (73,.871,.671)),
        )
        for hex_value, hsv_value in cases:
            with self.subTest(hex_value=hex_value, hsv_value=hsv_value):
                self.assertEqual(
                    hex_to_hsv(hex_value),
                    hsv_value
                )

    def test_cmyk_to_hsv(self):
        cases = (
            # CMYK              # HSV
            ((0,0,0,0),         (0,0,1.0)),
            ((0,0,0,1),         (0,0,0)),
            ((.72,0,.3,.33),    (155,.719,.671)),
            ((0,.4,.58,.15),    (19,.581,.851)),
            ((.63,.81,0,.75),   (254,.812,.251)),
        )
        for cmyk_value, hsv_value in cases:
            with self.subTest(cmyk_value=cmyk_value, hsv_value=hsv_value):
                self.assertEqual(
                    cmyk_to_hsv(*cmyk_value),
                    hsv_value
                )

    def test_hsl_to_hsv(self):
        cases = (
            # HSL               # HSV
            ((0,0,1),           (0,0,1.0)),
            ((0,0,0),           (0,0,0)),
            ((254,.68,.15),     (254,.812,.251)),
            ((77,.42,.59),      (77,.448,.761)),
            ((136,.43,.30),     (136,.596,.427)),
        )
        for hsl_value, hsv_value in cases:
            with self.subTest(hsl_value=hsl_value, hsv_value=hsv_value):
                self.assertEqual(
                    hsl_to_hsv(*hsl_value),
                    hsv_value
                )

    def test_rgb_to_cmyk(self):
        cases = (
            # RGB               # CMYK
            ((255,255,255),     (0,0,0,0)),
            ((0,0,0),           (0,0,0,1)),
            ((235, 64, 52),     (0.0, 0.728, 0.779, 0.078)),
            ((93, 73, 112),     (0.17, 0.348, 0.0, 0.561)),
            ((45, 164, 196),    (0.77, 0.163, 0.0, 0.231)),
        )
        for rgb_value, cmyk_value in cases:
            with self.subTest(cmyk_value=cmyk_value, rgb_value=rgb_value):
                self.assertEqual(
                    rgb_to_cmyk(*rgb_value),
                    cmyk_value
                )

    def test_hex_to_cmyk(self):
        cases = (
            # HEX       # CMYK
            ("#ffffff", (0,0,0,0)),
            ("#000000", (0,0,0,1)),
            ("2da4c4",  (0.77, 0.163, 0.0, 0.231)),
            ("454a40",  (0.068, 0.0, 0.135, 0.71)),
            ("9e80c2",  (0.186, 0.34, 0.0, 0.239)),
        )
        for hex_value, cmyk_value in cases:
            with self.subTest(cmyk_value=cmyk_value, hex_value=hex_value):
                self.assertEqual(
                    hex_to_cmyk(hex_value),
                    cmyk_value
                )

    def test_hsv_to_cmyk(self):
        cases = (
            # HSV               # CMYK
            ((0,0,1),           (0,0,0,0)),
            ((0,0,0),           (0,0,0,1)),
            ((345,.94,.62),     (0.0, 0.943, 0.703, 0.38)),
            ((98,.63,.67),      (0.398, 0.0, 0.632, 0.329)),
            ((187,.89,.41),     (0.886, 0.105, 0.0, 0.588)),
        )
        for hsv_value, cmyk_value in cases:
            with self.subTest(cmyk_value=cmyk_value, hsv_value=hsv_value):
                self.assertEqual(
                    hsv_to_cmyk(*hsv_value),
                    cmyk_value
                )

    def test_rgb_to_hsl(self):
        cases = (
            # RGB               # HSL
            ((255, 255, 255),   (0,0,1.0)),
            ((0, 0, 0),         (0,0,0)),
            ((67, 48, 110),     (258, 0.392, 0.31)),
            ((3, 238, 255),     (184, 1.0, 0.506)),
            ((139, 171, 22),    (73, 0.772, 0.378)),
        )
        for rgb_value, hsl_value in cases:
            with self.subTest(rgb_value=rgb_value, hsl_value=hsl_value):
                self.assertEqual(
                    rgb_to_hsl(*rgb_value),
                    hsl_value
                )

    def test_hex_to_hsl(self):
        cases = (
            # HEX       # HSL
            ("#ffffff", (0,0,1.0)),
            ("#000000", (0,0,0)),
            ("#43306e", (258, 0.392, 0.31)),
            ("#03eeff", (184, 1.0, 0.506)),
            ("#8bab16", (73, 0.772, 0.378)),
        )
        for hex_value, hsl_value in cases:
            with self.subTest(hex_value=hex_value, hsl_value=hsl_value):
                self.assertEqual(
                    hex_to_hsl(hex_value),
                    hsl_value
                )

    def test_hsv_to_hsl(self):
        cases = (
            # HSV               # HSV
            ((0,0,1),           (0,0,1.0)),
            ((0,0,0),           (0,0,0)),
            ((254,.68,.15),     (254, 0.52, 0.098)),
            ((77,.42,.59),      (76, 0.266, 0.465)),
            ((136,.43,.30),     (135, 0.273, 0.237)),
        )
        for hsv_value, hsl_value in cases:
            with self.subTest(hsl_value=hsl_value, hsv_value=hsv_value):
                self.assertEqual(
                    hsv_to_hsl(*hsv_value),
                    hsl_value
                )

    def test_cmyk_to_hsl(self):
        cases = (
            # CMYK              # HSL
            ((0,0,0,0),         (0,0,1.0)),
            ((0,0,0,1),         (0,0,0)),
            ((.72,0,.3,.33),    (155, 0.562, 0.429)),
            ((0,.4,.58,.15),    (19, 0.624, 0.604)),
            ((.63,.81,0,.75),   (254, 0.684, 0.149)),
        )
        for cmyk_value, hsl_value in cases:
            with self.subTest(cmyk_value=cmyk_value, hsl_value=hsl_value):
                self.assertEqual(
                    cmyk_to_hsl(*cmyk_value),
                    hsl_value
                )

    def test_hexa_to_rgba(self):
        cases = (
            # HEXA          # RGBA
            ("#ffffffff",   (255,255,255,255)),
            ("719146aa",    (113, 145, 70, 170)),
            ("#574c87bb",   (87, 76, 135, 187)),
            ("#a34d95ca",   (163, 77, 149, 202)),
            ("a196331f",    (161, 150, 51, 31)),
        )
        for hexa_value, rgba_value in cases:
            with self.subTest(hexa_value=hexa_value,rgba_value=rgba_value):
                self.assertEqual(
                    hexa_to_rgba(hexa_value),
                    rgba_value
                )

    def test_rgba_to_hexa(self):
        cases = (
            # RGBA  HEXA
            ((255,255,255,255),     "#ffffffff"),
            ((113, 145, 70, 170),   "#719146aa"),
            ((87, 76, 135, 187),    "#574c87bb"),
            ((163, 77, 149, 202),   "#a34d95ca"),
            ((161, 150, 51, 31),    "#a196331f"),
        )
        for rgba_value, hexa_value in cases:
            with self.subTest(hexa_value=hexa_value,rgba_value=rgba_value):
                self.assertEqual(
                    rgba_to_hexa(*rgba_value),
                    hexa_value
                )
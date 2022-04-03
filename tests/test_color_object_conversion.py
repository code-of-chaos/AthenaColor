# XXX mock out color systems

from __future__ import annotations

import unittest

from AthenaColor.Objects.ColorSystems import (
    HSL,
    HSV,
    RGB,
    HEX,
    CMYK,
    HEXA,
    RGBA
)


from AthenaColor.Functions.ColorObjectConversion import (
    to_CMYK,
    to_HEX,
    to_HEXA,
    to_HSL,
    to_HSV,
    to_RGB,
    to_RGBA
)


class TestToRGB(unittest.TestCase):
    def setUp(self) -> None:
        self.rgb_res = RGB(123, 23, 253)

    def test_is_already_rgb_color(self):
        self.assertEqual(
            to_RGB(self.rgb_res),
            self.rgb_res
        )

    def test_from_hex_lowercase(self):
        self.assertEqual(
            to_RGB(HEX('#7b17fd')),
            self.rgb_res
        )

    def test_from_hex_uppercase(self):
        self.assertEqual(
            to_RGB(HEX('#7B17FD')),
            self.rgb_res
        )

    def test_from_hsv(self):
        self.assertEqual(
            to_RGB(HSV(266, 0.909, 0.992)),
            self.rgb_res
        )

    def test_from_hsl(self):
        self.assertEqual(
            to_RGB(HSL(266, 0.982, 0.541)),
            self.rgb_res
        )

    def test_from_cmyk(self):
        self.assertEqual(
            to_RGB(CMYK(0.513, 0.909, 0.0, 0.007)),
            self.rgb_res
        )

    def test_from_rgba(self):
        self.assertEqual(
            to_RGB(RGBA(123, 23, 253, 60)),
            self.rgb_res
        )

    def test_from_hexa_lowercase(self):
        self.assertEqual(
            to_RGB(HEXA('#7b17fd99')),
            self.rgb_res
        )

    def test_from_hexa_uppercase(self):
        self.assertEqual(
            to_RGB(HEXA('#7B17FD99')),
            self.rgb_res
        )

    def test_from_other_type(self):
        self.assertEqual(
            to_RGB(1),
            NotImplemented
        )


class TestToHEX(unittest.TestCase):
    def setUp(self) -> None:
        self.hex_res = HEX('#45df9a')

    def test_is_already_hex_lowercase(self):
        self.assertEqual(
            to_HEX(self.hex_res),
            self.hex_res
        )

    def test_is_already_hex_uppercase(self):
        self.assertEqual(
            to_HEX(HEX(str(self.hex_res).upper())),
            self.hex_res
        )

    def test_from_rgb(self):
        self.assertEqual(
            to_HEX(RGB(69, 223, 154)),
            self.hex_res
        )

    def test_from_hsv(self):
        self.assertEqual(
            to_HEX(HSV(153, 0.690, 0.874)),
            self.hex_res
        )

    def test_from_hsl(self):
        self.assertEqual(
            to_HEX(HSL(153, 0.706, 0.572)),
            self.hex_res
        )

    def test_from_cmyk(self):
        self.assertEqual(
            to_HEX(CMYK(0.690, 0.0, 0.309, 0.125)),
            self.hex_res
        )

    def test_from_rgba(self):
        self.assertEqual(
            to_HEX(RGBA(69, 223, 154, 60)),
            self.hex_res
        )

    def test_from_hexa_lowercase(self):
        self.assertEqual(
            to_HEX(HEXA('#45df9a99')),
            self.hex_res
        )

    def test_from_hexa_uppercase(self):
        self.assertEqual(
            to_HEX(HEXA('#45DF9A99')),
            self.hex_res
        )

    def test_from_other_type(self):
        self.assertEqual(
            to_HEX(1),
            NotImplemented
        )


class TestToHSV(unittest.TestCase):
    def setUp(self) -> None:
        self.hsv_res = HSV(78.19672131147543, 0.5980392156862745, 0.8)

    def test_is_already_hsv(self):
        self.assertEqual(
            to_HSV(self.hsv_res),
            self.hsv_res
        )

    def test_from_rgb(self):
        self.assertEqual(
            to_HSV(RGB(167, 204, 82)),
            self.hsv_res
        )

    def test_from_hex_lowercase(self):
        self.assertEqual(
            to_HSV(HEX('#a7cc52')),
            self.hsv_res
        )

    def test_from_hex_uppercase(self):
        self.assertEqual(
            to_HSV(HEX('#A7CC52')),
            self.hsv_res
        )

    def test_from_hsl(self):
        self.assertEqual(
            to_HSV(HSL(78.19, 0.544, 0.560)),
            self.hsv_res
        )

    def test_from_cmyk(self):
        self.assertEqual(
            to_HSV(CMYK(0.181, 0.0, 0.598, 0.199)),
            self.hsv_res
        )

    def test_from_rgba(self):
        self.assertEqual(
            to_HSV(RGBA(167, 204, 82, 60)),
            self.hsv_res
        )

    def test_from_hexa_lowercase(self):
        self.assertEqual(
            to_HSV(HEXA('#a7cc5299')),
            self.hsv_res
        )

    def test_from_hexa_uppercase(self):
        self.assertEqual(
            to_HSV(HEXA('#A7CC5299')),
            self.hsv_res
        )

    def test_from_other_type(self):
        self.assertEqual(
            to_HSV(1),
            NotImplemented
        )


class TestToHSL(unittest.TestCase):
    def setUp(self) -> None:
        self.hsl_res = HSL(78.38709677419355, 0.6078431372549019, 0.8)

    def test_is_already_hsl(self):
        self.assertEqual(
            to_HSL(self.hsl_res),
            self.hsl_res
        )

    def test_from_rgb(self):
        self.assertEqual(
            to_HSL(RGB(216, 235, 173)),
            self.hsl_res
        )

    def test_from_hex_lowercase(self):
        self.assertEqual(
            to_HSL(HEX('#d8ebad')),
            self.hsl_res
        )

    def test_from_hex_uppercase(self):
        self.assertEqual(
            to_HSL(HEX('#D8EBAD')),
            self.hsl_res
        )

    def test_from_hsv(self):
        self.assertEqual(
            to_HSL(HSV(78, 0.263, 0.921)),
            self.hsl_res
        )

    def test_from_cmyk(self):
        self.assertEqual(
            to_HSL(CMYK(0.080, 0.0, 0.263, 0.078)),
            self.hsl_res
        )

    def test_from_rgba(self):
        self.assertEqual(
            to_HSL(RGBA(216, 235, 173, 60)),
            self.hsl_res
        )

    def test_from_hexa_lowercase(self):
        self.assertEqual(
            to_HSL(HEXA('#d8ebad99')),
            self.hsl_res
        )

    def test_from_hexa_uppercase(self):
        self.assertEqual(
            to_HSL(HEXA('#D8EBAD99')),
            self.hsl_res
        )

    def test_from_other_type(self):
        self.assertEqual(
            to_HSL(1),
            NotImplemented
        )


class TestToCMYK(unittest.TestCase):
    def setUp(self) -> None:
        self.cmyk_res = CMYK(0.7679999999999999, 0.9039999999999999, 0.0, 0.5098039215686274)

    def test_is_already_cmyk(self):
        self.assertEqual(
            to_CMYK(self.cmyk_res),
            self.cmyk_res
        )

    def test_from_rgb(self):
        self.assertEqual(
            to_CMYK(RGB(29, 12, 125)),
            self.cmyk_res
        )

    def test_from_hex_lowercase(self):
        self.assertEqual(
            to_CMYK(HEX('#1d0c7d')),
            self.cmyk_res
        )

    def test_from_hex_uppercase(self):
        self.assertEqual(
            to_CMYK(HEX('#1D0C7D')),
            self.cmyk_res
        )

    def test_from_hsl(self):
        self.assertEqual(
            to_CMYK(HSL(249, 0.824, 0.268)),
            self.cmyk_res
        )

    def test_from_hsv(self):
        self.assertEqual(
            to_HSL(HSV(249, 0.904, 0.490)),
            self.cmyk_res
        )

    def test_from_rgba(self):
        self.assertEqual(
            to_CMYK(RGBA(29, 12, 125, 60)),
            self.cmyk_res
        )

    def test_from_hexa_lowercase(self):
        self.assertEqual(
            to_CMYK(HEXA('#1d0c7d99')),
            self.cmyk_res
        )

    def test_from_hexa_uppercase(self):
        self.assertEqual(
            to_CMYK(HEXA('#1D0C7D99')),
            self.cmyk_res
        )

    def test_from_other_type(self):
        self.assertEqual(
            to_CMYK(1),
            NotImplemented
        )


class TestToRGBA(unittest.TestCase):
    def setUp(self) -> None:
        self.rgba_res = RGBA(158, 48, 125, 60)

    def test_is_already_rgba(self):
        self.assertEqual(
            to_RGBA(self.rgba_res),
            self.rgba_res
        )

    def test_from_rgb(self):
        self.assertEqual(
            to_RGBA(RGB(158, 48, 125)),
            self.rgba_res
        )

    def test_from_hex_lowercase(self):
        self.assertEqual(
            to_RGBA(HEX('#9e307d')),
            self.rgba_res
        )

    def test_from_hsv(self):
        self.assertEqual(
            to_RGBA(HSV(318, 0.696, 0.619)),
            self.rgba_res
        )

    def test_from_hsl(self):
        self.assertEqual(
            to_RGBA(HSL(318, 0.533, 0.403)),
            self.rgba_res
        )

    def test_from_cmyk(self):
        self.assertEqual(
            to_RGBA(HSL(0.0, 0.696, 0.208, 0.380)),
            self.rgba_res
        )

    def test_from_hexa_lowercase(self):
        self.assertEqual(
            to_RGBA(HEX('#9e307d00')),
            self.rgba_res
        )

    def test_from_hexa_uppercase(self):
        self.assertEqual(
            to_RGBA(HEX('#9E307D99')),
            self.rgba_res
        )

    def test_from_other_type(self):
        self.assertEqual(
            to_RGBA(1),
            NotImplemented
        )


class TestToHEXA(unittest.TestCase):
    def setUp(self) -> None:
        self.hexa_res = HEXA('#214df599')

    def test_is_already_hexa_lowercase(self):
        self.assertEqual(
            to_HEXA(self.hexa_res),
            self.hexa_res
        )

    def test_is_already_hexa_uppercase(self):
        self.assertEqual(
            to_HEXA(HEXA(str(self.hexa_res).upper())),
            self.hexa_res
        )

    def test_from_rgb(self):
        self.assertEqual(
            to_HEXA(RGB(33, 77, 245)),
            self.hexa_res
        )

    def test_from_hex_lowercase(self):
        self.assertEqual(
            to_HEXA(HEX('#214df5')),
            self.hexa_res
        )

    def test_from_hex_uppercase(self):
        self.assertEqual(
            to_HEXA(HEX('#214DF5')),
            self.hexa_res
        )

    def test_from_hsv(self):
        self.assertEqual(
            to_HEXA(HSV(228, 0.865, 0.960)),
            self.hexa_res
        )

    def test_from_hsl(self):
        self.assertEqual(
            to_HEXA(HSL(228, 0.913, 0.545)),
            self.hexa_res
        )

    def test_from_cmyk(self):
        self.assertEqual(
            to_HEXA(CMYK(0.865, 0.685, 0, 0.039)),
            self.hexa_res
        )

    def test_from_rgba(self):
        self.assertEqual(
            to_HEXA(RGBA(33, 77, 245, 60)),
            self.hexa_res
        )

    def test_from_other_type(self):
        self.assertEqual(
            to_HEXA(1),
            NotImplemented
        )

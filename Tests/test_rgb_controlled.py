# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import unittest

# Custom Library

# Custom Packages
from AthenaColor.data import colors_html
from AthenaColor.models.rgb_controlled import RgbControlled

# ----------------------------------------------------------------------------------------------------------------------
# - TestRGBControlled -
# ----------------------------------------------------------------------------------------------------------------------
class TestRGBControlled(unittest.TestCase):
    def setUp(self):
        self.rgb_controlled = RgbControlled('38;2;')

    def tearDown(self):
        self.rgb_controlled = None

    def test_RgbControlled(self):
        self.assertEqual(
            self.rgb_controlled.custom((13, 24, 56)),
            '\x1b[38;2;13;24;56m'
        )

    def test_all_colors(self):
        r = RgbControlled(';')
        rgb_controlled_vars = dict(
            map(
                lambda x: (x[0].lower(), x[1]),
                filter(
                    lambda x: x[0][0].isupper() and isinstance(x[1], property),
                    vars(RgbControlled).items()
                )
            )
        )

        for color_name, color_values in filter(
                lambda x: x[0].isupper(), vars(colors_html).items()
        ):
            color_name = color_name.lower()
            with self.subTest(msg=f'color-correct[{color_name}]'):
                self.assertIn(color_name, rgb_controlled_vars)
                self.assertEqual(
                    rgb_controlled_vars[color_name].__get__(r),
                    f'\x1b[;{";".join(map(str, color_values))}m'
                )

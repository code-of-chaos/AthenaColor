# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import unittest

# Custom Library

# Custom Packages
from AthenaColor.models.rgb_controlled_nested import RgbControlledNested
from AthenaColor.models.rgb_controlled_nested import RgbControlled

# ----------------------------------------------------------------------------------------------------------------------
# - TestRGBControlledNested -
# ----------------------------------------------------------------------------------------------------------------------
class TestRGBControlledNested(unittest.TestCase):
    def setUp(self):
        self.rgb_controlled_nested = RgbControlledNested(
            RgbControlled('38;2;'),
            '\x1b[0m'
        )
        self.testcases = (
            (('1', (13, 24, 56)), '\x1b[38;2;13;24;56m1\x1b[0m'),
            (
                ('1', '2', '3', (13, 24, 56)),
                '\x1b[38;2;13;24;56m1 \x1b[0m\x1b[38;2;13;24;56m2'\
                    ' \x1b[0m\x1b[38;2;13;24;56m3\x1b[0m'
            ),
            (
                ('1', '2', '3', (13, 24, 56), '+'),
                '\x1b[38;2;13;24;56m1+\x1b[0m\x1b[38;2;13;24;56m2+'\
                    '\x1b[0m\x1b[38;2;13;24;56m3\x1b[0m'
            )
        )


    def test_rgb_controlled_nested(self):
        for input_values, result in self.testcases:
            if isinstance(input_values[-2], tuple):
                obj = input_values[:-2]
                color = input_values[-2]
                sep = input_values[-1]
            else:
                obj = input_values[:-1]
                color = input_values[-1]
                sep = ' '

            with self.subTest(msg=result):
                self.assertEqual(
                    self.rgb_controlled_nested.custom(*obj, color=color, sep=sep),
                    result
                )

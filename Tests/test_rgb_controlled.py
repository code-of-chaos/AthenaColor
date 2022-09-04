# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import unittest

# Custom Library

# Custom Packages
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

# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library
from AthenaColor import *
from AthenaColor.func.blend_modes import *


# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Functions_BlendModes(unittest.TestCase):
    def test_blend_normal(self):
        self.assertEqual(
            RGBA(255,255,255,255),
            blend_normal(RGB(128,128,128), RGB(255,255,255))
        )

    def test_blend_multiply(self):
        self.assertEqual(
            RGBA(82, 77, 45,255),
            blend_multiply(RGB(246, 231, 134), RGB(85,85,85))
        )
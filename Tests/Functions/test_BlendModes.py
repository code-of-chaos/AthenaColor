# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library
from AthenaColor.Objects.Color.ColorSystem import RGB, RGBA
from AthenaColor.Functions.BlendModes import blend_normal


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
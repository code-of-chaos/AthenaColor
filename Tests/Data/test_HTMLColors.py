# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library
from AthenaColor.Data.HtmlColors import HtmlColorObjects, HtmlColorTuples


# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Data_HtmlColors(unittest.TestCase):
    def test_HtmlColors(self):
        for k,v in vars(HtmlColorTuples).items():
            if not k.startswith("__"):
                with self.subTest(k=k, v=v): # thanks for showing me, tedthetwonk
                    self.assertEqual(vars(HtmlColorObjects)[k], v)


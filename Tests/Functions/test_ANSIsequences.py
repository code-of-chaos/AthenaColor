# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library
from AthenaColor.func.ansi_sequences import *

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Functions_ANSISequences(unittest.TestCase):
    @staticmethod
    def nested(nested):
        return color_sequence_nested(("This is a test",
                                      nested), color_code="\033[38;2;128;0;0m", reset_code="\033[0m", sep="\n")

    def test_ColorSequence(self):
        self.assertEqual(
            color_sequence("38;2;128;0;0"),
            "[38;2;128;0;0m"
        )
        self.assertEqual(
            color_sequence(0),
            "[0m"
        )

    def test_NestedColorSequence(self):
        self.assertEqual(
            color_sequence_nested(("This is a test",
                                   "For real"), color_code="\033[38;2;128;0;0m", reset_code="\033[0m", sep="\n"),
f"""[38;2;128;0;0mThis is a test
[0m[38;2;128;0;0mFor real[0m"""
        )
        self.assertEqual(
            self.nested(self.nested(
                color_sequence_nested(("This is a test",
                                       "For real"), color_code="\033[38;2;128;0;0m", reset_code="\033[0m", sep="\n"))),
f"""[38;2;128;0;0mThis is a test
[0m[38;2;128;0;0m[38;2;128;0;0mThis is a test
[0m[38;2;128;0;0m[38;2;128;0;0mThis is a test
[0m[38;2;128;0;0mFor real[0m[0m[0m"""
            )
# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library
from AthenaColor.Data.General import EscCodes, ConsoleCodes

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Data_ANSIcodes(unittest.TestCase):
    def test_EscCodes(self):
        self.assertEqual(EscCodes.hex,"\x1b")
        self.assertEqual(EscCodes.octal,"\033")
        self.assertEqual(EscCodes.uni,"\u001b")

    def test_ConsoleCodes(self):
        self.assertEqual(ConsoleCodes.cursor_line_up, "A")
        self.assertEqual(ConsoleCodes.cursor_line_down, "B")
        self.assertEqual(ConsoleCodes.cursor_right, "C")
        self.assertEqual(ConsoleCodes.cursor_left, "D")
        self.assertEqual(ConsoleCodes.cursor_line_next, "E")
        self.assertEqual(ConsoleCodes.cursor_line_previous, "F")
        self.assertEqual(ConsoleCodes.cursor_to_column, "G")
        self.assertEqual(ConsoleCodes.color, "m")
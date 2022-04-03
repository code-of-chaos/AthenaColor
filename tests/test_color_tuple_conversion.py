# XXX Mock out typing test decorators?

from __future__ import annotations

import unittest

from AthenaColor.Functions.ColorTupleConversion import (
    hex_to_rgb
)


class TestHexToRgb(unittest.TestCase):
    def setUp(self) -> None:
        self.rgb_res = (12, 34, 56)

    def test_starts_with_hashtag_and_correct_length_lowercase(self):
        self.assertEqual(
            hex_to_rgb('#0c2238'),
            self.rgb_res
        )

    def test_starts_with_hashtag_and_correct_length_uppercase(self):
        self.assertEqual(
            hex_to_rgb('#0C2238'),
            self.rgb_res
        )

    def test_not_starting_with_hashtag_but_coorect_length_lowercase(self):
        self.assertEqual(
            hex_to_rgb('0c2238'),
            self.rgb_res
        )

    def test_not_starting_with_hashtag_but_coorect_length_uppercase(self):
        self.assertEqual(
            hex_to_rgb('0C2238'),
            self.rgb_res
        )

    def test_starts_with_hashtag_and_incorrect_length(self):
        with self.assertRaises(TypeError) as eh:
            hex_to_rgb('#3')
        self.assertTrue(isinstance(eh.exception, TypeError))

    def test_not_starting_with_hashtag_and_incorrect_length(self):
        with self.assertRaises(ValueError) as eh:
            hex_to_rgb('3')
        self.assertTrue(isinstance(eh.exception, ValueError))

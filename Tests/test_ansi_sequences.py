import unittest

from AthenaColor.func.ansi_sequences import color_sequence
from AthenaColor.func.ansi_sequences import color_sequence_nested
from AthenaColor.func.ansi_sequences import color_sequence_nested_no_reset


class TestColorSequence(unittest.TestCase):
    def test_color_sequence(self):
        for value, result in (
                ('123', '\x1b[123m'),
                (123, '\x1b[123m')
        ):
            with self.subTest(msg=f'{value}-{result}'):
                self.assertEqual(color_sequence(value), result)


class TestColorSequenceNested(unittest.TestCase):
    def setUp(self):
        self.testcases = (
            ((('1',), '\x1b[2m', '\x1b[0m'), '\x1b[2m1\x1b[0m'),
            (
                (('1', '2', '3'), '\x1b[4m', '\x1b[0m'),
                '\x1b[4m1 \x1b[0m\x1b[4m2 \x1b[0m\x1b[4m3\x1b[0m'
            ),
            (
                (('1', '2', '3'), '\x1b[4m', '\x1b[0m', '+'),
                '\x1b[4m1+\x1b[0m\x1b[4m2+\x1b[0m\x1b[4m3\x1b[0m'
            ),
        )

    def tearDown(self):
        self.testcases = None

    def test_color_sequence_nested(self):
        for input_vals, result in self.testcases:
            with self.subTest(msg=f'{input_vals!r}-{result}'):
                self.assertEqual(color_sequence_nested(*input_vals), result)


class TestColorSequenceNestedNoReset(unittest.TestCase):
    def setUp(self):
        self.testcases = (
            ((('1',), '\x1b[2m'), '\x1b[2m1'),
            (
                (('1', '2', '3'), '\x1b[4m'),
                '\x1b[4m1 \x1b[4m2 \x1b[4m3'
            ),
            (
                (('1', '2', '3'), '\x1b[4m', '+'),
                '\x1b[4m1+\x1b[4m2+\x1b[4m3'
            ),
        )

    def tearDown(self):
        self.testcases = None

    def test_color_sequence_nested_no_reset(self):
        for input_vals, result in self.testcases:
            with self.subTest(msg=f'{input_vals!r}-{result}'):
                self.assertEqual(color_sequence_nested_no_reset(*input_vals), result)


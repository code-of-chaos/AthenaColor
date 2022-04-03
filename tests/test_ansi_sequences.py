from __future__ import annotations

import unittest

from AthenaColor import init
import AthenaColor.Data.ConsoleCodes as ConsoleCodes


from AthenaColor.Functions.AnsiSquences import (
    ColorSequence,
    NestedColorSequence
)


class TestColorSequence(unittest.TestCase):
    def test_code_str(self):
        self.assertEqual(ColorSequence('123'), f'{init.esc}[123{ConsoleCodes.color}')

    def test_code_int(self):
        self.assertEqual(ColorSequence(123), f'{init.esc}[123{ConsoleCodes.color}')

    def test_code_none(self):
        # TODO define exception type and message
        with self.assertRaises(Exception) as eh:
            ColorSequence(None)
        self.assertTrue(isinstance(eh.exception, Exception))


class TestNestedColorSequence(unittest.TestCase):
    def test_no_objs(self):
        self.assertEqual(NestedColorSequence(control_code=123), '')

    def test_one_obj(self):
        self.assertEqual(
            NestedColorSequence(' LOL ', control_code=123, reset_code=321),
            '\x1b[123m LOL \x1b[321m'
        )

    def test_multiple_objs_with_no_reset_code_and_no_sep(self):
        self.assertEqual(
            NestedColorSequence(0, 3, 4, 5, control_code=123),
            '\x1b[123m0 \x1b[123m3 \x1b[123m4 \x1b[123m5'
        )

    def test_multiple_objs_full_param_list(self):
        self.assertEqual(
            NestedColorSequence(0, 3, 4, 5, control_code=123, reset_code=321, sep='(^-^)'),
            '\x1b[123m0\x1b[321m(^-^)\x1b[123m3\x1b[321m(^-^)\x1b[123m4\x1b[321m(^-^)\x1b[123m5\x1b[321m'
        )

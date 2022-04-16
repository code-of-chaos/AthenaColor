from __future__ import annotations

import unittest


from AthenaColor.Functions.AnsiSquences import (
    ColorSequence,
    NestedColorSequence
)


class TestColorSequence(unittest.TestCase):
    def test_type_int(self):
        self.assertEqual(ColorSequence(0), '\x1b[0m')

    def test_type_string_empty(self):
        self.assertEqual(ColorSequence(''), '\x1b[m')

    def test_type_string(self):
        self.assertEqual(ColorSequence('123'), '\x1b[123m')


# TODO more testing when nested
# TODO mocking?
class TestNestedColorSequence(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.longMessage = False

    def assertEmptyString(self, first, msg=None):
        if msg is not None:
            self.assertEqual(first, '', msg)
        else:
            self.assertEqual(first, '')

    def setUp(self) -> None:
        self.control_code = 42
        self.reset_code = 54
        self.sep = '--'

    def tearDown(self) -> None:
        self.control_code = self.reset_code = self.sep = None

    # BUG control_code should be keyword_argument with check for None
    def test_no_objs_no_args(self):
        with self.assertRaisesRegex(
                ValueError,
                'control_code parameter has to be set'
        ) as teh:
            NestedColorSequence()
        self.assertIsInstance(teh.exception, ValueError)

    def test_no_objs_with_cc(self):
        self.assertEmptyString(NestedColorSequence(control_code=42))

    def test_no_objs_with_cc_rc(self):
        self.assertEmptyString(
            NestedColorSequence(
                control_code=self.control_code,
                reset_code=self.reset_code
            )
        )

    def test_no_objs_with_cc_rc_sep(self):
        self.assertEmptyString(
            NestedColorSequence(
                control_code=self.control_code,
                reset_code=self.reset_code,
                sep=self.sep
            )
        )

    # BUG control_code should be keyword_argument with check for None
    def test_one_obj_no_args(self):
        with self.assertRaisesRegex(
                ValueError,
                'control_code parameter has to be set'
        ) as teh:
            NestedColorSequence('123')
        self.assertIsInstance(teh.exception, ValueError)

    def test_one_obj_with_cc(self):
        self.assertEqual(
            NestedColorSequence('123', control_code=self.control_code),
            '\x1b[42m123'
        )

    def test_one_obj_with_cc_rc(self):
        self.assertEqual(
            NestedColorSequence(
                '123',
                control_code=self.control_code,
                reset_code=self.reset_code
            ),
            '\x1b[42m123\x1b[54m'
        )

    def test_one_obj_with_cc_rc_sep(self):
        self.assertEqual(
            NestedColorSequence(
                '123',
                control_code=self.control_code,
                reset_code=self.reset_code,
                sep=self.sep
            ),
            '\x1b[42m123\x1b[54m'
        )

    # BUG control_code should be keyword_argument with check for None
    def test_multiple_objs_no_args(self):
        with self.assertRaisesRegex(
                ValueError,
                'control_code parameter has to be set'
        ) as teh:
            NestedColorSequence('123, 456', '789', '010')
        self.assertIsInstance(teh.exception, ValueError)

    def test_multiple_objs_with_cc(self):
        self.assertEqual(
            NestedColorSequence(
                '123', 456, True, None,
                control_code=self.control_code
            ),
            '\x1b[42m123\x1b[42m \x1b[42m456\x1b[42m '
            '\x1b[42mTrue\x1b[42m \x1b[42mNone'
        )

    def test_multiple_objs_with_cc_rc(self):
        self.assertEqual(
            NestedColorSequence(
                '123', 456, True, None,
                control_code=self.control_code,
                reset_code=self.reset_code
            ),
            '\x1b[42m123\x1b[54m\x1b[42m \x1b[54m\x1b[42m456\x1b[54m'
            '\x1b[42m \x1b[54m\x1b[42mTrue\x1b[54m\x1b[42m \x1b[54m'
            '\x1b[42mNone\x1b[54m'
        )

    def test_multiple_obj_with_cc_rc_sep(self):
        self.assertEqual(
            NestedColorSequence(
                '123', 456, True, None,
                control_code=self.control_code,
                reset_code=self.reset_code,
                sep=self.sep
            ),
            '\x1b[42m123\x1b[54m\x1b[42m--\x1b[54m'
            '\x1b[42m456\x1b[54m\x1b[42m--\x1b[54m'
            '\x1b[42mTrue\x1b[54m\x1b[42m--\x1b[54m'
            '\x1b[42mNone\x1b[54m'
        )

    def test_nested_with_one_obj_per_level_and_cc(self):
        self.assertEqual(
            NestedColorSequence(
                'def', NestedColorSequence(
                    'abc',
                    control_code=self.control_code + 1
                ),
                control_code=self.control_code
            ),
            '\x1b[42mdef\x1b[42m \x1b[42m\x1b[43mabc'
        )

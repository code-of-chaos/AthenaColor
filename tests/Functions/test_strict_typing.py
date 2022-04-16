# TODO Test more types?

from __future__ import annotations

from typing import Iterable
from typing import Union


import unittest


from AthenaColor.Functions.StrictTyping import (
    StrictError,
    StrictType,
    StrictInput,
    StrictOutput
)


class TestStrictType(unittest.TestCase):
    def setUp(self) -> None:
        self.pass_values = [
            (int, 5),
            (int, (5, 6, 7, 8)),
            (str, 'Hello World'), # HACK:FIXME string is an iterable
            (str, ('Hello World',)),
            ((int, float), (345, 6.34)),
            ((str, int), ('1', 2))
        ]
        self.fail_values = [
            (int, 5.5),
            (int, (5, 6.6, '123')),
            (str, True),
            (str, (123, 'Hello World')),
            ((int, float), 'LOL'),
            ((str, int), (123, 'Hello World', 0.1))
        ]

    def tearDown(self) -> None:
        self.pass_values = self.fail_values = None

    def test_strict_type_pass(self):
        for test_id, input_ in enumerate(self.pass_values, 1):
            with self.subTest(f'test_strict_type_pass {test_id}', input_=input_):
                StrictType(*input_)

    def test_strict_type_fail(self):
        for test_id, input_ in enumerate(self.fail_values, 1):
            with self.subTest(f'test_strict_type_fail {test_id}', input_=input_):
                with self.assertRaisesRegex(
                        StrictError,
                        f'Arguments don\'t fullfil type specs: {input_[:-1]}'
                ) as teh:
                    StrictType(*input_)
                self.assertIsInstance(teh.exception, StrictError)


class TestStrictInput(unittest.TestCase):
    def test_int(self):
        @StrictInput.int
        def helper(x: int) -> int:
            return x + 1

        with self.subTest(f'test_int_pass'):
            helper(1)

        with self.subTest(f'test_int_fail'):
            with self.assertRaisesRegex(
                    StrictError,
                    'Arguments don\'t fullfill type specs: (<class int>,)'
            ) as teh:
                helper(1.1)
            self.assertIsInstance(teh.exception, StrictError)

    def test_float(self):
        @StrictInput.float
        def helper(x: float) -> float:
            return x + 1

        with self.subTest(f'test_float_pass'):
            helper(1.1)

        with self.subTest(f'test_float_fail'):
            with self.assertRaisesRegex(
                    StrictError,
                    'Arguments don\'t fullfill type specs: (<class float>,)'
            ) as teh:
                helper(1)
            self.assertIsInstance(teh.exception, StrictError)

    def test_str(self):
        @StrictInput.str
        def helper(x: str) -> str:
            return x.upper()

        with self.subTest(f'test_str_pass'):
            helper('hello world')

        with self.subTest(f'test_str_fail'):
            with self.assertRaisesRegex(
                    StrictError,
                    'Arguments don\'t fullfill type specs: (<class str>,)'
            ) as teh:
                helper(1)
            self.assertIsInstance(teh.exception, StrictError)

    def test_number(self):
        @StrictInput.number
        def helper(x: Union[int, float]) -> Union[int, float]:
            return x + 1

        for test_id, input_ in enumerate([1, 1.1], 1):
            with self.subTest(f'test_number_pass {test_id}'):
                helper(input_)

        with self.subTest(f'test_number_fail'):
            with self.assertRaisesRegex(
                    StrictError,
                    'Arguments don\'t fullfill type specs: (<class float>, <class int>)'
            ) as teh:
                helper('abc')
            self.assertIsInstance(teh.exception, StrictError)

    # TODO more types?
    # TODO intended design?
    def test_custom(self):
        @StrictInput.Custom(tuple[int, int])
        def helper(x: tuple[int, int]) -> int:
            return x[0] + x[1]

        with self.subTest('test_custom(tuple[int, int])_pass'):
            helper((1, 2))

        with self.subTest('test_custom(tuple[int, int])_fail'):
            # TODO Error message?
            with self.assertRaisesRegex(
                    StrictError,
                    'Arguments don\'t fullfill type specs: (tuple[int, int])'
            ) as teh:
                helper('abc')
            self.assertIsInstance(teh.exception, StrictError)


class TestStrictOutput(unittest.TestCase):
    def test_int(self):
        @StrictOutput.int
        def helper(x: Union[int, float]) -> int:
            return x + 1

        with self.subTest('test_int_pass'):
            helper(1)

        with self.subTest('test_int_fail'):
            with self.assertRaisesRegex(
                    StrictError,
                    'Return doesn\'t fullfill type specs: (<class int>,)'
            ):
                helper(1.1)

    def test_float(self):
        @StrictOutput.float
        def helper(x: Union[int, float]) -> float:
            return x + 1

        with self.subTest('test_float_pass'):
            helper(1.1)

        # TODO Don't know if this should raise an axception, right know it doesn't
        # if it should'nt raise an exception delete this block
        with self.subTest('test_float_fail'):
            with self.assertRaisesRegex(
                    StrictError,
                    'Return doesn\'t fullfill type specs: (<class float>,)'
            ):
                helper(1)

    def test_str(self):
        @StrictOutput.str
        def helper(x: Iterable) -> str:
            if len(x) >= 1:
                return x[0]
            return x

        with self.subTest('test_str_pass'):
            helper("Hallo Welt")

        with self.subTest('test_str_fail'):
            with self.assertRaisesRegex(
                    StrictError,
                    'Return doesn\'t fullfill type specs: (<class str>,)'
            ):
                helper([1, 2, 3])

    # TODO more types?
    # TODO intended design?
    def test_custom(self):
        @StrictOutput.Custom(tuple[int, int])
        def helper(x: int) -> tuple[int, int]:
            return (x, x * -1)

        with self.subTest('test_custom(tuple[int, int])_pass'):
            helper(5)

        with self.subTest('test_custom(tuple[int, int])_fail'):
            # TODO Error message?
            with self.assertRaisesRegex(
                    StrictError,
                    'Arguments don\'t fullfill type specs: (tuple[int, int])'
            ) as teh:
                helper(5.5)
            self.assertIsInstance(teh.exception, StrictError)

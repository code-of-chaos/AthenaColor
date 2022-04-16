# TODO test more types?
# TODO general cleanup with the intention of the library priority

from __future__ import annotations

import unittest


from AthenaColor.Functions.DunderFunctions import (
    add,
    sub,
    mul,
    floordiv,
    truediv,
    mod,
    pow,
    gt,
    lt,
    eq,
    ne,
    le,
    ge
)


class TestAdd(unittest.TestCase):
    def setUp(self) -> None:
        self.values = (
            ((1, 2), 3),
            (('abc', 'def'), ('ad', 'be', 'cf')),
            ((('abc',), ('def',)), ('abcdef',)),
            (((1.12,), (2.21,)), (3.33,)),
        )

    def tearDown(self) -> None:
        self.values = None

    def test_add(self):
        for test_id, (input_, output) in enumerate(self.values, 1):
            with self.subTest(f'test_add {test_id}', input_=input_):
                self.assertEqual(add(*input_), output)

    # TODO define type and message of exception (if raised)
    def test_add_iterables_with_different_length(self):
        with self.assertRaisesRegex(
                ValueError,
                'Iterable arguments must have same length'
        ) as teh:
            add((1, 2, 3), (1,))
        self.assertIsInstance(teh.exception, ValueError)


class TestSub(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [
            ((1, 2), -1),
            (((1.12,), (2.22,)), (-1.1,)),
        ]
        self.throws_exception_values = [
            ('abc', 'def'),
            (('abc',), ('def',))
        ]

    def tearDown(self) -> None:
        self.values = self.throws_exception_values = None

    # FIXME don't know how to name it yet, improving in the future
    def test_sub_throws_exception(self):
        for test_id, input_ in enumerate(self.throws_exception_values, 1):
            with self.subTest(f'test_sub_fails {test_id}', input_=input_):
                # TODO define type and message of exception (if raised)
                with self.assertRaises(ValueError) as teh:
                    sub(*input_)
                self.assertIsInstance(teh.exception, ValueError)

    def test_sub(self):
        for test_id, (input_, output) in enumerate(self.values, 1):
            with self.subTest(f'test_sub {test_id}', input_=input_):
                self.assertEqual(sub(*input_), output)

    # TODO define type and message of exception (if raised)
    def test_sub_iterables_with_different_length(self):
        with self.assertRaisesRegex(
                ValueError,
                'Iterable arguments must have same length'
        ) as teh:
            sub((1, 2, 3), (1,))
        self.assertIsInstance(teh.exception, ValueError)


class TestMul(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [
            ((1, 2), 2),
            (('abc', 3), 'abcabcabc'),
            ((('abc',), (3,)), ('abcabcabc',)),
            (((1.12,), (2,)), (2.24,)),
        ]

    def tearDown(self) -> None:
        self.values = None

    def test_mul(self):
        for test_id, (input_, output) in enumerate(self.values, 1):
            with self.subTest(f'test_mul {test_id}', input_=input_):
                self.assertEqual(mul(*input_), output)

    def test_mul_iterables_with_different_length(self):
        with self.assertRaisesRegex(
                ValueError,
                'Iterable arguments must have same length'
        ) as teh:
            mul((1, 2, 3), (1,))
        self.assertIsInstance(teh.exception, ValueError)


class TestFloordiv(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [
            ((1, 2), 0),
            (((1,), (2,)), (0,)),
        ]
        self.throws_exception_values = [
            ('abc', 'def'),
            (('abc',), ('def',))
        ]

    def tearDown(self) -> None:
        self.values = self.throws_exception_values = None

    # FIXME don't know how to name it yet, improving in the future
    def test_floordiv_throws_exception(self):
        for test_id, input_ in enumerate(self.throws_exception_values, 1):
            with self.subTest(f'test_floordiv_fails {test_id}', input_=input_):
                # TODO define type and message of exception (if raised)
                with self.assertRaises(ValueError) as teh:
                    floordiv(*input_)
                self.assertIsInstance(teh.exception, ValueError)

    def test_floordiv(self):
        for test_id, (input_, output) in enumerate(self.values, 1):
            with self.subTest(f'test_floordiv {test_id}', input_=input_):
                self.assertEqual(floordiv(*input_), output)

    # TODO define type and message of exception (if raised)
    def test_floordiv_iterables_with_different_length(self):
        with self.assertRaisesRegex(
                ValueError,
                'Iterable arguments must have same length'
        ) as teh:
            floordiv((1, 2, 3), (1,))
        self.assertIsInstance(teh.exception, ValueError)


class TestTruediv(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [
            ((1, 2), 0.5),
            (((1,), (2,)), (0.5,)),
        ]
        self.throws_exception_values = [
            ('abc', 'def'),
            (('abc',), ('def',))
        ]

    def tearDown(self) -> None:
        self.values = self.throws_exception_values = None

    # FIXME don't know how to name it yet, improving in the future
    def test_truediv_throws_exception(self):
        for test_id, input_ in enumerate(self.throws_exception_values, 1):
            with self.subTest(f'test_truediv_fails {test_id}', input_=input_):
                # TODO define type and message of exception (if raised)
                with self.assertRaises(ValueError) as teh:
                    truediv(*input_)
                self.assertIsInstance(teh.exception, ValueError)

    def test_truediv(self):
        for test_id, (input_, output) in enumerate(self.values, 1):
            with self.subTest(f'test_truediv {test_id}', input_=input_):
                self.assertEqual(truediv(*input_), output)

    # TODO define type and message of exception (if raised)
    def test_truediv_iterables_with_different_length(self):
        with self.assertRaisesRegex(
                ValueError,
                'Iterable arguments must have same length'
        ) as teh:
            truediv((1, 2, 3), (1,))
        self.assertIsInstance(teh.exception, ValueError)


class TestMod(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [
            ((1, 2), 1),
            (((1,), (2,)), (1,)),
        ]
        self.throws_exception_values = [
            ('abc', 'def'),
            (('abc',), ('def',))
        ]

    def tearDown(self) -> None:
        self.values = self.throws_exception_values = None

    # FIXME don't know how to name it yet, improving in the future
    def test_mod_throws_exception(self):
        for test_id, input_ in enumerate(self.throws_exception_values, 1):
            with self.subTest(f'test_mod_fails {test_id}', input_=input_):
                # TODO define type and message of exception (if raised)
                with self.assertRaises(ValueError) as teh:
                    mod(*input_)
                self.assertIsInstance(teh.exception, ValueError)

    def test_mod(self):
        for test_id, (input_, output) in enumerate(self.values, 1):
            with self.subTest(f'test_mod {test_id}', input_=input_):
                self.assertEqual(mod(*input_), output)

    # TODO define type and message of exception (if raised)
    def test_mod_iterables_with_different_length(self):
        with self.assertRaisesRegex(
                ValueError,
                'Iterable arguments must have same length'
        ) as teh:
            mod((1, 2, 3), (1,))
        self.assertIsInstance(teh.exception, ValueError)


# FIXME:BUG shadows builtin pow() function
class TestPow(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [
            ((2, 2), 4),
            (((2,), (2,)), (4,)),
        ]
        self.throws_exception_values = [
            ('abc', 'def'),
            (('abc',), ('def',))
        ]

    def tearDown(self) -> None:
        self.values = self.throws_exception_values = None

    # FIXME don't know how to name it yet, improving in the future
    def test_pow_throws_exception(self):
        for test_id, input_ in enumerate(self.throws_exception_values, 1):
            with self.subTest(f'test_pow_fails {test_id}', input_=input_):
                # TODO define type and message of exception (if raised)
                with self.assertRaises(ValueError) as teh:
                    pow(*input_)
                self.assertIsInstance(teh.exception, ValueError)

    def test_pow(self):
        for test_id, (input_, output) in enumerate(self.values, 1):
            with self.subTest(f'test_pow {test_id}', input_=input_):
                self.assertEqual(pow(*input_), output)

    # TODO define type and message of exception (if raised)
    def test_pow_iterables_with_different_length(self):
        with self.assertRaisesRegex(
                ValueError,
                'Iterable arguments must have same length'
        ) as teh:
            pow((1, 2, 3), (1,))
        self.assertIsInstance(teh.exception, ValueError)


class TestGt(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [
            ((3, 2), True),
            (((3,), (2,)), True),
            (((32, 43, 54), (56, 67, 21)), False)
        ]

    def tearDown(self) -> None:
        self.values = None

    def test_gt(self):
        for test_id, (input_, output) in enumerate(self.values, 1):
            with self.subTest(f'test_gt {test_id}', input_=input_):
                self.assertEqual(gt(*input_), output)

    # TODO define type and message of exception (if raised)
    def test_gt_iterables_with_different_length(self):
        with self.assertRaisesRegex(
                ValueError,
                'Iterable arguments must have same length'
        ) as teh:
            gt((1, 2, 3), (1,))
        self.assertIsInstance(teh.exception, ValueError)


class TestLt(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [
            ((2, 3), True),
            (((3,), (2,)), False),
            (((32, 43, 54), (43, 65, 210)), True)
        ]

    def tearDown(self) -> None:
        self.values = None

    def test_lt(self):
        for test_id, (input_, output) in enumerate(self.values, 1):
            with self.subTest(f'test_lt {test_id}', input_=input_):
                self.assertEqual(lt(*input_), output)

    # TODO define type and message of exception (if raised)
    def test_lt_iterables_with_different_length(self):
        with self.assertRaisesRegex(
                ValueError,
                'Iterable arguments must have same length'
        ) as teh:
            lt((1, 2, 3), (1,))
        self.assertIsInstance(teh.exception, ValueError)


class TestEq(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [
            ((2, 2), True),
            (((3,), (2,)), False),
            (((32, 43, 54), (0, 43, 21)), False)
        ]

    def tearDown(self) -> None:
        self.values = None

    def test_eq(self):
        for test_id, (input_, output) in enumerate(self.values, 1):
            with self.subTest(f'test_eq {test_id}', input_=input_):
                self.assertEqual(eq(*input_), output)

    def test_eq_iterables_with_different_length(self):
        with self.assertRaisesRegex(
                ValueError,
                'Iterable arguments must have same length'
        ) as teh:
            eq((1, 2, 3), (1,))
        self.assertIsInstance(teh.exception, ValueError)


class TestNe(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [
            ((2, 2), False),
            (((3,), (2,)), True),
            (((32, 43, 54), (0, 43, 21)), False)
        ]

    def tearDown(self) -> None:
        self.values = None

    def test_ne(self):
        for test_id, (input_, output) in enumerate(self.values, 1):
            with self.subTest(f'test_ne {test_id}', input_=input_):
                self.assertEqual(ne(*input_), output)

    # TODO define type and message of exception (if raised)
    def test_ne_iterables_with_different_length(self):
        with self.assertRaisesRegex(
                ValueError,
                'Iterable arguments must have same length'
        ) as teh:
            ne((1, 2, 3), (1,))
        self.assertIsInstance(teh.exception, ValueError)


class TestLe(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [
            ((2, 2), True),
            (((3,), (2,)), False),
            (((32, 43, 54), (0, 43, 56)), False)
        ]

    def tearDown(self) -> None:
        self.values = None

    def test_le(self):
        for test_id, (input_, output) in enumerate(self.values, 1):
            with self.subTest(f'test_le {test_id}', input_=input_):
                self.assertEqual(le(*input_), output)

    # TODO define type and message of exception (if raised)
    def test_le_iterables_with_different_length(self):
        with self.assertRaisesRegex(
                ValueError,
                'Iterable arguments must have same length'
        ) as teh:
            le((1, 2, 3), (1,))
        self.assertIsInstance(teh.exception, ValueError)


class TestGe(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [
            ((2, 2), True),
            (((3,), (2,)), True),
            (((32, 43, 54), (0, 43, 21)), True)
        ]

    def tearDown(self) -> None:
        self.values = None

    def test_ge(self):
        for test_id, (input_, output) in enumerate(self.values, 1):
            with self.subTest(f'test_ge {test_id}', input_=input_):
                self.assertEqual(ge(*input_), output)

    # TODO define type and message of exception (if raised)
    def test_ge_iterables_with_different_length(self):
        with self.assertRaisesRegex(
                ValueError,
                'Iterable arguments must have same length'
        ) as teh:
            ge((1, 2, 3), (1,))
        self.assertIsInstance(teh.exception, ValueError)

# XXX How to test all possibilities?

from __future__ import annotations

import unittest


from AthenaColor.Functions.ColorSystemDunders import (
    add,
    eq,
    floordiv,
    ge,
    gt,
    le,
    lt,
    mod,
    mul,
    ne,
    sub,
    truediv,
    pow
)


class TestAdd(unittest.TestCase):
    def test_noniterable_objs(self):
        with self.assertRaises(ValueError) as eh:
            add(1, 1)
        self.assertTrue(isinstance(eh.exception, ValueError))

    def test_unequal_obj_length(self):
        with self.assertRaises(TypeError) as eh:
            add((4, 5, 6), (1, ))
        self.assertTrue(isinstance(eh.exception), TypeError)

    def test_should_pass(self):
        self.assertEqual(
            add((1, 2, 3), (4, 5, 6)),
            (5, 7, 9)
        )


class TestSub(unittest.TestCase):
    def test_noniterable_objs(self):
        with self.assertRaises(ValueError) as eh:
            sub(1, 1)
        self.assertTrue(isinstance(eh.exception, ValueError))

    def test_unequal_obj_length(self):
        with self.assertRaises(TypeError) as eh:
            sub((4, 5, 6), (1, ))
        self.assertTrue(isinstance(eh.exception), TypeError)

    def test_should_pass(self):
        self.assertEqual(
            sub((1, 2, 3), (4, 5, 6)),
            (-3, -3, -3)
        )


class TestMul(unittest.TestCase):
    def test_noniterable_objs(self):
        with self.assertRaises(ValueError) as eh:
            mul(1, 1)
        self.assertTrue(isinstance(eh.exception, ValueError))

    def test_unequal_obj_length(self):
        with self.assertRaises(TypeError) as eh:
            mul((4, 5, 6), (1, ))
        self.assertTrue(isinstance(eh.exception), TypeError)

    def test_should_pass(self):
        self.assertEqual(
            mul((1, 2, 3), (4, 5, 6)),
            (4, 10, 18)
        )


class TestFloordiv(unittest.TestCase):
    def test_noniterable_objs(self):
        with self.assertRaises(ValueError) as eh:
            floordiv(1, 1)
        self.assertTrue(isinstance(eh.exception, ValueError))

    def test_unequal_obj_length(self):
        with self.assertRaises(TypeError) as eh:
            floordiv((4, 5, 6), (1, ))
        self.assertTrue(isinstance(eh.exception), TypeError)

    def test_should_pass(self):
        self.assertEqual(
            floordiv((1, 2, 3), (4, 5, 6)),
            (0, 0, 0)
        )


class TestTruediv(unittest.TestCase):
    def test_noniterable_objs(self):
        with self.assertRaises(ValueError) as eh:
            truediv(1, 1)
        self.assertTrue(isinstance(eh.exception, ValueError))

    def test_unequal_obj_length(self):
        with self.assertRaises(TypeError) as eh:
            truediv((4, 5, 6), (1, ))
        self.assertTrue(isinstance(eh.exception), TypeError)

    def test_should_pass(self):
        self.assertEqual(
            truediv((1, 2, 3), (4, 5, 6)),
            (0.25, 0.4, 0.5)
        )


class TestMod(unittest.TestCase):
    def test_noniterable_objs(self):
        with self.assertRaises(ValueError) as eh:
            mod(1, 1)
        self.assertTrue(isinstance(eh.exception, ValueError))

    def test_unequal_obj_length(self):
        with self.assertRaises(TypeError) as eh:
            mod((4, 5, 6), (1, ))
        self.assertTrue(isinstance(eh.exception), TypeError)

    def test_should_pass(self):
        self.assertEqual(
            mod((1, 2, 3), (4, 5, 6)),
            (1, 2, 3)
        )


# TODO rename function, collides with the builtin "pow"
class TestPow(unittest.TestCase):
    def test_noniterable_objs(self):
        with self.assertRaises(ValueError) as eh:
            pow(1, 1)
        self.assertTrue(isinstance(eh.exception, ValueError))

    def test_unequal_obj_length(self):
        with self.assertRaises(TypeError) as eh:
            pow((4, 5, 6), (1, ))
        self.assertTrue(isinstance(eh.exception), TypeError)

    def test_should_pass(self):
        self.assertEqual(
            pow((1, 2, 3), (4, 5, 6)),
            (0.25, 0.4, 0.5)
        )


class TestGt(unittest.TestCase):
    def test_noniterable_objs(self):
        with self.assertRaises(ValueError) as eh:
            gt(1, 1)
        self.assertTrue(isinstance(eh.exception, ValueError))

    def test_unequal_obj_length(self):
        with self.assertRaises(TypeError) as eh:
            gt((4, 5, 6), (1, ))
        self.assertTrue(isinstance(eh.exception), TypeError)

    def test_should_pass(self):
        self.assertFalse(gt((1, 2, 3), (4, 5, 6)))


class TestLt(unittest.TestCase):
    def test_noniterable_objs(self):
        with self.assertRaises(ValueError) as eh:
            lt(1, 1)
        self.assertTrue(isinstance(eh.exception, ValueError))

    def test_unequal_obj_length(self):
        with self.assertRaises(TypeError) as eh:
            lt((4, 5, 6), (1, ))
        self.assertTrue(isinstance(eh.exception), TypeError)

    def test_should_pass(self):
        self.assertTrue(lt((1, 2, 3), (4, 5, 6)))


class TestEq(unittest.TestCase):
    def test_noniterable_objs(self):
        with self.assertRaises(ValueError) as eh:
            eq(1, 1)
        self.assertTrue(isinstance(eh.exception, ValueError))

    def test_unequal_obj_length(self):
        with self.assertRaises(TypeError) as eh:
            eq((4, 5, 6), (1, ))
        self.assertTrue(isinstance(eh.exception), TypeError)

    def test_should_pass(self):
        self.assertFalse(eq((1, 2, 3), (4, 5, 6)))


class TestNe(unittest.TestCase):
    def test_noniterable_objs(self):
        with self.assertRaises(ValueError) as eh:
            ne(1, 1)
        self.assertTrue(isinstance(eh.exception, ValueError))

    def test_unequal_obj_length(self):
        with self.assertRaises(TypeError) as eh:
            ne((4, 5, 6), (1, ))
        self.assertTrue(isinstance(eh.exception), TypeError)

    def test_should_pass(self):
        self.assertTrue(ne((1, 2, 3), (4, 5, 6)))


class TestLe(unittest.TestCase):
    def test_noniterable_objs(self):
        with self.assertRaises(ValueError) as eh:
            le(1, 1)
        self.assertTrue(isinstance(eh.exception, ValueError))

    def test_unequal_obj_length(self):
        with self.assertRaises(TypeError) as eh:
            le((4, 5, 6), (1, ))
        self.assertTrue(isinstance(eh.exception), TypeError)

    def test_should_pass(self):
        self.assertTrue(le((1, 2, 3), (4, 5, 6)))


class TestGe(unittest.TestCase):
    def test_noniterable_objs(self):
        with self.assertRaises(ValueError) as eh:
            ge(1, 1)
        self.assertTrue(isinstance(eh.exception, ValueError))

    def test_unequal_obj_length(self):
        with self.assertRaises(TypeError) as eh:
            ge((4, 5, 6), (1, ))
        self.assertTrue(isinstance(eh.exception), TypeError)

    def test_should_pass(self):
        self.assertFalse(ge((1, 2, 3), (4, 5, 6)))
from __future__ import annotations

import unittest

from AthenaColor.Functions.BoilerPlate import (
    Constrain,
    NormalizeRgb,
    RoundHalfUp,
    TestTypes
)


class TestNormalizeRgb(unittest.TestCase):
    def test_params_in_range(self):
        self.assertEqual(
            NormalizeRgb(100, 150, 200),
            (0.39215686274509803, 0.5882352941176471, 0.7843137254901961)
        )

    def test_params_out_of_range(self):
        self.assertEqual(
            NormalizeRgb(-32, 300, 123),
            (0, 1, 0.4823529411764706)
        )


class TestTestTypes(unittest.TestCase):
    # TODO Fix via https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists
    def test_one_type_one_object_true(self):
        self.assertTrue(TestTypes(int, 1))

    # TODO Fix via https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists
    def test_multiple_types_one_object_true(self):
        self.assertTrue(TestTypes(int | float, 23.4))

    def test_multiple_types_multiple_objects_true(self):
        self.assertTrue(TestTypes(int | float, (23.4, 213)))

    # TODO Fix via https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists
    def test_one_type_one_object_false(self):
        self.assertFalse(TestTypes(int, 23.4))

    # TODO Fix via https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists
    def test_multiple_types_one_object_false(self):
        self.assertFalse(TestTypes(int | float, True))


    def test_multiple_types_multiple_object_false(self):
        self.assertFalse(TestTypes(int | float, (12, "23.4")))

    def test_should_fail_when_object_is_one_string(self):
        # TODO Fix via https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists
        # Shouldn't throw an error, only here as a symbol?
        with self.assertRaises(Exception) as eh:
            TestTypes(int, "23,824")
        self.assertTrue(isinstance(eh.exception, Exception))


class TestConstrain(unittest.TestCase):
    def test_constrain_to_min(self):
        self.assertEqual(Constrain(-234, 255, 0), 0)

    def test_constrain_to_max(self):
        self.assertEqual(Constrain(986, 255, 0), 255)

    def test_already_in_bounds(self):
        self.assertEqual(Constrain(100, 255, 0), 100)


class TestRoundCorrectly(unittest.TestCase):
    def setUp(self) -> None:
        self.tenths = [1 / 10 * i for i in range(11)]

    def test_round_correctly_1_n(self):
        self.assertEqual(
            [RoundHalfUp(1 + x) for x in self.tenths],
            [1 if x < 0.5 else 2 for x in self.tenths]
        )

    def test_round_correctly_1_n_float(self):
        self.assertEqual(
            [RoundHalfUp(1.5 + x) for x in self.tenths],
            [2 if x < 1.0 else 3 for x in self.tenths]
        )

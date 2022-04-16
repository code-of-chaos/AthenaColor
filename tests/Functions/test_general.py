from __future__ import annotations

import unittest


from AthenaColor.Functions.General import (
    Normalize,
    RoundToDecimals,
    RoundHalfUp
)


class TestNormalize(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [
            ((13,), 0.13),
            ((25, 1000), 0.025),
            ((255, 255), 1),
            ((111,), 1.11)
        ]

    def tearDown(self) -> None:
        self.values = None

    def test_normalize(self):
        for test_id, (input_, output) in enumerate(self.values, 1):
            with self.subTest(f'test_normalize {test_id}', input_=input_):
                self.assertEqual(Normalize(*input_), output)


class TestRoundToDecimals(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [
            ((2,), 2),
            ((2.1,), 2),
            ((2.2,), 2),
            ((2.3,), 2),
            ((2.4,), 2),
            ((2.5,), 2),
            ((2.6,), 3),
            ((2.7,), 3),
            ((2.8,), 3),
            ((2.9,), 3),
            ((3,), 3)
        ]
        self.decimal_values = [
            ((2,), 2),
            ((2.1,), 2.1),
            ((2.2,), 2.2),
            ((2.3,), 2.3),
            ((2.4,), 2.4),
            ((2.5,), 2.5),
            ((2.6,), 2.6),
            ((2.7,), 2.7),
            ((2.8,), 2.8),
            ((2.9,), 2.9),
            ((3,), 3)
        ]

    def tearDown(self) -> None:
        self.values = None

    def test_round_to_decimals_with_no_decimals(self):
        for test_id, (input_, output) in enumerate(self.values, 1):
            with self.subTest(f'test_normalize {test_id}', input_=input_):
                self.assertEqual(RoundToDecimals(*input_, 0), output)

    def test_round_to_decimals_with_decimals(self):
        for test_id, (input_, output) in enumerate(self.decimal_values, 1):
            with self.subTest(f'test_normalize {test_id}', input_=input_):
                self.assertEqual(RoundToDecimals(*input_), output)


class TestRoundHalfUp(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [
            ((2,), 2),
            ((2.1,), 2),
            ((2.2,), 2),
            ((2.3,), 2),
            ((2.4,), 2),
            ((2.5,), 3),
            ((2.6,), 3),
            ((2.7,), 3),
            ((2.8,), 3),
            ((2.9,), 3),
            ((3,), 3)
        ]

    def tearDown(self) -> None:
        self.values = None

    def test_round_half_up(self):
        for test_id, (input_, output) in enumerate(self.values, 1):
            with self.subTest(f'test_normalize {test_id}', input_=input_):
                self.assertEqual(RoundHalfUp(*input_), output)
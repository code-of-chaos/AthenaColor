from __future__ import annotations

import unittest


from AthenaColor.Functions.Constraints import (
    Constrain,
    ConstrainHSV,
    ConstrainHSL,
    ConstrainRGB,
    ConstrainCMYK,
    ConstrainRGBA
)


class TestConstrain(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [
            ((-0.1, 1, 0), 0),
            ((5.1, 5, 0), 5),
            ((5.9, 6, 0), 5.9),
            ((0.1, 1000, 0), 0.1)
        ]

    def tearDown(self) -> None:
        self.values = None

    def test_contrain_hsv(self):
        for test_id, (input_, output) in enumerate(self.values, 1):
            with self.subTest(
                    f'test general constraining {test_id}',
                    input_=input_
            ):
                self.assertEqual(Constrain(*input_), output)


class TestConstrainHSV(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [
            ((-0.1, -0.1, -0.1), (0, 0, 0)),
            ((360.1, 1.1, 1.1), (360, 1, 1)),
            ((359.9, 0.9, 0.9), (359.9, 0.9, 0.9)),
            ((0.1, 0.1, 0.1), (0.1, 0.1, 0.1))
        ]

    def tearDown(self) -> None:
        self.values = None

    def test_contrain_hsv(self):
        for test_id, (input_, output) in enumerate(self.values, 1):
            with self.subTest(f'test_hsv {test_id}', input_=input_):
                self.assertEqual(ConstrainHSV(*input_), output)


class TestConstrainHSL(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [
            ((-0.1, -0.1, -0.1), (0, 0, 0)),
            ((360.1, 1.1, 1.1), (360, 1, 1)),
            ((359.9, 0.9, 0.9), (359.9, 0.9, 0.9)),
            ((0.1, 0.1, 0.1), (0.1, 0.1, 0.1))
        ]

    def tearDown(self) -> None:
        self.values = None

    def test_contrain_hsl(self):
        for test_id, (input_, output) in enumerate(self.values, 1):
            with self.subTest(f'test_hsl {test_id}', input_=input_):
                self.assertEqual(ConstrainHSL(*input_), output)


class TestConstrainRGB(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [
            ((-0.1, -0.1, -0.1), (0, 0, 0)),
            ((255.1, 255.1, 255.1), (255, 255, 255)),
            ((254.9, 254.9, 254.9), (254.9, 254.9, 254.9)),
            ((0.1, 0.1, 0.1), (0.1, 0.1, 0.1))
        ]

    def tearDown(self) -> None:
        self.values = None

    def test_contrain_rgb(self):
        for test_id, (input_, output) in enumerate(self.values, 1):
            with self.subTest(f'test_rgb {test_id}', input_=input_):
                self.assertEqual(ConstrainRGB(*input_), output)


class TestConstrainCMYK(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [
            ((-0.1, -0.1, -0.1, -0.1), (0, 0, 0, 0)),
            ((1.1, 1.1, 1.1, 1.1), (1, 1, 1, 1)),
            ((0.9, 0.9, 0.9, 0.9), (0.9, 0.9, 0.9, 0.9)),
            ((0.1, 0.1, 0.1, 0.1), (0.1, 0.1, 0.1, 0.1))
        ]

    def tearDown(self) -> None:
        self.values = None

    def test_contrain_cmyk(self):
        for test_id, (input_, output) in enumerate(self.values, 1):
            with self.subTest(f'test_cmyk {test_id}', input_=input_):
                self.assertEqual(ConstrainCMYK(*input_), output)


class TestConstrainRGBA(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [
            ((-0.1, -0.1, -0.1, -0.1), (0, 0, 0, 0)),
            ((255.1, 255.1, 255.1, 255.1), (255, 255, 255, 255)),
            ((254.9, 254.9, 254.9, 254.9), (254.9, 254.9, 254.9, 254.9)),
            ((0.1, 0.1, 0.1, 0.1), (0.1, 0.1, 0.1, 0.1))
        ]

    def tearDown(self) -> None:
        self.values = None

    def test_contrain_rgba(self):
        for test_id, (input_, output) in enumerate(self.values, 1):
            with self.subTest(f'test_rgba {test_id}', input_=input_):
                self.assertEqual(ConstrainRGBA(*input_), output)

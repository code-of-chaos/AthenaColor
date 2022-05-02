# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library
from AthenaColor.Functions.ANSIsquences import ColorSequence, NestedColorSequence

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Functions_ANSIsequences(unittest.TestCase):
    @staticmethod
    def nested(nested):
        return NestedColorSequence(
        # objects
        "This is a test",
        nested,
        # color/styling, reset and seperation
        control_code="38;2;128;0;0",
        reset_code=0,
        sep="\n"
    )

    def test_ColorSequence(self):
        self.assertEqual(
            ColorSequence("38;2;128;0;0"),
            "[38;2;128;0;0m"
        )
        self.assertEqual(
            ColorSequence(0),
            "[0m"
        )

    # noinspection PyTypeChecker
    def test_ColorSequence_Fails(self):
        with self.assertRaises(TypeError):
            ColorSequence((38,2,128,0,0))

    def test_NestedColorSequence(self):
        self.assertEqual(
            NestedColorSequence(
                # objects
                "This is a test",
                "For real",
                # color/styling, reset and seperation
                control_code="38;2;128;0;0",
                reset_code=0,
                sep="\n"
            ),
f"""[38;2;128;0;0mThis is a test[0m[38;2;128;0;0m
[0m[38;2;128;0;0mFor real[0m"""
        )

        self.assertEqual(
            NestedColorSequence(
                # objects
                "This is a test",
                "For real",
                # color/styling, reset and seperation
                reset_code=0,
                sep="\n"
            ),
f"""This is a test[0m
[0mFor real[0m"""
        )

        self.assertEqual(
            NestedColorSequence(
                # objects
                "This is a test",
                "For real",
                # color/styling, reset and seperation
                control_code="38;2;128;0;0",
                sep="\n"
            ),
f"""[38;2;128;0;0mThis is a test[38;2;128;0;0m
[38;2;128;0;0mFor real"""
        )


        self.assertEqual(
            self.nested(self.nested(
                NestedColorSequence(
                # objects
                "This is a test",
                "For real",
                # color/styling, reset and seperation
                control_code="38;2;128;0;0",
                reset_code=0,
                sep="\n"
            ))),
f"""[38;2;128;0;0mThis is a test[0m[38;2;128;0;0m
[0m[38;2;128;0;0m[38;2;128;0;0mThis is a test[0m[38;2;128;0;0m
[0m[38;2;128;0;0m[38;2;128;0;0mThis is a test[0m[38;2;128;0;0m
[0m[38;2;128;0;0mFor real[0m[0m[0m"""
            )

    # noinspection PyTypeChecker
    def test_NestedColorSequence_Fail(self):
        with self.assertRaises(TypeError):
            NestedColorSequence(
                # objects
                "This is a test",
                "For real",
                # color/styling, reset and seperation
                control_code="38;2;128;0;0",
                reset_code=0,
                sep=("\n",)
            )

        with self.assertRaises(TypeError):
            NestedColorSequence(
                # objects
                "This is a test",
                "For real",
                # color/styling, reset and seperation
                control_code=("38;2;128;0;0",),
                reset_code=0,
                sep="\n"
            )

        with self.assertRaises(TypeError):
            self.nested(self.nested(
                NestedColorSequence(
                    # objects
                    "This is a test",
                    "For real",
                    # color/styling, reset and seperation
                    control_code="38;2;128;0;0",
                    reset_code=(0,),
                    sep="\n"
                )))
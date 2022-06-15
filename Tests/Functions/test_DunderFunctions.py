# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library
from AthenaColor.functions.dunder_functions import *

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Functions_DunderFunctions(unittest.TestCase):
# ----------------------------------------------------------------------------------------------------------------------
# - Math Dunders -
# ----------------------------------------------------------------------------------------------------------------------
    def test_add(self):
        self.assertEqual(
            add((1,2,3),(4,5,6)),
            (5,7,9)
        )
        self.assertEqual(
            add(("d", "z", "u"), ("e", "n", "t")),
            ("de","zn","ut")
        )

    def test_sub(self):
        self.assertEqual(
            sub((5,7,9),(4,5,6)),
            (1, 2, 3)
        )
        with self.assertRaises(TypeError):
            sub(("a","b","c"),("d","e","f"))

    def test_mul(self):
        self.assertEqual(
            mul((1,2,3),(4,5,6)),
            (4,10,18)
        )
        with self.assertRaises(TypeError):
            mul(("a","b","c"),("d","e","f"))

    def test_floordiv(self):
        self.assertEqual(
            floordiv((24,76,56),(5,5,5)),
            (4,15,11)
        )
        with self.assertRaises(TypeError):
            floordiv(("a","b","c"),("d","e","f"))

    def test_truediv(self):
        self.assertEqual(
            truediv((24,76,56),(5,5,5)),
            (4.8, 15.2, 11.2)
        )
        with self.assertRaises(TypeError):
            truediv(("a","b","c"),("d","e","f"))

    def test_mod(self):
        self.assertEqual(
            mod((24,76,56),(5,5,5)),
            (4, 1, 1)
        )
        with self.assertRaises(TypeError):
            mod(("a","b","c"),("d","e","f"))

    def test_power(self):
        self.assertEqual(
            power((2,3,4),(3,4,5)),
            (8, 81, 1024)
        )
        with self.assertRaises(TypeError):
            power(("a","b","c"),("d","e","f"))

# ----------------------------------------------------------------------------------------------------------------------
# - Comparator Dunders -
# ----------------------------------------------------------------------------------------------------------------------
    def test_gt(self):
        self.assertFalse(
            gt((2,3,4),(3,4,5))
        )
        self.assertTrue(
            gt((3,4,5),(2,3,4))
        )
        self.assertFalse(
            gt(("a","b","c"),("d","e","f"))
        )
        self.assertTrue(
            gt(("d","e","f"),("a","b","c"))
        )

    def test_lt(self):
        self.assertTrue(
            lt((2,3,4),(3,4,5))
        )
        self.assertFalse(
            lt((3,4,5),(2,3,4))
        )
        self.assertTrue(
            lt(("a","b","c"),("d","e","f"))
        )
        self.assertFalse(
            lt(("d","e","f"),("a","b","c"))
        )

    def test_eq(self):
        self.assertTrue(
            eq((2,3,4),(2,3,4))
        )
        self.assertFalse(
            eq((3,4,5),(2,3,4))
        )
        self.assertTrue(
            eq(("a","b","c"),("a","b","c"))
        )
        self.assertFalse(
            eq(("d","e","f"),("a","b","c"))
        )

    def test_ne(self):
        self.assertFalse(
            ne((2,3,4),(2,3,4))
        )
        self.assertTrue(
            ne((3,4,5),(2,3,4))
        )
        self.assertFalse(
            ne(("a","b","c"),("a","b","c"))
        )
        self.assertTrue(
            ne(("d","e","f"),("a","b","c"))
        )

    def test_ge(self):
        self.assertFalse(
            ge((2,3,4),(3,3,5))
        )
        self.assertTrue(
            ge((3,4,5),(2,4,4))
        )
        self.assertFalse(
            ge(("a","b","c"),("d","b","f"))
        )
        self.assertTrue(
            ge(("d","e","f"),("a","e","c"))
        )

    def test_le(self):
        self.assertTrue(
            le((2,3,4),(3,3,5))
        )
        self.assertFalse(
            le((3,4,5),(2,4,4))
        )
        self.assertTrue(
            le(("a","b","c"),("d","b","f"))
        )
        self.assertFalse(
            le(("d","e","f"),("a","e","c"))
        )


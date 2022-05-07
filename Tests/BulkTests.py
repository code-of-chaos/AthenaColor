# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class BulkTests(unittest.TestCase):
    def Subtest_Equality(self, ObjectType:type, cases):
        for value, result, value_printer in cases:
            with self.subTest(ObjectType=ObjectType,value=value, result=result, value_printer=value_printer):
                self.assertEqual(ObjectType(value), result)

    def Subtest_Fail(self, ObjectType:type, cases):
        for value, error in cases:
            with self.subTest(ObjectType=ObjectType,value=value, error=error):
               with self.assertRaises(error):
                    ObjectType(value)

    def Subtest_ObjectOperation(self, ObjectType:type, args:tuple, kwargs:dict, cases):
        for operation, oargs, okwargs,result in cases:
            with self.subTest(ObjectType=ObjectType, args=args, kwargs=kwargs, oargs=oargs, okwargs=okwargs,result=result, ):
                test_object = ObjectType(*args, **kwargs)
                self.assertEqual(operation(test_object, *oargs, *okwargs), result)

    def Subtest_ObjectOperationBulk(self, ObjectType:type, cases):
        for operation, oargs, okwargs, args, kwargs,result in cases:
            with self.subTest(ObjectType=ObjectType, args=args, kwargs=kwargs, operation=operation,oargs=oargs, okwargs=okwargs,result=result, ):
                test_object = ObjectType(*args, **kwargs)
                self.assertEqual(operation(test_object, *oargs, *okwargs), result)
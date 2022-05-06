# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library
from AthenaColor import RGB, RGBA, HEX, HEXA, HSL, HSV, CMYK

# Custom Packages
from Tests.BulkTests import BulkTests

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class DunderTesting(BulkTests):
    def test_RGB(self):
        objectType=RGB
        casesOperation=(
            #operation  oargs   okwargs     args        kwargs      result
            (str,       (),     {},         (0,0,0),    {},         "0;0;0"),
            (repr,      (),     {},         (0,0,0),    {},         "RGB(r=0,g=0,b=0)"),
            (round,     (),     {},         (0,0,0),    {},         RGB(0,0,0)), # doesn't really impact the RGB or HEX objects, but exsists nonetheless
        )

        self.Subtest_ObjectOperationBulk(objectType, casesOperation)

    def test_HEX(self):
        objectType=HEX
        casesOperation=(
            #operation  oargs   okwargs     args            kwargs      result
            (str,       (),     {},         ("#000000",),   {},         "#000000"),
            (repr,      (),     {},         ("#000000",),   {},         'HEX(hex_value="#000000")'),
            (round,     (),     {},         ("#000000",),   {},         HEX("#000000")), # doesn't really impact the RGB or HEX objects, but exsists nonetheless
        )

        self.Subtest_ObjectOperationBulk(objectType, casesOperation)

    def test_RGBA(self):
        objectType=RGBA
        casesOperation=(
            #operation  oargs   okwargs     args        kwargs      result
            (str,       (),     {},         (0,0,0),    {},         "0;0;0;0"),
            (repr,      (),     {},         (0,0,0),    {},         "RGBA(r=0,g=0,b=0,a=0)"),
            (round,     (),     {},         (0,0,0),    {},         RGBA(0,0,0,0)), # doesn't really impact the RGB or HEX objects, but exsists nonetheless
        )

        self.Subtest_ObjectOperationBulk(objectType, casesOperation)

    def test_HEXA(self):
        objectType=HEXA
        casesOperation=(
            #operation  oargs   okwargs     args            kwargs      result
            (str,       (),     {},         ("#00000000",), {},         "#00000000"),
            (repr,      (),     {},         ("#00000000",), {},         'HEXA(hex_value="#00000000")'),
            (round,     (),     {},         ("#00000000",), {},         HEXA("#00000000")), # doesn't really impact the RGB or HEX objects, but exsists nonetheless
        )

        self.Subtest_ObjectOperationBulk(objectType, casesOperation)

    def test_HSV(self):pass
    def test_HSL(self):pass
    def test_CMYK(self):pass
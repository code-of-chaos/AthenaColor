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
            #operation  oargs           okwargs     args        kwargs      result
            (str,       (),             {},         (0,0,0),    {},         "0;0;0"),
            (repr,      (),             {},         (0,0,0),    {},         "RGB(r=0,g=0,b=0)"),
            (round,     (),             {},         (0,0,0),    {},         RGB(0,0,0)), # doesn't really impact the RGB or HEX objects, but exsists nonetheless
            (bool,      (),             {},         (0,0,0),    {},         False),
            (bool,      (),             {},         (0,0,1),    {},         True),
            (divmod,    (8,),           {},         (127,71,54),{},         (RGB(r=15,g=8,b=6), RGB(r=7,g=7,b=6))),
            (divmod,    ((8,4,2),),     {},         (127,71,54),{},         (RGB(r=15,g=17,b=27), RGB(r=7,g=3,b=0))),
            (divmod,    (RGB(8,4,2),),  {},         (127,71,54),{},         (RGB(r=15,g=17,b=27), RGB(r=7,g=3,b=0))),
            (divmod,    (HSL(180,.5,.5),),{},       (127,71,54),{},         (RGB(r=1,g=0,b=0), RGB(r=63,g=71,b=54))),
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

    def test_HSV(self):
        objectType=HSV
        casesOperation=(
            #operation  oargs   okwargs     args            kwargs      result
            (str,       (),     {},         (180,.5,.5),    {},         "180;0.5;0.5"),
            (repr,      (),     {},         (180,.5,.5),    {},         'HSV(h=180,s=0.5,v=0.5)'),
            (round,     (),     {},         (180,.5,.5),    {},         HSV(180,0,0)),
            (round,     (5,),   {},         (180,.123456,.123456),{},   HSV(180,.12346,.12346)),
        )
        self.Subtest_ObjectOperationBulk(objectType, casesOperation)

    def test_HSL(self):
        objectType=HSL
        casesOperation=(
            #operation  oargs   okwargs     args            kwargs      result
            (str,       (),     {},         (180,.5,.5),    {},         "180;0.5;0.5"),
            (repr,      (),     {},         (180,.5,.5),    {},         'HSL(h=180,s=0.5,l=0.5)'),
            (round,     (),     {},         (180,.5,.5),    {},         HSL(180,0,0)),
            (round,     (5,),   {},         (180,.123456,.123456),{},   HSL(180,.12346,.12346)),
        )
        self.Subtest_ObjectOperationBulk(objectType, casesOperation)

    def test_CMYK(self):
        objectType=CMYK
        casesOperation=(
            #operation  oargs   okwargs     args            kwargs      result
            (str,       (),     {},         (.5,.5,.5,.5),  {},         "0.5;0.5;0.5;0.5"),
            (repr,      (),     {},         (.5,.5,.5,.5),  {},         'CMYK(c=0.5,m=0.5,y=0.5,k=0.5)'),
            (round,     (),     {},         (.5,.5,.5,.5),  {},         CMYK(0,0,0,0)),
            (round,     (5,),   {},         (.123456,.123456,.123456,.123456),{},CMYK(.12346,.12346,.12346,.12346)),
        )
        self.Subtest_ObjectOperationBulk(objectType, casesOperation)
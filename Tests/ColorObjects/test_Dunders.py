# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import copy
import operator

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
            #operation  oargs               okwargs     args            kwargs      result
            (str,       (),                 {},         (0,0,0),        {},         "0;0;0"),
            (repr,      (),                 {},         (0,0,0),        {},         "RGB(r=0,g=0,b=0)"),
            (round,     (),                 {},         (0,0,0),        {},         RGB(0,0,0)), # doesn't really impact the RGB or HEX objects, but exsists nonetheless
            (bool,      (),                 {},         (0,0,0),        {},         False),
            (bool,      (),                 {},         (0,0,1),        {},         True),
            (divmod,    (8,),               {},         (127,71,54),    {},         (RGB(r=15,g=8,b=6), RGB(r=7,g=7,b=6))),
            (divmod,    ((8,4,2),),         {},         (127,71,54),    {},         (RGB(r=15,g=17,b=27), RGB(r=7,g=3,b=0))),
            (divmod,    (RGB(8,4,2),),      {},         (127,71,54),    {},         (RGB(r=15,g=17,b=27), RGB(r=7,g=3,b=0))),
            (divmod,    (HSL(180,.5,.5),),  {},         (127,71,54),    {},         (RGB(r=1,g=0,b=0), RGB(r=63,g=71,b=54))),
            (sum,       (),                 {},         (127,127,127),  {},         381),
            (max,       (),                 {},         (52,128,255),   {},         255),
            (min,       (),                 {},         (52,128,255),   {},         52),
            (hash,      (),                 {},         (52,128,255),   {},         335258822),
            (copy.copy, (),                 {},         (52,128,255),   {},         RGB(52,128,255)),
            (operator.contains,(52,),       {},         (52,128,255),   {},         True),
            (operator.contains,(12,),       {},         (52,128,255),   {},         False),
        )
        self.Subtest_ObjectOperationBulk(objectType, casesOperation)

    def test_HEX(self):
        objectType=HEX
        casesOperation=(
            #operation  oargs   okwargs     args            kwargs      result
            (str,       (),     {},         ("#000000",),   {},         "#000000"),
            (repr,      (),     {},         ("#000000",),   {},         'HEX(hex_value="#000000")'),
            (round,     (),     {},         ("#000000",),   {},         HEX("#000000")), # doesn't really impact the RGB or HEX objects, but exsists nonetheless
            (bool,      (),     {},         ("#000000",),   {},         False),
            (bool,      (),     {},         ("#000001",),   {},         True),
            (divmod,    (8,),   {},         ("#7f4736",),   {},         (HEX("#0f0806"), HEX("#070706"))),
            (hash,      (),     {},         ("#000001",),   {},         1105321676),

        )
        self.Subtest_ObjectOperationBulk(objectType, casesOperation)

    def test_RGBA(self):
        objectType=RGBA
        casesOperation=(
            #operation  oargs               okwargs     args                kwargs      result
            (str,       (),                 {},         (0,0,0),            {},         "0;0;0;0"),
            (repr,      (),                 {},         (0,0,0),            {},         "RGBA(r=0,g=0,b=0,a=0)"),
            (round,     (),                 {},         (0,0,0),            {},         RGBA(0,0,0,0)), # doesn't really impact the RGB or HEX objects, but exsists nonetheless
            (bool,      (),                 {},         (0,0,0),            {},         False),
            (bool,      (),                 {},         (0,0,1),            {},         True),
            (divmod,    (8,),               {},         (127,71,54,28),     {},         (RGBA(r=15,g=8,b=6,a=3), RGBA(r=7,g=7,b=6,a=4))),
            (divmod,    ((8,4,2,5),),       {},         (127,71,54,28),     {},         (RGBA(r=15,g=17,b=27,a=5), RGBA(r=7,g=3,b=0,a=3))),
            (divmod,    (RGBA(8,4,2,1),),   {},         (127,71,54,28),     {},         (RGBA(r=15,g=17,b=27,a=28), RGBA(r=7,g=3,b=0,a=0))),
            (divmod,    (HSL(180,.5,.5),),  {},         (127,71,54,28),     {},         (RGBA(r=1,g=0,b=0,a=0), RGBA(r=63,g=71,b=54,a=28))),
            (hash,      (),                 {},         (64,25,18,127),     {},         -502044045),
            (hash,      (),                 {},         (64,25,18,127),     {},         -502044045),
        )
        self.Subtest_ObjectOperationBulk(objectType, casesOperation)

    def test_HEXA(self):
        objectType=HEXA
        casesOperation=(
            #operation  oargs               okwargs     args            kwargs      result
            (str,       (),                 {},         ("#00000000",), {},         "#00000000"),
            (repr,      (),                 {},         ("#00000000",), {},         'HEXA(hex_value="#00000000")'),
            (round,     (),                 {},         ("#00000000",), {},         HEXA("#00000000")), # doesn't really impact the RGB or HEX objects, but exsists nonetheless
            (bool,      (),                 {},         ("#00000000",), {},         False),
            (bool,      (),                 {},         ("#00000100",), {},         True),
            (divmod,    (8,),               {},         ("#7f473612",), {},         (HEXA(hex_value="#0f080602"), HEXA(hex_value="#07070602"))),
            (divmod,    ((8,4,2,5),),       {},         ("#7f473612",), {},         (HEXA(hex_value="#0f111b03"), HEXA(hex_value="#07030003"))),
            (divmod,    (RGBA(8,4,2,1),),   {},         ("#7f473612",), {},         (HEXA(hex_value="#0f111b12"), HEXA(hex_value="#07030000"))),
            (divmod,    (HEXA("#0f111b12"),),{},        ("#7f473612",), {},         (HEXA(hex_value="#08040201"), HEXA(hex_value="#07030000"))),
            (divmod,    (HSL(180,.5,.5),),  {},         ("#7f473612",), {},         (HEXA(hex_value="#01000000"), HEXA(hex_value="#3f473612"))),
            (hash,      (),                 {},         ("#00000100",), {},         -855659026),
        )
        self.Subtest_ObjectOperationBulk(objectType, casesOperation)

    def test_HSV(self):
        objectType=HSV
        casesOperation=(
            #operation  oargs               okwargs     args                    kwargs      result
            (str,       (),                 {},         (180,.5,.5),            {},         "180;0.5;0.5"),
            (repr,      (),                 {},         (180,.5,.5),            {},         'HSV(h=180,s=0.5,v=0.5)'),
            (round,     (),                 {},         (180,.5,.5),            {},         HSV(180,0,0)),
            (round,     (5,),               {},         (180,.123456,.123456),  {},         HSV(180,.12346,.12346)),
            (bool,      (),                 {},         (0,0,0),                {},         False),
            (bool,      (),                 {},         (0,0,1),                {},         True),
            (divmod,    (8,),               {},         (180,.5,.5),            {},         (HSV(h=22,s=0.0,v=0.0), HSV(h=4,s=0.5,v=0.5))),
            (divmod,    ((8,.025,.02),),    {},         (180,.5,.5),            {},         (HSV(h=22,s=1,v=1), HSV(h=4,s=0.025,v=0.02))),
            (divmod,    (RGB(8,4,2),),      {},         (180,.5,.5),            {},         (HSV(h=9,s=0.0,v=1), HSV(h=0,s=0.5,v=0.004))),
            (divmod,    (HSV(8,.025,.02),), {},         (180,.5,.5),            {},         (HSV(h=22,s=1,v=1), HSV(h=4,s=0.025,v=0.02))),
            (hash,      (),                 {},         (289,.25,.145),         {},         1367479895),
        )
        self.Subtest_ObjectOperationBulk(objectType, casesOperation)

    def test_HSL(self):
        objectType=HSL
        casesOperation=(
            #operation  oargs               okwargs     args                    kwargs      result
            (str,       (),                 {},         (180,.5,.5),            {},         "180;0.5;0.5"),
            (repr,      (),                 {},         (180,.5,.5),            {},         'HSL(h=180,s=0.5,l=0.5)'),
            (round,     (),                 {},         (180,.5,.5),            {},         HSL(180,0,0)),
            (round,     (5,),               {},         (180,.123456,.123456),  {},         HSL(180,.12346,.12346)),
            (bool,      (),                 {},         (0,0,0),                {},         False),
            (bool,      (),                 {},         (0,0,1),                {},         True),
            (divmod,    (8,),               {},         (180,.5,.5),            {},         (HSL(h=22,s=0.0,l=0.0), HSL(h=4,s=0.5,l=0.5))),
            (divmod,    ((8,.025,.02),),    {},         (180,.5,.5),            {},         (HSL(h=22,s=1,l=1), HSL(h=4,s=0.025,l=0.02))),
            (divmod,    (RGB(8,4,2),),      {},         (180,.5,.5),            {},         (HSL(h=9,s=0.0,l=1), HSL(h=0,s=0.5,l=0.02))),
            (divmod,    (HSL(8,.025,.02),), {},         (180,.5,.5),            {},         (HSL(h=22,s=1,l=1), HSL(h=4,s=0.025,l=0.02))),
            (hash,      (),                 {},         (289,.25,.145),         {},         1367479895),
        )
        self.Subtest_ObjectOperationBulk(objectType, casesOperation)

    def test_CMYK(self):
        objectType=CMYK
        casesOperation=(
            #operation  oargs                       okwargs     args                                kwargs      result
            (str,       (),                         {},         (.5,.5,.5,.5),                      {},         "0.5;0.5;0.5;0.5"),
            (repr,      (),                         {},         (.5,.5,.5,.5),                      {},         'CMYK(c=0.5,m=0.5,y=0.5,k=0.5)'),
            (round,     (),                         {},         (.5,.5,.5,.5),                      {},         CMYK(0,0,0,0)),
            (round,     (5,),                       {},         (.123456,.123456,.123456,.123456),  {},         CMYK(.12346,.12346,.12346,.12346)),
            (divmod,    ((8,4,2,5),),               {},         (.5,.5,.5,.5),                      {},         (CMYK(c=0.0,m=0.0,y=0.0,k=0.0), CMYK(c=0.5,m=0.5,y=0.5,k=0.5))),
            (divmod,    ((.8,.4,.2,.5),),           {},         (.5,.5,.5,.5),                      {},         (CMYK(c=0.0,m=1.0,y=1,k=1.0), CMYK(c=0.5,m=0.1,y=0.1,k=0.0))),
            (bool,      (),                         {},         (0,0,0,0),                          {},         False),
            (bool,      (),                         {},         (0,0,0,1),                          {},         True),
            (divmod,    (8,),                       {},         (.5,.5,.5,.5),                      {},         (CMYK(c=0.0,m=0.0,y=0.0,k=0.0), CMYK(c=0.5,m=0.5,y=0.5,k=0.5))),
            (divmod,    ((8,.025,.02, 0.01),),      {},         (.5,.5,.5,.5),                      {},         (CMYK(c=0.0,m=1,y=1,k=1), CMYK(c=0.5,m=0.025,y=0.02,k=0.01))),
            (divmod,    (CMYK(8,.025,.02, 0.01),),  {},         (.5,.5,.5,.5),                      {},         (CMYK(c=0.0,m=1,y=1,k=1), CMYK(c=0.5,m=0.025,y=0.02,k=0.01))),
            (hash,      (),                         {},         (.125,.25,.145,.75),                {},         -629847754),
        )
        self.Subtest_ObjectOperationBulk(objectType, casesOperation)
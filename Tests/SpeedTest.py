# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaColor import *
import timeit

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def Conversion():
    RGB(255, 255, 255) - CMYK(.1, .1, .1, .1)

def ConversionInline():
    a = RGB(255, 255, 255)
    a -= CMYK(.1, .1, .1, .1)

if __name__ == '__main__':
    print(
        "Conversion: ",
        ForeNest.Red(
            timeit.repeat(lambda: Conversion(), number=1_000_000, repeat=5)
        )
    )

    print(
        "ConversionInline: ",
        ForeNest.Red(
            timeit.repeat(lambda: ConversionInline(), number=1_000_000, repeat=5)
        )
    )
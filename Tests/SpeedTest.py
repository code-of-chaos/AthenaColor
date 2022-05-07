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

def TextInline():
    a = f"{Fore.Red}SOMETHING{Style.NoForeground}"
    b = f"{Style.Bold}Bold{Style.NoBold}"
    c = f"{Back.Blue}I'M BLUE{Style.NoBackground}"
    return a,b,c

def TextNested():
    a = ForeNest.Red("SOMETHING")
    b = StyleNest.Bold("Bold")
    c = BackNest.Maroon("I'M BLUE")
    return a,b,c

def TextNestedBig():
    a = StyleNest.Bold(
        StyleNest.Bold(
            StyleNest.Bold(
                StyleNest.Bold(
                    StyleNest.Bold(
                        StyleNest.Bold(
                            StyleNest.Bold(
                                StyleNest.Bold(
                                    StyleNest.Bold(
                                        StyleNest.Bold(
                                            "Bold"))))))))))
    return

def ObjectCreation():
    RGB(255, 255, 255)

if __name__ == '__main__':
    print(f"Conversion:{ForeNest.Red(timeit.repeat(lambda: Conversion(), number=1_000_000, repeat=5))}")
    print(f"ConversionInline:{ForeNest.Red(timeit.repeat(lambda: ConversionInline(), number=1_000_000, repeat=5))}")
    print(f"TextInline:{ForeNest.Red(timeit.repeat(lambda: TextInline(), number=1_000_000, repeat=5))}")
    print(f"TextNested:{ForeNest.Red(timeit.repeat(lambda: TextNested(), number=1_000_000, repeat=5))}")
    print(f"TextNestedBig:{ForeNest.Red(timeit.repeat(lambda: TextNestedBig(), number=1_000_000, repeat=5))}")
    print(f"ObjectCreation:{ForeNest.Red(timeit.repeat(lambda: ObjectCreation(), number=1_000_000, repeat=5))}")


# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor import (
    RGB,HEX,HSV,HSL,CMYK,
    RGBA,HEXA
)

# ----------------------------------------------------------------------------------------------------------------------
# - COLORS -
# ----------------------------------------------------------------------------------------------------------------------
def new_color():
    print(
f"""
color1 = {repr(RGB(r=255,g=127,b=0))}
color2 = {repr(HEX(hex_value="#ff7f00"))}
color3 = {repr(HSV(h=360,s=.5,v=0))}
color4 = {repr(HSL(h=360,s=.5,l=0))}
color5 = {repr(CMYK(c=1,m=.75,y=.25,k=0))}
color6 = {repr(RGBA(r=255,g=127,b=63,a=0))}
color7 = {repr(HEXA(hex_value="#ff7f3f00"))}
"""
    )

def color_calculation_same():
    print(
f"""
color1 = {repr(color1 := RGB(r=255,g=127,b=0))}
color2 = {repr(color2 := HEX(hex_value="#ff7f00"))}

{repr(color1 - color2)} = {repr(color1)} - {repr(color2)}
"""
    )

def color_calculation_different():
    print(
f"""
color1 = {repr(color1 := HSV(h=140.83,s=.45,v=1.))}
color2 = {repr(color2 := RGB(r=74, g=221, b=81))}

result -> {repr(color1-color2)} = {repr(color1)} - {repr(color2)}
The resulting color object's class, will be the same class as the object on the left hand side of the operation.
When mixing together two different classes, it will convert the equation to an RGB format, and then reconvert it back into the correct type.
"""
    )

def color_calculation_multiple():
    print(
f"""
color1 = {repr(color1 := HSV(h=140.83,s=.45,v=1.))}
color2 = {repr(color2 := RGB(r=74,g=221,b=81))}
color3 = {repr(color3 := HSL(h=67.34,s=.5,l=1))}

result -> {repr(color1+(color2/color3))} = {repr(color1)} + ({repr(color2)} / {repr(color3)})
Mixing and matching multiple types together is possible.
"""
    )

# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor.Objects.ColorSystems.Opaque import (
    RGB ,
    HEX ,
    CMYK,
    HSL ,
    HSV
)
from AthenaColor.Objects.ColorSystems.Transparent import (
    RGBA ,
    HEXA ,
)
import AthenaColor.Functions.ColorTupleConversion as CTC

# ----------------------------------------------------------------------------------------------------------------------
# - OPAQUE COLORS -
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# - RGB -
# ----------------------------------------------------------------------------------------------------------------------
def to_rgb(color:RGB|HEX|CMYK|HSL|HSV) -> RGB:
    match color:
        case RGB():
            return color
        case HEX():
            return RGB(r=color.r,g=color.g,b=color.b)
        case HSV():
            return RGB(*CTC.hsv_to_rgb(h=color.h, s=color.s, v=color.v))
        case HSL():
            return RGB(*CTC.hsl_to_rgb(h=color.h, s=color.s, l=color.l))
        case CMYK():
            return RGB(*CTC.cmyk_to_rgb(c=color.c, m=color.m, y=color.y, k=color.k))
        case _:
            raise ValueError(f"No known Opaque Color system: {color=}")

# ----------------------------------------------------------------------------------------------------------------------
# - Hexadecimal -
# ----------------------------------------------------------------------------------------------------------------------
def to_hex(color:RGB|HEX|CMYK|HSL|HSV) -> HEX:
    match color:
        case RGB():
            return HEX(CTC.rgb_to_hex(r=color.r, g=color.g, b=color.b))
        case HEX():
            return color
        case HSV():
            return HEX(*CTC.hsv_to_hex(h=color.h, s=color.s, v=color.v))
        case HSL():
            return HEX(*CTC.hsl_to_hex(h=color.h, s=color.s, l=color.l))
        case CMYK():
            return HEX(*CTC.cmyk_to_hex(c=color.c, m=color.m, y=color.y, k=color.k))
        case _:
            raise ValueError(f"No known Opaque Color system: {color=}")

# ----------------------------------------------------------------------------------------------------------------------
# - HSV -
# ----------------------------------------------------------------------------------------------------------------------
def to_hsv(color:RGB|HEX|CMYK|HSL|HSV) -> HSV:
    match color:
        case RGB():
            return HSV(*CTC.rgb_to_hsv(r=color.r, g=color.g, b=color.b))
        case HEX():
            return HSV(*CTC.hex_to_hsv(str(color)))
        case HSV():
            return color
        case HSL():
            return HSV(*CTC.hsl_to_hsv(h=color.h, s=color.s, l=color.l))
        case CMYK():
            return HSV(*CTC.cmyk_to_hsv(c=color.c, m=color.m, y=color.y, k=color.k))
        case _:
            raise ValueError(f"No known Opaque Color system: {color=}")

# ----------------------------------------------------------------------------------------------------------------------
# - HSL -
# ----------------------------------------------------------------------------------------------------------------------
def to_hsl(color:RGB|HEX|CMYK|HSL|HSV) -> HSL:
    match color:
        case RGB():
            return HSL(*CTC.rgb_to_hsl(r=color.r, g=color.g, b=color.b))
        case HEX():
            return HSL(*CTC.hex_to_hsl(str(color)))
        case HSV():
            return HSL(*CTC.hsv_to_hsl(h=color.h, s=color.s, v=color.v))
        case HSL():
            return color
        case CMYK():
            return HSL(*CTC.cmyk_to_hsl(c=color.c, m=color.m, y=color.y, k=color.k))
        case _:
            raise ValueError(f"No known Opaque Color system: {color=}")

# ----------------------------------------------------------------------------------------------------------------------
# - CMYK -
# ----------------------------------------------------------------------------------------------------------------------
def to_cmyk(color:RGB|HEX|CMYK|HSL|HSV) -> CMYK:
    match color:
        case RGB():
            return CMYK(*CTC.rgb_to_cmyk(r=color.r, g=color.g, b=color.b))
        case HEX():
            return CMYK(*CTC.hex_to_cmyk(str(color)))
        case HSV():
            return CMYK(*CTC.hsv_to_cmyk(h=color.h, s=color.s, v=color.v))
        case HSL():
            return CMYK(*CTC.hsl_to_cmyk(h=color.h, s=color.s, l=color.l))
        case CMYK():
            return color
        case _:
            raise ValueError(f"No known Opaque Color system: {color=}")

# ----------------------------------------------------------------------------------------------------------------------
# - TRANSPARENT COLORS -
# ----------------------------------------------------------------------------------------------------------------------A
def to_rgba(color:RGBA|HEXA) -> RGBA:
    match color:
        case RGBA():
            return color
        case HEXA():
            return RGBA(*CTC.hexa_to_rgba(str(color)))
        case _:
            raise ValueError(f"No known Transparent Color system: {color=}")

def to_hexa(color:RGBA|HEXA) -> HEXA:
    match color:
        case RGBA():
            return HEXA(*CTC.rgba_to_hexa(r=color.r, g=color.g, b=color.b, a=color.a))
        case HEXA():
            return color
        case _:
            raise ValueError(f"No known Transparent Color system: {color=}")

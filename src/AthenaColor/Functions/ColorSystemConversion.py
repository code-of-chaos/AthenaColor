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
import AthenaColor.Functions.ColorConversion as ColorConversion

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
            return RGB(*ColorConversion.hsv_to_rgb(h=color.h, s=color.s, v=color.v))
        case HSL():
            return RGB(*ColorConversion.hsl_to_rgb(h=color.h, s=color.s, l=color.l))
        case CMYK():
            return RGB(*ColorConversion.cmyk_to_rgb(c=color.c, m=color.m, y=color.y, k=color.k))
        case _:
            raise ValueError(f"No known Color system: {color=}")

# ----------------------------------------------------------------------------------------------------------------------
# - Hexadecimal -
# ----------------------------------------------------------------------------------------------------------------------
def to_hex(color:RGB|HEX|CMYK|HSL|HSV) -> HEX:
    match color:
        case RGB():
            return HEX(ColorConversion.rgb_to_hex(r=color.r,g=color.g,b=color.b))
        case HEX():
            return color
        case HSV():
            return HEX(*ColorConversion.hsv_to_hex(h=color.h, s=color.s, v=color.v))
        case HSL():
            return HEX(*ColorConversion.hsl_to_hex(h=color.h, s=color.s, l=color.l))
        case CMYK():
            return HEX(*ColorConversion.cmyk_to_hex(c=color.c, m=color.m, y=color.y, k=color.k))
        case _:
            raise ValueError(f"No known Color system: {color=}")

# ----------------------------------------------------------------------------------------------------------------------
# - HSV -
# ----------------------------------------------------------------------------------------------------------------------
def to_hsv(color:RGB|HEX|CMYK|HSL|HSV) -> HSV:
    match color:
        case RGB():
            return HSV(*ColorConversion.rgb_to_hsv(r=color.r,g=color.g,b=color.b))
        case HEX():
            return HSV(*ColorConversion.hex_to_hsv(str(color)))
        case HSV():
            return color
        case HSL():
            return HSV(*ColorConversion.hsl_to_hsv(h=color.h, s=color.s, l=color.l))
        case CMYK():
            return HSV(*ColorConversion.cmyk_to_hsv(c=color.c, m=color.m, y=color.y, k=color.k))
        case _:
            raise ValueError(f"No known Color system: {color=}")

# ----------------------------------------------------------------------------------------------------------------------
# - HSL -
# ----------------------------------------------------------------------------------------------------------------------
def to_hsl(color:RGB|HEX|CMYK|HSL|HSV) -> HSL:
    match color:
        case RGB():
            return HSL(*ColorConversion.rgb_to_hsl(r=color.r,g=color.g,b=color.b))
        case HEX():
            return HSL(*ColorConversion.hex_to_hsl(str(color)))
        case HSV():
            return HSL(*ColorConversion.hsv_to_hsl(h=color.h, s=color.s, v=color.v))
        case HSL():
            return color
        case CMYK():
            return HSL(*ColorConversion.cmyk_to_hsl(c=color.c, m=color.m, y=color.y, k=color.k))
        case _:
            raise ValueError(f"No known Color system: {color=}")

# ----------------------------------------------------------------------------------------------------------------------
# - CMYK -
# ----------------------------------------------------------------------------------------------------------------------
def to_cmyk(color:RGB|HEX|CMYK|HSL|HSV) -> CMYK:
    match color:
        case RGB():
            return CMYK(*ColorConversion.rgb_to_cmyk(r=color.r,g=color.g,b=color.b))
        case HEX():
            return CMYK(*ColorConversion.hex_to_cmyk(str(color)))
        case HSV():
            return CMYK(*ColorConversion.hsv_to_cmyk(h=color.h, s=color.s, v=color.v))
        case HSL():
            return CMYK(*ColorConversion.hsl_to_cmyk(h=color.h, s=color.s, l=color.l))
        case CMYK():
            return color
        case _:
            raise ValueError(f"No known Color system: {color=}")

# ----------------------------------------------------------------------------------------------------------------------
# - TRANSPARENT COLORS -
# ----------------------------------------------------------------------------------------------------------------------A
def to_rgba(color:RGBA|HEXA) -> RGBA:
    match color:
        case RGBA():
            return color
        case HEXA():
            return RGBA(*ColorConversion.hexa_to_rgba(str(color)))
        case _:
            raise ValueError(f"No known Color system: {color=}")

def to_hexa(color:RGBA|HEXA) -> HEXA:
    match color:
        case RGBA():
            return HEXA(*ColorConversion.rgba_to_hexa(r=color.r,g=color.g,b=color.b,a=color.a))
        case HEXA():
            return color
        case _:
            raise ValueError(f"No known Color system: {color=}")

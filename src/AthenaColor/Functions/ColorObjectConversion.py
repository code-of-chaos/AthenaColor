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
from AthenaColor import init

# ----------------------------------------------------------------------------------------------------------------------
# - OPAQUE COLORS -
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# - RGB -
# ----------------------------------------------------------------------------------------------------------------------
def to_RGB(color:RGB|HEX|CMYK|HSL|HSV) -> RGB:
    """
    Function which converts any Opaque Color Object (RGB,HEX,CMYK,HSL,HSV) to an RGB object
    An inserted RGB color will not create a new RGB color, but simply return the original.
    """
    if isinstance(color, RGB):
        return color
    elif isinstance(color, (HEX,RGBA,HEXA)):
        return RGB(r=color.r,g=color.g,b=color.b)
    elif isinstance(color, HSV):
        return RGB(*CTC.hsv_to_rgb(h=color.h, s=color.s, v=color.v))
    elif isinstance(color, HSL):
        return RGB(*CTC.hsl_to_rgb(h=color.h, s=color.s, l=color.l))
    elif isinstance(color, CMYK):
        return RGB(*CTC.cmyk_to_rgb(c=color.c, m=color.m, y=color.y, k=color.k))
    else:
        raise ValueError(f"No known Opaque Color system: {color=}")

# ----------------------------------------------------------------------------------------------------------------------
# - Hexadecimal -
# ----------------------------------------------------------------------------------------------------------------------
def to_HEX(color:RGB|HEX|CMYK|HSL|HSV) -> HEX:
    """
    Function which converts any Opaque Color Object (RGB,HEX,CMYK,HSL,HSV) to an HEX object
    An inserted HEX color will not create a new HEX color, but simply return the original.
    """
    if isinstance(color, (RGB,RGBA,HEXA)):
        return HEX(CTC.rgb_to_hex(r=color.r, g=color.g, b=color.b))
    elif isinstance(color, HEX):
        return color
    elif isinstance(color, HSV):
        return HEX(*CTC.hsv_to_hex(h=color.h, s=color.s, v=color.v))
    elif isinstance(color, HSL):
        return HEX(*CTC.hsl_to_hex(h=color.h, s=color.s, l=color.l))
    elif isinstance(color, CMYK):
        return HEX(*CTC.cmyk_to_hex(c=color.c, m=color.m, y=color.y, k=color.k))
    else:
        raise ValueError(f"No known Opaque Color system: {color=}")

# ----------------------------------------------------------------------------------------------------------------------
# - HSV -
# ----------------------------------------------------------------------------------------------------------------------
def to_HSV(color:RGB|HEX|CMYK|HSL|HSV) -> HSV:
    """
    Function which converts any Opaque Color Object (RGB,HEX,CMYK,HSL,HSV) to an HSV object
    An inserted HSV color will not create a new HSV color, but simply return the original.
    """
    if isinstance(color, (RGB,RGBA,HEXA)):
        return HSV(*CTC.rgb_to_hsv(r=color.r, g=color.g, b=color.b))
    elif isinstance(color, HEX):
        return HSV(*CTC.hex_to_hsv(str(color)))
    elif isinstance(color, HSV):
        return color
    elif isinstance(color, HSL):
        return HSV(*CTC.hsl_to_hsv(h=color.h, s=color.s, l=color.l))
    elif isinstance(color, CMYK):
        return HSV(*CTC.cmyk_to_hsv(c=color.c, m=color.m, y=color.y, k=color.k))
    else:
        raise ValueError(f"No known Opaque Color system: {color=}")

# ----------------------------------------------------------------------------------------------------------------------
# - HSL -
# ----------------------------------------------------------------------------------------------------------------------
def to_HSL(color:RGB|HEX|CMYK|HSL|HSV) -> HSL:
    """
    Function which converts any Opaque Color Object (RGB,HEX,CMYK,HSL,HSV) to an HSL object
    An inserted HSL color will not create a new HSL color, but simply return the original.
    """
    if isinstance(color, (RGB,RGBA,HEXA)):
        return HSL(*CTC.rgb_to_hsl(r=color.r, g=color.g, b=color.b))
    elif isinstance(color, HEX):
        return HSL(*CTC.hex_to_hsl(str(color)))
    elif isinstance(color, HSV):
        return HSL(*CTC.hsv_to_hsl(h=color.h, s=color.s, v=color.v))
    elif isinstance(color, HSL):
        return color
    elif isinstance(color, CMYK):
        return HSL(*CTC.cmyk_to_hsl(c=color.c, m=color.m, y=color.y, k=color.k))
    else:
        raise ValueError(f"No known Opaque Color system: {color=}")

# ----------------------------------------------------------------------------------------------------------------------
# - CMYK -
# ----------------------------------------------------------------------------------------------------------------------
def to_CMYK(color:RGB|HEX|CMYK|HSL|HSV) -> CMYK:
    """
    Function which converts any Opaque Color Object (RGB,HEX,CMYK,HSL,HSV) to an CMYK object
    An inserted CMYK color will not create a new CMYK color, but simply return the original.
    """
    if isinstance(color, (RGB,RGBA,HEXA)):
        return CMYK(*CTC.rgb_to_cmyk(r=color.r, g=color.g, b=color.b))
    elif isinstance(color, HEX):
        return CMYK(*CTC.hex_to_cmyk(str(color)))
    elif isinstance(color, HSV):
        return CMYK(*CTC.hsv_to_cmyk(h=color.h, s=color.s, v=color.v))
    elif isinstance(color, HSL):
        return CMYK(*CTC.hsl_to_cmyk(h=color.h, s=color.s, l=color.l))
    elif isinstance(color, CMYK):
        return color
    else:
        raise ValueError(f"No known Opaque Color system: {color=}")

# ----------------------------------------------------------------------------------------------------------------------
# - TRANSPARENT COLORS -
# ----------------------------------------------------------------------------------------------------------------------A
def to_RGBA(color:RGBA|HEXA|RGB|HEX|CMYK|HSL|HSV) -> RGBA:
    """
    Function which converts any Opaque Color Object (RGB,HEX,CMYK,HSL,HSV) or Transparent Color Object (RGBA,HEXA) to an RGBA object
    An inserted RGBA color will not create a new RGBA color, but simply return the original.
    """
    if isinstance(color, RGBA):
        return color
    elif isinstance(color, HEXA):
        return RGBA(*CTC.hexa_to_rgba(str(color)))
    # below conversions will set the A part of RGBA to 1
    elif isinstance(color, RGB):
        return RGBA(r=color.r, g=color.g, b=color.b,a=init.transparent_default_float)
    elif isinstance(color, HEX):
        return RGBA(*CTC.hex_to_rgb(str(color)),a=init.transparent_default_float)
    elif isinstance(color, HSV):
        return RGBA(*CTC.hsv_to_rgb(h=color.h, s=color.s, v=color.v),a=init.transparent_default_float)
    elif isinstance(color, HSL):
        return RGBA(*CTC.hsl_to_rgb(h=color.h, s=color.s, l=color.l),a=init.transparent_default_float)
    elif isinstance(color, CMYK):
        return RGBA(*CTC.cmyk_to_rgb(c=color.c, m=color.m, y=color.y, k=color.k),a=init.transparent_default_float)
    else:
        raise ValueError(f"No known Transparent Color system: {color=}")

def to_HEXA(color:RGBA|HEXA|RGB|HEX|CMYK|HSL|HSV) -> HEXA:
    """
    Function which converts any Opaque Color Object (RGB,HEX,CMYK,HSL,HSV) or Transparent Color Object (RGBA,HEXA) to an HEXA object
    An inserted HEXA color will not create a new HEXA color, but simply return the original.
    """
    if isinstance(color, RGBA):
        return HEXA(*CTC.rgba_to_hexa(r=color.r, g=color.g, b=color.b, a=color.a))
    elif isinstance(color, HEXA):
        return color
    # below conversions will set the A part of HEXA to ff
    elif isinstance(color, RGB):
        return HEXA(CTC.rgb_to_hex(r=color.r, g=color.g, b=color.b)+init.transparent_default_str)
    elif isinstance(color, HEX):
        return HEXA(str(color)+init.transparent_default_str)
    elif isinstance(color, HSV):
        return HEXA(*CTC.hsv_to_hex(h=color.h, s=color.s, v=color.v)+init.transparent_default_str)
    elif isinstance(color, HSL):
        return HEXA(*CTC.hsl_to_hex(h=color.h, s=color.s, l=color.l)+init.transparent_default_str)
    elif isinstance(color, CMYK):
        return HEXA(*CTC.cmyk_to_hex(c=color.c, m=color.m, y=color.y, k=color.k)+init.transparent_default_str)
    else:
        raise ValueError(f"No known Transparent Color system: {color=}")

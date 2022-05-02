# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor.InitClass import init
import AthenaColor.Objects.Color.ColorTupleConversion as CTC
from AthenaColor.Objects.Color.ColorSystem import RGB,HEX,CMYK,HSL,HSV,RGBA,HEXA

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = [
    "to_RGB", "to_RGBA", "to_HSV", "to_HSL", "to_HEX", "to_HEXA", "to_CMYK"
]

# ----------------------------------------------------------------------------------------------------------------------
# - RGB -
# ----------------------------------------------------------------------------------------------------------------------
# noinspection PyProtectedMember
def to_RGB(color:RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA) -> RGB:
    """
    Function which converts any Color Object to an RGB object
    """
    if isinstance(color, HEX):
        return RGB(*CTC.hex_to_rgb(str(color)))
    elif isinstance(color, RGB):
        return RGB(*color.export())
    elif isinstance(color,(RGBA,HEXA)):
        return RGB(*color.export()[:-1])
    elif isinstance(color, HSV):
        return RGB(*CTC.hsv_to_rgb(*color.export()))
    elif isinstance(color, HSL):
        return RGB(*CTC.hsl_to_rgb(*color.export()))
    elif isinstance(color, CMYK):
        return RGB(*CTC.cmyk_to_rgb(*color.export()))
    else:
        return NotImplemented

# ----------------------------------------------------------------------------------------------------------------------
# - Hexadecimal -
# ----------------------------------------------------------------------------------------------------------------------
# noinspection PyProtectedMember
def to_HEX(color:RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA) -> HEX:
    """
    Function which converts any Color Object to an HEX object.
    """
    if isinstance(color, (RGB,HEX)):
        return HEX(CTC.rgb_to_hex(*color.export()))
    elif isinstance(color,(RGBA,HEXA)):
        return HEX(CTC.rgb_to_hex(*color.export()[:-1]))
    elif isinstance(color, HSV):
        return HEX(CTC.hsv_to_hex(*color.export()))
    elif isinstance(color, HSL):
        return HEX(CTC.hsl_to_hex(*color.export()))
    elif isinstance(color, CMYK):
        return HEX(CTC.cmyk_to_hex(*color.export()))
    else:
        return NotImplemented

# ----------------------------------------------------------------------------------------------------------------------
# - HSV -
# ----------------------------------------------------------------------------------------------------------------------
# noinspection PyProtectedMember
def to_HSV(color:RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA) -> HSV:
    """
    Function which converts any Color Object to an HSV object.
    """
    if isinstance(color, (RGB,HEX)):
        return HSV(*CTC.rgb_to_hsv(*color.export()))
    elif isinstance(color,(RGBA,HEXA)):
        return HSV(*CTC.rgb_to_hsv(*color.export()[:-1]))
    elif isinstance(color, HSV):
        return HSV(*color.export())
    elif isinstance(color, HSL):
        return HSV(*CTC.hsl_to_hsv(*color.export()))
    elif isinstance(color, CMYK):
        return HSV(*CTC.cmyk_to_hsv(*color.export()))
    else:
        return NotImplemented

# ----------------------------------------------------------------------------------------------------------------------
# - HSL -
# ----------------------------------------------------------------------------------------------------------------------
def to_HSL(color:RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA) -> HSL:
    """
    Function which converts any Color Object to an HSL object.
    """
    if isinstance(color, (RGB,HEX)):
        return HSL(*CTC.rgb_to_hsl(*color.export()))
    elif isinstance(color,(RGBA,HEXA)):
        return HSL(*CTC.rgb_to_hsl(*color.export()[:-1]))
    elif isinstance(color, HSV):
        return HSL(*CTC.hsv_to_hsl(*color.export()))
    elif isinstance(color, HSL):
        return HSL(*color.export())
    elif isinstance(color, CMYK):
        return HSL(*CTC.cmyk_to_hsl(*color.export()))
    else:
        return NotImplemented

# ----------------------------------------------------------------------------------------------------------------------
# - CMYK -
# ----------------------------------------------------------------------------------------------------------------------
def to_CMYK(color:RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA) -> CMYK:
    """
    Function which converts any Color Object to an CMYK object.
    """
    if isinstance(color, (RGB,HEX)):
        return CMYK(*CTC.rgb_to_cmyk(*color.export()))
    elif isinstance(color,(RGBA,HEXA)):
        return CMYK(*CTC.rgb_to_cmyk(*color.export()[:-1]))
    elif isinstance(color, HSV):
        return CMYK(*CTC.hsv_to_cmyk(*color.export()))
    elif isinstance(color, HSL):
        return CMYK(*CTC.hsl_to_cmyk(*color.export()))
    elif isinstance(color, CMYK):
        return CMYK(*color.export())
    else:
        return NotImplemented

# ----------------------------------------------------------------------------------------------------------------------
# - TRANSPARENT COLORS -
# ----------------------------------------------------------------------------------------------------------------------A
def to_RGBA(color:RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA) -> RGBA:
    """
    Function which converts any Color Object to an RGBA object.
    """
    if isinstance(color, RGBA):
        return RGBA(*color.export())
    elif isinstance(color, HEXA):
        return RGBA(*CTC.hexa_to_rgba(str(color)))
    # below conversions will set the A part of RGBA to 1
    elif isinstance(color, (RGB,HEX)):
        return RGBA(*color.export(), a=init.transparentDefault[1])
    elif isinstance(color, HSV):
        return RGBA(*CTC.hsv_to_rgb(*color.export()), a=init.transparentDefault[1])
    elif isinstance(color, HSL):
        return RGBA(*CTC.hsl_to_rgb(*color.export()), a=init.transparentDefault[1])
    elif isinstance(color, CMYK):
        return RGBA(*CTC.cmyk_to_rgb(*color.export()), a=init.transparentDefault[1])
    else:
        return NotImplemented

def to_HEXA(color:RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA) -> HEXA:
    """
    Function which converts any Color Object to an HEXA object.
    """
    if isinstance(color, RGBA):
        return HEXA(CTC.rgba_to_hexa(*color.export()))
    elif isinstance(color, HEXA):
        return HEXA(str(color))
    # below conversions will set the A part of HEXA to ff
    elif isinstance(color, (RGB,HEX)):
        return HEXA(CTC.rgb_to_hex(*color.export()) + init.transparentDefault[0])
    elif isinstance(color, HSV):
        return HEXA(CTC.hsv_to_hex(*color.export()) + init.transparentDefault[0])
    elif isinstance(color, HSL):
        return HEXA(CTC.hsl_to_hex(*color.export()) + init.transparentDefault[0])
    elif isinstance(color, CMYK):
        return HEXA(CTC.cmyk_to_hex(*color.export()) + init.transparentDefault[0])
    else:
        return NotImplemented
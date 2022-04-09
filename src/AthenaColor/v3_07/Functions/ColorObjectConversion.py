# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from typing import Union

# Custom Library

# Custom Packages
import AthenaColor.v3_07.Functions.ColorTupleConversion as CTC
from AthenaColor.v3_07.InitClass import init
from AthenaColor.v3_07.Objects.ColorSystems import (
    RGB,HEX,CMYK,HSL,HSV,RGBA,HEXA
)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
Colors = Union[RGB,HEX,CMYK,HSL,HSV,RGBA,HEXA]

# ----------------------------------------------------------------------------------------------------------------------
# - RGB -
# ----------------------------------------------------------------------------------------------------------------------
# noinspection PyProtectedMember
def to_RGB(color:Colors) -> RGB:
    """
    Function which converts any Color Object to an RGB object
    """
    if isinstance(color, (RGB,HEX)):
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
def to_HEX(color:Colors) -> HEX:
    """
    Function which converts any Color Object to an HEX object.
    """
    if isinstance(color, (RGB,HEX)):
        return HEX(*color.export())
    elif isinstance(color,(RGBA,HEXA)):
        return HEX(*color.export()[:-1])
    elif isinstance(color, HSV):
        return HEX(*CTC.hsv_to_hex(*color.export()))
    elif isinstance(color, HSL):
        return HEX(*CTC.hsl_to_hex(*color.export()))
    elif isinstance(color, CMYK):
        return HEX(*CTC.cmyk_to_hex(*color.export()))
    else:
        return NotImplemented

# ----------------------------------------------------------------------------------------------------------------------
# - HSV -
# ----------------------------------------------------------------------------------------------------------------------
# noinspection PyProtectedMember
def to_HSV(color:Colors) -> HSV:
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
def to_HSL(color:Colors) -> HSL:
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
def to_CMYK(color:Colors) -> CMYK:
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
def to_RGBA(color:Colors) -> RGBA:
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

def to_HEXA(color:Colors) -> HEXA:
    """
    Function which converts any Color Object to an HEXA object.
    """
    if isinstance(color, RGBA):
        return HEXA(*CTC.rgba_to_hexa(*color.export(), a=color.a))
    elif isinstance(color, HEXA):
        return HEXA(*color.export())
    # below conversions will set the A part of HEXA to ff
    elif isinstance(color, (RGB,HEX)):
        return HEXA(*CTC.rgb_to_hex(*color.export()) + init.transparentDefault[0])
    elif isinstance(color, HSV):
        return HEXA(*CTC.hsv_to_hex(*color.export()) + init.transparentDefault[0])
    elif isinstance(color, HSL):
        return HEXA(*CTC.hsl_to_hex(*color.export()) + init.transparentDefault[0])
    elif isinstance(color, CMYK):
        return HEXA(*CTC.cmyk_to_hex(*color.export()) + init.transparentDefault[0])
    else:
        return NotImplemented
# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor.func.color_tuple_conversion import rgb_to_hex, rgba_to_hexa
from AthenaColor.models.color_system import ColorSystem,RGB,HEX,CMYK,HSL,HSV,RGBA,HEXA, color_conversions_mapped

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
def to_RGB(color:ColorSystem|RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA) -> RGB:
    """
    Function which converts any Color Object to an RGB object

    Parameters:
    - color : ColorSystem|RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA -> Any valid ColorSystem object

    Returns : RGB
    """
    try:
        return RGB(*color_conversions_mapped[RGB][type(color)](color))
    except KeyError:
        return NotImplemented

# ----------------------------------------------------------------------------------------------------------------------
# - Hexadecimal -
# ----------------------------------------------------------------------------------------------------------------------
# noinspection PyProtectedMember
def to_HEX(color:ColorSystem|RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA) -> HEX:
    """
    Function which converts any Color Object to an HEX object.

    Parameters:
    - color : ColorSystem|RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA -> Any valid ColorSystem object

    Returns : HEX
    """
    try:
        return HEX(rgb_to_hex(*color_conversions_mapped[HEX][type(color)](color)))
    except KeyError:
        return NotImplemented

# ----------------------------------------------------------------------------------------------------------------------
# - HSV -
# ----------------------------------------------------------------------------------------------------------------------
# noinspection PyProtectedMember
def to_HSV(color:ColorSystem|RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA) -> HSV:
    """
    Function which converts any Color Object to an HSV object.

    Parameters:
    - color : ColorSystem|RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA -> Any valid ColorSystem object

    Returns : HSV
    """
    try:
        return HSV(*color_conversions_mapped[HSV][type(color)](color))
    except KeyError:
        return NotImplemented

# ----------------------------------------------------------------------------------------------------------------------
# - HSL -
# ----------------------------------------------------------------------------------------------------------------------
def to_HSL(color:ColorSystem|RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA) -> HSL:
    """
    Function which converts any Color Object to an HSL object.

    Parameters:
    - color : ColorSystem|RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA -> Any valid ColorSystem object

    Returns : HSL
    """
    try:
        return HSL(*color_conversions_mapped[HSL][type(color)](color))
    except KeyError:
        return NotImplemented

# ----------------------------------------------------------------------------------------------------------------------
# - CMYK -
# ----------------------------------------------------------------------------------------------------------------------
def to_CMYK(color:ColorSystem|RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA) -> CMYK:
    """
    Function which converts any Color Object to an CMYK object.

    Parameters:
    - color : ColorSystem|RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA -> Any valid ColorSystem object

    Returns : CMYK
    """
    try:
        return CMYK(*color_conversions_mapped[CMYK][type(color)](color))
    except KeyError:
        return NotImplemented

# ----------------------------------------------------------------------------------------------------------------------
# - TRANSPARENT COLORS -
# ----------------------------------------------------------------------------------------------------------------------A
def to_RGBA(color:ColorSystem|RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA) -> RGBA:
    """
    Function which converts any Color Object to an RGBA object.

    Parameters:
    - color : ColorSystem|RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA -> Any valid ColorSystem object

    Returns : RGBA
    """
    try:
        return RGBA(*color_conversions_mapped[RGBA][type(color)](color))
    except KeyError:
        return NotImplemented

def to_HEXA(color:ColorSystem|RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA) -> HEXA:
    """
    Function which converts any Color Object to an HEXA object.

    Parameters:
    - color : ColorSystem|RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA -> Any valid ColorSystem object

    Returns : HEXA
    """
    try:
        return HEXA(rgba_to_hexa(*color_conversions_mapped[HEXA][type(color)](color)))
    except KeyError:
        return NotImplemented
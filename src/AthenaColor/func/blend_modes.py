# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

import math
from typing import Callable

# Custom Library

# Custom Packages
from AthenaColor.models.color_system import ColorSystem, RGBA
from AthenaColor.func.color_object_conversion import to_RGBA
from AthenaColor.func.color_tuple_conversion import normalize_rgba

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = [
    "blend_normal", "blend_linearburn", "blend_colordodge", "blend_difference", "blend_lineardodge", "blend_screen",
    "blend_darken", "blend_linearlight", "blend_vividlight", "blend_colorburn", "blend_multiply", "blend_lighten",
    "blend_overlay", "blend_exclusion", "blend_hardlight", "blend_softlight", "blend_pinlight"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
def _blend_function(color1:ColorSystem,color2:ColorSystem, formula:Callable) -> RGBA:
    """
    A general function to combine two colors together with a specific formula.

    Parameters:
    - color1 : ColorSystem -> the first color. It's values undergo the formula
    - color2 : ColorSystem -> the second color. The values are used with the formula to affect the first color
    - formula : typing.Callable

    Returns : RGBA

    """
    color1_tuple = normalize_rgba(*to_RGBA(color1).export())
    color2_tuple = normalize_rgba(*to_RGBA(color2).export())

    # WARNING below values are normalized (aka between 0 and 1)
    normalized_outcome = (formula(a, b) for a, b in zip(color1_tuple, color2_tuple))
    return RGBA(*(n * 255 for n in normalized_outcome))  # need to de normalize them again

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def blend_normal(_:ColorSystem, color2:ColorSystem) -> RGBA:
    """
    Blend function which returns the color2 values in a new RGBA object

    Parameters:
    - color1 : ColorSystem -> the first color. It's values undergo the formula
    - color2 : ColorSystem -> the second color. The values are used with the formula to affect the first color
    - formula : typing.Callable

    Returns : RGBA
    """
    # possible because to_RGBA creates a new object
    return to_RGBA(color2)

def blend_darken(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    """
    Blend function which returns minimum value of the two colors into a new RGBA object

    Parameters:
    - color1 : ColorSystem -> the first color. It's values undergo the formula
    - color2 : ColorSystem -> the second color. The values are used with the formula to affect the first color
    - formula : typing.Callable

    Returns : RGBA
    """
    formula = lambda a, b: min(a, b)
    return _blend_function(color1,color2,formula)

def blend_multiply(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    """
    Blend function which returns the product of the values of the two colors into a new RGBA object

    Parameters:
    - color1 : ColorSystem -> the first color. It's values undergo the formula
    - color2 : ColorSystem -> the second color. The values are used with the formula to affect the first color
    - formula : typing.Callable

    Returns : RGBA
    """
    formula = lambda a,b : a*b
    return _blend_function(color1,color2,formula)

def blend_colorburn(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    """
    Blend function which returns the result of the colorburn formula of the two colors into a new RGBA object

    Parameters:
    - color1 : ColorSystem -> the first color. It's values undergo the formula
    - color2 : ColorSystem -> the second color. The values are used with the formula to affect the first color
    - formula : typing.Callable

    Returns : RGBA
    """
    formula = lambda a,b : 1-(1-a)/b
    return _blend_function(color1,color2,formula)

def blend_linearburn(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    """
    Blend function which returns the result of the linearburn formula of the two colors into a new RGBA object

    Parameters:
    - color1 : ColorSystem -> the first color. It's values undergo the formula
    - color2 : ColorSystem -> the second color. The values are used with the formula to affect the first color
    - formula : typing.Callable

    Returns : RGBA
    """
    formula = lambda a,b : a+b-1
    return _blend_function(color1,color2,formula)

def blend_lighten(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    """
    Blend function which returns maximum value of the two colors into a new RGBA object

    Parameters:
    - color1 : ColorSystem -> the first color. It's values undergo the formula
    - color2 : ColorSystem -> the second color. The values are used with the formula to affect the first color
    - formula : typing.Callable

    Returns : RGBA
    """
    formula = lambda a,b : max(a,b)
    return _blend_function(color1,color2,formula)

def blend_screen(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    """
    Blend function which returns the result of the screen formula of the two colors into a new RGBA object

    Parameters:
    - color1 : ColorSystem -> the first color. It's values undergo the formula
    - color2 : ColorSystem -> the second color. The values are used with the formula to affect the first color
    - formula : typing.Callable

    Returns : RGBA
    """
    formula = lambda a,b : 1-(1-a)(1-b)
    return _blend_function(color1,color2,formula)

def blend_colordodge(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    """
    Blend function which returns the result of the colordodge formula of the two colors into a new RGBA object

    Parameters:
    - color1 : ColorSystem -> the first color. It's values undergo the formula
    - color2 : ColorSystem -> the second color. The values are used with the formula to affect the first color
    - formula : typing.Callable

    Returns : RGBA
    """
    formula = lambda a,b : a/(1-b)
    return _blend_function(color1,color2,formula)

def blend_lineardodge(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    """
    Blend function which returns the result of the lineardodge formula of the two colors into a new RGBA object

    Parameters:
    - color1 : ColorSystem -> the first color. It's values undergo the formula
    - color2 : ColorSystem -> the second color. The values are used with the formula to affect the first color
    - formula : typing.Callable

    Returns : RGBA
    """
    formula = lambda a,b : a+b
    return _blend_function(color1,color2,formula)

def blend_overlay(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    """
    Blend function which returns the result of the overlay formula of the two colors into a new RGBA object

    Parameters:
    - color1 : ColorSystem -> the first color. It's values undergo the formula
    - color2 : ColorSystem -> the second color. The values are used with the formula to affect the first color
    - formula : typing.Callable

    Returns : RGBA
    """
    def formula(a: float, b: float):
        if a < 0.5:
            return 1 - 2 * (1 - a) * (1 - b)
        else:
            return 2 * a * b

    return _blend_function(color1,color2,formula)

def blend_softlight(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    """
    Blend function which returns the result of the softlight formula of the two colors into a new RGBA object

    Parameters:
    - color1 : ColorSystem -> the first color. It's values undergo the formula
    - color2 : ColorSystem -> the second color. The values are used with the formula to affect the first color
    - formula : typing.Callable

    Returns : RGBA
    """
    def formula(a: float, b: float):
        if a <= 0.25:
            g_w3c = ((16*a-12)*a+4)*a
        else:
            g_w3c = math.sqrt(a)

        if b <=0.5:
            return a-(1-2*b)*a*(1-a)
        else:
            return a+(2*b-1)*(g_w3c-a)

    return _blend_function(color1,color2,formula)

def blend_hardlight(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    """
    Blend function which returns the result of the hardlight formula of the two colors into a new RGBA object

    Parameters:
    - color1 : ColorSystem -> the first color. It's values undergo the formula
    - color2 : ColorSystem -> the second color. The values are used with the formula to affect the first color
    - formula : typing.Callable

    Returns : RGBA
    """
    def formula(a: float, b: float):
        if b < 0.5:
            return a*(2*b)
        else:
            return 1-(1-a)*(1-2*(b-0.5))

    return _blend_function(color1,color2,formula)

def blend_vividlight(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    """
    Blend function which returns the result of the vividlight formula of the two colors into a new RGBA object

    Parameters:
    - color1 : ColorSystem -> the first color. It's values undergo the formula
    - color2 : ColorSystem -> the second color. The values are used with the formula to affect the first color
    - formula : typing.Callable

    Returns : RGBA
    """
    def formula(a: float, b: float):
        if b < 0.5:
            return 1-(1-a)/(2*b)
        else:
            return a/(1-2*(b-.5))

    return _blend_function(color1,color2,formula)

def blend_linearlight(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    """
    Blend function which returns the result of the linearlight formula of the two colors into a new RGBA object

    Parameters:
    - color1 : ColorSystem -> the first color. It's values undergo the formula
    - color2 : ColorSystem -> the second color. The values are used with the formula to affect the first color
    - formula : typing.Callable

    Returns : RGBA
    """
    def formula(a: float, b: float):
        if b < 0.5:
            return a+2*b-1
        else:
            return a+2*(b-.5)

    return _blend_function(color1,color2,formula)

def blend_pinlight(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    """
    Blend function which returns the result of the pinlight formula of the two colors into a new RGBA object

    Parameters:
    - color1 : ColorSystem -> the first color. It's values undergo the formula
    - color2 : ColorSystem -> the second color. The values are used with the formula to affect the first color
    - formula : typing.Callable

    Returns : RGBA
    """
    def formula(a: float, b: float):
        if b < 0.5:
            return min(a,2*b)
        else:
            return max(a,2*(b-.5))

    return _blend_function(color1,color2,formula)

def blend_difference(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    """
    Blend function which returns the result of the difference formula of the two colors into a new RGBA object

    Parameters:
    - color1 : ColorSystem -> the first color. It's values undergo the formula
    - color2 : ColorSystem -> the second color. The values are used with the formula to affect the first color
    - formula : typing.Callable

    Returns : RGBA
    """
    formula = lambda a,b : abs(a-b)
    return _blend_function(color1,color2,formula)

def blend_exclusion(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    """
    Blend function which returns the result of the exclusion formula of the two colors into a new RGBA object

    Parameters:
    - color1 : ColorSystem -> the first color. It's values undergo the formula
    - color2 : ColorSystem -> the second color. The values are used with the formula to affect the first color
    - formula : typing.Callable

    Returns : RGBA
    """
    formula = lambda a,b : 0.5-2*(a-.5)*(2-.5)
    return _blend_function(color1,color2,formula)
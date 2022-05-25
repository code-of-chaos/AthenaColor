# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

import math
from typing import Callable

# Custom Library

# Custom Packages
from AthenaColor.Objects.Color.ColorSystem import ColorSystem, RGBA
from AthenaColor.Objects.Color.ColorObjectConversion import to_RGBA
from AthenaColor.Objects.Color.ColorTupleConversion import NormalizeRgba

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
    color1_tuple = NormalizeRgba(*to_RGBA(color1).export())
    color2_tuple = NormalizeRgba(*to_RGBA(color2).export())

    # WARNING below values are normalized (aka between 0 and 1)
    normalized_outcome = (formula(a, b) for a, b in zip(color1_tuple, color2_tuple))
    return RGBA(*(n * 255 for n in normalized_outcome))  # need to de normalize them again

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def blend_normal(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    # possible because to_RGBA creates a new object
    return to_RGBA(color2)

def blend_darken(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    formula = lambda a, b: min(a, b)
    return _blend_function(color1,color2,formula)

def blend_multiply(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    formula = lambda a,b : a*b
    return _blend_function(color1,color2,formula)

def blend_colorburn(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    formula = lambda a,b : 1-(1-a)/b
    return _blend_function(color1,color2,formula)

def blend_linearburn(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    formula = lambda a,b : a+b-1
    return _blend_function(color1,color2,formula)

def blend_lighten(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    formula = lambda a,b : max(a,b)
    return _blend_function(color1,color2,formula)

def blend_screen(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    formula = lambda a,b : 1-(1-a)(1-b)
    return _blend_function(color1,color2,formula)

def blend_colordodge(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    formula = lambda a,b : a/(1-b)
    return _blend_function(color1,color2,formula)

def blend_lineardodge(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    formula = lambda a,b : a+b
    return _blend_function(color1,color2,formula)

def blend_overlay(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    def formula(a: float, b: float):
        if a < 0.5:
            return 1 - 2 * (1 - a) * (1 - b)
        else:
            return 2 * a * b

    return _blend_function(color1,color2,formula)

def blend_softlight(color1:ColorSystem, color2:ColorSystem) -> RGBA:
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
    def formula(a: float, b: float):
        if b < 0.5:
            return a*(2*b)
        else:
            return 1-(1-a)*(1-2*(b-0.5))

    return _blend_function(color1,color2,formula)

def blend_vividlight(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    def formula(a: float, b: float):
        if b < 0.5:
            return 1-(1-a)/(2*b)
        else:
            return a/(1-2*(b-.5))

    return _blend_function(color1,color2,formula)

def blend_linearlight(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    def formula(a: float, b: float):
        if b < 0.5:
            return a+2*b-1
        else:
            return a+2*(b-.5)

    return _blend_function(color1,color2,formula)

def blend_pinlight(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    def formula(a: float, b: float):
        if b < 0.5:
            return min(a,2*b)
        else:
            return max(a,2*(b-.5))

    return _blend_function(color1,color2,formula)

def blend_difference(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    formula = lambda a,b : abs(a-b)
    return _blend_function(color1,color2,formula)

def blend_exclusion(color1:ColorSystem, color2:ColorSystem) -> RGBA:
    formula = lambda a,b : 0.5-2*(a-.5)*(2-.5)
    return _blend_function(color1,color2,formula)
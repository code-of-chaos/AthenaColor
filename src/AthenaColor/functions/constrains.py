# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Tuple

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = [
    "constrain", "constrain_rgb", "constrain_hsl", "constrain_rgba", "constrain_hsv", "constrain_cmyk"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def constrain(value: int | float, maximum: int | float, minimum: int | float=0) -> int | float:
    return max(min(value, maximum),minimum)

# ----------------------------------------------------------------------------------------------------------------------
# - Constraints for COLORS -
# ----------------------------------------------------------------------------------------------------------------------
def constrain_hsv(h:int|float,s:int|float,v:int|float)->Tuple[int|float,int|float,int|float]:
    """
    Constrain the given values to the HSV format
    """
    return constrain(h, 360), constrain(s, 1), constrain(v, 1)

def constrain_hsl(h:int|float,s:int|float,l:int|float)->Tuple[int|float,int|float,int|float]:
    """
    Constrain the given values to the HSL format
    """
    return constrain(h, 360), constrain(s, 1), constrain(l, 1)

def constrain_rgb(r:int,g:int,b:int)->Tuple[int,int,int]:
    """
    Constrain the given values to the RGB format
    """
    return constrain(r, 255), constrain(g, 255), constrain(b, 255)

def constrain_cmyk(c:int|float,m:int|float,y:int|float,k:int|float)->Tuple[int|float,int|float,int|float,int|float]:
    """
    Constrain the given values to the CMYK format
    """
    return constrain(c, 1), constrain(m, 1), constrain(y, 1), constrain(k, 1)

def constrain_rgba(r:int,g:int,b:int,a:int)->Tuple[int,int,int,int]:
    """
    Constrain the given values to the RGBA format
    """
    return constrain(r, 255), constrain(g, 255), constrain(b, 255), constrain(a, 255)
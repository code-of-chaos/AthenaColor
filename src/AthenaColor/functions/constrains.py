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
    "contrain", "constrain_rgb", "constrain_hsl", "constrain_rgba", "contrain_hsv", "constrain_cmyk"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def contrain(value:int|float, maximum:int|float, minimum:int|float=0) -> int|float:
    return max(min(value, maximum),minimum)

# ----------------------------------------------------------------------------------------------------------------------
# - Constraints for COLORS -
# ----------------------------------------------------------------------------------------------------------------------
def contrain_hsv(h:int|float,s:int|float,v:int|float)->Tuple[int|float,int|float,int|float]:
    return contrain(h, 360), contrain(s, 1), contrain(v, 1)

def constrain_hsl(h:int|float,s:int|float,l:int|float)->Tuple[int|float,int|float,int|float]:
    return contrain(h, 360), contrain(s, 1), contrain(l, 1)

def constrain_rgb(r:int,g:int,b:int)->Tuple[int,int,int]:
    return contrain(r, 255), contrain(g, 255), contrain(b, 255)

def constrain_cmyk(c:int|float,m:int|float,y:int|float,k:int|float)->Tuple[int|float,int|float,int|float,int|float]:
    return contrain(c, 1), contrain(m, 1), contrain(y, 1), contrain(k, 1)

def constrain_rgba(r:int,g:int,b:int,a:int)->Tuple[int,int,int,int]:
    return contrain(r, 255), contrain(g, 255), contrain(b, 255), contrain(a, 255)
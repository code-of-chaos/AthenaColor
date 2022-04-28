# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Tuple

# Custom Library

# Custom Packages
from AthenaColor.AthenaLib.StrictAnnotated import StrictAnnotated

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = [
    "Constrain", "ConstrainRGB","ConstrainHSL","ConstrainRGBA","ConstrainHSV","ConstrainCMYK"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@StrictAnnotated
def Constrain(value:int|float, maximum:int|float, minimum:int|float=0) -> int|float:
    return max(min(value, maximum),minimum)

# ----------------------------------------------------------------------------------------------------------------------
# - Constraints for OPAQUE COLORSs -
# ----------------------------------------------------------------------------------------------------------------------
@StrictAnnotated
def ConstrainHSV(h:int|float,s:int|float,v:int|float)->Tuple[int|float,int|float,int|float]:
    return Constrain(h, 360),Constrain(s,1),Constrain(v,1)

@StrictAnnotated
def ConstrainHSL(h:int|float,s:int|float,l:int|float)->Tuple[int|float,int|float,int|float]:
    return Constrain(h, 360),Constrain(s,1),Constrain(l,1)

@StrictAnnotated
def ConstrainRGB(r:int,g:int,b:int)->Tuple[int,int,int]:
    return Constrain(r, 255),Constrain(g, 255),Constrain(b, 255)

@StrictAnnotated
def ConstrainCMYK(c:int|float,m:int|float,y:int|float,k:int|float)->Tuple[int|float,int|float,int|float,int|float]:
    return Constrain(c,1),Constrain(m,1),Constrain(y,1),Constrain(k,1)

# ----------------------------------------------------------------------------------------------------------------------
# - Constraints for TRANSPARENT COLORSs -
# ----------------------------------------------------------------------------------------------------------------------
@StrictAnnotated
def ConstrainRGBA(r:int,g:int,b:int,a:int)->Tuple[int,int,int,int]:
    return Constrain(r, 255),Constrain(g, 255),Constrain(b, 255),Constrain(a, 255)
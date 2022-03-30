# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from typing import Any
import math

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def NormalizeRgb(r:int,g:int,b:int) -> tuple[float,float,float]:
    return r/255,g/255,b/255

def TestTypes(types: Any, objects:object|tuple[object]) -> bool:
    return all(map(lambda n: isinstance(n, types),objects))

def Constrain(value:int|float, maximum:int|float, minimum:int|float=0) -> int|float:
    return max(min(value, maximum),minimum)

def round_correctly(value:int|float):
    if value - (value_:=math.floor(value)) < 0.5:
        return value_
    else:
        return math.ceil(value)

# ----------------------------------------------------------------------------------------------------------------------
# - Constraints for ColorSystems -
# ----------------------------------------------------------------------------------------------------------------------
def ConstrainHSV_Tuple(h,s,v)->tuple[int|float,int|float,int|float]:
    s,v = map(lambda x: Constrain(x, 1), (s,v))
    return Constrain(h, 360),s,v

def ConstrainHSL_Tuple(h,s,l)->tuple[int|float,int|float,int|float]:
    s,l = map(lambda x: Constrain(x, 1), (s,l))
    return Constrain(h, 360),s,l

def ConstrainRGB_Tuple(r,g,b)->tuple[int|float,int|float,int|float]:
    r,g,b = map(lambda x: Constrain(x, 255), (r,g,b))
    return r,g,b

def ConstrainCMYK_Tuple(c,m,y,k)->tuple[int|float,int|float,int|float,int|float]:
    c,m,y,k = map(lambda x: Constrain(x, 1), (c,m,y,k))
    return c,m,y,k
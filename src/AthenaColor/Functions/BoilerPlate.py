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

def RoundCorrectly(value:int|float) -> int:
    if value - (value_:=math.floor(value)) < 0.5:
        return value_
    else:
        return math.ceil(value)
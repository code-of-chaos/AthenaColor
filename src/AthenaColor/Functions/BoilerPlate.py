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
    """
    Returns r,g,b elements, each divided by 255
    """
    return r/255,g/255,b/255

def TestTypes(types: Any, objects:object|tuple[object,...]) -> bool:
    """
    runs an isinstance(...,types) against multiple objects.
    All have to pass, for the function to return a TRUE
    """
    return all(map(lambda n: isinstance(n, types),objects))

def Constrain(value:int|float, maximum:int|float, minimum:int|float=0) -> int|float:
    """
    Maxes and Minimizes the given value to the two defined constraints
    minimum is set to 0 by default, while maximum has no default value
    """
    return max(min(value, maximum),minimum)

def RoundHalfUp(value:int|float) -> int: # because Twidi didn't like RoundCorrectly :P
    """
    Round a given number to the nearest integer value.
    In comparison to the standard round(), it rounds values which land exactly on 0.5 to the upperbound.
    """
    if value - (value_:=math.floor(value)) < 0.5:
        return value_
    else:
        return math.ceil(value)
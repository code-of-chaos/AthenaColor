# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import math

# Custom Library

# Custom Packages
from .TypeTesting import InputTest

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@InputTest.Custom(types=(int, float))
def Normalize(value:int|float, factor:int|float=100)->float:
    return value/factor

@InputTest.Custom(types=(int, float))
def Constrain(value:int|float, maximum:int|float, minimum:int|float=0) -> int|float:
    return max(min(value, maximum),minimum)


@InputTest.Custom(types=(int, float))
def RoundHalfUp(value:int|float) -> int: # because Twidi didn't like RoundCorrectly :P
    if value - (value_:=math.floor(value)) < 0.5:
        return value_
    else:
        return math.ceil(value)
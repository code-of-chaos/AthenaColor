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
from .Union import IntFloat

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@InputTest.Custom(types=(int, float))
def Normalize(value:IntFloat, factor:IntFloat=100)->float:
    return value/factor

@InputTest.Custom(types=(int, float))
def Constrain(value:IntFloat, maximum:IntFloat, minimum:IntFloat=0) -> IntFloat:
    return max(min(value, maximum),minimum)


@InputTest.Custom(types=(int, float))
def RoundHalfUp(value:IntFloat) -> int: # because Twidi didn't like RoundCorrectly :P
    if value - (value_:=math.floor(value)) < 0.5:
        return value_
    else:
        return math.ceil(value)
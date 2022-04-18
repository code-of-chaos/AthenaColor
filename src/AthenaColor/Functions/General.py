# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import math

# Custom Library

# Custom Packages
from AthenaColor.Functions.StrictTyping import StrictInput

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = [
    "Normalize", "RoundHalfUp","RoundToDecimals"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@StrictInput.Custom(types=(int, float))
def Normalize(value:int|float, factor:int|float=100)->float:
    return value/factor

@StrictInput.Custom(types=(int, float))
def RoundToDecimals(value:float, decimals=3):
    return round(value, decimals)

@StrictInput.Custom(types=(int, float))
def RoundHalfUp(value:int|float) -> int: # because Twidi didn't like RoundCorrectly :P
    value_ = math.floor(value)
    if value - value_ < 0.5:
        return value_
    else:
        return math.ceil(value)
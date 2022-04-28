# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import math

# Custom Library

# Custom Packages
from AthenaColor.InitClass import init
from AthenaColor.AthenaLib.StrictAnnotated import StrictAnnotated

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = [
    "Normalize", "RoundHalfUp","RoundToDecimals"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@StrictAnnotated
def Normalize(value:int|float, factor:int|float=100)->float:
    return value/factor

@StrictAnnotated
def RoundToDecimals(value:int|float, decimals=init.decimalPlaces):
    return round(value, decimals)

@StrictAnnotated
def RoundHalfUp(value:int|float) -> int: # because Twidi didn't like RoundCorrectly :P
    value_ = math.floor(value)
    if value - value_ < 0.5:
        return value_
    else:
        return math.ceil(value)
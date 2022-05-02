# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any

# Custom Library

# Custom Packages
from AthenaColor.InitClass import init

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = [
    "Normalize", "RoundHalfUp","RoundToDecimals", "StrictType"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def Normalize(value:int|float, factor:int|float=100)->float:
    return value/factor

def RoundToDecimals(value:int|float, decimals:int=None):
    if decimals is None:
        decimals = init.decimalPlaces
    return round(value, decimals)

def RoundHalfUp(value:int|float) -> int: # because Twidi didn't like RoundCorrectly :P
    return int(value + 0.5) # thanks for tedthetwonk for refinement

def StrictType(object_, type_) -> Any:
    if not isinstance(object_, type_):
        raise TypeError(f"{object_} was not of the type: {type_}")
    return object_
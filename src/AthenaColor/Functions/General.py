# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor.InitClass import init

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = [
    "RoundHalfUp","RoundToDecimals"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def RoundToDecimals(value:int|float, decimals:int=init.decimalPlaces):
    return round(value, decimals)

def RoundHalfUp(value:int|float) -> int: # because Twidi didn't like RoundCorrectly :P
    return int(value + 0.5) # thanks for tedthetwonk for refinement
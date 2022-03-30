# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor.Functions.ColorConversion import (
    hexa_to_rgba,
    rgba_to_hexa
)
from .RGBA import RGBA
from ._ColorSystem import _HEXA


# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
# inherits from rgb as it is just another notation of the rgb format
class HEXA(RGBA,_HEXA):
    def __init__(self, hex_value:str):
        self.r,self.g,self.b,self.a = hexa_to_rgba(hex_value)

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __str__(self) -> str:
        return rgba_to_hexa(self.r,self.g,self.b,self.a)

    def __repr__(self) -> str:
        return f"hexadecimal(r={self.r},g={self.g},b={self.b},a={self.a})"
# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from .Rgb import RGB
from ...Functions.ColorConversion import (
    hexadecimal_to_rgb,
    rgb_to_hexadecimal
)


# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
# inherits from rgb as it is just another notation of the rgb format
class hexadecimal(RGB):
    def __init__(self, hex_value:str):
        self.r,self.g,self.b = hexadecimal_to_rgb(hex_value)

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __str__(self) -> str:
        return rgb_to_hexadecimal(self.r,self.g,self.b)

    def __repr__(self) -> str:
        return f"hexadecimal(r={self.r},g={self.g},b={self.b})"
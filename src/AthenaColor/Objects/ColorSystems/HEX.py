# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor.Functions.ColorsTuples import (
    hex_to_rgb,
    rgb_to_hex
)
from .RGB import RGB


# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
# inherits from rgb as it is just another notation of the rgb format
class HEX(RGB):
    def __init__(self, hex_value:str):
        self.r,self.g,self.b = hex_to_rgb(hex_value)

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __str__(self) -> str:
        return rgb_to_hex(self.r,self.g,self.b)

    def __repr__(self) -> str:
        return f"hexadecimal(r={self.r},g={self.g},b={self.b})"
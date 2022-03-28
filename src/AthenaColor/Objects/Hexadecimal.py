# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from .Rgb import rgb

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class hexadecimal(rgb):
    # ------------------------------------------------------------------------------------------------------------------
    # INIT method
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, hex_value:str):
        if isinstance(hex_value, str):
            # Form hex value in usable state (cast away the '#' value)
            if hex_value[0] == "#":
                hex_v = hex_value[1:]
            elif len(hex_value) == 6:
                hex_v=hex_value
            else:
                raise ValueError("Hexadecimal was given in an incorrect format")

            # Unpack hex into integer rgb values
            self.r, self.g, self.b = tuple(
                int(hex_v[i:i + 2], 16)
                for i in (0, 2, 4)
            )

        else:
            raise ValueError("no correct str was given on creation")
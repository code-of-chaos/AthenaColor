# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
import AthenaColor

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    a = AthenaColor.ColorSystems.RGB(255,255,255)
    AthenaColor.init.rgb_round_05_up = True
    a -= (125,14.5,13)
    print(a)
    print(a==AthenaColor.ColorSystems.RGB(255,255,255))

    from AthenaColor.Functions.ColorObjectConversion import *

    print(a)

    b = to_hsl(a)
    print(repr(b))
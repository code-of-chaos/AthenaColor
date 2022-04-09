# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = [
    "init",
    "ConvertColorTuple","ConvertColorObject",
    "RGB","RGBA","HEX","HEXA","HSV","HSL",
    "Fore","Back","Underline","Style",
    "ForeNest","BackNest","UnderlineNest","StyleNest",
]
# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor.v3_09.Data import *
from AthenaColor.v3_09.InitClass import init
from AthenaColor.v3_09.Objects.ColorSystems import (
    RGB,RGBA,HEX,HEXA,HSV,HSL,CMYK
)
from AthenaColor.v3_09.Objects.Console.Styling import (
    Fore,ForeNest,Back,BackNest,Underline,UnderlineNest,Style,StyleNest
)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ConvertColorTuple:
    from AthenaColor.v3_09.Functions.ColorTupleConversion import (
        hsl_to_hsv,hsv_to_hsl,hex_to_hsl,hsl_to_hex,hex_to_hsv,hsv_to_hex,rgb_to_hsl,hsl_to_rgb,rgb_to_hsv,hsv_to_rgb,
        hsv_to_cmyk,cmyk_to_hsv,cmyk_to_hsl,hsl_to_cmyk,hex_to_cmyk,cmyk_to_hex,rgb_to_cmyk,cmyk_to_rgb,hex_to_rgb,
        hexa_to_rgba,rgba_to_hexa,rgb_to_hex
    )

class ConvertColorObject:
    from AthenaColor.v3_09.Functions.ColorObjectConversion import (
        to_RGB, to_RGBA, to_HSV, to_HSL, to_HEX, to_HEXA, to_CMYK
    )
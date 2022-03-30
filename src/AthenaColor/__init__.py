# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import os
import sys

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - INIT class -
# ----------------------------------------------------------------------------------------------------------------------
class _InitClass:
    esc_hex = "\x1b"
    esc_octal = "\033"
    esc_uni = "\u001b"

    esc = esc_hex

    def __init__(self, escape_code:str=None):
        self.set_esc(escape_code)

        # prep the console for colors
        if sys.platform == 'win32':
            os.system("color")
            
    @classmethod
    def set_esc(cls, escape_code:str=None):
        # define escape codes
        if escape_code is None:
            cls.esc = cls.esc_hex
        elif escape_code in [cls.esc_hex,cls.esc_octal, cls.esc_octal]:
            cls.esc = escape_code
        else:
            raise ValueError("escape_code not defined correctly")

init = _InitClass()

# ----------------------------------------------------------------------------------------------------------------------
# - AthenaColor Imports -
# ----------------------------------------------------------------------------------------------------------------------
from .Objects.Console import (
    Fore,
    Back,
    Underline, #technically present but doesn't work in PyCharm
    Style,

    ForeNest,
    BackNest,
    UnderlineNest, #technically present but doesn't work in PyCharm
    StyleNest
)

class ColorSystems:
    from AthenaColor.Objects import (
        RGB,
        HEX,
        CMYK,
        HSL,
        HSV
    )

# ----------------------------------------------------------------------------------------------------------------------
# - Import other systems -
# ----------------------------------------------------------------------------------------------------------------------
import AthenaColor.Data
import AthenaColor.Functions
import AthenaColor.Objects
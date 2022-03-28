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
class Init:
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

init = Init()

# ----------------------------------------------------------------------------------------------------------------------
# - AthenaColor Imports -
# ----------------------------------------------------------------------------------------------------------------------
from AthenaColor.Styling.Inline import (
    Fore,
    Back,
    Style
)

from AthenaColor.Styling.Nested import (
    Fore    as ForeNest ,
    Back    as BackNest ,
    Style   as StyleNest
)

from AthenaColor.Objects import (
    rgb,
    HtmlColors,
    hexadecimal
)

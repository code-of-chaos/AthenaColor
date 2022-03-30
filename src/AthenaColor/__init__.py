__all__=[
    "init",
    # Styles Inline
    "Fore","Back","Underline","Style",
    # Styles Nested
    "ForeNest","BackNest","UnderlineNest","StyleNest",
    # Color Objects
    "RGB","HEX","CMYK","HSL","HSV",
    "RGBA","HEXA",
]
# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import os
import sys

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - INIT class -
# ----------------------------------------------------------------------------------------------------------------------
class _InitClass:
    from .Data.ConsoleCodes import (esc_hex,esc_octal,esc_uni)
    _esc:str
    _rgb_round_05_up:bool

    def __init__(self):
        # prep the console for colors
        if sys.platform == 'win32':
            os.system("color")
        self.esc = self.esc_hex
        self.rgb_round_05_up = True

    # ------------------------------------------------------------------------------------------------------------------
    # - ANSI esc character -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def esc(self):
        return self._esc
    @esc.setter
    def esc(self,value:str):
        if value in [self.esc_octal,self.esc_hex, self.esc_uni]:
            self._esc = value
        else:
            raise ValueError("escape_code not defined correctly")
    def esc_list(self):
        return self.esc_hex,self.esc_octal,self.esc_uni

    # ------------------------------------------------------------------------------------------------------------------
    # - RGB rounding -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def rgb_round_05_up(self):
        return self._rgb_round_05_up
    @rgb_round_05_up.setter
    def rgb_round_05_up(self, value: bool):
        if isinstance(value, bool):
            self._rgb_round_05_up = value
        else:
            raise ValueError("rgb_round_05_up not defined correctly")

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

from AthenaColor.Objects.ColorSystems.Opaque import (
    RGB,
    HEX,
    CMYK,
    HSL,
    HSV
)
from AthenaColor.Objects.ColorSystems.Transparent import (
    RGBA,
    HEXA,
)

# ----------------------------------------------------------------------------------------------------------------------
# - Import other systems -
# ----------------------------------------------------------------------------------------------------------------------
import AthenaColor.Data
import AthenaColor.Functions
import AthenaColor.Objects
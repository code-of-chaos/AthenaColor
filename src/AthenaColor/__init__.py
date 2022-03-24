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

    esc:str

    def __init__(self, escape_code:str=None):
        self.set_esc(escape_code)

        # prep the console for colors
        if sys.platform == 'win32':
            os.system("color")

    def set_esc(self, escape_code:str=None):
        # define escape codes
        if escape_code is None:
            self.esc = self.esc_hex
        elif escape_code in [self.esc_hex,self.esc_octal, self.esc_octal]:
            self.esc = escape_code
        else:
            raise ValueError("escape_code not defined correctly")

init = Init()

# ----------------------------------------------------------------------------------------------------------------------
# - AthenaColor Imports -
# ----------------------------------------------------------------------------------------------------------------------
from AthenaColor.Styling import(
    Fore,
    Back,
    Basic
)
from AthenaColor.Objects import (
    rgb,
    HtmlColors,
    hexadecimal
)

class Style:
    from AthenaColor.Styling.MakeUp import (
        Reset,
        Italic,
        NoItalic,
        Bold,
        NoBold,
        Underline,
        NoUnderline,
        Crossed,
        NoCrossed,
        Reversed,
        NoReversed,
        Frame,
        NoFrame,
        Circle,
        NoCircle,
        UnderlineDouble,
        NoForeground,
        NoBackground
    )
    class Unverfified:
        from AthenaColor.Styling.MakeUp import (
            BlinkSlow,
            NoBlinkSlow,
            BlinkRapid,
            NoBlinkRapid,
            Conceal,
            NoConceal,
            FontPrimary,
            FontSecond1,
            FontSecond2,
            FontSecond3,
            FontSecond4,
            FontSecond5,
            FontSecond6,
            FontSecond8,
            FontSecond9,
            FontSecond10,
            NoFont,
            Fraktur,
            PropSpacing,
            NoPropSpacing,
        )

# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from functools import partial

# Custom Library

# Custom Packages
from ...Functions import (
    NestedSequence
)

# ----------------------------------------------------------------------------------------------------------------------
# - Style Sequences -
# ----------------------------------------------------------------------------------------------------------------------
Reset                       = partial(NestedSequence, control_code=0)
Bold                        = partial(NestedSequence, control_code=1 , reset_code=22)
NoBold                      = partial(NestedSequence, control_code=22, reset_code=1 )
Dim                         = partial(NestedSequence, control_code=2 , reset_code=22)
NoDim                       = partial(NestedSequence, control_code=22, reset_code=2 )
Italic                      = partial(NestedSequence, control_code=3 , reset_code=23)
NoItalic                    = partial(NestedSequence, control_code=23, reset_code=3 )
Underline                   = partial(NestedSequence, control_code=4 , reset_code=24)
NoUnderline                 = partial(NestedSequence, control_code=24, reset_code=4 )
BlinkSlow                   = partial(NestedSequence, control_code=5 , reset_code=25)
NoBlinkSlow                 = partial(NestedSequence, control_code=25, reset_code=5 )
BlinkRapid                  = partial(NestedSequence, control_code=6 , reset_code=25)
NoBlinkRapid                = partial(NestedSequence, control_code=25, reset_code=6 )
Reversed                    = partial(NestedSequence, control_code=7 , reset_code=27)
NoReversed                  = partial(NestedSequence, control_code=27, reset_code=7 )
Conceal                     = partial(NestedSequence, control_code=8 , reset_code=28)
NoConceal                   = partial(NestedSequence, control_code=28, reset_code=8 )
Crossed                     = partial(NestedSequence, control_code=9 , reset_code=29)
NoCrossed                   = partial(NestedSequence, control_code=29, reset_code=9 )
FontPrimary                 = partial(NestedSequence, control_code=10, reset_code=10)
FontSecond1                 = partial(NestedSequence, control_code=11, reset_code=10)
FontSecond2                 = partial(NestedSequence, control_code=12, reset_code=10)
FontSecond3                 = partial(NestedSequence, control_code=13, reset_code=10)
FontSecond4                 = partial(NestedSequence, control_code=14, reset_code=10)
FontSecond5                 = partial(NestedSequence, control_code=15, reset_code=10)
FontSecond6                 = partial(NestedSequence, control_code=16, reset_code=10)
FontSecond8                 = partial(NestedSequence, control_code=17, reset_code=10)
FontSecond9                 = partial(NestedSequence, control_code=18, reset_code=10)
FontSecond10                = partial(NestedSequence, control_code=19, reset_code=10)
NoFont                      = partial(NestedSequence, control_code=10)
Fraktur                     = partial(NestedSequence, control_code=20)
UnderlineDouble             = partial(NestedSequence, control_code=21, reset_code=24)
NoUnderlineDouble           = partial(NestedSequence, control_code=24, reset_code=21)
PropSpacing                 = partial(NestedSequence, control_code=26, reset_code=26)
NoPropSpacing               = partial(NestedSequence, control_code=26, reset_code=26)
NoForeground                = partial(NestedSequence, control_code=39)
NoBackground                = partial(NestedSequence, control_code=49)
Frame                       = partial(NestedSequence, control_code=51, reset_code=54)
NoFrame                     = partial(NestedSequence, control_code=54, reset_code=51)
Circle                      = partial(NestedSequence, control_code=52, reset_code=54)
NoCircle                    = partial(NestedSequence, control_code=54, reset_code=52)
OverLine                    = partial(NestedSequence, control_code=53, reset_code=55)
NoOverLine                  = partial(NestedSequence, control_code=55, reset_code=53)
UnderColourDefault          = partial(NestedSequence, control_code=59)
IdeogramUnderLine           = partial(NestedSequence, control_code=60, reset_code=65)
IdeogramUnderLineDouble     = partial(NestedSequence, control_code=61, reset_code=65)
IdeogramOverLine            = partial(NestedSequence, control_code=62, reset_code=65)
IdeogramOverLineDouble      = partial(NestedSequence, control_code=63, reset_code=65)
IdeogramStress              = partial(NestedSequence, control_code=64, reset_code=65)
NoIdeogram                  = partial(NestedSequence, control_code=65)
SuperScript                 = partial(NestedSequence, control_code=73, reset_code=75)
SubScript                   = partial(NestedSequence, control_code=74, reset_code=75)
NoScript                    = partial(NestedSequence, control_code=75)


# ----------------------------------------------------------------------------------------------------------------------
# - Basic Sequences -
# ----------------------------------------------------------------------------------------------------------------------
class Basic:
    class Fore:
        Black           = partial(NestedSequence, color_code=30, reset_code=39)
        Red             = partial(NestedSequence, color_code=31, reset_code=39)
        Green           = partial(NestedSequence, color_code=32, reset_code=39)
        Yellow          = partial(NestedSequence, color_code=33, reset_code=39)
        Blue            = partial(NestedSequence, color_code=34, reset_code=39)
        Magenta         = partial(NestedSequence, color_code=35, reset_code=39)
        Cyan            = partial(NestedSequence, color_code=36, reset_code=39)
        White           = partial(NestedSequence, color_code=37, reset_code=39)
        BrightBlack     = partial(NestedSequence, color_code=90, reset_code=39)
        BrightRed       = partial(NestedSequence, color_code=91, reset_code=39)
        BrightGreen     = partial(NestedSequence, color_code=92, reset_code=39)
        BrightYellow    = partial(NestedSequence, color_code=93, reset_code=39)
        BrightBlue      = partial(NestedSequence, color_code=94, reset_code=39)
        BrightMagenta   = partial(NestedSequence, color_code=95, reset_code=39)
        BrightCyan      = partial(NestedSequence, color_code=96, reset_code=39)
        BrightWhite     = partial(NestedSequence, color_code=97, reset_code=39)

    class Back:
        Black           = partial(NestedSequence, color_code=40 , reset_code=49)
        Red             = partial(NestedSequence, color_code=41 , reset_code=49)
        Green           = partial(NestedSequence, color_code=42 , reset_code=49)
        Yellow          = partial(NestedSequence, color_code=43 , reset_code=49)
        Blue            = partial(NestedSequence, color_code=44 , reset_code=49)
        Magenta         = partial(NestedSequence, color_code=45 , reset_code=49)
        Cyan            = partial(NestedSequence, color_code=46 , reset_code=49)
        White           = partial(NestedSequence, color_code=47 , reset_code=49)
        BrightBlack     = partial(NestedSequence, color_code=100, reset_code=49)
        BrightRed       = partial(NestedSequence, color_code=101, reset_code=49)
        BrightGreen     = partial(NestedSequence, color_code=102, reset_code=49)
        BrightYellow    = partial(NestedSequence, color_code=103, reset_code=49)
        BrightBlue      = partial(NestedSequence, color_code=104, reset_code=49)
        BrightMagenta   = partial(NestedSequence, color_code=105, reset_code=49)
        BrightCyan      = partial(NestedSequence, color_code=106, reset_code=49)
        BrightWhite     = partial(NestedSequence, color_code=107, reset_code=49)

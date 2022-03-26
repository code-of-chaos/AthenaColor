# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from functools import partial

# Custom Library

# Custom Packages
from AthenaColor import init
from AthenaColor.BASE import end_codes

# ----------------------------------------------------------------------------------------------------------------------
# - Support Functions -
# ----------------------------------------------------------------------------------------------------------------------
def SequenceColor(*obj, control_code: str | int = '',reset_code:str|int=None) -> str:
    return ''.join([
        # Define the Style first, else the next "o" will not have the Style set
        f'{init.esc}[{control_code}{end_codes.color}',
        *[
            # Negate the last code, doesn't do a thing if reset code is called
            (o+f'{init.esc}[{control_code}{end_codes.color}') if o != obj[-1] else o
            for o in obj
        ],
        # Reset the specifc Style Choice with the corresponding "No..." code
        f'{init.esc}[{reset_code}{end_codes.color}' if reset_code is not None else ''
    ])

# ----------------------------------------------------------------------------------------------------------------------
# - Style Sequences -
# ----------------------------------------------------------------------------------------------------------------------
Reset                       = partial(SequenceColor, control_code=0)
Bold                        = partial(SequenceColor, control_code=1 , reset_code=22)
NoBold                      = partial(SequenceColor, control_code=22, reset_code=1 )
Dim                         = partial(SequenceColor, control_code=2 , reset_code=22)
NoDim                       = partial(SequenceColor, control_code=22, reset_code=2 )
Italic                      = partial(SequenceColor, control_code=3 , reset_code=23)
NoItalic                    = partial(SequenceColor, control_code=23, reset_code=3 )
Underline                   = partial(SequenceColor, control_code=4 , reset_code=24)
NoUnderline                 = partial(SequenceColor, control_code=24, reset_code=4 )
BlinkSlow                   = partial(SequenceColor, control_code=5 , reset_code=25)
NoBlinkSlow                 = partial(SequenceColor, control_code=25, reset_code=5 )
BlinkRapid                  = partial(SequenceColor, control_code=6 , reset_code=25)
NoBlinkRapid                = partial(SequenceColor, control_code=25, reset_code=6 )
Reversed                    = partial(SequenceColor, control_code=7 , reset_code=27)
NoReversed                  = partial(SequenceColor, control_code=27, reset_code=7 )
Conceal                     = partial(SequenceColor, control_code=8 , reset_code=28)
NoConceal                   = partial(SequenceColor, control_code=28, reset_code=8 )
Crossed                     = partial(SequenceColor, control_code=9 , reset_code=29)
NoCrossed                   = partial(SequenceColor, control_code=29, reset_code=9 )
FontPrimary                 = partial(SequenceColor, control_code=10, reset_code=10)
FontSecond1                 = partial(SequenceColor, control_code=11, reset_code=10)
FontSecond2                 = partial(SequenceColor, control_code=12, reset_code=10)
FontSecond3                 = partial(SequenceColor, control_code=13, reset_code=10)
FontSecond4                 = partial(SequenceColor, control_code=14, reset_code=10)
FontSecond5                 = partial(SequenceColor, control_code=15, reset_code=10)
FontSecond6                 = partial(SequenceColor, control_code=16, reset_code=10)
FontSecond8                 = partial(SequenceColor, control_code=17, reset_code=10)
FontSecond9                 = partial(SequenceColor, control_code=18, reset_code=10)
FontSecond10                = partial(SequenceColor, control_code=19, reset_code=10)
NoFont                      = partial(SequenceColor, control_code=10)
Fraktur                     = partial(SequenceColor, control_code=20)
UnderlineDouble             = partial(SequenceColor, control_code=21, reset_code=24)
NoUnderlineDouble           = partial(SequenceColor, control_code=24, reset_code=21)
PropSpacing                 = partial(SequenceColor, control_code=26, reset_code=26)
NoPropSpacing               = partial(SequenceColor, control_code=26, reset_code=26)
NoForeground                = partial(SequenceColor, control_code=39)
NoBackground                = partial(SequenceColor, control_code=49)
Frame                       = partial(SequenceColor, control_code=51, reset_code=54)
NoFrame                     = partial(SequenceColor, control_code=54, reset_code=51)
Circle                      = partial(SequenceColor, control_code=52, reset_code=54)
NoCircle                    = partial(SequenceColor, control_code=54, reset_code=52)
OverLine                    = partial(SequenceColor, control_code=53, reset_code=55)
NoOverLine                  = partial(SequenceColor, control_code=55, reset_code=53)
UnderColourDefault          = partial(SequenceColor, control_code=59)
IdeogramUnderLine           = partial(SequenceColor, control_code=60, reset_code=65)
IdeogramUnderLineDouble     = partial(SequenceColor, control_code=61, reset_code=65)
IdeogramOverLine            = partial(SequenceColor, control_code=62, reset_code=65)
IdeogramOverLineDouble      = partial(SequenceColor, control_code=63, reset_code=65)
IdeogramStress              = partial(SequenceColor, control_code=64, reset_code=65)
NoIdeogram                  = partial(SequenceColor, control_code=65)
SuperScript                 = partial(SequenceColor, control_code=73, reset_code=75)
SubScript                   = partial(SequenceColor, control_code=74, reset_code=75)
NoScript                    = partial(SequenceColor, control_code=75)


# ----------------------------------------------------------------------------------------------------------------------
# - Basic Sequences -
# ----------------------------------------------------------------------------------------------------------------------
class Basic:
    class Fore:
        Black           = partial(SequenceColor, color_code=30, reset_code=39)
        Red             = partial(SequenceColor, color_code=31, reset_code=39)
        Green           = partial(SequenceColor, color_code=32, reset_code=39)
        Yellow          = partial(SequenceColor, color_code=33, reset_code=39)
        Blue            = partial(SequenceColor, color_code=34, reset_code=39)
        Magenta         = partial(SequenceColor, color_code=35, reset_code=39)
        Cyan            = partial(SequenceColor, color_code=36, reset_code=39)
        White           = partial(SequenceColor, color_code=37, reset_code=39)
        BrightBlack     = partial(SequenceColor, color_code=90, reset_code=39)
        BrightRed       = partial(SequenceColor, color_code=91, reset_code=39)
        BrightGreen     = partial(SequenceColor, color_code=92, reset_code=39)
        BrightYellow    = partial(SequenceColor, color_code=93, reset_code=39)
        BrightBlue      = partial(SequenceColor, color_code=94, reset_code=39)
        BrightMagenta   = partial(SequenceColor, color_code=95, reset_code=39)
        BrightCyan      = partial(SequenceColor, color_code=96, reset_code=39)
        BrightWhite     = partial(SequenceColor, color_code=97, reset_code=39)

    class Back:
        Black           = partial(SequenceColor, color_code=40 , reset_code=49)
        Red             = partial(SequenceColor, color_code=41 , reset_code=49)
        Green           = partial(SequenceColor, color_code=42 , reset_code=49)
        Yellow          = partial(SequenceColor, color_code=43 , reset_code=49)
        Blue            = partial(SequenceColor, color_code=44 , reset_code=49)
        Magenta         = partial(SequenceColor, color_code=45 , reset_code=49)
        Cyan            = partial(SequenceColor, color_code=46 , reset_code=49)
        White           = partial(SequenceColor, color_code=47 , reset_code=49)
        BrightBlack     = partial(SequenceColor, color_code=100, reset_code=49)
        BrightRed       = partial(SequenceColor, color_code=101, reset_code=49)
        BrightGreen     = partial(SequenceColor, color_code=102, reset_code=49)
        BrightYellow    = partial(SequenceColor, color_code=103, reset_code=49)
        BrightBlue      = partial(SequenceColor, color_code=104, reset_code=49)
        BrightMagenta   = partial(SequenceColor, color_code=105, reset_code=49)
        BrightCyan      = partial(SequenceColor, color_code=106, reset_code=49)
        BrightWhite     = partial(SequenceColor, color_code=107, reset_code=49)

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
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def control_sequence(*obj, control_code: str | int = '') -> str:
    if control_code in ['0', 0]:
        last = f''
    else:
        last = f'{init.esc}[{control_code}{end_codes.color}'
    return ''.join([
        f'{init.esc}[{control_code}{end_codes.color}',
        *[o+ f'{init.esc}[{control_code}{end_codes.color}' for o in obj],
        last
    ])


def color_sequence(*obj, color_code: str | int = '') -> str:
    return ''.join([
        f'{init.esc}[{color_code}m',
        *[o+f'{init.esc}[{color_code}m' for o in obj],
        f'{init.esc}[39m'
    ])


Reset                       = partial(control_sequence, control_code=0)
Bold                        = partial(control_sequence, control_code=1)
NoBold                      = partial(control_sequence, control_code=22)
Dim                         = partial(control_sequence, control_code=2)
NoDim                       = partial(control_sequence, control_code=22)
Italic                      = partial(control_sequence, control_code=3)
NoItalic                    = partial(control_sequence, control_code=23)
Underline                   = partial(control_sequence, control_code=4)
NoUnderline                 = partial(control_sequence, control_code=24)
BlinkSlow                   = partial(control_sequence, control_code=5)
NoBlinkSlow                 = partial(control_sequence, control_code=25)
BlinkRapid                  = partial(control_sequence, control_code=6)
NoBlinkRapid                = partial(control_sequence, control_code=25)
Reversed                    = partial(control_sequence, control_code=7)
NoReversed                  = partial(control_sequence, control_code=27)
Conceal                     = partial(control_sequence, control_code=8)
NoConceal                   = partial(control_sequence, control_code=28)
Crossed                     = partial(control_sequence, control_code=9)
NoCrossed                   = partial(control_sequence, control_code=29)
FontPrimary                 = partial(control_sequence, control_code=10)
FontSecond1                 = partial(control_sequence, control_code=11)
FontSecond2                 = partial(control_sequence, control_code=12)
FontSecond3                 = partial(control_sequence, control_code=13)
FontSecond4                 = partial(control_sequence, control_code=14)
FontSecond5                 = partial(control_sequence, control_code=15)
FontSecond6                 = partial(control_sequence, control_code=16)
FontSecond8                 = partial(control_sequence, control_code=17)
FontSecond9                 = partial(control_sequence, control_code=18)
FontSecond10                = partial(control_sequence, control_code=19)
NoFont                      = partial(control_sequence, control_code=10)
Fraktur                     = partial(control_sequence, control_code=20)
UnderlineDouble             = partial(control_sequence, control_code=21)
NoUnderlineDouble           = partial(control_sequence, control_code=24)
PropSpacing                 = partial(control_sequence, control_code=26)
NoPropSpacing               = partial(control_sequence, control_code=26)
NoForeground                = partial(control_sequence, control_code=39)
NoBackground                = partial(control_sequence, control_code=49)
Frame                       = partial(control_sequence, control_code=51)
NoFrame                     = partial(control_sequence, control_code=54)
Circle                      = partial(control_sequence, control_code=52)
NoCircle                    = partial(control_sequence, control_code=54)
OverLine                    = partial(control_sequence, control_code=53)
NoOverLine                  = partial(control_sequence, control_code=55)
UnderColourDefault          = partial(control_sequence, control_code=59)
IdeogramUnderLine           = partial(control_sequence, control_code=60)
IdeogramUnderLineDouble     = partial(control_sequence, control_code=61)
IdeogramOverLine            = partial(control_sequence, control_code=62)
IdeogramOverLineDouble      = partial(control_sequence, control_code=63)
IdeogramStress              = partial(control_sequence, control_code=64)
NoIdeogram                  = partial(control_sequence, control_code=65)
SuperScript                 = partial(control_sequence, control_code=73)
SubScript                   = partial(control_sequence, control_code=74)
NoScript                    = partial(control_sequence, control_code=75)


class Basic:
    class Fore:
        Black           = partial(color_sequence, color_code=30)
        Red             = partial(color_sequence, color_code=31)
        Green           = partial(color_sequence, color_code=32)
        Yellow          = partial(color_sequence, color_code=33)
        Blue            = partial(color_sequence, color_code=34)
        Magenta         = partial(color_sequence, color_code=35)
        Cyan            = partial(color_sequence, color_code=36)
        White           = partial(color_sequence, color_code=37)
        BrightBlack     = partial(color_sequence, color_code=90)
        BrightRed       = partial(color_sequence, color_code=91)
        BrightGreen     = partial(color_sequence, color_code=92)
        BrightYellow    = partial(color_sequence, color_code=93)
        BrightBlue      = partial(color_sequence, color_code=94)
        BrightMagenta   = partial(color_sequence, color_code=95)
        BrightCyan      = partial(color_sequence, color_code=96)
        BrightWhite     = partial(color_sequence, color_code=97)

    class Back:
        Black           = partial(color_sequence, color_code=40)
        Red             = partial(color_sequence, color_code=41)
        Green           = partial(color_sequence, color_code=42)
        Yellow          = partial(color_sequence, color_code=43)
        Blue            = partial(color_sequence, color_code=44)
        Magenta         = partial(color_sequence, color_code=45)
        Cyan            = partial(color_sequence, color_code=46)
        White           = partial(color_sequence, color_code=47)
        BrightBlack     = partial(color_sequence, color_code=100)
        BrightRed       = partial(color_sequence, color_code=101)
        BrightGreen     = partial(color_sequence, color_code=102)
        BrightYellow    = partial(color_sequence, color_code=103)
        BrightBlue      = partial(color_sequence, color_code=104)
        BrightMagenta   = partial(color_sequence, color_code=105)
        BrightCyan      = partial(color_sequence, color_code=106)
        BrightWhite     = partial(color_sequence, color_code=107)

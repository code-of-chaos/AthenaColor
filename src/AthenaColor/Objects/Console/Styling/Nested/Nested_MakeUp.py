# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from functools import partial

# Custom Library

# Custom Packages
from AthenaColor.Functions.AnsiSquences import NestedColorSequence

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "StyleNest", "BasicNest"
]

# ----------------------------------------------------------------------------------------------------------------------
# - StyleNest Sequences -
# ----------------------------------------------------------------------------------------------------------------------
class StyleNest:
    # noinspection PyUnresolvedReferences
    __all__ = [
        "Reset",
        "Italic",
        "NoItalic",
        "Bold",
        "NoBold",
        "UnderlineNest",
        "NoUnderline",
        "Crossed",
        "NoCrossed",
        "Reversed",
        "NoReversed",
        "Frame",
        "NoFrame",
        "Circle",
        "NoCircle",
        "UnderlineDouble",
        "NoForeground",
        "NoBackground"
    ]

    Reset = partial(NestedColorSequence, control_code=0)
    Bold = partial(NestedColorSequence, control_code=1, reset_code=22)
    NoBold = partial(NestedColorSequence, control_code=22)
    Dim = partial(NestedColorSequence, control_code=2, reset_code=22)
    NoDim = partial(NestedColorSequence, control_code=22)
    Italic = partial(NestedColorSequence, control_code=3, reset_code=23)
    NoItalic = partial(NestedColorSequence, control_code=23)
    Underline = partial(NestedColorSequence, control_code=4, reset_code=24)
    NoUnderline = partial(NestedColorSequence, control_code=24)
    BlinkSlow = partial(NestedColorSequence, control_code=5, reset_code=25)
    NoBlinkSlow = partial(NestedColorSequence, control_code=25)
    BlinkRapid = partial(NestedColorSequence, control_code=6, reset_code=25)
    NoBlinkRapid = partial(NestedColorSequence, control_code=25)
    Reversed = partial(NestedColorSequence, control_code=7, reset_code=27)
    NoReversed = partial(NestedColorSequence, control_code=27)
    Conceal = partial(NestedColorSequence, control_code=8, reset_code=28)
    NoConceal = partial(NestedColorSequence, control_code=28)
    Crossed = partial(NestedColorSequence, control_code=9, reset_code=29)
    NoCrossed = partial(NestedColorSequence, control_code=29)
    FontPrimary = partial(NestedColorSequence, control_code=10, reset_code=10)
    FontSecond1 = partial(NestedColorSequence, control_code=11, reset_code=10)
    FontSecond2 = partial(NestedColorSequence, control_code=12, reset_code=10)
    FontSecond3 = partial(NestedColorSequence, control_code=13, reset_code=10)
    FontSecond4 = partial(NestedColorSequence, control_code=14, reset_code=10)
    FontSecond5 = partial(NestedColorSequence, control_code=15, reset_code=10)
    FontSecond6 = partial(NestedColorSequence, control_code=16, reset_code=10)
    FontSecond8 = partial(NestedColorSequence, control_code=17, reset_code=10)
    FontSecond9 = partial(NestedColorSequence, control_code=18, reset_code=10)
    FontSecond10 = partial(NestedColorSequence, control_code=19, reset_code=10)
    NoFont = partial(NestedColorSequence, control_code=10)
    Fraktur = partial(NestedColorSequence, control_code=20)
    UnderlineDouble = partial(NestedColorSequence, control_code=21, reset_code=24)
    NoUnderlineDouble = partial(NestedColorSequence, control_code=24)
    PropSpacing = partial(NestedColorSequence, control_code=26, reset_code=26)
    NoPropSpacing = partial(NestedColorSequence, control_code=26)
    NoForeground = partial(NestedColorSequence, control_code=39)
    NoBackground = partial(NestedColorSequence, control_code=49)
    Frame = partial(NestedColorSequence, control_code=51, reset_code=54)
    NoFrame = partial(NestedColorSequence, control_code=54)
    Circle = partial(NestedColorSequence, control_code=52, reset_code=54)
    NoCircle = partial(NestedColorSequence, control_code=54)
    OverLine = partial(NestedColorSequence, control_code=53, reset_code=55)
    NoOverLine = partial(NestedColorSequence, control_code=55)
    UnderColourDefault = partial(NestedColorSequence, control_code=59)
    IdeogramUnderLine = partial(NestedColorSequence, control_code=60, reset_code=65)
    IdeogramUnderLineDouble = partial(NestedColorSequence, control_code=61, reset_code=65)
    IdeogramOverLine = partial(NestedColorSequence, control_code=62, reset_code=65)
    IdeogramOverLineDouble = partial(NestedColorSequence, control_code=63, reset_code=65)
    IdeogramStress = partial(NestedColorSequence, control_code=64, reset_code=65)
    NoIdeogram = partial(NestedColorSequence, control_code=65)
    SuperScript = partial(NestedColorSequence, control_code=73, reset_code=75)
    SubScript = partial(NestedColorSequence, control_code=74, reset_code=75)
    NoScript = partial(NestedColorSequence, control_code=75)

# ----------------------------------------------------------------------------------------------------------------------
# - BasicNest Sequences -
# ----------------------------------------------------------------------------------------------------------------------
class BasicNest:
    class Fore:
        Black           = partial(NestedColorSequence, color_code=30, reset_code=39)
        Red             = partial(NestedColorSequence, color_code=31, reset_code=39)
        Green           = partial(NestedColorSequence, color_code=32, reset_code=39)
        Yellow          = partial(NestedColorSequence, color_code=33, reset_code=39)
        Blue            = partial(NestedColorSequence, color_code=34, reset_code=39)
        Magenta         = partial(NestedColorSequence, color_code=35, reset_code=39)
        Cyan            = partial(NestedColorSequence, color_code=36, reset_code=39)
        White           = partial(NestedColorSequence, color_code=37, reset_code=39)
        BrightBlack     = partial(NestedColorSequence, color_code=90, reset_code=39)
        BrightRed       = partial(NestedColorSequence, color_code=91, reset_code=39)
        BrightGreen     = partial(NestedColorSequence, color_code=92, reset_code=39)
        BrightYellow    = partial(NestedColorSequence, color_code=93, reset_code=39)
        BrightBlue      = partial(NestedColorSequence, color_code=94, reset_code=39)
        BrightMagenta   = partial(NestedColorSequence, color_code=95, reset_code=39)
        BrightCyan      = partial(NestedColorSequence, color_code=96, reset_code=39)
        BrightWhite     = partial(NestedColorSequence, color_code=97, reset_code=39)

    class Back:
        Black           = partial(NestedColorSequence, color_code=40, reset_code=49)
        Red             = partial(NestedColorSequence, color_code=41, reset_code=49)
        Green           = partial(NestedColorSequence, color_code=42, reset_code=49)
        Yellow          = partial(NestedColorSequence, color_code=43, reset_code=49)
        Blue            = partial(NestedColorSequence, color_code=44, reset_code=49)
        Magenta         = partial(NestedColorSequence, color_code=45, reset_code=49)
        Cyan            = partial(NestedColorSequence, color_code=46, reset_code=49)
        White           = partial(NestedColorSequence, color_code=47, reset_code=49)
        BrightBlack     = partial(NestedColorSequence, color_code=100, reset_code=49)
        BrightRed       = partial(NestedColorSequence, color_code=101, reset_code=49)
        BrightGreen     = partial(NestedColorSequence, color_code=102, reset_code=49)
        BrightYellow    = partial(NestedColorSequence, color_code=103, reset_code=49)
        BrightBlue      = partial(NestedColorSequence, color_code=104, reset_code=49)
        BrightMagenta   = partial(NestedColorSequence, color_code=105, reset_code=49)
        BrightCyan      = partial(NestedColorSequence, color_code=106, reset_code=49)
        BrightWhite     = partial(NestedColorSequence, color_code=107, reset_code=49)
# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor.Functions.AnsiSquences import ColorSequence

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "Style","Basic"
]

# ----------------------------------------------------------------------------------------------------------------------
# - StyleNest Sequences -
# ----------------------------------------------------------------------------------------------------------------------
class Style:
    # noinspection PyUnresolvedReferences
    __all__=[
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
    Reset                       = ColorSequence(0)
    Bold                        = ColorSequence(1)
    NoBold                      = ColorSequence(22)
    Dim                         = ColorSequence(2)
    NoDim                       = ColorSequence(22)
    Italic                      = ColorSequence(3)
    NoItalic                    = ColorSequence(23)
    Underline                   = ColorSequence(4)
    NoUnderline                 = ColorSequence(24)
    BlinkSlow                   = ColorSequence(5)  # NOT WORKING PYCHARM
    NoBlinkSlow                 = ColorSequence(25)  # NOT WORKING PYCHARM
    BlinkRapid                  = ColorSequence(6)  # NOT WORKING PYCHARM
    NoBlinkRapid                = ColorSequence(25)  # NOT WORKING PYCHARM
    Reversed                    = ColorSequence(7)
    NoReversed                  = ColorSequence(27)
    Conceal                     = ColorSequence(8)  # NOT WORKING PYCHARM
    NoConceal                   = ColorSequence(28)  # NOT WORKING PYCHARM
    Crossed                     = ColorSequence(9)
    NoCrossed                   = ColorSequence(29)
    FontPrimary                 = ColorSequence(10)  # NOT WORKING PYCHARM
    FontSecond1                 = ColorSequence(11)  # NOT WORKING PYCHARM
    FontSecond2                 = ColorSequence(12)  # NOT WORKING PYCHARM
    FontSecond3                 = ColorSequence(13)  # NOT WORKING PYCHARM
    FontSecond4                 = ColorSequence(14)  # NOT WORKING PYCHARM
    FontSecond5                 = ColorSequence(15)  # NOT WORKING PYCHARM
    FontSecond6                 = ColorSequence(16)  # NOT WORKING PYCHARM
    FontSecond8                 = ColorSequence(17)  # NOT WORKING PYCHARM
    FontSecond9                 = ColorSequence(18)  # NOT WORKING PYCHARM
    FontSecond10                = ColorSequence(19)  # NOT WORKING PYCHARM
    NoFont                      = ColorSequence(10)  # NOT WORKING PYCHARM
    Fraktur                     = ColorSequence(20)  # NOT WORKING PYCHARM
    UnderlineDouble             = ColorSequence(21)
    NoUnderlineDouble           = ColorSequence(24)
    PropSpacing                 = ColorSequence(26)  # NOT WORKING PYCHARM
    NoPropSpacing               = ColorSequence(26)  # NOT WORKING PYCHARM
    # 30 - 37 -> see BasicNest
    # 38 -> see RgbControlled.BackNest
    NoForeground                = ColorSequence(39)
    # 40 - 47 -> see BasicNest
    # 48 -> see RgbControlled.BackNest
    NoBackground                = ColorSequence(49)
    Frame                       = ColorSequence(51)
    NoFrame                     = ColorSequence(54)
    Circle                      = ColorSequence(52)
    NoCircle                    = ColorSequence(54)
    OverLine                    = ColorSequence(53)
    NoOverLine                  = ColorSequence(55)
    # ? 56
    # ? 57
    # 58 -> see RgbControlled.UnderlineNest
    UnderColourDefault          = ColorSequence(59)
    IdeogramUnderLine           = ColorSequence(60)
    IdeogramUnderLineDouble     = ColorSequence(61)
    IdeogramOverLine            = ColorSequence(62)
    IdeogramOverLineDouble      = ColorSequence(63)
    IdeogramStress              = ColorSequence(64)
    NoIdeogram                  = ColorSequence(65)
    SuperScript                 = ColorSequence(73)
    SubScript                   = ColorSequence(74)
    NoScript                    = ColorSequence(75)
    # ? 76 - 89
    # 100 - 107 see BasicNest
    # 90 - 97 see BasicNest

# ----------------------------------------------------------------------------------------------------------------------
# - BasicNest Sequences -
# ----------------------------------------------------------------------------------------------------------------------
class Basic:
    class Fore:
        Black = ColorSequence(30)
        Red = ColorSequence(31)
        Green = ColorSequence(32)
        Yellow = ColorSequence(33)
        Blue = ColorSequence(34)
        Magenta = ColorSequence(35)
        Cyan = ColorSequence(36)
        White = ColorSequence(37)
        BrightBlack = ColorSequence(90)
        BrightRed = ColorSequence(91)
        BrightGreen = ColorSequence(92)
        BrightYellow = ColorSequence(93)
        BrightBlue = ColorSequence(94)
        BrightMagenta = ColorSequence(95)
        BrightCyan = ColorSequence(96)
        BrightWhite = ColorSequence(97)

    class Back:
        Black = ColorSequence(40)
        Red = ColorSequence(41)
        Green = ColorSequence(42)
        Yellow = ColorSequence(43)
        Blue = ColorSequence(44)
        Magenta = ColorSequence(45)
        Cyan = ColorSequence(46)
        White = ColorSequence(47)
        BrightBlack = ColorSequence(100)
        BrightRed = ColorSequence(101)
        BrightGreen = ColorSequence(102)
        BrightYellow = ColorSequence(103)
        BrightBlue = ColorSequence(104)
        BrightMagenta = ColorSequence(105)
        BrightCyan = ColorSequence(106)
        BrightWhite = ColorSequence(107)


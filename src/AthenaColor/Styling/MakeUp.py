# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from ..Functions import (
    AnsiEscape
)
from AthenaColor.BASE import end_codes

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
Reset                       = AnsiEscape(0 , end_code=end_codes.color)
Bold                        = AnsiEscape(1 , end_code=end_codes.color)
NoBold                      = AnsiEscape(22, end_code=end_codes.color)
Dim                         = AnsiEscape(2 , end_code=end_codes.color)
NoDim                       = AnsiEscape(22, end_code=end_codes.color)
Italic                      = AnsiEscape(3 , end_code=end_codes.color)
NoItalic                    = AnsiEscape(23, end_code=end_codes.color)
Underline                   = AnsiEscape(4 , end_code=end_codes.color)
NoUnderline                 = AnsiEscape(24, end_code=end_codes.color)
BlinkSlow                   = AnsiEscape(5 , end_code=end_codes.color)      # NOT WORKING PYCHARM
NoBlinkSlow                 = AnsiEscape(25, end_code=end_codes.color)      # NOT WORKING PYCHARM
BlinkRapid                  = AnsiEscape(6 , end_code=end_codes.color)      # NOT WORKING PYCHARM
NoBlinkRapid                = AnsiEscape(25, end_code=end_codes.color)      # NOT WORKING PYCHARM
Reversed                    = AnsiEscape(7 , end_code=end_codes.color)
NoReversed                  = AnsiEscape(27, end_code=end_codes.color)
Conceal                     = AnsiEscape(8 , end_code=end_codes.color)      # NOT WORKING PYCHARM
NoConceal                   = AnsiEscape(28, end_code=end_codes.color)      # NOT WORKING PYCHARM
Crossed                     = AnsiEscape(9 , end_code=end_codes.color)
NoCrossed                   = AnsiEscape(29, end_code=end_codes.color)
FontPrimary                 = AnsiEscape(10, end_code=end_codes.color)      # NOT WORKING PYCHARM
FontSecond1                 = AnsiEscape(11, end_code=end_codes.color)      # NOT WORKING PYCHARM
FontSecond2                 = AnsiEscape(12, end_code=end_codes.color)      # NOT WORKING PYCHARM
FontSecond3                 = AnsiEscape(13, end_code=end_codes.color)      # NOT WORKING PYCHARM
FontSecond4                 = AnsiEscape(14, end_code=end_codes.color)      # NOT WORKING PYCHARM
FontSecond5                 = AnsiEscape(15, end_code=end_codes.color)      # NOT WORKING PYCHARM
FontSecond6                 = AnsiEscape(16, end_code=end_codes.color)      # NOT WORKING PYCHARM
FontSecond8                 = AnsiEscape(17, end_code=end_codes.color)      # NOT WORKING PYCHARM
FontSecond9                 = AnsiEscape(18, end_code=end_codes.color)      # NOT WORKING PYCHARM
FontSecond10                = AnsiEscape(19, end_code=end_codes.color)      # NOT WORKING PYCHARM
NoFont                      = AnsiEscape(10, end_code=end_codes.color)      # NOT WORKING PYCHARM
Fraktur                     = AnsiEscape(20, end_code=end_codes.color)      # NOT WORKING PYCHARM
UnderlineDouble             = AnsiEscape(21, end_code=end_codes.color)
NoUnderlineDouble           = AnsiEscape(24, end_code=end_codes.color)
PropSpacing                 = AnsiEscape(26, end_code=end_codes.color)      # NOT WORKING PYCHARM
NoPropSpacing               = AnsiEscape(26, end_code=end_codes.color)     # NOT WORKING PYCHARM
# 30 - 37 -> see Basic
# 38 -> see RgbControlled.Back
NoForeground                = AnsiEscape(39, end_code=end_codes.color)
# 40 - 47 -> see Basic
# 48 -> see RgbControlled.Back
NoBackground                = AnsiEscape(49, end_code=end_codes.color)
Frame                       = AnsiEscape(51, end_code=end_codes.color)
NoFrame                     = AnsiEscape(54, end_code=end_codes.color)
Circle                      = AnsiEscape(52, end_code=end_codes.color)
NoCircle                    = AnsiEscape(54, end_code=end_codes.color)
OverLine                    = AnsiEscape(53, end_code=end_codes.color)
NoOverLine                  = AnsiEscape(55, end_code=end_codes.color)
# ? 56
# ? 57
# 58 -> see RgbControlled.Underline
UnderColourDefault          = AnsiEscape(59, end_code=end_codes.color)
IdeogramUnderLine           = AnsiEscape(60, end_code=end_codes.color)
IdeogramUnderLineDouble     = AnsiEscape(61, end_code=end_codes.color)
IdeogramOverLine            = AnsiEscape(62, end_code=end_codes.color)
IdeogramOverLineDouble      = AnsiEscape(63, end_code=end_codes.color)
IdeogramStress              = AnsiEscape(64, end_code=end_codes.color)
NoIdeogram                  = AnsiEscape(65, end_code=end_codes.color)
SuperScript                 = AnsiEscape(73, end_code=end_codes.color)
SubScript                   = AnsiEscape(74, end_code=end_codes.color)
NoScript                    = AnsiEscape(75, end_code=end_codes.color)
# ? 76 - 89
# 90 - 97 see Basic
# 100 - 107 see Basic


class Basic:
    class Fore:
        Black           = AnsiEscape(30, end_code=end_codes.color)
        Red             = AnsiEscape(31, end_code=end_codes.color)
        Green           = AnsiEscape(32, end_code=end_codes.color)
        Yellow          = AnsiEscape(33, end_code=end_codes.color)
        Blue            = AnsiEscape(34, end_code=end_codes.color)
        Magenta         = AnsiEscape(35, end_code=end_codes.color)
        Cyan            = AnsiEscape(36, end_code=end_codes.color)
        White           = AnsiEscape(37, end_code=end_codes.color)
        BrightBlack     = AnsiEscape(90, end_code=end_codes.color)
        BrightRed       = AnsiEscape(91, end_code=end_codes.color)
        BrightGreen     = AnsiEscape(92, end_code=end_codes.color)
        BrightYellow    = AnsiEscape(93, end_code=end_codes.color)
        BrightBlue      = AnsiEscape(94, end_code=end_codes.color)
        BrightMagenta   = AnsiEscape(95, end_code=end_codes.color)
        BrightCyan      = AnsiEscape(96, end_code=end_codes.color)
        BrightWhite     = AnsiEscape(97, end_code=end_codes.color)

    class Back:
        Black           = AnsiEscape(40 , end_code=end_codes.color)
        Red             = AnsiEscape(41 , end_code=end_codes.color)
        Green           = AnsiEscape(42 , end_code=end_codes.color)
        Yellow          = AnsiEscape(43 , end_code=end_codes.color)
        Blue            = AnsiEscape(44 , end_code=end_codes.color)
        Magenta         = AnsiEscape(45 , end_code=end_codes.color)
        Cyan            = AnsiEscape(46 , end_code=end_codes.color)
        White           = AnsiEscape(47 , end_code=end_codes.color)
        BrightBlack     = AnsiEscape(100, end_code=end_codes.color)
        BrightRed       = AnsiEscape(101, end_code=end_codes.color)
        BrightGreen     = AnsiEscape(102, end_code=end_codes.color)
        BrightYellow    = AnsiEscape(103, end_code=end_codes.color)
        BrightBlue      = AnsiEscape(104, end_code=end_codes.color)
        BrightMagenta   = AnsiEscape(105, end_code=end_codes.color)
        BrightCyan      = AnsiEscape(106, end_code=end_codes.color)
        BrightWhite     = AnsiEscape(107, end_code=end_codes.color)
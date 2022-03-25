# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor import init
from AthenaColor.BASE import end_codes


# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def ansi_escape(code: str | int = '') -> str:
    return f'{init.esc}[{code}{end_codes.color}'


Reset                       = ansi_escape(0)
Bold                        = ansi_escape(1)
NoBold                      = ansi_escape(22)
Dim                         = ansi_escape(2)
NoDim                       = ansi_escape(22)
Italic                      = ansi_escape(3)
NoItalic                    = ansi_escape(23)
Underline                   = ansi_escape(4)
NoUnderline                 = ansi_escape(24)
BlinkSlow                   = ansi_escape(5 )      # NOT WORKING PYCHARM
NoBlinkSlow                 = ansi_escape(25)      # NOT WORKING PYCHARM
BlinkRapid                  = ansi_escape(6 )      # NOT WORKING PYCHARM
NoBlinkRapid                = ansi_escape(25)      # NOT WORKING PYCHARM
Reversed                    = ansi_escape(7)
NoReversed                  = ansi_escape(27)
Conceal                     = ansi_escape(8 )      # NOT WORKING PYCHARM
NoConceal                   = ansi_escape(28)      # NOT WORKING PYCHARM
Crossed                     = ansi_escape(9)
NoCrossed                   = ansi_escape(29)
FontPrimary                 = ansi_escape(10)      # NOT WORKING PYCHARM
FontSecond1                 = ansi_escape(11)      # NOT WORKING PYCHARM
FontSecond2                 = ansi_escape(12)      # NOT WORKING PYCHARM
FontSecond3                 = ansi_escape(13)      # NOT WORKING PYCHARM
FontSecond4                 = ansi_escape(14)      # NOT WORKING PYCHARM
FontSecond5                 = ansi_escape(15)      # NOT WORKING PYCHARM
FontSecond6                 = ansi_escape(16)      # NOT WORKING PYCHARM
FontSecond8                 = ansi_escape(17)      # NOT WORKING PYCHARM
FontSecond9                 = ansi_escape(18)      # NOT WORKING PYCHARM
FontSecond10                = ansi_escape(19)      # NOT WORKING PYCHARM
NoFont                      = ansi_escape(10)      # NOT WORKING PYCHARM
Fraktur                     = ansi_escape(20)      # NOT WORKING PYCHARM
UnderlineDouble             = ansi_escape(21)
NoUnderlineDouble           = ansi_escape(24)
PropSpacing                 = ansi_escape(26)      # NOT WORKING PYCHARM
NoPropSpacing               = ansi_escape(26)     # NOT WORKING PYCHARM
# 30 - 37 -> see Basic
# 38 -> see RgbControlled.Back
NoForeground                = ansi_escape(39)
# 40 - 47 -> see Basic
# 48 -> see RgbControlled.Back
NoBackground                = ansi_escape(49)
Frame                       = ansi_escape(51)
NoFrame                     = ansi_escape(54)
Circle                      = ansi_escape(52)
NoCircle                    = ansi_escape(54)
OverLine                    = ansi_escape(53)
NoOverLine                  = ansi_escape(55)
# ? 56
# ? 57
# 58 -> see RgbControlled.Underline
UnderColourDefault          = ansi_escape(59)
IdeogramUnderLine           = ansi_escape(60)
IdeogramUnderLineDouble     = ansi_escape(61)
IdeogramOverLine            = ansi_escape(62)
IdeogramOverLineDouble      = ansi_escape(63)
IdeogramStress              = ansi_escape(64)
NoIdeogram                  = ansi_escape(65)
SuperScript                 = ansi_escape(73)
SubScript                   = ansi_escape(74)
NoScript                    = ansi_escape(75)
# ? 76 - 89
# 90 - 97 see Basic
# 100 - 107 see Basic


class Basic:
    class Fore:
        Black           = ansi_escape(30)
        Red             = ansi_escape(31)
        Green           = ansi_escape(32)
        Yellow          = ansi_escape(33)
        Blue            = ansi_escape(34)
        Magenta         = ansi_escape(35)
        Cyan            = ansi_escape(36)
        White           = ansi_escape(37)
        BrightBlack     = ansi_escape(90)
        BrightRed       = ansi_escape(91)
        BrightGreen     = ansi_escape(92)
        BrightYellow    = ansi_escape(93)
        BrightBlue      = ansi_escape(94)
        BrightMagenta   = ansi_escape(95)
        BrightCyan      = ansi_escape(96)
        BrightWhite     = ansi_escape(97)

    class Back:
        Black           = ansi_escape(40)
        Red             = ansi_escape(41)
        Green           = ansi_escape(42)
        Yellow          = ansi_escape(43)
        Blue            = ansi_escape(44)
        Magenta         = ansi_escape(45)
        Cyan            = ansi_escape(46)
        White           = ansi_escape(47)
        BrightBlack     = ansi_escape(100)
        BrightRed       = ansi_escape(101)
        BrightGreen     = ansi_escape(102)
        BrightYellow    = ansi_escape(103)
        BrightBlue      = ansi_escape(104)
        BrightMagenta   = ansi_escape(105)
        BrightCyan      = ansi_escape(106)
        BrightWhite     = ansi_escape(107)
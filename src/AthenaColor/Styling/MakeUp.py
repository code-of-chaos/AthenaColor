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
esc = init.esc
end = end_codes.color

Reset                       = f"{esc}[0{end}"

Bold                        = f"{esc}[1{end}"
NoBold                      = f"{esc}[22{end}"

Dim                         = f"{esc}[2{end}"
NoDim                       = f"{esc}[22{end}"

Italic                      = f"{esc}[3{end}"
NoItalic                    = f"{esc}[23{end}"

Underline                   = f"{esc}[4{end}"
NoUnderline                 = f"{esc}[24{end}"

BlinkSlow                   = f"{esc}[5{end}"       # NOT WORKING PYCHARM
NoBlinkSlow                 = f"{esc}[25{end}"      # NOT WORKING PYCHARM

BlinkRapid                  = f"{esc}[6{end}"       # NOT WORKING PYCHARM
NoBlinkRapid                = f"{esc}[25{end}"      # NOT WORKING PYCHARM

Reversed                    = f"{esc}[7{end}"
NoReversed                  = f"{esc}[27{end}"

Conceal                     = f"{esc}[8{end}"       # NOT WORKING PYCHARM
NoConceal                   = f"{esc}[28{end}"      # NOT WORKING PYCHARM

Crossed                     = f"{esc}[9{end}"
NoCrossed                   = f"{esc}[29{end}"

FontPrimary                 = f"{esc}[10{end}"      # NOT WORKING PYCHARM
FontSecond1                 = f"{esc}[11{end}"      # NOT WORKING PYCHARM
FontSecond2                 = f"{esc}[12{end}"      # NOT WORKING PYCHARM
FontSecond3                 = f"{esc}[13{end}"      # NOT WORKING PYCHARM
FontSecond4                 = f"{esc}[14{end}"      # NOT WORKING PYCHARM
FontSecond5                 = f"{esc}[15{end}"      # NOT WORKING PYCHARM
FontSecond6                 = f"{esc}[16{end}"      # NOT WORKING PYCHARM
FontSecond8                 = f"{esc}[17{end}"      # NOT WORKING PYCHARM
FontSecond9                 = f"{esc}[18{end}"      # NOT WORKING PYCHARM
FontSecond10                = f"{esc}[19{end}"      # NOT WORKING PYCHARM
NoFont                      = f"{esc}[10{end}"      # NOT WORKING PYCHARM
Fraktur                     = f"{esc}[20{end}"      # NOT WORKING PYCHARM

UnderlineDouble             = f"{esc}[21{end}"
NoUnderlineDouble           = f"{esc}[24{end}"

PropSpacing                 = f"{esc}[26{end}"      # NOT WORKING PYCHARM
NoPropSpacing               = f"{esc}[26{end}"      # NOT WORKING PYCHARM

# 30 - 37 -> see Basic


# 38 -> see RgbControlled.Back
NoForeground                = f"{esc}[39m"

# 40 - 47 -> see Basic

# 48 -> see RgbControlled.Back


NoBackground                = f"{esc}[49{end}"

Frame                       = f"{esc}[51{end}"
NoFrame                     = f"{esc}[54{end}"

Circle                      = f"{esc}[52{end}"
NoCircle                    = f"{esc}[54{end}"

OverLine                    = f"{esc}[53{end}"
NoOverLine                  = f"{esc}[55{end}"

# ? 56
# ? 57
# 58 -> see RgbControlled.Underline

UnderColourDefault          = f"{esc}[59{end}"

IdeogramUnderLine           = f"{esc}[60{end}"
IdeogramUnderLineDouble     = f"{esc}[61{end}"
IdeogramOverLine            = f"{esc}[62{end}"
IdeogramOverLineDouble      = f"{esc}[63{end}"
IdeogramStress              = f"{esc}[64{end}"
NoIdeogram                  = f"{esc}[65{end}"

SuperScript                 = f"{esc}[73{end}"
SubScript                   = f"{esc}[74{end}"
NoScript                    = f"{esc}[75{end}"

# ? 76 - 89

# 90 - 97 see Basic
# 100 - 107 see Basic

class Basic:
    class Fore:
        Black           = f"{esc}[30m"
        Red             = f"{esc}[31m"
        Green           = f"{esc}[32m"
        Yellow          = f"{esc}[33m"
        Blue            = f"{esc}[34m"
        Magenta         = f"{esc}[35m"
        Cyan            = f"{esc}[36m"
        White           = f"{esc}[37m"

        BrightBlack     = f"{esc}[90m"
        BrightRed       = f"{esc}[91m"
        BrightGreen     = f"{esc}[92m"
        BrightYellow    = f"{esc}[93m"
        BrightBlue      = f"{esc}[94m"
        BrightMagenta   = f"{esc}[95m"
        BrightCyan      = f"{esc}[96m"
        BrightWhite     = f"{esc}[97m"

    class Back:
        Black           = f"{esc}[40m"
        Red             = f"{esc}[41m"
        Green           = f"{esc}[42m"
        Yellow          = f"{esc}[43m"
        Blue            = f"{esc}[44m"
        Magenta         = f"{esc}[45m"
        Cyan            = f"{esc}[46m"
        White           = f"{esc}[47m"

        BrightBlack     = f"{esc}[100m"
        BrightRed       = f"{esc}[101m"
        BrightGreen     = f"{esc}[102m"
        BrightYellow    = f"{esc}[103m"
        BrightBlue      = f"{esc}[104m"
        BrightMagenta   = f"{esc}[105m"
        BrightCyan      = f"{esc}[106m"
        BrightWhite     = f"{esc}[107m"
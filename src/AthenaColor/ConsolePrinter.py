# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Packages
from .Objects import rgb

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
_esc = "\033"

Reset                       = f"{_esc}[0m"

Bold                        = f"{_esc}[1m"
NoBold                      = f"{_esc}[22m"

Dim                         = f"{_esc}[2m"
NoDim                       = f"{_esc}[22m"

Italic                      = f"{_esc}[3m"
NoItalic                    = f"{_esc}[23m"

Underline                   = f"{_esc}[4m"
NoUnderline                 = f"{_esc}[24m"

BlinkSlow                   = f"{_esc}[5m"      # NOT WORKING PYCHARM
NoBlinkSlow                 = f"{_esc}[25m"     # NOT WORKING PYCHARM

BlinkRapid                  = f"{_esc}[6m"      # NOT WORKING PYCHARM
NoBlinkRapid                = f"{_esc}[25m"     # NOT WORKING PYCHARM

Reversed                    = f"{_esc}[7m"
NoReversed                  = f"{_esc}[27m"

Conceal                     = f"{_esc}[8m"       # NOT WORKING PYCHARM
NoConceal                   = f"{_esc}[28m"      # NOT WORKING PYCHARM

Crossed                     = f"{_esc}[9m"
NoCrossed                   = f"{_esc}[29m"

FontPrimary                 = f"{_esc}[10m"     # NOT WORKING PYCHARM
FontSecond1                 = f"{_esc}[11m"     # NOT WORKING PYCHARM
FontSecond2                 = f"{_esc}[12m"     # NOT WORKING PYCHARM
FontSecond3                 = f"{_esc}[13m"     # NOT WORKING PYCHARM
FontSecond4                 = f"{_esc}[14m"     # NOT WORKING PYCHARM
FontSecond5                 = f"{_esc}[15m"     # NOT WORKING PYCHARM
FontSecond6                 = f"{_esc}[16m"     # NOT WORKING PYCHARM
FontSecond8                 = f"{_esc}[17m"     # NOT WORKING PYCHARM
FontSecond9                 = f"{_esc}[18m"     # NOT WORKING PYCHARM
FontSecond10                = f"{_esc}[19m"     # NOT WORKING PYCHARM
NoFont                      = f"{_esc}[10m"     # NOT WORKING PYCHARM
Fraktur                     = f"{_esc}[20m"     # NOT WORKING PYCHARM

UnderlineDouble             = f"{_esc}[21m"
NoUnderlineDouble           = f"{_esc}[24m"

PropSpacing                 = f"{_esc}[26m"     # NOT WORKING PYCHARM
NoPropSpacing               = f"{_esc}[26m"     # NOT WORKING PYCHARM

ForeEasyBlack               = f"{_esc}[30m"
ForeEasyRed                 = f"{_esc}[31m"
ForeEasyGreen               = f"{_esc}[32m"
ForeEasyYellow              = f"{_esc}[33m"
ForeEasyBlue                = f"{_esc}[34m"
ForeEasyMagenta             = f"{_esc}[35m"
ForeEasyCyan                = f"{_esc}[36m"
ForeEasyWhite               = f"{_esc}[37m"

def Foreground(color:rgb) -> str:
    return f"{_esc}[38;2;{color}m"

ForegroundDefault           = f"{_esc}[39m"

BackEasyBlack               = f"{_esc}[40m"
BackEasyRed                 = f"{_esc}[41m"
BackEasyGreen               = f"{_esc}[42m"
BackEasyYellow              = f"{_esc}[43m"
BackEasyBlue                = f"{_esc}[44m"
BackEasyMagenta             = f"{_esc}[45m"
BackEasyCyan                = f"{_esc}[46m"
BackEasyWhite               = f"{_esc}[47m"

def Background(color:rgb) -> str:
    return f"{_esc}[48;2;{color}m"

BackgroundDefault           = f"{_esc}[49m"

Frame                       = f"{_esc}[51m"
NoFrame                     = f"{_esc}[54m"

Circle                      = f"{_esc}[52m"
NoCircle                    = f"{_esc}[54m"

OverLine                    = f"{_esc}[53m"
NoOverLine                  = f"{_esc}[55m"

# ? 56
# ? 57

def UnderColour(color:rgb) -> str:
    return f"{_esc}[58;2;{color}m"

UnderColourDefault  = f"{_esc}[59m"

IdeogramUnderLine           = f"{_esc}[60m"
IdeogramUnderLineDouble     = f"{_esc}[61m"
IdeogramOverLine            = f"{_esc}[62m"
IdeogramOverLineDouble      = f"{_esc}[63m"
IdeogramStress              = f"{_esc}[64m"
NoIdeogram                  = f"{_esc}[65m"

SuperScript                 = f"{_esc}[73m"
SubScript                   = f"{_esc}[74m"
NoScript                    = f"{_esc}[75m"

# ? 76 - 89

FrontBrightBlack            = f"{_esc}[90m"
FrontBrightRed              = f"{_esc}[91m"
FrontBrightGreen            = f"{_esc}[92m"
FrontBrightYellow           = f"{_esc}[93m"
FrontBrightBlue             = f"{_esc}[94m"
FrontBrightMagenta          = f"{_esc}[95m"
FrontBrightCyan             = f"{_esc}[96m"
FrontBrightWhite            = f"{_esc}[97m"


BackBrightBlack             = f"{_esc}[100m"
BackBrightRed               = f"{_esc}[101m"
BackBrightGreen             = f"{_esc}[102m"
BackBrightYellow            = f"{_esc}[103m"
BackBrightBlue              = f"{_esc}[104m"
BackBrightMagenta           = f"{_esc}[105m"
BackBrightCyan              = f"{_esc}[106m"
BackBrightWhite             = f"{_esc}[107m"
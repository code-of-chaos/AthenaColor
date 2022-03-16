# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Packages
from AthenaColor.Objects import rgb

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
esc = "\033"

Reset                       = f"{esc}[0m"

Bold                        = f"{esc}[1m"
NoBold                      = f"{esc}[22m"

Dim                         = f"{esc}[2m"
NoDim                       = f"{esc}[22m"

Italic                      = f"{esc}[3m"
NoItalic                    = f"{esc}[23m"

Underline                   = f"{esc}[4m"
NoUnderline                 = f"{esc}[24m"

BlinkSlow                   = f"{esc}[5m"      # NOT WORKING PYCHARM
NoBlinkSlow                 = f"{esc}[25m"     # NOT WORKING PYCHARM

BlinkRapid                  = f"{esc}[6m"      # NOT WORKING PYCHARM
NoBlinkRapid                = f"{esc}[25m"     # NOT WORKING PYCHARM

Reversed                    = f"{esc}[7m"
NoReversed                  = f"{esc}[27m"

Conceal                     = f"{esc}[8m"       # NOT WORKING PYCHARM
NoConceal                   = f"{esc}[28m"      # NOT WORKING PYCHARM

Crossed                     = f"{esc}[9m"
NoCrossed                   = f"{esc}[29m"

FontPrimary                 = f"{esc}[10m"     # NOT WORKING PYCHARM
FontSecond1                 = f"{esc}[11m"     # NOT WORKING PYCHARM
FontSecond2                 = f"{esc}[12m"     # NOT WORKING PYCHARM
FontSecond3                 = f"{esc}[13m"     # NOT WORKING PYCHARM
FontSecond4                 = f"{esc}[14m"     # NOT WORKING PYCHARM
FontSecond5                 = f"{esc}[15m"     # NOT WORKING PYCHARM
FontSecond6                 = f"{esc}[16m"     # NOT WORKING PYCHARM
FontSecond8                 = f"{esc}[17m"     # NOT WORKING PYCHARM
FontSecond9                 = f"{esc}[18m"     # NOT WORKING PYCHARM
FontSecond10                = f"{esc}[19m"     # NOT WORKING PYCHARM
NoFont                      = f"{esc}[10m"     # NOT WORKING PYCHARM
Fraktur                     = f"{esc}[20m"     # NOT WORKING PYCHARM

UnderlineDouble             = f"{esc}[21m"
NoUnderlineDouble           = f"{esc}[24m"

PropSpacing                 = f"{esc}[26m"     # NOT WORKING PYCHARM
NoPropSpacing               = f"{esc}[26m"     # NOT WORKING PYCHARM

# 30 - 37 -> see ColorsBasic

def Foreground(color:rgb) -> str:
    return f"{esc}[38;2;{color}m"
NoForeground                = f"{esc}[39m"

# 40 - 47 -> see Colors Basic

def Background(color:rgb) -> str:
    return f"{esc}[48;2;{color}m"

BackgroundDefault           = f"{esc}[49m"

Frame                       = f"{esc}[51m"
NoFrame                     = f"{esc}[54m"

Circle                      = f"{esc}[52m"
NoCircle                    = f"{esc}[54m"

OverLine                    = f"{esc}[53m"
NoOverLine                  = f"{esc}[55m"

# ? 56
# ? 57

def UnderColour(color:rgb) -> str:              # NOT WORKING PYCHARM
    return f"{esc}[58;2;{color}m"

UnderColourDefault  = f"{esc}[59m"

IdeogramUnderLine           = f"{esc}[60m"
IdeogramUnderLineDouble     = f"{esc}[61m"
IdeogramOverLine            = f"{esc}[62m"
IdeogramOverLineDouble      = f"{esc}[63m"
IdeogramStress              = f"{esc}[64m"
NoIdeogram                  = f"{esc}[65m"

SuperScript                 = f"{esc}[73m"
SubScript                   = f"{esc}[74m"
NoScript                    = f"{esc}[75m"

# ? 76 - 89

# 90 - 97 see Colors Basic
# 100 - 107 see Colors Basic
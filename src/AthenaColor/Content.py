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

def Foreground(color:rgb) -> str:
    return f"{_esc}[38;2;{color}m"

def Background(color:rgb) -> str:
    return f"{_esc}[48;2;{color}m"

Reset               = f"{_esc}[0m"

Bold                = f"{_esc}[1m"
NoBold              = f"{_esc}[22m"

Dim                 = f"{_esc}[2m"
NoDim               = f"{_esc}[22m"

Italic              = f"{_esc}[3m"
NoItalic            = f"{_esc}[23m"

Underline           = f"{_esc}[4m"
NoUnderline         = f"{_esc}[24m"

BlinkSlow           = f"{_esc}[5m"      # NOT WORKING PYCHARM
NoBlinkSlow         = f"{_esc}[25m"     # NOT WORKING PYCHARM

BlinkRapid          = f"{_esc}[6m"      # NOT WORKING PYCHARM
NoBlinkRapid        = f"{_esc}[25m"     # NOT WORKING PYCHARM

Reversed            = f"{_esc}[7m"
NoReversed          = f"{_esc}[27m"

Conceal             = f"{_esc}[8m"       # NOT WORKING PYCHARM
NoConceal           = f"{_esc}[28m"      # NOT WORKING PYCHARM

Crossed             = f"{_esc}[9m"
NoCrossed           = f"{_esc}[29m"

FontPrimary         = f"{_esc}[10m"     # NOT WORKING PYCHARM
FontSecond1         = f"{_esc}[11m"     # NOT WORKING PYCHARM
FontSecond2         = f"{_esc}[12m"     # NOT WORKING PYCHARM
FontSecond3         = f"{_esc}[13m"     # NOT WORKING PYCHARM
FontSecond4         = f"{_esc}[14m"     # NOT WORKING PYCHARM
FontSecond5         = f"{_esc}[15m"     # NOT WORKING PYCHARM
FontSecond6         = f"{_esc}[16m"     # NOT WORKING PYCHARM
FontSecond8         = f"{_esc}[17m"     # NOT WORKING PYCHARM
FontSecond9         = f"{_esc}[18m"     # NOT WORKING PYCHARM
FontSecond10        = f"{_esc}[19m"     # NOT WORKING PYCHARM
NoFont              = f"{_esc}[10m"     # NOT WORKING PYCHARM
Fraktur             = f"{_esc}[20m"     # NOT WORKING PYCHARM

UnderlineDouble     = f"{_esc}[21m"
NoUnderlineDouble   = f"{_esc}[24m"

PropSpacing         = f"{_esc}[26m"     # NOT WORKING PYCHARM

ColorBlack          = f"{_esc}["

Frame               = f"{_esc}[51m"
NoFrame             = f"{_esc}[54m"

Circle              = f"{_esc}[52m"
NoCircle            = f"{_esc}[54m"
# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor.InitClass import init
from AthenaColor.Data.General import ConsoleCodes
from AthenaColor.Functions.General import StrictType

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = [
    "ColorSequence", "NestedColorSequence"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def ColorSequence(control_code:int|str)->str:
    """
    Used for quick assembly of correct Ansi Escape functions
    Used the escape code defined in AthenaColor init
    """
    return f'{init.esc}[{control_code}m'

def NestedColorSequence(*obj, control_code:int|str,reset_code:int|str, sep:str=" ") -> str:
    """
    Used by Nested Console StyleNest Makeup operations like ForeNest, BackNest, StyleNest.
    Function wraps every obj in the properly defined control- and reset codes.
    This is made to prevent style makeup bleed
    """
    init_esc = init.esc
    color = f'{init_esc}[{control_code}m'
    reset = f'{init_esc}[{reset_code}m'

    # SHHH, don't touch this, this is speed 101
    text = ""
    for o in obj[:-1]:
        text += f"{color}{o}{sep}{reset}" # SEP moved to within the color - reset, as previously, it was color-reset anyways
    return text + f"{color}{obj[-1]}{reset}"
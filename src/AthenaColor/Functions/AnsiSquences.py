# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages

from AthenaColor.Data.General import ConsoleCodes
from AthenaColor.InitClass import init

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
    return f'{init.esc}[{control_code}{ConsoleCodes.color}'

def NestedColorSequence(*obj, control_code:int|str,reset_code:int|str=None, sep:str=" ") -> str:
    """
    Used by Nested Console StyleNest Makeup operations like ForeNest, BackNest, StyleNest.
    Function wraps every obj in the properly defined control- and reset codes.
    This is made to prevent style makeup bleed
    """
    color = ColorSequence(control_code=control_code)
    reset = ColorSequence(control_code=reset_code) if reset_code is not None else ''

    if len(obj) == 1:
        return  ''.join([f"{color}{o}{reset}"for o in obj])
    else:
        return sep.join([f"{color}{o}{reset}"for o in obj])
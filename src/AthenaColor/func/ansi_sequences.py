# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

from typing import Any
# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def color_sequence(control_code:int|str)->str:
    """
    Used for quick assembly of correct Ansi Escape functions
    Used the escape code defined in AthenaColor init

    Parameters:
    - control_code : int|str -> numerical ANSI fragment
    """
    return f'\x1b[{control_code}m'

def color_sequence_nested(obj:tuple[Any, ...], color_code:str, reset_code:str, sep:str=" ") -> str:
    """
    Used by Nested Console StyleNest Makeup operations like ForeNest, BackNest, StyleNest.
    Function wraps every obj in the properly defined control- and reset codes.
    This is made to prevent style makeup bleed

    Parameters:
    - obj : tuple -> Collection of all objects to be wrapped
    - color_code : str -> Full color_sequenced ANSI code
    - reset_code : int|str -> Full color_sequenced ANSI code to reset the given color
    - sep : str -> separation string between the various objects
    """

    # SHH, don't touch this, this is speed 101
    text = ""
    for o in obj[:-1]:
        text += f"{color_code}{o}{sep}{reset_code}" # SEP moved to within the color - reset, as previously, it was color-reset anyway
    return text + f"{color_code}{obj[-1]}{reset_code}"

def color_sequence_nested_no_reset(obj:tuple[Any, ...], color_code:str, sep:str=" ") -> str:
    """
    Used by Nested Console StyleNest Makeup operations like ForeNest, BackNest, StyleNest.
    Function wraps every obj in the properly defined control- and reset codes.
    This is made to prevent style makeup bleed

    Parameters:
    - obj : tuple -> Collection of all objects to be wrapped
    - color_code : str -> Full color_sequenced ANSI code
    - sep : str -> separation string between the various objects
    """

    # SHH, don't touch this, this is speed 101
    text = ""
    for o in obj[:-1]:
        text += f"{color_code}{o}{sep}" # SEP moved to within the color - reset, as previously, it was color-reset anyway
    return text + f"{color_code}{obj[-1]}"
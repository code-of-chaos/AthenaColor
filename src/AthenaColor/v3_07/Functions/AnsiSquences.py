# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor.v3_07.InitClass import AthenaColorInitClass
from AthenaColor.v3_07.Data.General import ConsoleCodes
from AthenaColor.v3_07.BoilerPlate.Union import IntStr

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def ColorSequence(control_code:IntStr)->str:
    """
    Used for quick assembly of correct Ansi Escape functions
    Used the escape code defined in AthenaColor init
    """
    return f'{AthenaColorInitClass.esc}[{control_code}{ConsoleCodes.color}'

def NestedColorSequence(*obj, control_code:IntStr,reset_code:IntStr=None, sep:str=" ") -> str:
    """
    Used by Nested Console Style Makeup operations like ForeNest, BackNest, StyleNest.
    Function wraps every obj in the properly defined control- and reset codes.
    This is made to prevent style makeup bleed
    """
    color = ColorSequence(control_code=control_code)
    reset = ColorSequence(control_code=reset_code) if reset_code is not None else ''

    if len(obj) == 1:
        return  ''.join([f"{color}{o}{reset}"for o in obj])
    else:
        return sep.join([f"{color}{o}{reset}"for o in obj])
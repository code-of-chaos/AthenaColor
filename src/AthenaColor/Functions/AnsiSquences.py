# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor import init
import AthenaColor.Data.ConsoleCodes as ConsoleCodes

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def ColorSequence(code:str|int)->str:
    return f'{init.esc}[{code}{ConsoleCodes.color}'

def NestedColorSequence(*obj, control_code:str|int,reset_code:str|int=None, sep:str=" ") -> str:
    color = ColorSequence(code=control_code)
    reset = ColorSequence(code=reset_code) if reset_code is not None else ''

    content = [
        f"{color}{o}{reset}"
        for o in obj
    ]

    if len(obj) == 1:
        return  ''.join(content)
    else:
        return sep.join(content)
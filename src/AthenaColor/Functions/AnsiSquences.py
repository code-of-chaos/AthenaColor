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
def AnsiEscape(code: str | int,end_code:str) -> str:
    return f'{init.esc}[{code}{end_code}'

def NestedSequence(*obj, control_code: str | int,reset_code:str|int=None, sep:str=" ", **_) -> str:
    styleCode = AnsiEscape(code=control_code,end_code=end_codes.color)
    resetCode = AnsiEscape(code=reset_code,end_code=end_codes.color) if reset_code is not None else ''

    if len(obj) == 1:
        return  ''.join([*((styleCode+o+styleCode) for o in obj),resetCode])
    else:
        return sep.join([*((styleCode+o+styleCode) for o in obj),resetCode])
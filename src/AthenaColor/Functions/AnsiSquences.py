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

def NestedSequence(*obj, control_code: str | int,reset_code:str|int=None, sep:str=" ") -> str:
    styleCode = AnsiEscape(code=control_code,end_code=end_codes.color)
    resetCode = AnsiEscape(code=reset_code,end_code=end_codes.color)
    return ''.join([
        # Define the Style first, else the next "o" will not have the Style set
        styleCode,
        *[
            # Negate the last code, doesn't do a thing if reset code is called
            (styleCode+o+styleCode+sep) if o != obj[-1] else o
            for o in obj
        ],
        # Reset the specifc Style Choice with the corresponding "No..." code
        resetCode if reset_code is not None else ''
    ])
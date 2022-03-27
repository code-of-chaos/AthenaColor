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

def NestedColorSequence(*obj, control_code: str | int = '',reset_code:str|int=None) -> str:
    color_escape = AnsiEscape(code=control_code,end_code=end_codes.color)
    return ''.join([
        # Define the Style first, else the next "o" will not have the Style set
        color_escape,
        *[
            # Negate the last code, doesn't do a thing if reset code is called
            (o+color_escape) if o != obj[-1] else o
            for o in obj
        ],
        # Reset the specifc Style Choice with the corresponding "No..." code
        color_escape if reset_code is not None else ''
    ])
# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def hexadecimal_to_rgb(hex_str:str) -> tuple[int,int,int]:
    # Form hex value in usable state (cast away the '#' value)
    if hex_str[0] == "#":
        hex_v = hex_str[1:]
    elif len(hex_str) == 6:
        hex_v = hex_str
    else:
        raise ValueError("Hexadecimal was given in an incorrect format")

    # Actually convert to rgb integers
    r,g,b = tuple(
        int(hex_v[i:i + 2], 16)
        for i in (0, 2, 4)
    )
    return r,g,b

def rgb_to_hexadecimal(r:int,g:int,b:int) -> str:
    hex_str = '#%02x%02x%02x' % (r, g, b)
    return hex_str

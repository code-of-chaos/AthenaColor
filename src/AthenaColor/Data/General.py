# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class EscCodes:
    hex:str = "\x1b"
    octal:str = "\033"
    uni:str = "\u001b"

class ConsoleCodes:
    cursor_line_up:str = "A"
    cursor_line_down:str = "B"
    cursor_right:str = "C"
    cursor_left:str = "D"
    cursor_line_next:str = "E"
    cursor_line_previous:str = "F"
    cursor_to_column:str = "G"
    color:str = "m"
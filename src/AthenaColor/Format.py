# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from .BASE import esc, end

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Format:
    Reset = f"{esc}[0{end}"

    Italic = f"{esc}[3{end}"
    NoItalic = f"{esc}[23{end}"

    Bold = f"{esc}[1{end}"
    NoBold = f"{esc}[22{end}"

    Underline = f"{esc}[4{end}"
    NoUnderline = f"{esc}[24{end}"

    Dim = f"{esc}[2{end}"
    NoDim = f"{esc}[22{end}"

    Crossed = f"{esc}[9{end}"
    NoCrossed = f"{esc}[29{end}"

    Reversed = f"{esc}[7{end}"
    NoReversed = f"{esc}[27{end}"

    Frame = f"{esc}[51{end}"
    NoFrame = f"{esc}[54{end}"

    Circle = f"{esc}[52{end}"
    NoCircle = f"{esc}[54{end}"
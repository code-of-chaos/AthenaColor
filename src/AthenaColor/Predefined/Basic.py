# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor.BASE import esc

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Basic:
    class Fore:
        Black           = f"{esc}[30m"
        Red             = f"{esc}[31m"
        Green           = f"{esc}[32m"
        Yellow          = f"{esc}[33m"
        Blue            = f"{esc}[34m"
        Magenta         = f"{esc}[35m"
        Cyan            = f"{esc}[36m"
        White           = f"{esc}[37m"

        BrightBlack     = f"{esc}[90m"
        BrightRed       = f"{esc}[91m"
        BrightGreen     = f"{esc}[92m"
        BrightYellow    = f"{esc}[93m"
        BrightBlue      = f"{esc}[94m"
        BrightMagenta   = f"{esc}[95m"
        BrightCyan      = f"{esc}[96m"
        BrightWhite     = f"{esc}[97m"

    class Back:
        Black           = f"{esc}[40m"
        Red             = f"{esc}[41m"
        Green           = f"{esc}[42m"
        Yellow          = f"{esc}[43m"
        Blue            = f"{esc}[44m"
        Magenta         = f"{esc}[45m"
        Cyan            = f"{esc}[46m"
        White           = f"{esc}[47m"

        BrightBlack     = f"{esc}[100m"
        BrightRed       = f"{esc}[101m"
        BrightGreen     = f"{esc}[102m"
        BrightYellow    = f"{esc}[103m"
        BrightBlue      = f"{esc}[104m"
        BrightMagenta   = f"{esc}[105m"
        BrightCyan      = f"{esc}[106m"
        BrightWhite     = f"{esc}[107m"
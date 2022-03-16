# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor.ConsolePrinter.ConsolePrinter import esc

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ColorsBasic:
    ForeEasyBlack       = f"{esc}[30m"
    ForeEasyRed         = f"{esc}[31m"
    ForeEasyGreen       = f"{esc}[32m"
    ForeEasyYellow      = f"{esc}[33m"
    ForeEasyBlue        = f"{esc}[34m"
    ForeEasyMagenta     = f"{esc}[35m"
    ForeEasyCyan        = f"{esc}[36m"
    ForeEasyWhite       = f"{esc}[37m"

    BackEasyBlack       = f"{esc}[40m"
    BackEasyRed         = f"{esc}[41m"
    BackEasyGreen       = f"{esc}[42m"
    BackEasyYellow      = f"{esc}[43m"
    BackEasyBlue        = f"{esc}[44m"
    BackEasyMagenta     = f"{esc}[45m"
    BackEasyCyan        = f"{esc}[46m"
    BackEasyWhite       = f"{esc}[47m"

    FrontBrightBlack    = f"{esc}[90m"
    FrontBrightRed      = f"{esc}[91m"
    FrontBrightGreen    = f"{esc}[92m"
    FrontBrightYellow   = f"{esc}[93m"
    FrontBrightBlue     = f"{esc}[94m"
    FrontBrightMagenta  = f"{esc}[95m"
    FrontBrightCyan     = f"{esc}[96m"
    FrontBrightWhite    = f"{esc}[97m"

    BackBrightBlack     = f"{esc}[100m"
    BackBrightRed       = f"{esc}[101m"
    BackBrightGreen     = f"{esc}[102m"
    BackBrightYellow    = f"{esc}[103m"
    BackBrightBlue      = f"{esc}[104m"
    BackBrightMagenta   = f"{esc}[105m"
    BackBrightCyan      = f"{esc}[106m"
    BackBrightWhite     = f"{esc}[107m"
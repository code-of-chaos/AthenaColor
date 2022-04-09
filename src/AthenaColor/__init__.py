# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "init",
    "ConvertColorTuple","ConvertColorObject",
    "RGB","RGBA","HEX","HEXA","HSV","HSL",
    "Fore","Back","Underline","Style",
    "ForeNest","BackNest","UnderlineNest","StyleNest",
]
# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import sys

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
_PyMayor = sys.version_info.major
_PyMinor = sys.version_info.minor
ErrorText_Development = f"AthenaColor for v{_PyMayor}.{_PyMinor} is currently still in development"
ErrorText_Never = f"AthenaColor for v{_PyMayor}.{_PyMinor} is not supported"

if _PyMayor == 3:
    if _PyMinor == 10:
        from .v3_10 import *
    elif _PyMinor == 9:
        from .v3_09 import *
    elif _PyMinor == 8:
        from .v3_08 import *
    elif _PyMinor == 7:
        from .v3_07 import *
    else:
        raise RuntimeError(ErrorText_Never)
else:
    raise RuntimeError(ErrorText_Never)
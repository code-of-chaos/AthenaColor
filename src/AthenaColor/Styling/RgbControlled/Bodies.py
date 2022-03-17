# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor.BASE import (
    esc,
    end,
)
from .RgbControlled import RgbControlled

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
Fore = RgbControlled(
    prefix= f"{esc}[38;2;",
    sufix= end
)

Back = RgbControlled(
    prefix= f"{esc}[48;2;",
    sufix= end
)

Underline = RgbControlled(
    prefix= f"{esc}[58;2;",
    sufix= end
)
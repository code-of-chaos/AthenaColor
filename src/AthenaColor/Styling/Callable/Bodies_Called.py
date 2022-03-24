# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from .RgbControlled_Callable import RgbControlled_Callable
from .MakeUp import (
    NoForeground,
    NoBackground,
    NoUnderline
)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
Fore = RgbControlled_Callable(
    param_code= f"[38;2;",
    reset=NoForeground
)

Back = RgbControlled_Callable(
    param_code= f"[48;2;",
    reset=NoBackground
)

Underline = RgbControlled_Callable(
    param_code= f"[58;2;",
    reset=NoUnderline
)
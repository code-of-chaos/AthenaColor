# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from .Nested_RgbControlled import Nested_RgbControlled

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
Fore = Nested_RgbControlled(
    param_code= f"38;2;",
    reset_code=39
)

Back = Nested_RgbControlled(
    param_code= f"48;2;",
    reset_code=49
)

Underline = Nested_RgbControlled(
    param_code= f"58;2;",
    reset_code=24
)
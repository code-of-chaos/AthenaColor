# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = [
    "Fore","Back","Underline","Style","Basic",
    "ForeNest","BackNest","UnderlineNest","StyleNest","BasicNest"
]
# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import os
import sys

# Custom Library

# Custom Packages
import AthenaColor.data.colors_html as HtmlColorObjects
from AthenaColor.data.style import Style, StyleNest, Basic, BasicNest
from AthenaColor.models.rgb_controlled import RgbControlled
from AthenaColor.models.rgb_controlled_nested import RgbControlledNested

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
# Applies a quick fix to make color appear in console
if sys.platform == 'win32':
    os.system("color")

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
# Collection of both inline and nested objects
#   These can be used to use color in the console
Fore = RgbControlled(param_code=f"38;2;",)
Back = RgbControlled(param_code=f"48;2;",)
Underline = RgbControlled(param_code=f"58;2;",)

ForeNest = RgbControlledNested(inline_class=Fore, reset=Style.NoForeground)
BackNest = RgbControlledNested(inline_class=Back,reset=Style.NoBackground)
UnderlineNest = RgbControlledNested(inline_class=Underline,reset=Style.NoUnderline)
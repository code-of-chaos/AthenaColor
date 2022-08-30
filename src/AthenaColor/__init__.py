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
import AthenaColor.data.colors_html as HtmlColorObjects
from AthenaColor.data.style import Style, StyleNest, Basic, BasicNest
from AthenaColor.data.bodies import Fore, ForeNest, Back, BackNest, Underline, UnderlineNest

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
import os
import sys

# Applies a quick fix to make color appear in console
if sys.platform == 'win32':
    os.system("color")
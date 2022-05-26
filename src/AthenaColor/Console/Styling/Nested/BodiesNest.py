# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor.Console.Styling.Nested.RgbControlledNest import RgbControlledNested
from AthenaColor.Console.Styling.Inline.Bodies import Fore, Back, Underline
from AthenaColor.Console.Styling.Inline.Style import Style

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "ForeNest","BackNest", "UnderlineNest"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
ForeNest = RgbControlledNested(
    inline_class=Fore,
    reset=Style.NoForeground
)

BackNest = RgbControlledNested(
    inline_class=Back,
    reset=Style.NoBackground
)

UnderlineNest = RgbControlledNested(
    inline_class=Underline,
    reset=Style.NoUnderline
)
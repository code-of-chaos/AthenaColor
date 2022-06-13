# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor.models.console.styling.rgb_controlled import RgbControlled
from AthenaColor.models.console.styling.rgb_controlled_nested import RgbControlledNested

from AthenaColor.data.style import Style

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "Fore","Back", "Underline",
    "ForeNest", "BackNest", "UnderlineNest"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
Fore = RgbControlled(
    param_code= f"38;2;",
)

Back = RgbControlled(
    param_code= f"48;2;",
)

Underline = RgbControlled(
    param_code= f"58;2;",
)

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
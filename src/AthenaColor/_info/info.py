# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
import AthenaColor._info.formatting as f
from AthenaColor._info._v import _version

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def info(*, to_str: bool = False) -> None | str:
    line = "-" * 128
    header = f.header(f"""{line}
{f.title("AthenaColor", to_str)} v{_version()}
is made by Andreas Sas and is a pacakge which allows you to use RGB colors in the console
{line}
""", to_str)

    body = f"""
Package setup:
    {f.sub_modules("models", to_str)} : Basic classes which are meant to hold data. 
        These sort of classes are not meant to house a lot methods which interact with lots of other classes

    {f.sub_modules("data", to_str)} : A collection of all premade data, ready for a user to use

    {f.sub_modules("functions", to_str)} : A collection of basic functions needed to make various things work
"""

    text = f"{header}{body}{line}"

    # export to console or string
    if to_str:
        return text
    else:
        print(text)
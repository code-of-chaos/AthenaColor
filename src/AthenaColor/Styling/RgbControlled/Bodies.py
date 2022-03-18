# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from .RgbControlled import RgbControlled
from AthenaColor import init
from AthenaColor.BASE import end_codes

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
esc = init.esc
end = end_codes.color

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
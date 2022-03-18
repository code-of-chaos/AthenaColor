# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor import (
    Fore,
    Back,
    Style,
    HtmlColors,
    rgb,
)
from AthenaColor.Styling.RgbControlled import Underline

# ----------------------------------------------------------------------------------------------------------------------
# - Support -
# ----------------------------------------------------------------------------------------------------------------------
color_list = [(k,v) for k,v in HtmlColors.__dict__.items() if k[:1] != "_"]
color_len = len("".join(f" {c_name}" for c_name, _ in color_list))

def _all(cls:object, styling:str=None):
    if styling is None:
        for name, styling in vars(cls).items():
            if name[0] != "_":
                print(f"{styling}{name}{Style.Reset}")
    else:
        for name in vars(cls):
            if name[0] != "_":
                print(f"{styling}{name}{Style.Reset}")

# ----------------------------------------------------------------------------------------------------------------------
# - PrintOut functions -
# ----------------------------------------------------------------------------------------------------------------------
def AllFore():
    _all(Fore)

def AllBack():
    _all(Back)

def AllTable():
    nl = "\n"
    all_styles = Style.UnderlineDouble + Style.Italic + Style.Bold + Style.Underline + Style.Crossed + Style.Reversed + Style.Frame + Style.Circle

    print(
f"""
┏━{Style.Bold}Colors{Style.Reset}━━━━━━━━━━━━━┳━{"━" * color_len}
┃ Color Name         ┃ {" ".join(f"{Fore.c(color_rgb)}{color_name}{Style.Reset}" for color_name, color_rgb in vars(HtmlColors).items() if isinstance(color_rgb, rgb))}
┣────────────────────╂─{"─" * color_len}
{nl.join(
    f"┃ {style_name}{' '*(19 - len(style_name))}┃ {' '.join(f'{style}{Fore.c(color_rgb)}{color_name}{Style.Reset}' for color_name, color_rgb in vars(HtmlColors).items() if isinstance(color_rgb, rgb))}"
    for style_name, style in vars(Style).items()
    if not any((style_name.startswith("_") , style_name.startswith("No") , style_name in ("Reset","Unverfified","BackgroundDefault")))
)}
┃ ALL                ┃ {" ".join(f"{all_styles}{Fore.c(color_rgb)}{color_name}{Style.Reset}" for color_name, color_rgb in vars(HtmlColors).items() if isinstance(color_rgb, rgb))}
┗━━━━━━━━━━━━━━━━━━━━┻━{"━" * color_len}
"""
    )
def AllTable_UnverfifiedPycharm():
    nl = "\n"
    print(
f"""
┏━{Style.Bold}Unverfified{Style.Reset}━━━━━━━━┳━{"━" * color_len}
┃ Color Name         ┃ {" ".join(f"{Fore.c(color_rgb)}{color_name}{Style.Reset}" for color_name, color_rgb in vars(HtmlColors).items() if isinstance(color_rgb, rgb))}
┣────────────────────╂─{"─" * color_len}
{nl.join(
    f"┃ {style_name}{' '*(19 - len(style_name))}┃ {' '.join(f'{style}{Fore.c(color_rgb)}{color_name}{Style.Reset}' for color_name, color_rgb in vars(HtmlColors).items() if isinstance(color_rgb, rgb))}"
    for style_name, style in vars(Style.Unverfified).items()
    if not any((style_name.startswith("_") , style_name.startswith("No") , style_name in ("Reset","Unverfified")))
)}
┃ Underline          ┃ {" ".join(f"{Underline.c(color_rgb)}{color_name}{Style.Reset}" for color_name, color_rgb in vars(HtmlColors).items() if isinstance(color_rgb, rgb))}
┗━━━━━━━━━━━━━━━━━━━━┻━{"━" * color_len}
"""
    )

def AllBoxes(rows=4):
    x,y = 0,0
    list_blocks = [[None]*round(len(color_list)/rows)for _ in range(rows)]
    for color_name, color_rgb in vars(HtmlColors).items():
        if isinstance(color_rgb, rgb):
            list_blocks[y][x] = f"{Fore.c(color_rgb)}█{Style.Reset}"
            y+=1
            if y == rows:
                x += 1
                y = 0
    print(
        "\n".join(
            "".join(
                c if c is not None else f" "
                for c in r
            )
            for r in list_blocks
        )
    )
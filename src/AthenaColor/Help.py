# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor import (
    ConsolePrinter as CP,
    Colors
)
from AthenaColor.Predefined.ColorsBasic import ColorsBasic
from AthenaColor.Objects import rgb

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
color_list = [(k,v) for k,v in Colors.__class__.__dict__.items() if k[:1] != "_"]
color_len = len("".join(f" {c_name}" for c_name, _ in color_list))

def all_Foregrounds():
    for c_name, c in color_list: #type:str,rgb
        print(f"{CP.Foreground(c)}{c_name}{CP.Reset}")

def all_Backgrounds():
    for c_name, c in color_list: #type:str,rgb
        print(f"{CP.Reversed}{CP.Foreground(c)}{c_name}{CP.Reset}")

def all_Colours_Limited():
    easy_color_list = [(k,v) for k,v in ColorsBasic.__dict__.items() if k[:1] != "_"]
    for c_name, c in easy_color_list: #type:str,rgb
        print(f"{c}{c_name}{CP.Reset}")

def all_Formats() -> None:
    all_format = CP.UnderlineDouble + CP.Italic + CP.Bold + CP.Underline + CP.Crossed + CP.Reversed + CP.Frame + CP.Circle
    print("┏━WORKING━━━━━━━━━━━━┳━" + "━"*color_len)
    print("┃ Color Name         ┃ " + " ".join(f"{CP.Foreground(c)  }{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┣────────────────────╂─" + "─" * color_len)
    print("┃ Italic             ┃ " + " ".join(f"{CP.Italic         }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ Bold               ┃ " + " ".join(f"{CP.Bold           }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ Underline          ┃ " + " ".join(f"{CP.Underline      }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ Crossed            ┃ " + " ".join(f"{CP.Crossed        }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ Reversed           ┃ " + " ".join(f"{CP.Reversed       }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ Frame              ┃ " + " ".join(f"{CP.Frame          }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ Circle             ┃ " + " ".join(f"{CP.Circle         }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ UnderlineDouble    ┃ " + " ".join(f"{CP.UnderlineDouble}{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ ALL                ┃ " + " ".join(f"{all_format        }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┗━━━━━━━━━━━━━━━━━━━━┻━" + "━"*color_len)

def all_NotWorkingPycharm() -> None:
    print("┏━NOT WORKING━━━━━━━━┳━" + "━"*color_len)
    print("┃ Dim                ┃ " + " ".join(f"{CP.GraphicMakeup.Dim                  }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ BlinkSlow          ┃ " + " ".join(f"{CP.GraphicMakeup.BlinkSlow            }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ BlinkRapid         ┃ " + " ".join(f"{CP.GraphicMakeup.BlinkRapid           }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ Conceal            ┃ " + " ".join(f"{CP.GraphicMakeup.Conceal              }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ FontPrimary        ┃ " + " ".join(f"{CP.GraphicMakeup.FontPrimary          }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ FontSecond1        ┃ " + " ".join(f"{CP.GraphicMakeup.FontSecond1          }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ FontSecond2        ┃ " + " ".join(f"{CP.GraphicMakeup.FontSecond2          }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ FontSecond3        ┃ " + " ".join(f"{CP.GraphicMakeup.FontSecond3          }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ FontSecond4        ┃ " + " ".join(f"{CP.GraphicMakeup.FontSecond4          }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ FontSecond5        ┃ " + " ".join(f"{CP.GraphicMakeup.FontSecond5          }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ FontSecond6        ┃ " + " ".join(f"{CP.GraphicMakeup.FontSecond6          }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ FontSecond8        ┃ " + " ".join(f"{CP.GraphicMakeup.FontSecond8          }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ FontSecond9        ┃ " + " ".join(f"{CP.GraphicMakeup.FontSecond9          }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ FontSecond10       ┃ " + " ".join(f"{CP.GraphicMakeup.FontSecond10         }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ Fraktur            ┃ " + " ".join(f"{CP.GraphicMakeup.Fraktur              }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ PropSpacing        ┃ " + " ".join(f"{CP.GraphicMakeup.PropSpacing          }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ OverLine           ┃ " + " ".join(f"{CP.GraphicMakeup.OverLine             }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ UnderColour        ┃ " + " ".join(f"{CP.GraphicMakeup.UnderColour(c)       }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ UnderColourDefault ┃ " + " ".join(f"{CP.GraphicMakeup.UnderColourDefault   }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ SuperScript        ┃ " + " ".join(f"{CP.GraphicMakeup.SuperScript          }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ SubScript          ┃ " + " ".join(f"{CP.GraphicMakeup.SubScript            }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┃ NoScript           ┃ " + " ".join(f"{CP.GraphicMakeup.NoScript             }{CP.Foreground(c)}{c_name}{CP.Reset}" for c_name, c in color_list))
    print("┗━━━━━━━━━━━━━━━━━━━━┻━" + "━"*color_len)

def color_box(rows=4):
    x,y = 0,0
    list_blocks = [[None]*round(len(color_list)/rows)for _ in range(rows)]
    for _, c in color_list:
        list_blocks[y][x] = f"{CP.Foreground(c)}█{CP.Reset}"
        y+=1
        if y == rows:
            x += 1
            y = 0
    print(
        "\n".join(
            "".join(
                c if c is not None else f"{CP.Foreground(Colors.Black)}█{CP.Reset}"
                for c in r
            )
            for r in list_blocks
        )
    )
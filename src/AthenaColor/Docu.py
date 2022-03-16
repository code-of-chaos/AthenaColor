# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Packages
import AthenaColor as AC

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
color_list = [(k,v) for k,v in AC.Colors.__class__.__dict__.items() if k[:1] != "_"]
color_len = len("".join(f" {c_name}" for c_name, _ in color_list))

def all_Foregrounds():
    for c_name, c in color_list: #type:str,AC.rgb
        print(f"{AC.Foreground(c)}{c_name}{AC.Reset}")

def all_Backgrounds():
    for c_name, c in color_list: #type:str,AC.rgb
        print(f"{AC.Reversed}{AC.Foreground(c)}{c_name}{AC.Reset}")

def all_Colours_Limited():
    easy_color_list = [(k,v) for k,v in AC.Colours_Limited.__dict__.items() if k[:1] != "_"]
    for c_name, c in easy_color_list: #type:str,AC.rgb
        print(f"{c}{c_name}{AC.Reset}")

def all_Formats() -> None:
    all_format = AC.UnderlineDouble + AC.Italic + AC.Bold + AC.Underline + AC.Crossed + AC.Reversed + AC.Frame + AC.Circle
    print("┏━WORKING━━━━━━━━━━━━┳━" + "━"*color_len)
    print("┃ Color Name         ┃ " + " ".join(f"{AC.Foreground(c)  }{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┣────────────────────╂─" + "─" * color_len)
    print("┃ Italic             ┃ " + " ".join(f"{AC.Italic         }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ Bold               ┃ " + " ".join(f"{AC.Bold           }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ Underline          ┃ " + " ".join(f"{AC.Underline      }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ Crossed            ┃ " + " ".join(f"{AC.Crossed        }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ Reversed           ┃ " + " ".join(f"{AC.Reversed       }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ Frame              ┃ " + " ".join(f"{AC.Frame          }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ Circle             ┃ " + " ".join(f"{AC.Circle         }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ UnderlineDouble    ┃ " + " ".join(f"{AC.UnderlineDouble}{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ ALL                ┃ " + " ".join(f"{all_format        }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┗━━━━━━━━━━━━━━━━━━━━┻━" + "━"*color_len)

def all_NotWorkingPycharm() -> None:
    print("┏━NOT WORKING━━━━━━━━┳━" + "━"*color_len)
    print("┃ Dim                ┃ " + " ".join(f"{AC.maybe_working.ConsolePrinter.Dim                       }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ BlinkSlow          ┃ " + " ".join(f"{AC.maybe_working.ConsolePrinter.BlinkSlow                 }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ BlinkRapid         ┃ " + " ".join(f"{AC.maybe_working.ConsolePrinter.BlinkRapid                }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ Conceal            ┃ " + " ".join(f"{AC.maybe_working.ConsolePrinter.Conceal                   }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ FontPrimary        ┃ " + " ".join(f"{AC.maybe_working.ConsolePrinter.FontPrimary               }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ FontSecond1        ┃ " + " ".join(f"{AC.maybe_working.ConsolePrinter.FontSecond1               }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ FontSecond2        ┃ " + " ".join(f"{AC.maybe_working.ConsolePrinter.FontSecond2               }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ FontSecond3        ┃ " + " ".join(f"{AC.maybe_working.ConsolePrinter.FontSecond3               }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ FontSecond4        ┃ " + " ".join(f"{AC.maybe_working.ConsolePrinter.FontSecond4               }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ FontSecond5        ┃ " + " ".join(f"{AC.maybe_working.ConsolePrinter.FontSecond5               }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ FontSecond6        ┃ " + " ".join(f"{AC.maybe_working.ConsolePrinter.FontSecond6               }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ FontSecond8        ┃ " + " ".join(f"{AC.maybe_working.ConsolePrinter.FontSecond8               }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ FontSecond9        ┃ " + " ".join(f"{AC.maybe_working.ConsolePrinter.FontSecond9               }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ FontSecond10       ┃ " + " ".join(f"{AC.maybe_working.ConsolePrinter.FontSecond10              }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ Fraktur            ┃ " + " ".join(f"{AC.maybe_working.ConsolePrinter.Fraktur                   }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ PropSpacing        ┃ " + " ".join(f"{AC.maybe_working.ConsolePrinter.PropSpacing               }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ OverLine           ┃ " + " ".join(f"{AC.maybe_working.ConsolePrinter.OverLine                  }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ UnderColour        ┃ " + " ".join(f"{AC.maybe_working.ConsolePrinter.UnderColour(c)            }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ UnderColourDefault ┃ " + " ".join(f"{AC.maybe_working.ConsolePrinter.UnderColourDefault        }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ SuperScript        ┃ " + " ".join(f"{AC.maybe_working.ConsolePrinter.SuperScript               }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ SubScript          ┃ " + " ".join(f"{AC.maybe_working.ConsolePrinter.SubScript                 }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┃ NoScript           ┃ " + " ".join(f"{AC.maybe_working.ConsolePrinter.NoScript                  }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("┗━━━━━━━━━━━━━━━━━━━━┻━"+ "━"*color_len)

def color_box(rows=5):
    x,y = 0,0
    list_blocks = [[None]*round(len(color_list)/rows+1)for _ in range(rows)]
    for _, c in color_list:
        list_blocks[y][x] = f"{AC.Foreground(c)}█{AC.Reset}"
        y+=1
        if y == rows:
            x += 1
            y = 0
    print(
        "\n".join(
            "".join(
                c if c is not None else f"{AC.Foreground(AC.Colors.Black)}█{AC.Reset}"
                for c in r
            )
            for r in list_blocks
        )
    )
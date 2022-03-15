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

def all_Foregrounds():
    for c_name, c in color_list: #type:str,AC.rgb
        print(f"{AC.Foreground(c)}{c_name}{AC.Reset}")

def all_Backgrounds():
    for c_name, c in color_list: #type:str,AC.rgb
        print(f"{AC.Reversed}{AC.Foreground(c)}{c_name}{AC.Reset}")

def all_Formats() -> None:

    color_len = "-"*len("".join(f" {c_name}" for c_name, _ in color_list))

    print()
    print("---------------------" + color_len)
    print("Color Name       :   " + " ".join(f"{AC.Foreground(c)  }{c_name}{AC.Reset}" for c_name, c in color_list))
    print("Italic           :   " + " ".join(f"{AC.Italic         }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("Bold             :   " + " ".join(f"{AC.Bold           }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("Underline        :   " + " ".join(f"{AC.Underline      }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("Dim              :   " + " ".join(f"{AC.Dim            }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("Crossed          :   " + " ".join(f"{AC.Crossed        }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("Reversed         :   " + " ".join(f"{AC.Reversed       }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("Frame            :   " + " ".join(f"{AC.Frame          }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("Circle           :   " + " ".join(f"{AC.Circle         }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("UnderlineDouble  :   " + " ".join(f"{AC.UnderlineDouble}{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("ALL              :   " + " ".join(f"{AC.UnderlineDouble}{AC.Italic}{AC.Bold}{AC.Underline}{AC.Dim}{AC.Crossed}{AC.Reversed}{AC.Frame}{AC.Circle}{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("---------------------" + color_len)
    print()
    print("-NOT WORKING PYCHARM-" + color_len)
    print("BlinkSlow        :   " + " ".join(f"{AC.maybe_working.BlinkSlow}{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("BlinkRapid       :   " + " ".join(f"{AC.maybe_working.BlinkRapid}{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("Conceal          :   " + " ".join(f"{AC.maybe_working.Conceal}{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("FontPrimary      :   " + " ".join(f"{AC.maybe_working.FontPrimary }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("FontSecond1      :   " + " ".join(f"{AC.maybe_working.FontSecond1 }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("FontSecond2      :   " + " ".join(f"{AC.maybe_working.FontSecond2 }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("FontSecond3      :   " + " ".join(f"{AC.maybe_working.FontSecond3 }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("FontSecond4      :   " + " ".join(f"{AC.maybe_working.FontSecond4 }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("FontSecond5      :   " + " ".join(f"{AC.maybe_working.FontSecond5 }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("FontSecond6      :   " + " ".join(f"{AC.maybe_working.FontSecond6 }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("FontSecond8      :   " + " ".join(f"{AC.maybe_working.FontSecond8 }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("FontSecond9      :   " + " ".join(f"{AC.maybe_working.FontSecond9 }{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("FontSecond10     :   " + " ".join(f"{AC.maybe_working.FontSecond10}{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("Fraktur          :   " + " ".join(f"{AC.maybe_working.Fraktur}{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("PropSpacing      :   " + " ".join(f"{AC.maybe_working.PropSpacing}{AC.Foreground(c)}{c_name}{AC.Reset}" for c_name, c in color_list))
    print("---------------------"+ color_len)
    print()

if __name__ == "__main__":
    all_Foregrounds()
    all_Backgrounds()
    all_Formats()
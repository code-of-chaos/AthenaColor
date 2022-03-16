# *-* Base Needed imports *-*
from AthenaColor import (
    ConsolePrinter as ACP,
    Colors
)

# *-* Use the objects in an f-string *-*
print(
f"""||| {ACP.Bold}Welcome to the AthenaColor Package!{ACP.Reset} |||

- The {ACP.Foreground(Colors.HotPink)}ACP.Foreground(Colors.HotPink){ACP.Reset} Changes the Foreground color
- The {ACP.Background(Colors.Indigo)}ACP.Background(Colors.Indigo){ACP.Reset} changes the background color
- Combinations like {ACP.Background(Colors.Teal) + ACP.Foreground(Colors.LightGoldenRodYellow)} ACP.Background(Colors.Teal) + ACP.Foreground(Colors.LightGoldenRodYellow){ACP.Reset} are also supported
"""
)

text_style = ACP.Background(Colors.DarkSlateBlue) + ACP.Foreground(Colors.Violet) + ACP.Underline

print(
f"""Usage of custom combined styles can also be used without any issue
{text_style}ACP.Background(Colors.DarkSlateBlue) + ACP.Foreground(Colors.Violet) + ACP.Underline{ACP.Reset}"""
)

# *-* Create your own rgb objects *-*
from AthenaColor.Objects import rgb

custom_color = rgb(r=86,g=54,b=186)
print(f"{ACP.Foreground(custom_color) + ACP.Reversed}Text with a newly made rgb object{ACP.Reset}\n")

# *-* Print out of all colours and Style Formats *-*
from AthenaColor.Help import (
    all_Formats,
    color_box
)
print(f"""{ACP.Bold}
The following is a full list of all predefined colors.
Together with all Style makeups found in AthenaColor.ConsolePrinter:
{ACP.Reset}""")

all_Formats()

print(f"""{ACP.Bold}
The following is a small view of all predefined colors:
{ACP.Reset}""")

color_box()
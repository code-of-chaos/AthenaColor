import AthenaColor as AC
from AthenaColor.Predefined import Colors

# *-*
# Use the objects in an f-string
# *-*
print(f"{AC.Bold}Hello there!{AC.Reset}")
print(f"{AC.Foreground(Colors.Olive)}This changes the foreground color{AC.Reset}")
print(f"{AC.Foreground(Colors.DarkViolet)}This changes the background color{AC.Reset}")
print(f"{AC.Background(Colors.Teal)}{AC.Foreground(Colors.LightGoldenRodYellow)}You can also combine them{AC.Reset}")

text_style = AC.Background(Colors.DarkSlateBlue) + AC.Foreground(Colors.Violet) + AC.Underline
print(f"{text_style}This works as well!{AC.Reset}")


# *-*
# Use the objects in a concat-ed string
# *-*
print(AC.Bold + "Hello there!" + AC.Reset)

# *-*
# To see all available colors and format styles, the following functions will print out all the available colors and the available
# *-*

from AthenaColor.Docu import (
    all_Formats,
    color_box
)
all_Formats()
color_box()
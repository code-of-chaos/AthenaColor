# - Athena Color Package - v2.0.0

A little package which allows you to use ANSI codes to print colour to the console.

---
## Details and features
- Support for Fore- and Background colours
- Support for Underline, Bold, Italic and other Format styles
- Custom rgb class with full support for math operators
- All basic and extended web colors available to be printed to console
- Access to the full rgb spectrum to be printed to the console

---

## Usage
The code below is an example:
```python
import AthenaColor as AC
from AthenaColor import Colors

# *-*
# Use the objects in an f-string
# *-*
print(f"{AC.Bold}Hello there!{AC.Reset}")
print(f"{AC.Foreground(Colors.Olive)}This changes the foreground color{AC.Reset}")
print(f"{AC.Foreground(Colors.DarkViolet)}This changes the background color{AC.Reset}")
print(f"{AC.Background(Colors.Teal)}{AC.Foreground(Colors.LightGoldenRodYellow)}You can also combine them{AC.Reset}")

text_style = AC.Background(Colors.DarkSlateBlue) + Colors.Violet + AC.Underline
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

```
---
## Links
Project files can be found at:
- [GitHub Repo](https://github.com/DirectiveAthena/AthenaColor) 
- [Pypi link](https://pypi.org/project/AthenaColor/)

Pip install by the following command: 
```
pip install AthenaColor
```
Made By Andreas Sas, 2022
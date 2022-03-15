# - Athena Color Package - v1.0.1

A little package which allows you to use ANSI codes to print colour to the console.

---
## Details and features
- Support for Fore- and Background colours
- Support for Underline, Bold, Italic and other Format styles

---

## Usage
The code below is an example:
```python
from AthenaColor import (
    Format,         # Holds content like the RESET, BOLD and other changes
    Foreground,
    Background,
    Colors          # These are just the colour codes, not actually usable on its own
)

# *-*
# Use the objects in an f-string
# *-*

print(f"{Format.Bold}Hello there!{Format.Reset}")
print(f"{Foreground.Olive_Dark}This changes the foreground color{Format.Reset}")
print(f"{Background.Purple_Dark}This changes the background color{Format.Reset}")
print(f"{Background.Teal_Dark}{Foreground.Yellow_Light}You can also combine them{Format.Reset}")

text_style = Background.Blue_Dark + Foreground.Violet + Format.Underline
print(f"{text_style}This works as well!{Format.Reset}")


# *-*
# Use the objects in a concat-ed string
# *-*

print(Format.Bold + "Hello there!" + Format.Reset)

# *-*
# To see all available colors and format styles, the following functions will print out all the available colors and the available 
# *-*

from AthenaColor.main import (
    all_Formats,
    all_Backgrounds,
    all_Foregrounds
)

all_Foregrounds()
all_Backgrounds()
all_Formats()

```

---

## All Colors available:
- Black
- Black_Light
- Grey_Dark
- Grey
- Grey_Light
- White_Dark
- White
- Red_Dark
- Red
- Red_Light
- Green_Dark
- Green
- Green_Light
- Yellow_Dark
- Yellow
- Yellow_Light
- Blue_Dark
- Blue
- Blue_Light
- Purple_Dark
- Purple
- Purple_Light
- Teal_Dark
- Teal
- Teal_Light
- Violet_Dark
- Violet
- Violet_Light
- Orange_Dark
- Orange
- Orange_Light
- Cyan_Dark
- Cyan
- Cyan_Light
- Pink_Dark
- Pink
- Pink_Light
- Olive_Dark
- Olive
- Olive_Light


---

## Links
Project files can be found at:
- [GitHub Repo](https://github.com/DirectiveAthena/AthenaColor) 
- [Pypi link](https://pypi.org/project/AthenaColor/)

Pip installs by the following command: 
```
pip install AthenaColor
```
Made By Andreas Sas, 2022
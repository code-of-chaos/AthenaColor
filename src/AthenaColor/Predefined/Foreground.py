# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from ..BASE import cc,end,esc,Colors

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Foreground:
    Black =             f"{esc}[38;{cc}{Colors.Black       }{end}"
    Black_Light =       f"{esc}[38;{cc}{Colors.Black_Light }{end}"
    Grey_Dark =         f"{esc}[38;{cc}{Colors.Grey_Dark   }{end}"
    Grey =              f"{esc}[38;{cc}{Colors.Grey        }{end}"
    Grey_Light =        f"{esc}[38;{cc}{Colors.Grey_Light  }{end}"
    White_Dark =        f"{esc}[38;{cc}{Colors.White_Dark  }{end}"
    White =             f"{esc}[38;{cc}{Colors.White       }{end}"

    Red_Dark =          f"{esc}[38;{cc}{Colors.Red_Dark    }{end}"
    Red =               f"{esc}[38;{cc}{Colors.Red         }{end}"
    Red_Light =         f"{esc}[38;{cc}{Colors.Red_Light   }{end}"

    Green_Dark =        f"{esc}[38;{cc}{Colors.Green_Dark  }{end}"
    Green =             f"{esc}[38;{cc}{Colors.Green       }{end}"
    Green_Light =       f"{esc}[38;{cc}{Colors.Green_Light }{end}"

    Yellow_Dark =       f"{esc}[38;{cc}{Colors.Yellow_Dark }{end}"
    Yellow =            f"{esc}[38;{cc}{Colors.Yellow      }{end}"
    Yellow_Light =      f"{esc}[38;{cc}{Colors.Yellow_Light}{end}"

    Blue_Dark =         f"{esc}[38;{cc}{Colors.Blue_Dark   }{end}"
    Blue =              f"{esc}[38;{cc}{Colors.Blue        }{end}"
    Blue_Light =        f"{esc}[38;{cc}{Colors.Blue_Light  }{end}"

    Purple_Dark =       f"{esc}[38;{cc}{Colors.Purple_Dark }{end}"
    Purple =            f"{esc}[38;{cc}{Colors.Purple      }{end}"
    Purple_Light =      f"{esc}[38;{cc}{Colors.Purple_Light}{end}"

    Teal_Dark =         f"{esc}[38;{cc}{Colors.Teal_Dark   }{end}"
    Teal =              f"{esc}[38;{cc}{Colors.Teal        }{end}"
    Teal_Light =        f"{esc}[38;{cc}{Colors.Teal_Light  }{end}"

    Violet_Dark =       f"{esc}[38;{cc}{Colors.Violet_Dark }{end}"
    Violet =            f"{esc}[38;{cc}{Colors.Violet      }{end}"
    Violet_Light =      f"{esc}[38;{cc}{Colors.Violet_Light}{end}"

    Orange_Dark =       f"{esc}[38;{cc}{Colors.Orange_Dark }{end}"
    Orange =            f"{esc}[38;{cc}{Colors.Orange      }{end}"
    Orange_Light =      f"{esc}[38;{cc}{Colors.Orange_Light}{end}"

    Cyan_Dark =         f"{esc}[38;{cc}{Colors.Cyan_Dark   }{end}"
    Cyan =              f"{esc}[38;{cc}{Colors.Cyan        }{end}"
    Cyan_Light =        f"{esc}[38;{cc}{Colors.Cyan_Light  }{end}"

    Pink_Dark =         f"{esc}[38;{cc}{Colors.Pink_Dark   }{end}"
    Pink =              f"{esc}[38;{cc}{Colors.Pink        }{end}"
    Pink_Light =        f"{esc}[38;{cc}{Colors.Pink_Light  }{end}"

    Olive_Dark =        f"{esc}[38;{cc}{Colors.Olive_Dark  }{end}"
    Olive =             f"{esc}[38;{cc}{Colors.Olive       }{end}"
    Olive_Light =       f"{esc}[38;{cc}{Colors.Olive_Light }{end}"

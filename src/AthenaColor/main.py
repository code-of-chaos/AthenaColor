# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor import (
Format,
Foreground,
Background,
Colors
)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------

def _print_all(class_object:object) -> None:
    for k,v in class_object.__class__.__dict__.items():
        if isinstance(v, str):
            print(f"{v}{k}{Format.Reset}")

def all_Colors() -> None:
    for k, v in Colors.__class__.__dict__.items():
        if isinstance(v, int):
            print(f"{k} = {v}")

def all_Foregrounds() -> None:
    _print_all(Foreground)

def all_Backgrounds() -> None:
    _print_all(Background)

def all_Formats() -> None:
    for k, v in Foreground.__class__.__dict__.items():
        if isinstance(v, str):
            print(f"{v}{k}{Format.Reset}")
            print(f"{Format.Italic}{v}{k}{Format.Reset}")
            print(f"{Format.Bold}{v}{k}{Format.Reset}")
            print(f"{Format.Underline}{v}{k}{Format.Reset}")
            print(f"{Format.Dim}{v}{k}{Format.Reset}")
            print(f"{Format.Crossed}{v}{k}{Format.Reset}")
            print(f"{Format.Reversed}{v}{k}{Format.Reset}")
            print(f"{Format.Frame}{v}{k}{Format.Reset}")
            print(f"{Format.Circle}{v}{k}{Format.Reset}")
            print(f"{Format.Italic}{Format.Bold}{Format.Underline}{Format.Dim}{Format.Crossed}{Format.Reversed}{Format.Frame}{Format.Circle}{v}{k}{Format.Reset}")


if __name__ == "__main__":
    all_Colors()
    all_Foregrounds()
    all_Backgrounds()
    all_Formats()
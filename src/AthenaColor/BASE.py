# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class end_codes:
    cursor_line_up = "A"
    cursor_line_down = "B"
    cursor_right = "C"
    cursor_left = "D"
    cursor_line_next = "E"
    cursor_line_previous = "F"
    cursor_to_column = "G"
    color = "m"


class ColorClass:
    # ------------------------------------------------------------------------------------------------------------------
    # Conversion Methods
    # ------------------------------------------------------------------------------------------------------------------
    def to_hexadecimal(self) -> str:
        return NotImplemented
    def to_cmyk(self) -> tuple[float, float, float, float]:
        return NotImplemented
    def to_hsl(self) -> tuple[float, float, float]:
        return NotImplemented
    def to_hsv(self) -> tuple[float, float, float]:
        return NotImplemented

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __str__(self) -> str:
        return NotImplemented

    def __repr__(self) -> str:
        return NotImplemented

    # Comparison operators
    # >
    def __gt__(self, other: ColorClass | int | float) -> bool:
        return NotImplemented

    # <
    def __lt__(self, other: ColorClass | int | float) -> bool:
        return NotImplemented

    # ==
    def __eq__(self, other: ColorClass | int | float) -> bool:
        return NotImplemented

    # !=
    def __ne__(self, other: ColorClass | int | float) -> bool:
        return NotImplemented

    # <=
    def __le__(self, other: ColorClass | int | float) -> bool:
        return NotImplemented

    # >=
    def __ge__(self, other: ColorClass | int | float) -> bool:
        return NotImplemented

    # math operators
    # +
    def __add__(self, other: ColorClass | int | float) -> ColorClass:
        return NotImplemented

    # -
    def __sub__(self, other: ColorClass | int | float) -> ColorClass:
        return NotImplemented

    # *
    def __mul__(self, other: ColorClass | int | float) -> ColorClass:
        return NotImplemented

    # //
    def __floordiv__(self, other: ColorClass | int | float) -> ColorClass:
        return NotImplemented

    # /
    def __truediv__(self, other: ColorClass | int | float) -> ColorClass:
        return NotImplemented

    # %
    def __mod__(self, other: ColorClass | int | float) -> ColorClass:
        return NotImplemented

    # **
    def __pow__(self, other: ColorClass | int | float) -> ColorClass:
        return NotImplemented

    # Augmented assignments
    # +=
    def __iadd__(self, other: ColorClass | int | float) -> ColorClass:
        return self.__add__(other)

    # -=
    def __isub__(self, other: ColorClass | int | float) -> ColorClass:
        return self.__sub__(other)

    # *=
    def __imul__(self, other: ColorClass | int | float) -> ColorClass:
        return self.__mul__(other)
    # //=
    def __ifloordiv__(self, other: ColorClass | int | float) -> ColorClass:
        return self.__floordiv__(other)
    # /=
    def __itruediv__(self, other: ColorClass | int | float) -> ColorClass:
        return self.__truediv__(other)
    # %=
    def __imod__(self, other: ColorClass | int | float) -> ColorClass:
        return self.__mod__(other)
    # **=
    def __ipow__(self, other: ColorClass | int | float) -> ColorClass:
        return self.__pow__(other)
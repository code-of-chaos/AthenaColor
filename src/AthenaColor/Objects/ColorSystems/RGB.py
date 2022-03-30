# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor.Functions.BoilerPlate import (
    Constrain,
    TestTypes,
    round_correctly
)
from ._ColorSystem import ColorSystem

# ------------------------------------------------------------------------------------------------------------------
# - Color -
# ------------------------------------------------------------------------------------------------------------------
class RGB(ColorSystem):
    # ------------------------------------------------------------------------------------------------------------------
    # INIT method
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,r: int, g: int, b: int):
        if not TestTypes(types=int,objects=(r,g,b)):
            raise ValueError(f"RGB values {r=},{g=},{b=} did not consist of integer values")

        self.r = r
        self.g = g
        self.b = b

    # ------------------------------------------------------------------------------------------------------------------
    # RGB Properties
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, value: int | float):
        self._r = round_correctly(Constrain(value,255))

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value: int | float):
        self._g = round_correctly(Constrain(value,255))

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value: int | float):
        self._b = round_correctly(Constrain(value,255))

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    def __int__(self):
        return self.r + self.g + self.b

    # String magic methods
    def __str__(self) -> str:
        return f"{self.r};{self.g};{self.b}"

    def __repr__(self) -> str:
        return f"rgb(r={self.r}, g={self.g}, b={self.b})"

    # Comparison operators
    # >
    def __gt__(self, other: RGB | int | float | tuple[int|float,int|float,int|float]) -> bool:
        if isinstance(other, RGB):
            return all(((self.r > other.r), (self.g > other.g), (self.b > other.b)))
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) > (other + other + other)
        elif isinstance(other, tuple):
            r_,g_,b_ = other
            return all((self.r > r_, self.g > g_, self.b > b_))
        else:
            return NotImplemented

    # <
    def __lt__(self, other: RGB | int | float | tuple[int|float,int|float,int|float]) -> bool:
        if isinstance(other, RGB):
            return all(((self.r < other.r), (self.g < other.g), (self.b < other.b)))
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) < (other + other + other)
        elif isinstance(other, tuple):
            r_,g_,b_ = other
            return all((self.r < r_, self.g < g_, self.b < b_))
        else:
            return NotImplemented

    # ==
    def __eq__(self, other: RGB | int | float | tuple[int|float,int|float,int|float]) -> bool:
        if isinstance(other, RGB):
            return all(((self.r == other.r), (self.g == other.g), (self.b == other.b)))
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) == (other + other + other)
        elif isinstance(other, tuple):
            r_,g_,b_ = other
            return all((self.r == r_, self.g == g_, self.b == b_))
        else:
            return NotImplemented

    # !=
    def __ne__(self, other: RGB | int | float | tuple[int|float,int|float,int|float]) -> bool:
        if isinstance(other, RGB):
            return all(((self.r != other.r), (self.g != other.g), (self.b != other.b)))
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) != (other + other + other)
        elif isinstance(other, tuple):
            r_,g_,b_ = other
            return all((self.r != r_, self.g != g_, self.b != b_))
        else:
            return NotImplemented

    # <=
    def __le__(self, other: RGB | int | float | tuple[int|float,int|float,int|float]) -> bool:
        if isinstance(other, RGB):
            return all((self.r <= other.r, self.g <= other.g, self.b >= other.b))
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) >= (other + other + other)
        elif isinstance(other, tuple):
            r_,g_,b_ = other
            return all((self.r <= r_, self.g <= g_, self.b >= b_))
        else:
            return NotImplemented

    # >=
    def __ge__(self, other: RGB | int | float | tuple[int|float,int|float,int|float]) -> bool:
        if isinstance(other, RGB):
            return all((self.r >= other.r, self.g >= other.g, self.b >= other.b))
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) >= (other + other + other)
        elif isinstance(other, tuple):
            r_,g_,b_ = other
            return all((self.r >= r_, self.g >=g_, self.b>=b_))
        else:
            return NotImplemented

    # math operators
    # +
    def __add__(self, other: RGB | int| float | tuple[int|float,int|float,int|float]) -> RGB:
        if isinstance(other, RGB):
            self.r = self.r + other.r
            self.g = self.g + other.g
            self.b = self.b + other.b
        elif isinstance(other, (int, float)):
            self.r = self.r + other
            self.g = self.g + other
            self.b = self.b + other
        elif isinstance(other, tuple):
            r_,g_,b_ = other
            self.r = self.r + r_
            self.g = self.g + g_
            self.b = self.b + b_
        else:
            return NotImplemented
        return self

    # -
    def __sub__(self, other: RGB | int | float | tuple[int|float,int|float,int|float]) -> RGB:
        if isinstance(other, RGB):
            self.r = self.r - other.r
            self.g = self.g - other.g
            self.b = self.b - other.b
        elif isinstance(other, (int, float)):
            self.r = self.r - other
            self.g = self.g - other
            self.b = self.b - other
        elif isinstance(other, tuple):
            r_,g_,b_ = other
            self.r = self.r - r_
            self.g = self.g - g_
            self.b = self.b - b_
        else:
            return NotImplemented
        return self

    # *
    def __mul__(self, other: RGB | int | float | tuple[int|float,int|float,int|float]) -> RGB:
        if isinstance(other, RGB):
            self.r = self.r * other.r
            self.g = self.g * other.g
            self.b = self.b * other.b
        elif isinstance(other, (int, float)):
            self.r = self.r * other
            self.g = self.g * other
            self.b = self.b * other
        elif isinstance(other, tuple):
            r_,g_,b_ = other
            self.r = self.r * r_
            self.g = self.g * g_
            self.b = self.b * b_
        else:
            return NotImplemented
        return self

    # //
    def __floordiv__(self, other: RGB | int | float | tuple[int|float,int|float,int|float]) -> RGB:
        if isinstance(other, RGB):
            self.r = self.r // other.r
            self.g = self.g // other.g
            self.b = self.b // other.b
        elif isinstance(other, (int, float)):
            self.r = self.r // other
            self.g = self.g // other
            self.b = self.b // other
        elif isinstance(other, tuple):
            r_,g_,b_ = other
            self.r = self.r // r_
            self.g = self.g // g_
            self.b = self.b // b_
        else:
            return NotImplemented
        return self

    # /
    def __truediv__(self, other: RGB | int | float | tuple[int|float,int|float,int|float]) -> RGB:
        if isinstance(other, RGB):
            self.r = self.r / other.r
            self.g = self.g / other.g
            self.b = self.b / other.b
        elif isinstance(other, (int, float)):
            self.r = self.r / other
            self.g = self.g / other
            self.b = self.b / other
        elif isinstance(other, tuple):
            r_,g_,b_ = other
            self.r = self.r / r_
            self.g = self.g / g_
            self.b = self.b / b_
        else:
            return NotImplemented
        return self

    # %
    def __mod__(self, other: RGB | int | float | tuple[int|float,int|float,int|float]) -> RGB:
        if isinstance(other, RGB):
            self.r = self.r % other.r
            self.g = self.g % other.g
            self.b = self.b % other.b
        elif isinstance(other, (int, float)):
            self.r = self.r % other
            self.g = self.g % other
            self.b = self.b % other
        elif isinstance(other, tuple):
            r_,g_,b_ = other
            self.r = self.r % r_
            self.g = self.g % g_
            self.b = self.b % b_
        else:
            return NotImplemented
        return self

    # **
    def __pow__(self, other: RGB | int | float | tuple[int|float,int|float,int|float]) -> RGB:
        if isinstance(other, RGB):
            self.r = self.r ** other.r
            self.g = self.g ** other.g
            self.b = self.b ** other.b
        elif isinstance(other, (int, float)):
            self.r = self.r ** other
            self.g = self.g ** other
            self.b = self.b ** other
        elif isinstance(other, tuple):
            r_,g_,b_ = other
            self.r = self.r ** r_
            self.g = self.g ** g_
            self.b = self.b ** b_
        else:
            return NotImplemented
        return self
        
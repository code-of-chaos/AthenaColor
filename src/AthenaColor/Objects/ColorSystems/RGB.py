# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from .ColorSystem import ColorSystem
# ----------------------------------------------------------------------------------------------------------------------
# - Support Methods -
# ----------------------------------------------------------------------------------------------------------------------
def boundary(value:int|float) -> int|float:
    return min(max(value, 0), 255)

# ------------------------------------------------------------------------------------------------------------------
# - Color -
# ------------------------------------------------------------------------------------------------------------------
class RGB(ColorSystem):
    # ------------------------------------------------------------------------------------------------------------------
    # INIT method
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,r: int | float, g: int | float, b: int | float):
        if isinstance(r, (int,float)) and isinstance(g, (int,float)) and isinstance(b, (int,float)):
            self.r = r
            self.g = g
            self.b = b
        else:
            raise ValueError("no int or float were given on rgb creation")

    # ------------------------------------------------------------------------------------------------------------------
    # RGB Properties
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, value: int | float):
        self._r = round(boundary(value))

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value: int | float):
        self._g = round(boundary(value))

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value: int | float):
        self._b = round(boundary(value))

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
    def __gt__(self, other: RGB | int | float) -> bool:
        if isinstance(other, RGB):
            return (self.r + self.g + self.b) > (other.r + other.g + other.b)
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) > (other + other + other)
        else:
            return NotImplemented

    # <
    def __lt__(self, other: RGB | int | float) -> bool:
        if isinstance(other, RGB):
            return (self.r + self.g + self.b) < (other.r + other.g + other.b)
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) < (other + other + other)
        else:
            return NotImplemented

    # ==
    def __eq__(self, other: RGB | int | float) -> bool:
        if isinstance(other, RGB):
            return all(((self.r == other.r), (self.g == other.g), (self.b == other.b)))
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) == (other + other + other)
        else:
            return NotImplemented

    # !=
    def __ne__(self, other: RGB | int | float) -> bool:
        if isinstance(other, RGB):
            return all(((self.r != other.r), (self.g != other.g), (self.b != other.b)))
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) != (other + other + other)
        else:
            return NotImplemented
        # <=

    def __le__(self, other: RGB | int | float) -> bool:
        if isinstance(other, RGB):
            return (self.r + self.g + self.b) > (other.r + other.g + other.b)
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) > (other + other + other)
        else:
            return NotImplemented

    # >=
    def __ge__(self, other: RGB | int | float) -> bool:
        if isinstance(other, RGB):
            return (self.r + self.g + self.b) >= (other.r + other.g + other.b)
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) >= (other + other + other)
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
        
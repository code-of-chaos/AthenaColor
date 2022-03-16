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
def boundary(value:int|float) -> int|float:
    if 0 <= value <= 255:
        return value
    elif value < 0:
        return 0
    elif value > 255:
        return 255
    else:
        ValueError("Value out of range")

class rgb:
    # ------------------------------------------------------------------------------------------------------------------
    # INIT method
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,r:int|float,g:int|float,b:int|float):
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
    def r(self, value:int|float):
        self._r = int(round(boundary(value)))

    @property
    def g(self):
        return self._g
    @g.setter
    def g(self, value: int | float):
        self._g = int(round(boundary(value)))

    @property
    def b(self):
        return self._b
    @b.setter
    def b(self, value: int | float):
        self._b = int(round(boundary(value)))

    # ------------------------------------------------------------------------------------------------------------------
    # Special Methods
    # ------------------------------------------------------------------------------------------------------------------
    def decrease(self, value:float):
        if 0 > value or value > 1:
            raise ValueError("Value decreased can not be larger than 1 or smaller than 0")
        self.r -= self.r * value
        self.g -= self.g * value
        self.b -= self.b * value

    def increase(self, value:float):
        if 0 > value or value > 1:
            raise ValueError("Value increased can not be larger than 1 or smaller than 0")
        self.r += self.r * value
        self.g += self.g * value
        self.b += self.b * value

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __str__(self) -> str:
        return f"{self.r};{self.g};{self.b}"

    def __repr__(self) -> str:
        return f"rgb(r={self.r},g={self.g},b={self.b})"

    # conversion magic methods
    def __hex__(self) -> str:
        return '#%02x%02x%02x' % (self.r, self.b, self.g)

    # Comparison operators
    # >
    def __gt__(self, other:rgb|int|float) -> bool:
        if isinstance(other, rgb):
            return (self.r + self.g + self.b) > (other.r + other.g + other.b)
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) > (other + other + other)
        else:
            raise TypeError(f"Expected types: rgb, int or float. Got: {type(other)=}")

    # <
    def __lt__(self, other:rgb|int|float) -> bool:
        if isinstance(other, rgb):
            return (self.r + self.g + self.b) < (other.r + other.g + other.b)
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) < (other + other + other)
        else:
            raise TypeError(f"Expected types: rgb, int or float. Got: {type(other)=}")

    # ==
    def __eq__(self, other:rgb|int|float) -> bool:
        if isinstance(other, rgb):
            return all(((self.r == other.r), (self.g == other.g), (self.b == other.b)))
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) == (other + other + other)
        else:
            raise TypeError(f"Expected types: rgb, int or float. Got: {type(other)=}")
    # !=
    def __ne__(self, other:rgb|int|float) -> bool:
        if isinstance(other, rgb):
            return all(((self.r != other.r), (self.g != other.g), (self.b != other.b)))
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) != (other + other + other)
        else:
            raise TypeError(f"Expected types: rgb, int or float. Got: {type(other)=}")
    # <=
    def __le__(self, other:rgb|int|float) -> bool:
        if isinstance(other, rgb):
            return (self.r + self.g + self.b) > (other.r + other.g + other.b)
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) > (other + other + other)
        else:
            raise TypeError(f"Expected types: rgb, int or float. Got: {type(other)=}")
    # >=
    def __ge__(self, other:rgb|int|float) -> bool:
        if isinstance(other, rgb):
            return (self.r + self.g + self.b) >= (other.r + other.g + other.b)
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) >= (other + other + other)
        else:
            raise TypeError(f"Expected types: rgb, int or float. Got: {type(other)=}")

    # math operators
    # +
    def __add__(self, other:rgb|int|float) -> rgb:
        if isinstance(other, rgb):
            self.r = self.r + other.r
            self.g = self.g + other.g
            self.b = self.b + other.b
            return self
        elif isinstance(other, (int,float)):
            self.r = self.r + other
            self.g = self.g + other
            self.b = self.b + other
            return self
        else:
            raise TypeError(f"Expected types: rgb, int or float. Got: {type(other)=}")
    # -
    def __sub__(self, other: rgb | int | float) -> rgb:
        if isinstance(other, rgb):
            self.r = self.r - other.r
            self.g = self.g - other.g
            self.b = self.b - other.b
            return self
        elif isinstance(other, (int, float)):
            self.r = self.r - other
            self.g = self.g - other
            self.b = self.b - other
            return self
        else:
            raise TypeError(f"Expected types: rgb, int or float. Got: {type(other)=}")
    # *
    def __mul__(self, other: rgb | int | float) -> rgb:
        if isinstance(other, rgb):
            self.r = self.r * other.r
            self.g = self.g * other.g
            self.b = self.b * other.b
            return self
        elif isinstance(other, (int, float)):
            self.r = self.r * other
            self.g = self.g * other
            self.b = self.b * other
            return self
        else:
            raise TypeError(f"Expected types: rgb, int or float. Got: {type(other)=}")
    # //
    def __floordiv__(self, other: rgb | int | float) -> rgb:
        if isinstance(other, rgb):
            self.r = self.r // other.r
            self.g = self.g // other.g
            self.b = self.b // other.b
            return self
        elif isinstance(other, (int, float)):
            self.r = self.r // other
            self.g = self.g // other
            self.b = self.b // other
            return self
        else:
            raise TypeError(f"Expected types: rgb, int or float. Got: {type(other)=}")
    # /
    def __truediv__(self, other: rgb | int | float) -> rgb:
        if isinstance(other, rgb):
            self.r = self.r / other.r
            self.g = self.g / other.g
            self.b = self.b / other.b
            return self
        elif isinstance(other, (int, float)):
            self.r = self.r / other
            self.g = self.g / other
            self.b = self.b / other
            return self
        else:
            raise TypeError(f"Expected types: rgb, int or float. Got: {type(other)=}")

    # %
    def __mod__(self, other: rgb | int | float) -> rgb:
        if isinstance(other, rgb):
            self.r = self.r % other.r
            self.g = self.g % other.g
            self.b = self.b % other.b
            return self
        elif isinstance(other, (int, float)):
            self.r = self.r % other
            self.g = self.g % other
            self.b = self.b % other
            return self
        else:
            raise TypeError(f"Expected types: rgb, int or float. Got: {type(other)=}")

    # **
    def __pow__(self, other: rgb | int | float) -> rgb:
        if isinstance(other, rgb):
            self.r = self.r ** other.r
            self.g = self.g ** other.g
            self.b = self.b ** other.b
            return self
        elif isinstance(other, (int, float)):
            self.r = self.r ** other
            self.g = self.g ** other
            self.b = self.b ** other
            return self
        else:
            raise TypeError(f"Expected types: rgb, int or float. Got: {type(other)=}")

    # Augmented assignments
    # +=
    def __iadd__(self, other: rgb | int | float) -> rgb:
        return self.__add__(other)
    # -=
    def __isub__(self, other: rgb | int | float) -> rgb:
        return self.__sub__(other)
    # *=
    def __imul__(self, other: rgb | int | float) -> rgb:
        return self.__mul__(other)
    # //=
    def __ifloordiv__(self, other: rgb | int | float) -> rgb:
        return self.__floordiv__(other)
    # /=
    def __itruediv__(self, other: rgb | int | float) -> rgb:
        return self.__truediv__(other)
    # %=
    def __imod__(self, other: rgb | int | float) -> rgb:
        return self.__mod__(other)
    # **=
    def __ipow__(self, other: rgb | int | float) -> rgb:
        return self.__pow__(other)
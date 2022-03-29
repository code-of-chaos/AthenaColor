# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

from functools import wraps
import operator
# Custom Library

# Custom Packages
from AthenaColor.Objects.ColorClasses._color import ColorSystem
from ...Functions.ColorConversion import (
    rgb_to_hexadecimal,
    rgb_to_hsl,
    rgb_to_cmyk,
    rgb_to_hsv
)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def boundary(value:int|float) -> int|float:
    return min(max(value, 0), 255)

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
    # Conversion Methods
    # ------------------------------------------------------------------------------------------------------------------
    def to_hexadecimal(self) -> str:
        return rgb_to_hexadecimal(
            r=self.r,
            g=self.g,
            b=self.b
        )
    def to_cmyk(self) -> tuple[float,float,float,float]:
        return rgb_to_cmyk(
            r=self.r,
            g=self.g,
            b=self.b
        )
    def to_hsl(self) -> tuple[float,float,float]:
        return rgb_to_hsl(
            r=self.r,
            g=self.g,
            b=self.b
        )
    def to_hsv(self) -> tuple[float,float,float]:
        return rgb_to_hsv(
            r=self.r,
            g=self.g,
            b=self.b
        )

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

    def _compare(operation):
        def outer_wrapper(f):
            @wraps(f)
            def wrapper(self, other):
                if isinstance(other, RGB):
                    return operation(int(self), int(other))
                elif isinstance(other, (int, float)):
                    return operation(int(self), 3 * other)
                else:
                    return NotImplemented
            return wrapper
        return outer_wrapper

    def _calculate(operation):
        def outer_wrapper(f):
            @wraps(f)
            def wrapper(self, other):
                if isinstance(other, RGB):
                    self.r = operation(self.r, other.r)
                    self.g = operation(self.g, other.g)
                    self.b = operation(self.b, other.b)
                    return self
                elif isinstance(other, (int,float)):
                    self.r = operation(self.r, other)
                    self.g = operation(self.g, other)
                    self.b = operation(self.b, other)
                    return self
                else:
                    return NotImplemented
            return wrapper
        return outer_wrapper

    # Comparison operators.
    __gt__ = _compare(operator.gt)
    __lt__ = _compare(operator.lt)
    __eq__ = _compare(operator.eq)
    __ne__ = _compare(operator.ne)
    __le__ = _compare(operator.le)
    __ge__ = _compare(operator.ge)

    # math operators
    __add__ = _calculate(operator.add)
    __sub__ = _calculate(operator.sub)
    __mul__ = _calculate(operator.mul)
    __floordiv__ = _calculate(operator.floordiv)
    __truediv__ = _calculate(operator.truediv)
    __mod__ = _calculate(operator.mod)
    __pow__ = _calculate(operator.pow)
        
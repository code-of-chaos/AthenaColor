# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from abc import ABC, abstractmethod

# Custom Library

# Custom Packages
from AthenaColor.Functions.ColorConversion import *
from AthenaColor.Functions.BoilerPlate import Constrain

# ----------------------------------------------------------------------------------------------------------------------
# - Support functions -
# ----------------------------------------------------------------------------------------------------------------------
def _to_rgb(n:object) -> tuple[int|float,int|float,int|float]:
    if isinstance(n, (_RGB, _HEX)):
        return n.r, n.g, n.b
    elif isinstance(n, _CMYK):
        return cmyk_to_rgb(n.c, n.m, n.y, n.k)
    elif isinstance(n, _HSL):
        return hsl_to_rgb(n.h, n.s, n.l)
    elif isinstance(n, _HSV):
        return hsl_to_rgb(n.h, n.s, n.v)
    elif isinstance(n, tuple) and len(n)==3:
        return n
    elif isinstance(n, (int,float)):
        n_ = Constrain(n, 255)
        return n_,n_,n_
    else:
        return NotImplemented

def _to_system(n:object, r:int,g:int,b:int):
    if isinstance(n, (_RGB, _HEX)):
        n.r, n.g, n.b = r,g,b
    elif isinstance(n, _CMYK):
        n.c, n.m, n.y, n.k = rgb_to_cmyk(r,g,b)
    elif isinstance(n, _HSL):
        n.h, n.s, n.l = rgb_to_hsl(r,g,b)
    elif isinstance(n, _HSV):
        n.h, n.s, n.v = rgb_to_hsv(r,g,b)
    else:
        return NotImplemented

# ----------------------------------------------------------------------------------------------------------------------
# - Various Supported Color Systems -
# ----------------------------------------------------------------------------------------------------------------------
class _RGB:
    r:int
    g:int
    b:int

class _CMYK:
    c:float
    m:float
    y:float
    k:float

class _HEX:
    r:int
    g:int
    b:int

class _HSL:
    h:float
    s:float
    l:float

class _HSV:
    h:float
    s:float
    v:float

# ----------------------------------------------------------------------------------------------------------------------
# - Actual Color System -
# ----------------------------------------------------------------------------------------------------------------------
class ColorSystem(ABC):
    @abstractmethod
    def __str__(self): ...
    @abstractmethod
    def __repr__(self): ...

    # ------------------------------------------------------------------------------------------------------------------
    # - Math Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    def __add__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float]) -> ColorSystem:
        r,g,b = map(
            lambda x, x_ : x + x_ ,
            zip(_to_rgb(self), _to_rgb(other))
        )
        _to_system(self, r,g,b)
        return self

    def __sub__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float]) -> ColorSystem:
        r, g, b = map(
            lambda x, x_: x - x_,
            zip(_to_rgb(self), _to_rgb(other))
        )
        _to_system(self, r, g, b)
        return self

    def __mul__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float]) -> ColorSystem:
        r, g, b = map(
            lambda x, x_: x * x_,
            zip(_to_rgb(self), _to_rgb(other))
        )
        _to_system(self, r, g, b)
        return self

    def __floordiv__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float]) -> ColorSystem:
        r, g, b = map(
            lambda x, x_: x // x_,
            zip(_to_rgb(self), _to_rgb(other))
        )
        _to_system(self, r, g, b)
        return self

    def __truediv__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float]) -> ColorSystem:
        r, g, b = map(
            lambda x, x_: x / x_,
            zip(_to_rgb(self), _to_rgb(other))
        )
        _to_system(self, r, g, b)
        return self

    def __mod__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float]) -> ColorSystem:
        r, g, b = map(
            lambda x, x_: x % x_,
            zip(_to_rgb(self), _to_rgb(other))
        )
        _to_system(self, r, g, b)
        return self

    def __pow__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float]) -> ColorSystem:
        r, g, b = map(
            lambda x, x_: x ** x_,
            zip(_to_rgb(self), _to_rgb(other))
        )
        _to_system(self, r, g, b)
        return self

    def __iadd__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float]) -> ColorSystem:
        return self.__add__(other)
    def __isub__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float]) -> ColorSystem:
        return self.__sub__(other)
    def __imul__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float]) -> ColorSystem:
        return self.__mul__(other)
    def __ifloordiv__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float]) -> ColorSystem:
        return self.__floordiv__(other)
    def __itruediv__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float]) -> ColorSystem:
        return self.__truediv__(other)
    def __imod__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float]) -> ColorSystem:
        return self.__mod__(other)
    def __ipow__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float]) -> ColorSystem:
        return self.__pow__(other)

    # ------------------------------------------------------------------------------------------------------------------
    # - Comparison Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    def __gt__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float]) -> bool:
        return all(map(
            lambda x, x_: x > x_,
            zip(_to_rgb(self), _to_rgb(other))
        ))
    def __lt__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float]) -> bool:
        return all(map(
            lambda x, x_: x < x_,
            zip(_to_rgb(self), _to_rgb(other))
        ))
    def __eq__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float]) -> bool:
        return all(map(
            lambda x, x_: x == x_,
            zip(_to_rgb(self), _to_rgb(other))
        ))
    def __ne__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float]) -> bool:
        return all(map(
            lambda x, x_: x != x_,
            zip(_to_rgb(self), _to_rgb(other))
        ))
    def __le__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float]) -> bool:
        return all(map(
            lambda x, x_: x <= x_,
            zip(_to_rgb(self), _to_rgb(other))
        ))
    def __ge__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float]) -> bool:
        return all(map(
            lambda x, x_: x >= x_,
            zip(_to_rgb(self), _to_rgb(other))
        ))
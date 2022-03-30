# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from abc import ABC, abstractmethod

# Custom Library

# Custom Packages
from AthenaColor.Functions.BoilerPlate import Constrain

# ----------------------------------------------------------------------------------------------------------------------
# - Support functions -
# ----------------------------------------------------------------------------------------------------------------------
def _to_rgba(color:ColorSystem|_RGBA|_HEXA|int|float|tuple):
    match color:
        case _RGBA() | _HEXA():
            return color.r, color.g, color.b,color.a
        case tuple() if len(color) == 4 and all(map(lambda x: isinstance(x, (int, float)), color)):
            return tuple(Constrain(x, 255) for x in color)
        case int() | float():
            c = Constrain(color, 255)
            return c,c,c,c
        case _:
            return NotImplemented

def _to_system(color:ColorSystem|_RGBA|_HEXA, r:int,g:int,b:int,a:int):
    match color:
        case _RGBA() | _HEXA():
            color.r, color.g, color.b, color.a = r,g,b,a
        case _:
            return NotImplemented

# ----------------------------------------------------------------------------------------------------------------------
# - Various Supported Color Systems -
# ----------------------------------------------------------------------------------------------------------------------
class _RGBA:
    r:int
    g:int
    b:int
    a:int

class _HEXA:
    r:int
    g:int
    b:int
    a:int

# ----------------------------------------------------------------------------------------------------------------------
# - Actual Color System -
# ----------------------------------------------------------------------------------------------------------------------
class ColorSystem(ABC):
    @abstractmethod
    def __str__(self): ...
    @abstractmethod
    def __repr__(self): ...

    # ------------------------------------------------------------------------------------------------------------------
    # - Other Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    def __len__(self):
        return NotImplemented

    # ------------------------------------------------------------------------------------------------------------------
    # - Math Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    def __add__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> ColorSystem:
        r, g, b, a = map(
            (lambda c: c[0] + c[1]) ,
            zip(_to_rgba(self), _to_rgba(other))
        )
        _to_system(self, r, g, b, a)
        return self

    def __sub__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> ColorSystem:
        r, g, b, a = map(
            (lambda c: c[0] - c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        )
        _to_system(self, r, g, b, a)
        return self

    def __mul__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> ColorSystem:
        r, g, b, a = map(
            (lambda c: c[0] * c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        )
        _to_system(self, r, g, b, a)
        return self

    def __floordiv__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> ColorSystem:
        r, g, b, a = map(
            (lambda c: c[0] // c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        )
        _to_system(self, r, g, b, a)
        return self

    def __truediv__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> ColorSystem:
        r, g, b, a = map(
            (lambda c: c[0] / c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        )
        _to_system(self, r, g, b, a)
        return self

    def __mod__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> ColorSystem:
        r, g, b, a = map(
            (lambda c: c[0] % c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        )
        _to_system(self, r, g, b, a)
        return self

    def __pow__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> ColorSystem:
        r, g, b, a = map(
            (lambda c: c[0] ** c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        )
        _to_system(self, r, g, b, a)
        return self

    def __iadd__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> ColorSystem:
        return self.__add__(other)
    def __isub__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> ColorSystem:
        return self.__sub__(other)
    def __imul__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> ColorSystem:
        return self.__mul__(other)
    def __ifloordiv__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> ColorSystem:
        return self.__floordiv__(other)
    def __itruediv__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> ColorSystem:
        return self.__truediv__(other)
    def __imod__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> ColorSystem:
        return self.__mod__(other)
    def __ipow__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> ColorSystem:
        return self.__pow__(other)

    # ------------------------------------------------------------------------------------------------------------------
    # - Comparison Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    def __gt__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> bool:
        return all(map(
            (lambda c: c[0] > c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        ))
    def __lt__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> bool:
        return all(map(
            (lambda c: c[0] < c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        ))
    def __eq__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> bool:
        return all(map(
            (lambda c: c[0] == c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        ))
    def __ne__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> bool:
        return all(map(
            (lambda c: c[0] != c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        ))
    def __le__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> bool:
        return all(map(
            (lambda c: c[0] <= c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        ))
    def __ge__(self, other: ColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> bool:
        return all(map(
            (lambda c: c[0] >= c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        ))
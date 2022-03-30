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
def _to_rgba(color:TransparentColorSystem|_RGBA|_HEXA|int|float|tuple)->tuple[int|float,int|float,int|float,int|float]:
    if isinstance(color, (_RGBA, _HEXA)):
        return color.r, color.g, color.b, color.a
    elif isinstance(color, tuple) and len(color) == 3 and all(map(lambda x: isinstance(x, (int, float)), color)):
        return color
    elif isinstance(color, (int, float)):
        c = Constrain(color, 255)
        return c,c,c,c
    else:
        return NotImplemented

def _to_system(color:TransparentColorSystem|_RGBA|_HEXA, r:int,g:int,b:int,a:int)->tuple[int|float,int|float,int|float,int|float]:
    if isinstance(color, (_RGBA, _HEXA)):
        color.r, color.g, color.b, color.a = r, g, b, a
    else:
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
class TransparentColorSystem(ABC):
    @abstractmethod
    def __str__(self)->str: ...
    @abstractmethod
    def __repr__(self)->str: ...

    # ------------------------------------------------------------------------------------------------------------------
    # - Math Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    def __add__(self, other: TransparentColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> TransparentColorSystem:
        r, g, b, a = map(
            (lambda c: c[0] + c[1]) ,
            zip(_to_rgba(self), _to_rgba(other))
        )
        _to_system(self, r, g, b, a)
        return self

    def __sub__(self, other: TransparentColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> TransparentColorSystem:
        r, g, b, a = map(
            (lambda c: c[0] - c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        )
        _to_system(self, r, g, b, a)
        return self

    def __mul__(self, other: TransparentColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> TransparentColorSystem:
        r, g, b, a = map(
            (lambda c: c[0] * c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        )
        _to_system(self, r, g, b, a)
        return self

    def __floordiv__(self, other: TransparentColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> TransparentColorSystem:
        r, g, b, a = map(
            (lambda c: c[0] // c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        )
        _to_system(self, r, g, b, a)
        return self

    def __truediv__(self, other: TransparentColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> TransparentColorSystem:
        r, g, b, a = map(
            (lambda c: c[0] / c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        )
        _to_system(self, r, g, b, a)
        return self

    def __mod__(self, other: TransparentColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> TransparentColorSystem:
        r, g, b, a = map(
            (lambda c: c[0] % c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        )
        _to_system(self, r, g, b, a)
        return self

    def __pow__(self, other: TransparentColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> TransparentColorSystem:
        r, g, b, a = map(
            (lambda c: c[0] ** c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        )
        _to_system(self, r, g, b, a)
        return self

    def __iadd__(self, other: TransparentColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> TransparentColorSystem:
        return self.__add__(other)
    def __isub__(self, other: TransparentColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> TransparentColorSystem:
        return self.__sub__(other)
    def __imul__(self, other: TransparentColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> TransparentColorSystem:
        return self.__mul__(other)
    def __ifloordiv__(self, other: TransparentColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> TransparentColorSystem:
        return self.__floordiv__(other)
    def __itruediv__(self, other: TransparentColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> TransparentColorSystem:
        return self.__truediv__(other)
    def __imod__(self, other: TransparentColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> TransparentColorSystem:
        return self.__mod__(other)
    def __ipow__(self, other: TransparentColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> TransparentColorSystem:
        return self.__pow__(other)

    # ------------------------------------------------------------------------------------------------------------------
    # - Comparison Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    def __gt__(self, other: TransparentColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> bool:
        return all(map(
            (lambda c: c[0] > c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        ))
    def __lt__(self, other: TransparentColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> bool:
        return all(map(
            (lambda c: c[0] < c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        ))
    def __eq__(self, other: TransparentColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> bool:
        return all(map(
            (lambda c: c[0] == c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        ))
    def __ne__(self, other: TransparentColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> bool:
        return all(map(
            (lambda c: c[0] != c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        ))
    def __le__(self, other: TransparentColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> bool:
        return all(map(
            (lambda c: c[0] <= c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        ))
    def __ge__(self, other: TransparentColorSystem | int | float | tuple[int|float,int|float,int|float,int|float]) -> bool:
        return all(map(
            (lambda c: c[0] >= c[1]),
            zip(_to_rgba(self), _to_rgba(other))
        ))
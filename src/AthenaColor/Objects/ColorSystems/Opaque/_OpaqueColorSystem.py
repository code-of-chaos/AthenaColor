# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from abc import ABC, abstractmethod

# Custom Library

# Custom Packages
from AthenaColor.Functions.ColorTupleConversion import *
from AthenaColor.Functions.BoilerPlate import Constrain

# ----------------------------------------------------------------------------------------------------------------------
# - Support functions -
# ----------------------------------------------------------------------------------------------------------------------
def _to_rgb(color:OpaqueColorSystem|_RGB|_HEX|_CMYK|_HSL|_HSV|int|float|tuple)->tuple[int|float,int|float,int|float]:
    if isinstance(color, (_RGB, _HEX)):
        return color.r, color.g, color.b
    elif isinstance(color, _CMYK):
        return cmyk_to_rgb(color.c, color.m, color.y, color.k)
    elif isinstance(color, _HSL):
        return hsl_to_rgb(color.h, color.s, color.l)
    elif isinstance(color, _HSV):
        return hsl_to_rgb(color.h, color.s, color.v)
    elif isinstance(color, tuple) and len(color) == 3 and all(map(lambda x: isinstance(x, (int, float)),color)):
        return color
    elif isinstance(color, (int, float)):
        c = Constrain(color, 255)
        return c,c,c
    else:
        return NotImplemented

def _to_system(color:OpaqueColorSystem|_RGB|_HEX|_CMYK|_HSL|_HSV, r:int,g:int,b:int)->tuple[int|float,int|float,int|float]:
    if isinstance(color, (_RGB, _HEX)):
        color.r, color.g, color.b = r, g, b
    elif isinstance(color, _CMYK):
        color.c, color.m, color.y, color.k = rgb_to_cmyk(r, g, b)
    elif isinstance(color, _HSL):
        color.h, color.s, color.l = rgb_to_hsl(r, g, b)
    elif isinstance(color, _HSV):
        color.h, color.s, color.v = rgb_to_hsv(r, g, b)
    else:
        return NotImplemented

# ----------------------------------------------------------------------------------------------------------------------
# - Various Supported Color Systems -
# ----------------------------------------------------------------------------------------------------------------------
class _RGB:
    r:int
    g:int
    b:int

class _HEX:
    r:int
    g:int
    b:int

class _CMYK:
    c:float
    m:float
    y:float
    k:float

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
class OpaqueColorSystem(ABC):
    @abstractmethod
    def __str__(self)->str: ...
    @abstractmethod
    def __repr__(self)->str: ...

    # ------------------------------------------------------------------------------------------------------------------
    # - Math Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    def __add__(self, other: OpaqueColorSystem | int | float | tuple[int|float,int|float,int|float]) -> OpaqueColorSystem:
        r,g,b = map(
            (lambda xy: xy[0] + xy[1]),
            zip(_to_rgb(self), _to_rgb(other))
        )
        _to_system(self, r,g,b)
        return self

    def __sub__(self, other: OpaqueColorSystem | int | float | tuple[int|float,int|float,int|float]) -> OpaqueColorSystem:
        r, g, b = map(
            (lambda xy: xy[0] - xy[1]),
            zip(_to_rgb(self), _to_rgb(other))
        )
        _to_system(self, r, g, b)
        return self

    def __mul__(self, other: OpaqueColorSystem | int | float | tuple[int|float,int|float,int|float]) -> OpaqueColorSystem:
        r, g, b = map(
            (lambda xy: xy[0] * xy[1]),
            zip(_to_rgb(self), _to_rgb(other))
        )
        _to_system(self, r, g, b)
        return self

    def __floordiv__(self, other: OpaqueColorSystem | int | float | tuple[int|float,int|float,int|float]) -> OpaqueColorSystem:
        r, g, b = map(
            (lambda xy: xy[0] // xy[1]),
            zip(_to_rgb(self), _to_rgb(other))
        )
        _to_system(self, r, g, b)
        return self

    def __truediv__(self, other: OpaqueColorSystem | int | float | tuple[int|float,int|float,int|float]) -> OpaqueColorSystem:
        r, g, b = map(
            (lambda xy: xy[0] / xy[1]),
            zip(_to_rgb(self), _to_rgb(other))
        )
        _to_system(self, r, g, b)
        return self

    def __mod__(self, other: OpaqueColorSystem | int | float | tuple[int|float,int|float,int|float]) -> OpaqueColorSystem:
        r, g, b = map(
            (lambda xy: xy[0] % xy[1]),
            zip(_to_rgb(self), _to_rgb(other))
        )
        _to_system(self, r, g, b)
        return self

    def __pow__(self, other: OpaqueColorSystem | int | float | tuple[int|float,int|float,int|float]) -> OpaqueColorSystem:
        r, g, b = map(
            (lambda xy: xy[0] ** xy[1]),
            zip(_to_rgb(self), _to_rgb(other))
        )
        _to_system(self, r, g, b)
        return self

    def __iadd__(self, other: OpaqueColorSystem | int | float | tuple[int|float,int|float,int|float]) -> OpaqueColorSystem:
        return self.__add__(other)
    def __isub__(self, other: OpaqueColorSystem | int | float | tuple[int|float,int|float,int|float]) -> OpaqueColorSystem:
        return self.__sub__(other)
    def __imul__(self, other: OpaqueColorSystem | int | float | tuple[int|float,int|float,int|float]) -> OpaqueColorSystem:
        return self.__mul__(other)
    def __ifloordiv__(self, other: OpaqueColorSystem | int | float | tuple[int|float,int|float,int|float]) -> OpaqueColorSystem:
        return self.__floordiv__(other)
    def __itruediv__(self, other: OpaqueColorSystem | int | float | tuple[int|float,int|float,int|float]) -> OpaqueColorSystem:
        return self.__truediv__(other)
    def __imod__(self, other: OpaqueColorSystem | int | float | tuple[int|float,int|float,int|float]) -> OpaqueColorSystem:
        return self.__mod__(other)
    def __ipow__(self, other: OpaqueColorSystem | int | float | tuple[int|float,int|float,int|float]) -> OpaqueColorSystem:
        return self.__pow__(other)

    # ------------------------------------------------------------------------------------------------------------------
    # - Comparison Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    def __gt__(self, other: OpaqueColorSystem | int | float | tuple[int|float,int|float,int|float]) -> bool:
        return all(map(
            (lambda xy: xy[0] > xy[1]),
            zip(_to_rgb(self), _to_rgb(other))
        ))
    def __lt__(self, other: OpaqueColorSystem | int | float | tuple[int|float,int|float,int|float]) -> bool:
        return all(map(
            (lambda xy: xy[0] < xy[1]),
            zip(_to_rgb(self), _to_rgb(other))
        ))
    def __eq__(self, other: OpaqueColorSystem | int | float | tuple[int|float,int|float,int|float]) -> bool:
        return all(map(
            (lambda xy: xy[0] == xy[1]),
            zip(_to_rgb(self), _to_rgb(other))
        ))
    def __ne__(self, other: OpaqueColorSystem | int | float | tuple[int|float,int|float,int|float]) -> bool:
        return all(map(
            (lambda xy: xy[0] != xy[1]),
            zip(_to_rgb(self), _to_rgb(other))
        ))
    def __le__(self, other: OpaqueColorSystem | int | float | tuple[int|float,int|float,int|float]) -> bool:
        return all(map(
            (lambda xy: xy[0] <= xy[1]),
            zip(_to_rgb(self), _to_rgb(other))
        ))
    def __ge__(self, other: OpaqueColorSystem | int | float | tuple[int|float,int|float,int|float]) -> bool:
        return all(map(
            (lambda xy: xy[0] >= xy[1]),
            zip(_to_rgb(self), _to_rgb(other))
        ))
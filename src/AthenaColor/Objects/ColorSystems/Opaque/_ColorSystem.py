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
def _to_rgb(color:OpaqueColorSystem|_RGB|_HEX|_CMYK|_HSL|_HSV|int|float|tuple):
    match color:
        case _RGB(r=r,g=g,b=b) | _HEX(r=r,g=g,b=b):
            return r,g,b
        case _CMYK(c=c,m=m,y=y,k=k):
            return cmyk_to_rgb(c,m,y,k)
        case _HSL(h=h,s=s,l=l):
            return hsl_to_rgb(h,s,l)
        case _HSV(h=h,s=s,v=v):
            return hsv_to_rgb(h,s,v)
        case tuple() if len(color) == 3 and all(map(lambda x: isinstance(x, (int, float)), color)):
            return tuple(Constrain(x, 255) for x in color)
        case int() | float():
            c = Constrain(color, 255)
            return c,c,c
        case _:
            return NotImplemented

def _to_system(color:OpaqueColorSystem|_RGB|_HEX|_CMYK|_HSL|_HSV, r:int,g:int,b:int):
    match color:
        case _RGB() | _HEX():
            color.r, color.g, color.b = r,g,b
        case _CMYK():
            color.c, color.m, color.y, color.k = rgb_to_cmyk(r,g,b)
        case _HSL():
            color.h, color.s, color.l = rgb_to_hsl(r,g,b)
        case _HSV():
            color.h, color.s, color.v = rgb_to_hsv(r,g,b)
        case _:
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
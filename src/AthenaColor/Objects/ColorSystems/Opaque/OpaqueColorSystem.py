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
import AthenaColor.Functions.ColorSystemDunders as CSD

# ----------------------------------------------------------------------------------------------------------------------
# - Support functions -
# ----------------------------------------------------------------------------------------------------------------------
def _to_rgb(color:OpaqueColorSystem|_RGB|_HEX|_CMYK|_HSL|_HSV|int|float|tuple)->tuple:
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

def _to_system(color:OpaqueColorSystem|_RGB|_HEX|_CMYK|_HSL|_HSV, r:int,g:int,b:int)->tuple:
    if isinstance(color, (_RGB, _HEX)):
        return r, g, b
    elif isinstance(color, _CMYK):
        return rgb_to_cmyk(r, g, b)
    elif isinstance(color, _HSL):
        return rgb_to_hsl(r, g, b)
    elif isinstance(color, _HSV):
        return rgb_to_hsv(r, g, b)
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
    def __init__(self, *_):...
    @abstractmethod
    def __str__(self)->str: ...
    @abstractmethod
    def __repr__(self)->str: ...

    @abstractmethod
    def _export(self) -> tuple:...

    # ------------------------------------------------------------------------------------------------------------------
    # - Math Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    def __add__(self, other: OpaqueColorSystem | int | float | tuple) -> OpaqueColorSystem:
        """
        Math Dunder which executes an addition operator on the RGB notations of its own and the other class.
        Reassembles the RGB values to the current object's needed values
        """
        if type(self) is type(other):
            return type(self)(*CSD.add(self._export(),other._export()))
        else:
            return type(self)(*_to_system(self, *CSD.add(_to_rgb(self),_to_rgb(other))))


    def __sub__(self, other: OpaqueColorSystem | int | float | tuple) -> OpaqueColorSystem:
        """
        Math Dunder which executes a subtraction operator on the RGB notations of its own and the other class.
        Reassembles the RGB values to the current object's needed values
        """
        if type(self) is type(other):
            return type(self)(*CSD.sub(self._export(),other._export()))
        else:
            return type(self)(*_to_system(self, *CSD.sub(_to_rgb(self),_to_rgb(other))))

    def __mul__(self, other: OpaqueColorSystem | int | float | tuple) -> OpaqueColorSystem:
        """
        Math Dunder which executes a multiplication operator on the RGB notations of its own and the other class.
        Reassembles the RGB values to the current object's needed values
        """
        if type(self) is type(other):
            return type(self)(*CSD.mul(self._export(),other._export()))
        else:
            return type(self)(*_to_system(self, *CSD.mul(_to_rgb(self),_to_rgb(other))))

    def __floordiv__(self, other: OpaqueColorSystem | int | float | tuple) -> OpaqueColorSystem:
        """
        Math Dunder which executes a floor division operator on the RGB notations of its own and the other class.
        Reassembles the RGB values to the current object's needed values
        """
        if type(self) is type(other):
            return type(self)(*CSD.floordiv(self._export(),other._export()))
        else:
            return type(self)(*_to_system(self, *CSD.floordiv(_to_rgb(self),_to_rgb(other))))

    def __truediv__(self, other: OpaqueColorSystem | int | float | tuple) -> OpaqueColorSystem:
        """
        Math Dunder which executes a division operator on the RGB notations of its own and the other class.
        Reassembles the RGB values to the current object's needed values
        """
        if type(self) is type(other):
            return type(self)(*CSD.truediv(self._export(),other._export()))
        else:
            return type(self)(*_to_system(self, *CSD.truediv(_to_rgb(self),_to_rgb(other))))

    def __mod__(self, other: OpaqueColorSystem | int | float | tuple) -> OpaqueColorSystem:
        """
        Math Dunder which executes a modulo operator on the RGB notations of its own and the other class.
        Reassembles the RGB values to the current object's needed values
        """
        if type(self) is type(other):
            return type(self)(*CSD.mod(self._export(),other._export()))
        else:
            return type(self)(*_to_system(self, *CSD.mod(_to_rgb(self),_to_rgb(other))))

    def __pow__(self, other: OpaqueColorSystem | int | float | tuple) -> OpaqueColorSystem:
        """
        Math Dunder which executes a power operator on the RGB notations of its own and the other class.
        Reassembles the RGB values to the current object's needed values
        """
        if type(self) is type(other):
            return type(self)(*CSD.pow(self._export(),other._export()))
        else:
            return type(self)(*_to_system(self, *CSD.pow(_to_rgb(self),_to_rgb(other))))

    def __iadd__(self, other: OpaqueColorSystem | int | float | tuple) -> OpaqueColorSystem:
        return self.__add__(other)
    def __isub__(self, other: OpaqueColorSystem | int | float | tuple) -> OpaqueColorSystem:
        return self.__sub__(other)
    def __imul__(self, other: OpaqueColorSystem | int | float | tuple) -> OpaqueColorSystem:
        return self.__mul__(other)
    def __ifloordiv__(self, other: OpaqueColorSystem | int | float | tuple) -> OpaqueColorSystem:
        return self.__floordiv__(other)
    def __itruediv__(self, other: OpaqueColorSystem | int | float | tuple) -> OpaqueColorSystem:
        return self.__truediv__(other)
    def __imod__(self, other: OpaqueColorSystem | int | float | tuple) -> OpaqueColorSystem:
        return self.__mod__(other)
    def __ipow__(self, other: OpaqueColorSystem | int | float | tuple) -> OpaqueColorSystem:
        return self.__pow__(other)

    # ------------------------------------------------------------------------------------------------------------------
    # - Comparison Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    def __gt__(self, other: OpaqueColorSystem | int | float | tuple) -> bool:
        """
        Comparison Dunder which compares the RGB notations of its own and the other class against eachother.
        Tests for greater than the other
        """
        if type(self) is type(other):
            return CSD.gt(self._export(),other._export())
        else:
            return CSD.gt(_to_rgb(self),_to_rgb(other))

    def __lt__(self, other: OpaqueColorSystem | int | float | tuple) -> bool:
        """
        Comparison Dunder which compares the RGB notations of its own and the other class against eachother.
        Tests for smaller than the other
        """
        if type(self) is type(other):
            return CSD.lt(self._export(),other._export())
        else:
            return CSD.lt(_to_rgb(self),_to_rgb(other))

    def __eq__(self, other: OpaqueColorSystem | int | float | tuple) -> bool:
        """
        Comparison Dunder which compares the RGB notations of its own and the other class against eachother.
        Tests for equality to the other
        """
        if type(self) is type(other):
            return CSD.eq(self._export(),other._export())
        else:
            return CSD.eq(_to_rgb(self),_to_rgb(other))

    def __ne__(self, other: OpaqueColorSystem | int | float | tuple) -> bool:
        """
        Comparison Dunder which compares the RGB notations of its own and the other class against eachother.
        Tests for inequality to the other
        """
        if type(self) is type(other):
            return CSD.ne(self._export(),other._export())
        else:
            return CSD.ne(_to_rgb(self),_to_rgb(other))

    def __le__(self, other: OpaqueColorSystem | int | float | tuple) -> bool:
        """
        Comparison Dunder which compares the RGB notations of its own and the other class against eachother.
        Tests for smaller than or equality to the other
        """
        if type(self) is type(other):
            return CSD.le(self._export(),other._export())
        else:
            return CSD.le(_to_rgb(self),_to_rgb(other))

    def __ge__(self, other: OpaqueColorSystem | int | float | tuple) -> bool:
        """
        Comparison Dunder which compares the RGB notations of its own and the other class against eachother.
        Tests for greater than or equality to the other
        """
        if type(self) is type(other):
            return CSD.ge(self._export(),other._export())
        else:
            return CSD.ge(_to_rgb(self),_to_rgb(other))
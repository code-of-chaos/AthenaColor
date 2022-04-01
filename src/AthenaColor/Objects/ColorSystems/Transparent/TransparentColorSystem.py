# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from abc import ABC, abstractmethod

# Custom Library

# Custom Packages
from AthenaColor.Functions.BoilerPlate import Constrain
import AthenaColor.Functions.ColorSystemDunders as CSD

# ----------------------------------------------------------------------------------------------------------------------
# - Support functions -
# ----------------------------------------------------------------------------------------------------------------------
def _to_rgba(color:TransparentColorSystem|_RGBA|_HEXA|int|float|tuple)->tuple:
    if isinstance(color, (_RGBA, _HEXA)):
        return color.r, color.g, color.b, color.a
    elif isinstance(color, tuple) and len(color) == 3 and all(map(lambda x: isinstance(x, (int, float)), color)):
        return color
    elif isinstance(color, (int, float)):
        c = Constrain(color, 255)
        return c,c,c,c
    else:
        return NotImplemented

def _to_system(color:TransparentColorSystem|_RGBA|_HEXA, r:int,g:int,b:int,a:int)->tuple:
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
    def __init__(self, *_):
        # no 'OpaqueColorSystem' can be created on its own
        raise PermissionError
    @abstractmethod
    def __str__(self)->str:
        """
        Returns a string with the various elements in a ';' separated string.
        """

    @abstractmethod
    def __repr__(self)->str:
        """
        Returns a string, starting with the name of the class, followed by the various elements.
        example: 'RGB(r=255,g=255,b=255)'
        """

    @abstractmethod
    def _export(self) -> tuple:
        """
        'Private' method of a color object. Used internally in dunder operations.
        Done to not need specific dunders for each separate color class.
        """

    # ------------------------------------------------------------------------------------------------------------------
    # - Math Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    def __add__(self, other: TransparentColorSystem | int | float | tuple) -> TransparentColorSystem:
        """
        Math Dunder which executes an ADDITION operator between the left- and righthand side of the operation.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        The returned object will be a new instance of the lefthand-object's class.
        """
        if type(self) is type(other):
            return type(self)(*CSD.add(self._export(),other._export()))
        else:
            return type(self)(*_to_system(self, *CSD.add(_to_rgba(self),_to_rgba(other))))

    def __sub__(self, other: TransparentColorSystem | int | float | tuple) -> TransparentColorSystem:
        """
        Math Dunder which executes an SUBTRACTION operator between the left- and righthand side of the operation.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        The returned object will be a new instance of the lefthand-object's class.
        """
        if type(self) is type(other):
            return type(self)(*CSD.sub(self._export(), other._export()))
        else:
            return type(self)(*_to_system(self, *CSD.sub(_to_rgba(self),_to_rgba(other))))

    def __mul__(self, other: TransparentColorSystem | int | float | tuple) -> TransparentColorSystem:
        """
        Math Dunder which executes an MULTIPLICATION operator between the left- and righthand side of the operation.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        The returned object will be a new instance of the lefthand-object's class.
        """
        if type(self) is type(other):
            return type(self)(*CSD.mul(self._export(), other._export()))
        else:
            return type(self)(*_to_system(self, *CSD.mul(_to_rgba(self),_to_rgba(other))))

    def __floordiv__(self, other: TransparentColorSystem | int | float | tuple) -> TransparentColorSystem:
        """
        Math Dunder which executes an FLOOR DIVISION operator between the left- and righthand side of the operation.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        The returned object will be a new instance of the lefthand-object's class.
        """
        if type(self) is type(other):
            return type(self)(*CSD.floordiv(self._export(), other._export()))
        else:
            return type(self)(*_to_system(self, *CSD.floordiv(_to_rgba(self),_to_rgba(other))))

    def __truediv__(self, other: TransparentColorSystem | int | float | tuple) -> TransparentColorSystem:
        """
        Math Dunder which executes an DIVISION operator between the left- and righthand side of the operation.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        The returned object will be a new instance of the lefthand-object's class.
        """
        if type(self) is type(other):
            return type(self)(*CSD.truediv(self._export(), other._export()))
        else:
            return type(self)(*_to_system(self, *CSD.truediv(_to_rgba(self),_to_rgba(other))))

    def __mod__(self, other: TransparentColorSystem | int | float | tuple) -> TransparentColorSystem:
        """
        Math Dunder which executes an MODULO operator between the left- and righthand side of the operation.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        The returned object will be a new instance of the lefthand-object's class.
        """
        if type(self) is type(other):
            return type(self)(*CSD.mod(self._export(), other._export()))
        else:
            return type(self)(*_to_system(self, *CSD.mod(_to_rgba(self),_to_rgba(other))))

    def __pow__(self, other: TransparentColorSystem | int | float | tuple) -> TransparentColorSystem:
        """
        Math Dunder which executes an POWER operator between the left- and righthand side of the operation.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        The returned object will be a new instance of the lefthand-object's class.
        """
        if type(self) is type(other):
            return type(self)(*CSD.pow(self._export(), other._export()))
        else:
            return type(self)(*_to_system(self, *CSD.pow(_to_rgba(self),_to_rgba(other))))

    def __iadd__(self, other: TransparentColorSystem | int | float | tuple) -> TransparentColorSystem:
        return self.__add__(other)
    def __isub__(self, other: TransparentColorSystem | int | float | tuple) -> TransparentColorSystem:
        return self.__sub__(other)
    def __imul__(self, other: TransparentColorSystem | int | float | tuple) -> TransparentColorSystem:
        return self.__mul__(other)
    def __ifloordiv__(self, other: TransparentColorSystem | int | float | tuple) -> TransparentColorSystem:
        return self.__floordiv__(other)
    def __itruediv__(self, other: TransparentColorSystem | int | float | tuple) -> TransparentColorSystem:
        return self.__truediv__(other)
    def __imod__(self, other: TransparentColorSystem | int | float | tuple) -> TransparentColorSystem:
        return self.__mod__(other)
    def __ipow__(self, other: TransparentColorSystem | int | float | tuple) -> TransparentColorSystem:
        return self.__pow__(other)

    # ------------------------------------------------------------------------------------------------------------------
    # - Comparison Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    def __gt__(self, other: TransparentColorSystem | int | float | tuple) -> bool:
        """
        Comparison Dunder which compares for GREATER THAN.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        """
        if type(self) is type(other):
            return CSD.gt(self._export(), other._export())
        else:
            return CSD.gt(_to_rgba(self), _to_rgba(other))

    def __lt__(self, other: TransparentColorSystem | int | float | tuple) -> bool:
        """
        Comparison Dunder which compares for SMALLER THAN.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        """
        if type(self) is type(other):
            return CSD.lt(self._export(), other._export())
        else:
            return CSD.lt(_to_rgba(self), _to_rgba(other))

    def __eq__(self, other: TransparentColorSystem | int | float | tuple) -> bool:
        """
        Comparison Dunder which compares for EQUALITY.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        """
        if type(self) is type(other):
            return CSD.eq(self._export(), other._export())
        else:
            return CSD.eq(_to_rgba(self), _to_rgba(other))

    def __ne__(self, other: TransparentColorSystem | int | float | tuple) -> bool:
        """
        Comparison Dunder which compares for INEQUALITY.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        """
        if type(self) is type(other):
            return CSD.ne(self._export(), other._export())
        else:
            return CSD.ne(_to_rgba(self), _to_rgba(other))

    def __le__(self, other: TransparentColorSystem | int | float | tuple) -> bool:
        """
        Comparison Dunder which compares for SMALLER OR EQUAL TO.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        """
        if type(self) is type(other):
            return CSD.le(self._export(), other._export())
        else:
            return CSD.le(_to_rgba(self), _to_rgba(other))

    def __ge__(self, other: TransparentColorSystem | int | float | tuple) -> bool:
        """
        Comparison Dunder which compares for GREATER OR EQUAL TO.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        """
        if type(self) is type(other):
            return CSD.ge(self._export(), other._export())
        else:
            return CSD.ge(_to_rgba(self), _to_rgba(other))
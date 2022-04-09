# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Callable,Union

# Custom Library

# Custom Packages
import AthenaColor.v3_08.Functions.ColorSystemDunders as CSD
from AthenaColor.v3_08.Objects.ColorSystems._BASE_ColorSystem import (
    BASE_RGBA as _RGBA,
    BASE_RGB as _RGB,
    BASE_CMYK as _CMYK,
    BASE_HEX as _HEX,
    BASE_HSV as _HSV,
    BASE_HSL as _HSL,
    BASE_HEXA as _HEXA,
)
from AthenaColor.v3_08.Functions.ColorTupleConversion import *
from AthenaColor.v3_08.InitClass import init

# ----------------------------------------------------------------------------------------------------------------------
# - Support Methods -
# ----------------------------------------------------------------------------------------------------------------------
def dunder_func(func:Callable,left:ColorSystem,right:Union[ColorSystem,int,float,tuple]):
    if type(left) is type(right):
        return func(left.export(), right.export())
    elif isinstance(right, ColorSystem):
        return func(left.export(), map_color(left, right))
    elif isinstance(right, (int, float)):
        return func(left.export(), (right,) * len(left.export()))
    elif isinstance(right, tuple) and len(right) == len(left.export()):
        return func(left.export(), right)
    else:
        return NotImplemented

def map_color(left:ColorSystem,right:ColorSystem) -> tuple:
    if isinstance(left, (_RGB,_HEX,)):
        if isinstance(right, (_RGB,_HEX)):
            return right.export()
        elif isinstance(right,_HSL):
            return hsl_to_rgb(*right.export())
        elif isinstance(right,_HSV):
            return hsv_to_rgb(*right.export())
        elif isinstance(right,_CMYK):
            return cmyk_to_rgb(*right.export())
        elif isinstance(right, (_RGBA,_HEXA)):
            return right.export()[:-1]

    elif isinstance(left, _HSL):
        if isinstance(right, (_RGB,_HEX)):
            return rgb_to_hsl(*right.export())
        elif isinstance(right,_HSL):
            return right.export()
        elif isinstance(right,_HSV):
            return hsv_to_hsl(*right.export())
        elif isinstance(right,_CMYK):
            return cmyk_to_hsl(*right.export())
        elif isinstance(right, (_RGBA,_HEXA)):
            return rgb_to_hsl(*right.export()[:-1])

    elif isinstance(left, _HSV):
        if isinstance(right, (_RGB,_HEX)):
            return rgb_to_hsv(*right.export())
        elif isinstance(right,_HSL):
            return hsv_to_hsl(*right.export())
        elif isinstance(right,_HSV):
            return right.export()
        elif isinstance(right,_CMYK):
            return cmyk_to_hsv(*right.export())
        elif isinstance(right, (_RGBA,_HEXA)):
            return rgb_to_hsv(*right.export()[:-1])

    elif isinstance(left, _CMYK):
        if isinstance(right, (_RGB,_HEX)):
            return rgb_to_cmyk(*right.export())
        elif isinstance(right,_HSL):
            return hsl_to_cmyk(*right.export())
        elif isinstance(right,_HSV):
            return hsv_to_cmyk(*right.export())
        elif isinstance(right,_CMYK):
            return right.export()
        elif isinstance(right, (_RGBA,_HEXA)):
            return rgb_to_cmyk(*right.export()[:-1])

    elif isinstance(left, (_RGBA,_HEXA)):
        if isinstance(right, (_RGB,_HEX)):
            return right.export(), init.transparent_default_float
        elif isinstance(right,_HSL):
            return hsl_to_rgb(*right.export()), init.transparent_default_float
        elif isinstance(right,_HSV):
            return hsv_to_rgb(*right.export()), init.transparent_default_float
        elif isinstance(right,_CMYK):
            return cmyk_to_rgb(*right.export()), init.transparent_default_float
        elif isinstance(right, (_RGBA,_HEXA)):
            return right.export()

    # If nothing has matched, this will return ->
    return NotImplemented

# ----------------------------------------------------------------------------------------------------------------------
# - Actual Color System -
# ----------------------------------------------------------------------------------------------------------------------
class ColorSystem(ABC):
    @abstractmethod
    def __init__(self, *_):
        # no 'ColorSystem' can be created on its own
        raise PermissionError

    def __str__(self)->str:
        """
        Returns a string with the various color system elements in a ';' separated string.
        """
        return ";".join(str(c) for c in self.export())

    @abstractmethod
    def __repr__(self)->str:
        """
        Returns a string, starting with the name of the class, followed by the various elements.
        example: 'RGB(r=255,g=255,b=255)'
        """

    @abstractmethod
    def export(self) -> tuple:
        """
        Returns all the object's color system elements.
        Used internally in dunder operations.
        Done to not need specific dunders for each separate color class.
        """

    # ------------------------------------------------------------------------------------------------------------------
    # - Math Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    # noinspection PyTypeChecker
    def __add__(self, other: Union[ColorSystem,int,float,tuple]) -> ColorSystem:
        """
        Math Dunder which executes an ADDITION operator between the left- and right-hand side of the operation.
        The returned object will be a new instance of the left-hand object's class.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return type(self)(*dunder_func(func=CSD.add, left=self, right=other))

    # noinspection PyTypeChecker
    def __sub__(self, other: Union[ColorSystem,int,float,tuple]) -> ColorSystem:
        """
        Math Dunder which executes an SUBTRACTION operator between the left- and right-hand side of the operation.
        The returned object will be a new instance of the left-hand object's class.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return type(self)(*dunder_func(func=CSD.sub, left=self, right=other))

    # noinspection PyTypeChecker
    def __mul__(self, other: Union[ColorSystem,int,float,tuple]) -> ColorSystem:
        """
        Math Dunder which executes an MULTIPLICATION operator between the left- and right-hand side of the operation.
        The returned object will be a new instance of the left-hand object's class.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return type(self)(*dunder_func(func=CSD.mul, left=self, right=other))

    # noinspection PyTypeChecker
    def __floordiv__(self, other: Union[ColorSystem,int,float,tuple]) -> ColorSystem:
        """
        Math Dunder which executes an FLOOR DIVISION operator between the left- and right-hand side of the operation.
        The returned object will be a new instance of the left-hand object's class.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return type(self)(*dunder_func(func=CSD.floordiv, left=self, right=other))

    # noinspection PyTypeChecker
    def __truediv__(self, other: Union[ColorSystem,int,float,tuple]) -> ColorSystem:
        """
        Math Dunder which executes an DIVISION operator between the left- and right-hand side of the operation.
        The returned object will be a new instance of the left-hand object's class.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return type(self)(*dunder_func(func=CSD.truediv, left=self, right=other))

    # noinspection PyTypeChecker
    def __mod__(self, other: Union[ColorSystem,int,float,tuple]) -> ColorSystem:
        """
        Math Dunder which executes an MODULO operator between the left- and right-hand side of the operation.
        The returned object will be a new instance of the left-hand object's class.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return type(self)(*dunder_func(func=CSD.mod, left=self, right=other))

    # noinspection PyTypeChecker
    def __pow__(self, other: Union[ColorSystem,int,float,tuple]) -> ColorSystem:
        """
        Math Dunder which executes an POWER operator between the left- and right-hand side of the operation.
        The returned object will be a new instance of the left-hand object's class.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return type(self)(*dunder_func(func=CSD.pow, left=self, right=other))

    def __iadd__(self, other: Union[ColorSystem,int,float,tuple]) -> ColorSystem:
        return self.__add__(other)
    def __isub__(self, other: Union[ColorSystem,int,float,tuple]) -> ColorSystem:
        return self.__sub__(other)
    def __imul__(self, other: Union[ColorSystem,int,float,tuple]) -> ColorSystem:
        return self.__mul__(other)
    def __ifloordiv__(self, other: Union[ColorSystem,int,float,tuple]) -> ColorSystem:
        return self.__floordiv__(other)
    def __itruediv__(self, other: Union[ColorSystem,int,float,tuple]) -> ColorSystem:
        return self.__truediv__(other)
    def __imod__(self, other: Union[ColorSystem,int,float,tuple]) -> ColorSystem:
        return self.__mod__(other)
    def __ipow__(self, other: Union[ColorSystem,int,float,tuple]) -> ColorSystem:
        return self.__pow__(other)

    # ------------------------------------------------------------------------------------------------------------------
    # - Comparison Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    # noinspection PyTypeChecker
    def __gt__(self, other: Union[ColorSystem,int,float,tuple]) -> bool:
        """
        Comparison Dunder which compares for GREATER THAN.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return dunder_func(func=CSD.gt,left=self,right=other)

    # noinspection PyTypeChecker
    def __lt__(self, other: Union[ColorSystem,int,float,tuple]) -> bool:
        """
        Comparison Dunder which compares for SMALLER THAN.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return dunder_func(func=CSD.lt,left=self,right=other)

    # noinspection PyTypeChecker
    def __eq__(self, other: Union[ColorSystem,int,float,tuple]) -> bool:
        """
        Comparison Dunder which compares for EQUALITY.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return dunder_func(func=CSD.eq,left=self,right=other)

    # noinspection PyTypeChecker
    def __ne__(self, other: Union[ColorSystem,int,float,tuple]) -> bool:
        """
        Comparison Dunder which compares for INEQUALITY.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return dunder_func(func=CSD.ne,left=self,right=other)

    # noinspection PyTypeChecker
    def __le__(self, other: Union[ColorSystem,int,float,tuple]) -> bool:
        """
        Comparison Dunder which compares for SMALLER OR EQUAL TO.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return dunder_func(func=CSD.le,left=self,right=other)

    # noinspection PyTypeChecker
    def __ge__(self, other: Union[ColorSystem,int,float,tuple]) -> bool:
        """
        Comparison Dunder which compares for GREATER OR EQUAL TO.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return dunder_func(func=CSD.ge,left=self,right=other)
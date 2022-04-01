# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Callable

# Custom Library

# Custom Packages
import AthenaColor.Functions.ColorSystemDunders as CSD
from ._Bases import (
    _RGBA,
    _RGB,
    _CMYK,
    _HEX,
    _HSV,
    _HSL,
    _HEXA,
)
from AthenaColor.Functions.ColorTupleConversion import *
from AthenaColor import init

# ----------------------------------------------------------------------------------------------------------------------
# - Support Methods -
# ----------------------------------------------------------------------------------------------------------------------
# noinspection PyProtectedMember
def calculation_dunder(func:Callable,left:ColorSystem,right:ColorSystem|int|float|tuple) -> ColorSystem:
    if type(left) is type(right):
        return type(left)(*func(left,right))
    elif isinstance(right, ColorSystem):
        return type(left)(*func(left._export(),map_color(left,right)))
    elif isinstance(right, (int, float)):
        return type(left)(*func(left._export(),(right,)*len(left._export())))
    elif isinstance(right, tuple) and len(right) == len(left._export()):
        return type(left)(*func(left._export(),right))
    else:
        return NotImplemented

# noinspection PyProtectedMember
def comparison_dunder(func:Callable,left:ColorSystem,right:ColorSystem|int|float|tuple) -> bool:
    if type(left) is type(right):
        return func(left._export(), right._export())
    elif isinstance(right, ColorSystem):
        return func(left._export(),map_color(left,right))
    elif isinstance(right, (int, float)):
        return func(left._export(), (right,)*len(left._export()))
    elif isinstance(right, tuple) and len(right) == len(left._export()):
        return func(left._export(), right)
    else:
        return NotImplemented

# noinspection PyProtectedMember
def map_color(left:ColorSystem,right:ColorSystem) -> tuple:
    if isinstance(left, (_RGB,_HEX,)):
        if isinstance(right, (_RGB,_HEX)):
            return right._export()
        elif isinstance(right,_HSL):
            return hsl_to_rgb(*right._export())
        elif isinstance(right,_HSV):
            return hsv_to_rgb(*right._export())
        elif isinstance(right,_CMYK):
            return cmyk_to_rgb(*right._export())
        elif isinstance(right, (_RGBA,_HEXA)):
            return right._export()[:-1]

    elif isinstance(left, _HSL):
        if isinstance(right, (_RGB,_HEX)):
            return rgb_to_hsl(*right._export())
        elif isinstance(right,_HSL):
            return right._export()
        elif isinstance(right,_HSV):
            return hsv_to_hsl(*right._export())
        elif isinstance(right,_CMYK):
            return cmyk_to_hsl(*right._export())
        elif isinstance(right, (_RGBA,_HEXA)):
            return rgb_to_hsl(*right._export()[:-1])

    elif isinstance(left, _HSV):
        if isinstance(right, (_RGB,_HEX)):
            return rgb_to_hsv(*right._export())
        elif isinstance(right,_HSL):
            return hsv_to_hsl(*right._export())
        elif isinstance(right,_HSV):
            return right._export()
        elif isinstance(right,_CMYK):
            return cmyk_to_hsv(*right._export())
        elif isinstance(right, (_RGBA,_HEXA)):
            return rgb_to_hsv(*right._export()[:-1])

    elif isinstance(left, _CMYK):
        if isinstance(right, (_RGB,_HEX)):
            return rgb_to_cmyk(*right._export())
        elif isinstance(right,_HSL):
            return hsl_to_cmyk(*right._export())
        elif isinstance(right,_HSV):
            return hsv_to_cmyk(*right._export())
        elif isinstance(right,_CMYK):
            return right._export()
        elif isinstance(right, (_RGBA,_HEXA)):
            return rgb_to_cmyk(*right._export()[:-1])

    elif isinstance(left, (_RGBA,_HEXA)):
        if isinstance(right, (_RGB,_HEX)):
            return right._export(), init.transparent_default_float
        elif isinstance(right,_HSL):
            return hsl_to_rgb(*right._export()), init.transparent_default_float
        elif isinstance(right,_HSV):
            return hsv_to_rgb(*right._export()), init.transparent_default_float
        elif isinstance(right,_CMYK):
            return cmyk_to_rgb(*right._export()), init.transparent_default_float
        elif isinstance(right, (_RGBA,_HEXA)):
            return right._export()

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
    # noinspection PyTypeChecker
    def __add__(self, other: ColorSystem | int | float | tuple) -> ColorSystem:
        """
        Math Dunder which executes an ADDITION operator between the left- and righthand side of the operation.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        The returned object will be a new instance of the lefthand-object's class.
        """
        return calculation_dunder(func=CSD.add, left=self, right=other)

    # noinspection PyTypeChecker
    def __sub__(self, other: ColorSystem | int | float | tuple) -> ColorSystem:
        """
        Math Dunder which executes an SUBTRACTION operator between the left- and righthand side of the operation.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        The returned object will be a new instance of the lefthand-object's class.
        """
        return calculation_dunder(func=CSD.sub, left=self, right=other)

    # noinspection PyTypeChecker
    def __mul__(self, other: ColorSystem | int | float | tuple) -> ColorSystem:
        """
        Math Dunder which executes an MULTIPLICATION operator between the left- and righthand side of the operation.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        The returned object will be a new instance of the left-hand object's class.
        """
        return calculation_dunder(func=CSD.mul, left=self, right=other)

    # noinspection PyTypeChecker
    def __floordiv__(self, other: ColorSystem | int | float | tuple) -> ColorSystem:
        """
        Math Dunder which executes an FLOOR DIVISION operator between the left- and righthand side of the operation.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        The returned object will be a new instance of the lefthand-object's class.
        """
        return calculation_dunder(func=CSD.floordiv, left=self, right=other)

    # noinspection PyTypeChecker
    def __truediv__(self, other: ColorSystem | int | float | tuple) -> ColorSystem:
        """
        Math Dunder which executes an DIVISION operator between the left- and righthand side of the operation.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        The returned object will be a new instance of the lefthand-object's class.
        """
        return calculation_dunder(func=CSD.truediv, left=self, right=other)

    # noinspection PyTypeChecker
    def __mod__(self, other: ColorSystem | int | float | tuple) -> ColorSystem:
        """
        Math Dunder which executes an MODULO operator between the left- and righthand side of the operation.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        The returned object will be a new instance of the lefthand-object's class.
        """
        return calculation_dunder(func=CSD.mod, left=self, right=other)

    # noinspection PyTypeChecker
    def __pow__(self, other: ColorSystem | int | float | tuple) -> ColorSystem:
        """
        Math Dunder which executes an POWER operator between the left- and righthand side of the operation.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        The returned object will be a new instance of the lefthand-object's class.
        """
        return calculation_dunder(func=CSD.pow, left=self, right=other)

    def __iadd__(self, other: ColorSystem | int | float | tuple) -> ColorSystem:
        return self.__add__(other)
    def __isub__(self, other: ColorSystem | int | float | tuple) -> ColorSystem:
        return self.__sub__(other)
    def __imul__(self, other: ColorSystem | int | float | tuple) -> ColorSystem:
        return self.__mul__(other)
    def __ifloordiv__(self, other: ColorSystem | int | float | tuple) -> ColorSystem:
        return self.__floordiv__(other)
    def __itruediv__(self, other: ColorSystem | int | float | tuple) -> ColorSystem:
        return self.__truediv__(other)
    def __imod__(self, other: ColorSystem | int | float | tuple) -> ColorSystem:
        return self.__mod__(other)
    def __ipow__(self, other: ColorSystem | int | float | tuple) -> ColorSystem:
        return self.__pow__(other)

    # ------------------------------------------------------------------------------------------------------------------
    # - Comparison Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    # noinspection PyTypeChecker
    def __gt__(self, other: ColorSystem | int | float | tuple) -> bool:
        """
        Comparison Dunder which compares for GREATER THAN.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        """
        return calculation_dunder(func=CSD.gt,left=self,right=other)

    # noinspection PyTypeChecker
    def __lt__(self, other: ColorSystem | int | float | tuple) -> bool:
        """
        Comparison Dunder which compares for SMALLER THAN.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        """
        return calculation_dunder(func=CSD.lt,left=self,right=other)

    # noinspection PyTypeChecker
    def __eq__(self, other: ColorSystem | int | float | tuple) -> bool:
        """
        Comparison Dunder which compares for EQUALITY.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        """
        return calculation_dunder(func=CSD.eq,left=self,right=other)

    # noinspection PyTypeChecker
    def __ne__(self, other: ColorSystem | int | float | tuple) -> bool:
        """
        Comparison Dunder which compares for INEQUALITY.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        """
        return calculation_dunder(func=CSD.ne,left=self,right=other)

    # noinspection PyTypeChecker
    def __le__(self, other: ColorSystem | int | float | tuple) -> bool:
        """
        Comparison Dunder which compares for SMALLER OR EQUAL TO.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        """
        return calculation_dunder(func=CSD.le,left=self,right=other)

    # noinspection PyTypeChecker
    def __ge__(self, other: ColorSystem | int | float | tuple) -> bool:
        """
        Comparison Dunder which compares for GREATER OR EQUAL TO.
        If the two sides of the operation are NOT of the same type, it will convert both types to an RGB format.
        """
        return calculation_dunder(func=CSD.ge,left=self,right=other)
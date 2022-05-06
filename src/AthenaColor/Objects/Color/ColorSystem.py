# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Callable, Tuple
# Custom Library

# Custom Packages
import AthenaColor.Functions.DunderFunctions as CSD
from AthenaColor.Objects.Color.ColorTupleConversion import *
from AthenaColor.InitClass import init
from AthenaColor.Functions.Constraints import Constrain
from AthenaColor.Functions.General import RoundHalfUp,RoundToDecimals
from AthenaColor.Functions.General import StrictType

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = [
    "ColorSystem", "RGB", "RGBA", "HEX", "HEXA", "HSV", "HSL", "CMYK"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Support Methods -
# ----------------------------------------------------------------------------------------------------------------------
def dunder_func(func:Callable,left:ColorSystem,right:ColorSystem|int|float|tuple):
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
    if isinstance(left, (RGB,HEX,)):
        if isinstance(right, (RGB,HEX)):
            return right.export()
        elif isinstance(right,HSL):
            return hsl_to_rgb(*right.export())
        elif isinstance(right,HSV):
            return hsv_to_rgb(*right.export())
        elif isinstance(right,CMYK):
            return cmyk_to_rgb(*right.export())
        elif isinstance(right, (RGBA,HEXA)):
            return (*right.export()[:-1],)

    elif isinstance(left, HSL):
        if isinstance(right, (RGB,HEX)):
            return rgb_to_hsl(*right.export())
        elif isinstance(right,HSL):
            return (*right.export(),)
        elif isinstance(right,HSV):
            return hsv_to_hsl(*right.export())
        elif isinstance(right,CMYK):
            return cmyk_to_hsl(*right.export())
        elif isinstance(right, (RGBA,HEXA)):
            return rgb_to_hsl(*right.export()[:-1])

    elif isinstance(left, HSV):
        if isinstance(right, (RGB,HEX)):
            return rgb_to_hsv(*right.export())
        elif isinstance(right,HSL):
            return hsl_to_hsv(*right.export())
        elif isinstance(right,HSV):
            return (*right.export(),)
        elif isinstance(right,CMYK):
            return cmyk_to_hsv(*right.export())
        elif isinstance(right, (RGBA,HEXA)):
            return rgb_to_hsv(*right.export()[:-1])

    elif isinstance(left, CMYK):
        if isinstance(right, (RGB,HEX)):
            return rgb_to_cmyk(*right.export())
        elif isinstance(right,HSL):
            return hsl_to_cmyk(*right.export())
        elif isinstance(right,HSV):
            return hsv_to_cmyk(*right.export())
        elif isinstance(right,CMYK):
            return (*right.export(),)
        elif isinstance(right, (RGBA,HEXA)):
            return rgb_to_cmyk(*right.export()[:-1])

    elif isinstance(left, (RGBA,HEXA)):
        if isinstance(right, (RGB,HEX)):
            return (*right.export(), init.transparentDefault[1])
        elif isinstance(right,HSL):
            return (*hsl_to_rgb(*right.export()), init.transparentDefault[1])
        elif isinstance(right,HSV):
            return (*hsv_to_rgb(*right.export()), init.transparentDefault[1])
        elif isinstance(right,CMYK):
            return (*cmyk_to_rgb(*right.export()), init.transparentDefault[1])
        elif isinstance(right, (RGBA,HEXA)):
            return (*right.export(),)

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
        return init.stringSeparation.join(str(c) for c in self.export())

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

    def __bool__(self) -> bool:
        """
        Returns a True value if any values of the Color System are not 0
        """
        return any(color!=0 for color in self.export())

    def __round__(self, n=None) -> ColorSystem:
        """
        Returns a new object, with its values rounded to n
        """
        return self.__class__(*(round(value,n) for value in self.export()))

    def __int__(self) -> int:
        """
        Returns the average value of all Color Elements as an integer value
        """
        return int(self.__float__())

    def __float__(self) -> float:
        """
        Returns the average value of all Color Elements as a float value
        """
        values = self.export()
        return sum(values)/len(values)

    # ------------------------------------------------------------------------------------------------------------------
    # - Math Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    # noinspection PyTypeChecker
    def __add__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        """
        Math Dunder which executes an ADDITION operator between the left- and right-hand side of the operation.
        The returned object will be a new instance of the left-hand object's class.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        result = dunder_func(func=CSD.add, left=self, right=other)
        if result is NotImplemented:
            return result
        return self.__class__(*result)

    # noinspection PyTypeChecker
    def __sub__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        """
        Math Dunder which executes an SUBTRACTION operator between the left- and right-hand side of the operation.
        The returned object will be a new instance of the left-hand object's class.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        result = dunder_func(func=CSD.sub, left=self, right=other)
        if result is NotImplemented:
            return result
        return self.__class__(*result)

    # noinspection PyTypeChecker
    def __mul__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        """
        Math Dunder which executes an MULTIPLICATION operator between the left- and right-hand side of the operation.
        The returned object will be a new instance of the left-hand object's class.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        result = dunder_func(func=CSD.mul, left=self, right=other)
        if result is NotImplemented:
            return result
        return self.__class__(*result)

    # noinspection PyTypeChecker
    def __floordiv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        """
        Math Dunder which executes an FLOOR DIVISION operator between the left- and right-hand side of the operation.
        The returned object will be a new instance of the left-hand object's class.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        result = dunder_func(func=CSD.floordiv, left=self, right=other)
        if result is NotImplemented:
            return result
        return self.__class__(*result)

    # noinspection PyTypeChecker
    def __truediv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        """
        Math Dunder which executes an DIVISION operator between the left- and right-hand side of the operation.
        The returned object will be a new instance of the left-hand object's class.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        result = dunder_func(func=CSD.truediv, left=self, right=other)
        if result is NotImplemented:
            return result
        return self.__class__(*result)

    # noinspection PyTypeChecker
    def __mod__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        """
        Math Dunder which executes an MODULO operator between the left- and right-hand side of the operation.
        The returned object will be a new instance of the left-hand object's class.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        result = dunder_func(func=CSD.mod, left=self, right=other)
        if result is NotImplemented:
            return result
        return self.__class__(*result)

    # noinspection PyTypeChecker
    def __pow__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        """
        Math Dunder which executes an POWER operator between the left- and right-hand side of the operation.
        The returned object will be a new instance of the left-hand object's class.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        result = dunder_func(func=CSD.power, left=self, right=other)
        if result is NotImplemented:
            return result
        return self.__class__(*result)

    def __divmod__(self, other: ColorSystem|int|float|tuple):
        result = dunder_func(func=CSD.divmod_function, left=self, right=other)
        if result is NotImplemented:
            return result
        return (*(self.__class__(*colors) for colors in result),)

    @abstractmethod
    def __iadd__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:...
    @abstractmethod
    def __isub__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:...
    @abstractmethod
    def __imul__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:...
    @abstractmethod
    def __ifloordiv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:...
    @abstractmethod
    def __itruediv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:...
    @abstractmethod
    def __imod__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:...
    @abstractmethod
    def __ipow__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:...

    # ------------------------------------------------------------------------------------------------------------------
    # - Comparison Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    # noinspection PyTypeChecker
    def __gt__(self, other: ColorSystem|int|float|tuple) -> bool:
        """
        Comparison Dunder which compares for GREATER THAN.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return dunder_func(func=CSD.gt,left=self,right=other)

    # noinspection PyTypeChecker
    def __lt__(self, other: ColorSystem|int|float|tuple) -> bool:
        """
        Comparison Dunder which compares for SMALLER THAN.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return dunder_func(func=CSD.lt,left=self,right=other)

    # noinspection PyTypeChecker
    def __eq__(self, other: ColorSystem|int|float|tuple) -> bool:
        """
        Comparison Dunder which compares for EQUALITY.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return dunder_func(func=CSD.eq,left=self,right=other)

    # noinspection PyTypeChecker
    def __ne__(self, other: ColorSystem|int|float|tuple) -> bool:
        """
        Comparison Dunder which compares for INEQUALITY.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return dunder_func(func=CSD.ne,left=self,right=other)

    # noinspection PyTypeChecker
    def __le__(self, other: ColorSystem|int|float|tuple) -> bool:
        """
        Comparison Dunder which compares for SMALLER OR EQUAL TO.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return dunder_func(func=CSD.le,left=self,right=other)

    # noinspection PyTypeChecker
    def __ge__(self, other: ColorSystem|int|float|tuple) -> bool:
        """
        Comparison Dunder which compares for GREATER OR EQUAL TO.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return dunder_func(func=CSD.ge,left=self,right=other)

# ------------------------------------------------------------------------------------------------------------------
# - RGB -
# ------------------------------------------------------------------------------------------------------------------
class RGB(ColorSystem):
    """
    Color Object for RGB values.
    All r,g,b values are integer values which range between 0 and 255, including.
    """
    # ------------------------------------------------------------------------------------------------------------------
    # INIT method
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,r:int|float=0, g:int|float=0, b:int|float=0):
        self.r, self.g, self.b = r, g, b

    def export(self) -> Tuple[int,int,int]:
         return self.r,self.g,self.b

    # ------------------------------------------------------------------------------------------------------------------
    # RGB Properties
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def r(self) -> int:
        return self._r
    @r.setter
    def r(self, value: int|float):
        if init.roundUp:
            self._r = RoundHalfUp(Constrain(StrictType(value, (int,float)), 255))
        else:
            self._r = round(Constrain(StrictType(value, (int,float)), 255))

    @property
    def g(self) -> int:
        return self._g
    @g.setter
    def g(self, value: int|float):
        if init.roundUp:
            self._g = RoundHalfUp(Constrain(StrictType(value, (int,float)), 255))
        else:
            self._g = round(Constrain(StrictType(value, (int,float)), 255))

    @property
    def b(self) -> int:
        return self._b
    @b.setter
    def b(self, value: int|float):
        if init.roundUp:
            self._b = RoundHalfUp(Constrain(StrictType(value, (int,float)), 255))
        else:
            self._b = round(Constrain(StrictType(value, (int,float)), 255))

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __repr__(self) -> str:
        return f"RGB(r={self.r},g={self.g},b={self.b})"

    def __iadd__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.add, left=self, right=other)
        if value is NotImplemented:
            return value
        self.r, self.g, self.b = value
        return self
    def __isub__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.sub, left=self, right=other)
        if value is NotImplemented:
            return value
        self.r, self.g, self.b = value
        return self
    def __imul__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.mul, left=self, right=other)
        if value is NotImplemented:
            return value
        self.r, self.g, self.b = value
        return self
    def __ifloordiv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.floordiv, left=self, right=other)
        if value is NotImplemented:
            return value
        self.r, self.g, self.b = value
        return self
    def __itruediv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.truediv, left=self, right=other)
        if value is NotImplemented:
            return value
        self.r, self.g, self.b = value
        return self
    def __imod__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.mod, left=self, right=other)
        if value is NotImplemented:
            return value
        self.r, self.g, self.b = value
        return self
    def __ipow__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.power, left=self, right=other)
        if value is NotImplemented:
            return value
        self.r, self.g, self.b = value
        return self

# ----------------------------------------------------------------------------------------------------------------------
# - HEX -
# ----------------------------------------------------------------------------------------------------------------------
# inherits from rgb as it is just another notation of the rgb format
class HEX(RGB):
    """
    Color Object for HEX values.
    Inherits from RGB as this is just another notation for RGB values.
    """
    def __init__(self, hex_value:str="#000000"):
        super().__init__(*hex_to_rgb(StrictType(hex_value, str)))

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __str__(self) -> str:
        return rgb_to_hex(*self.export())

    def __repr__(self) -> str:
        return f"""HEX(hex_value="{rgb_to_hex(*self.export())}")"""

    # Cast dunders
    def __round__(self, n=None):
        return self.__class__(rgb_to_hex(*(round(value,n) for value in self.export())))

    def __divmod__(self, other: ColorSystem|int|float|tuple):
        result = dunder_func(func=CSD.divmod_function, left=self, right=other)
        if result is NotImplemented:
            return result
        return (*(self.__class__(rgb_to_hex(*colors)) for colors in result),)

    # ------------------------------------------------------------------------------------------------------------------
    # - Math Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    # noinspection PyTypeChecker
    def __add__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return self.__class__(rgb_to_hex(*dunder_func(func=CSD.add, left=self, right=other)))

    # noinspection PyTypeChecker
    def __sub__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return self.__class__(rgb_to_hex(*dunder_func(func=CSD.sub, left=self, right=other)))

    # noinspection PyTypeChecker
    def __mul__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return self.__class__(rgb_to_hex(*dunder_func(func=CSD.mul, left=self, right=other)))

    # noinspection PyTypeChecker
    def __floordiv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return self.__class__(rgb_to_hex(*dunder_func(func=CSD.floordiv, left=self, right=other)))

    # noinspection PyTypeChecker
    def __truediv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return self.__class__(rgb_to_hex(*dunder_func(func=CSD.truediv, left=self, right=other)))

    # noinspection PyTypeChecker
    def __mod__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return self.__class__(rgb_to_hex(*dunder_func(func=CSD.mod, left=self, right=other)))

    # noinspection PyTypeChecker
    def __pow__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return self.__class__(rgb_to_hex(*dunder_func(func=CSD.power, left=self, right=other)))

# ------------------------------------------------------------------------------------------------------------------
# - RGBA -
# ------------------------------------------------------------------------------------------------------------------
class RGBA(ColorSystem):
    """
    Color Object for RGBA values.
    All r,g,b,a values are integer values which range between 0 and 255, including.
    """
    # ------------------------------------------------------------------------------------------------------------------
    # INIT method
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,r:int=0, g:int=0, b:int=0, a:int=0):
        self.r,self.g,self.b,self.a = r,g,b,a

    def export(self) -> Tuple[int,int,int,int]:
         return self.r,self.g,self.b,self.a

    # ------------------------------------------------------------------------------------------------------------------
    # RGB Properties
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def r(self) -> int:
        return self._r
    @r.setter
    def r(self, value: int|float):
        if init.roundUp:
            self._r = RoundHalfUp(Constrain(StrictType(value, (int,float)), 255))
        else:
            self._r = round(Constrain(StrictType(value, (int,float)), 255))

    @property
    def g(self) -> int:
        return self._g
    @g.setter
    def g(self, value: int|float):
        if init.roundUp:
            self._g = RoundHalfUp(Constrain(StrictType(value, (int,float)), 255))
        else:
            self._g = round(Constrain(StrictType(value, (int,float)), 255))

    @property
    def b(self) -> int:
        return self._b
    @b.setter
    def b(self, value: int|float):
        if init.roundUp:
            self._b = RoundHalfUp(Constrain(StrictType(value, (int,float)), 255))
        else:
            self._b = round(Constrain(StrictType(value, (int,float)), 255))

    @property
    def a(self) -> int:
        return self._a
    @a.setter
    def a(self, value: int|float):
        if init.roundUp:
            self._a = RoundHalfUp(Constrain(StrictType(value, (int,float)), 255))
        else:
            self._a = round(Constrain(StrictType(value, (int,float)), 255))
    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __repr__(self) -> str:
        return f"RGBA(r={self.r},g={self.g},b={self.b},a={self.a})"

    def __iadd__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.add, left=self, right=other)
        if value is NotImplemented:
            return value
        self.r, self.g, self.b, self.a = value
        return self
    def __isub__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.sub, left=self, right=other)
        if value is NotImplemented:
            return value
        self.r, self.g, self.b, self.a = value
        return self
    def __imul__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.mul, left=self, right=other)
        if value is NotImplemented:
            return value
        self.r, self.g, self.b, self.a = value
        return self
    def __ifloordiv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.floordiv, left=self, right=other)
        if value is NotImplemented:
            return value
        self.r, self.g, self.b, self.a = value
        return self
    def __itruediv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.truediv, left=self, right=other)
        if value is NotImplemented:
            return value
        self.r, self.g, self.b, self.a = value
        return self
    def __imod__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.mod, left=self, right=other)
        if value is NotImplemented:
            return value
        self.r, self.g, self.b, self.a = value
        return self
    def __ipow__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.power, left=self, right=other)
        if value is NotImplemented:
            return value
        self.r, self.g, self.b, self.a = value
        return self


# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
# inherits from rgba as it is just another notation of the rgb format
class HEXA(RGBA):
    """
    Color Object for HEXA values.
    Inherits from RGBA as this is just another notation for RGBA values.
    """
    def __init__(self, hex_value:str="#00000000"):
        super().__init__(*hexa_to_rgba(hex_value))

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __str__(self) -> str:
        return rgba_to_hexa(*self.export())

    def __repr__(self) -> str:
        return f"""HEXA(hex_value="{rgba_to_hexa(*self.export())}")"""

    # Cast dunders
    def __round__(self, n=None):
        return self.__class__(rgba_to_hexa(*(round(value,n) for value in self.export())))

    def __divmod__(self, other: ColorSystem|int|float|tuple):
        result = dunder_func(func=CSD.divmod_function, left=self, right=other)
        if result is NotImplemented:
            return result
        return (*(self.__class__(rgba_to_hexa(*colors)) for colors in result),)


    # ------------------------------------------------------------------------------------------------------------------
    # - Math Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    # noinspection PyTypeChecker
    def __add__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return self.__class__(rgba_to_hexa(*dunder_func(func=CSD.add, left=self, right=other)))

    # noinspection PyTypeChecker
    def __sub__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return self.__class__(rgba_to_hexa(*dunder_func(func=CSD.sub, left=self, right=other)))

    # noinspection PyTypeChecker
    def __mul__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return self.__class__(rgba_to_hexa(*dunder_func(func=CSD.mul, left=self, right=other)))

    # noinspection PyTypeChecker
    def __floordiv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return self.__class__(rgba_to_hexa(*dunder_func(func=CSD.floordiv, left=self, right=other)))

    # noinspection PyTypeChecker
    def __truediv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return self.__class__(rgba_to_hexa(*dunder_func(func=CSD.truediv, left=self, right=other)))

    # noinspection PyTypeChecker
    def __mod__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return self.__class__(rgba_to_hexa(*dunder_func(func=CSD.mod, left=self, right=other)))

    # noinspection PyTypeChecker
    def __pow__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return self.__class__(rgba_to_hexa(*dunder_func(func=CSD.power, left=self, right=other)))

# ------------------------------------------------------------------------------------------------------------------
# - HSV -
# ------------------------------------------------------------------------------------------------------------------
class HSV(ColorSystem):
    """
    Color Object for HSV values.
    The h value is a float value which ranges between 0 and 360, including.
    Both s,v values are float values which range between 0 and 1, including.
    """
    # ------------------------------------------------------------------------------------------------------------------
    # INIT method
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,h: int|float=0.0, s: int|float=0.0, v: int|float=0.0):
        self.h,self.s,self.v = h,s,v

    def export(self) -> Tuple[int|float,int|float,int|float]:
         return self.h,self.s,self.v

    # ------------------------------------------------------------------------------------------------------------------
    # RGB Properties
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def h(self) -> int|float:
        return self._h
    @h.setter
    def h(self, value: int|float):
        self._h = RoundToDecimals(Constrain(StrictType(value, (int,float)), 360))

    @property
    def s(self) -> int|float:
        return self._s
    @s.setter
    def s(self, value: int|float):
        self._s = RoundToDecimals(Constrain(StrictType(value, (int,float)), 1))

    @property
    def v(self) -> int|float:
        return self._v
    @v.setter
    def v(self, value: int|float):
        self._v = RoundToDecimals(Constrain(StrictType(value, (int,float)), 1))

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __repr__(self) -> str:
        return f"HSV(h={self.h},s={self.s},v={self.v})"

    def __iadd__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.add, left=self, right=other)
        if value is NotImplemented:
            return value
        self.h,self.s,self.v = value
        return self
    def __isub__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.sub, left=self, right=other)
        if value is NotImplemented:
            return value
        self.h,self.s,self.v = value
        return self
    def __imul__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.mul, left=self, right=other)
        if value is NotImplemented:
            return value
        self.h,self.s,self.v = value
        return self
    def __ifloordiv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.floordiv, left=self, right=other)
        if value is NotImplemented:
            return value
        self.h,self.s,self.v = value
        return self
    def __itruediv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.truediv, left=self, right=other)
        if value is NotImplemented:
            return value
        self.h,self.s,self.v = value
        return self
    def __imod__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.mod, left=self, right=other)
        if value is NotImplemented:
            return value
        self.h,self.s,self.v = value
        return self
    def __ipow__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.power, left=self, right=other)
        if value is NotImplemented:
            return value
        self.h,self.s,self.v = value
        return self



# ------------------------------------------------------------------------------------------------------------------
# - HSL -
# ------------------------------------------------------------------------------------------------------------------
class HSL(ColorSystem):
    """
    Color Object for HSL values.
    The h value is a float value which ranges between 0 and 360, including.
    Both s,l values are float values which range between 0 and 1, including.
    """
    # ------------------------------------------------------------------------------------------------------------------
    # INIT method
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,h:int|float=0, s:int|float=0, l:int|float=0):
        self.h,self.s,self.l = h,s,l

    def export(self) -> Tuple[int|float,int|float,int|float]:
         return self.h,self.s,self.l

    # ------------------------------------------------------------------------------------------------------------------
    # RGB Properties
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def h(self) -> int|float:
        return self._h
    @h.setter
    def h(self, value: int|float):
        self._h = RoundToDecimals(Constrain(StrictType(value, (int,float)), 360))

    @property
    def s(self) -> int|float:
        return self._s
    @s.setter
    def s(self, value: int|float):
        self._s = RoundToDecimals(Constrain(StrictType(value, (int,float)), 1))

    @property
    def l(self) -> int|float:
        return self._l
    @l.setter
    def l(self, value: int|float):
        self._l = RoundToDecimals(Constrain(StrictType(value, (int,float)), 1))

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __repr__(self) -> str:
        return f"HSL(h={self.h},s={self.s},l={self.l})"

    def __iadd__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.add, left=self, right=other)
        if value is NotImplemented:
            return value
        self.h,self.s,self.l = value
        return self
    def __isub__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.sub, left=self, right=other)
        if value is NotImplemented:
            return value
        self.h,self.s,self.l = value
        return self
    def __imul__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.mul, left=self, right=other)
        if value is NotImplemented:
            return value
        self.h,self.s,self.l = value
        return self
    def __ifloordiv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.floordiv, left=self, right=other)
        if value is NotImplemented:
            return value
        self.h,self.s,self.l = value
        return self
    def __itruediv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.truediv, left=self, right=other)
        if value is NotImplemented:
            return value
        self.h,self.s,self.l = value
        return self
    def __imod__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.mod, left=self, right=other)
        if value is NotImplemented:
            return value
        self.h,self.s,self.l = value
        return self
    def __ipow__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.power, left=self, right=other)
        if value is NotImplemented:
            return value
        self.h,self.s,self.l = value
        return self


# ----------------------------------------------------------------------------------------------------------------------
# - CMYK -
# ----------------------------------------------------------------------------------------------------------------------
class CMYK(ColorSystem):
    """
    Color Object for CMYK values.
    All c,m,y,k values are float values which range between 0 and 1, including
    """
    # ------------------------------------------------------------------------------------------------------------------
    # INIT method
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, c:int|float=0, m:int|float=0, y:int|float=0, k:int|float=0):
        self.c, self.m, self.y, self.k = c, m, y, k

    def export(self) -> Tuple[int|float,int|float,int|float,int|float]:
         return self.c,self.m,self.y,self.k

    # ------------------------------------------------------------------------------------------------------------------
    # CMYK Properties
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def c(self) -> int|float:
        return self._c
    @c.setter
    def c(self, value: int|float):
        self._c = RoundToDecimals(Constrain(StrictType(value, (int,float)), 1))

    @property
    def m(self) -> int|float:
        return self._m
    @m.setter
    def m(self, value: int|float):
        self._m = RoundToDecimals(Constrain(StrictType(value, (int,float)), 1))

    @property
    def y(self) -> int|float:
        return self._y
    @y.setter
    def y(self, value: int|float):
        self._y = RoundToDecimals(Constrain(StrictType(value, (int,float)), 1))

    @property
    def k(self) -> int|float:
        return self._k
    @k.setter
    def k(self, value: int|float):
        self._k = RoundToDecimals(Constrain(StrictType(value, (int,float)), 1))

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __repr__(self) -> str:
        return f"CMYK(c={self.c},m={self.m},y={self.y},k={self.k})"

    def __iadd__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.add, left=self, right=other)
        if value is NotImplemented:
            return value
        self.c,self.m,self.y,self.k = value
        return self
    def __isub__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.sub, left=self, right=other)
        if value is NotImplemented:
            return value
        self.c,self.m,self.y,self.k = value
        return self
    def __imul__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.mul, left=self, right=other)
        if value is NotImplemented:
            return value
        self.c,self.m,self.y,self.k = value
        return self
    def __ifloordiv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.floordiv, left=self, right=other)
        if value is NotImplemented:
            return value
        self.c,self.m,self.y,self.k = value
        return self
    def __itruediv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.truediv, left=self, right=other)
        if value is NotImplemented:
            return value
        self.c,self.m,self.y,self.k = value
        return self
    def __imod__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.mod, left=self, right=other)
        if value is NotImplemented:
            return value
        self.c,self.m,self.y,self.k = value
        return self
    def __ipow__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        value = dunder_func(func=CSD.power, left=self, right=other)
        if value is NotImplemented:
            return value
        self.c,self.m,self.y,self.k = value
        return self
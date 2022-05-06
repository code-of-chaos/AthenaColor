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

def map_color(left,right) -> tuple:
    try:
        a = color_conversions_mapped[type(left)][type(right)]
        return a(right)
    except KeyError:
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
        return init.stringSeparation.join(str(c) for c in self)

    @abstractmethod
    def __repr__(self)->str:...

    @abstractmethod
    def export(self) -> tuple:...

    @abstractmethod
    def _value_setter(self, values:tuple):...

    def average(self) -> float:
        values = self.export()
        return sum(values)/len(values)

    def __bool__(self) -> bool:
        return any(color!=0 for color in self)

    def __round__(self, n=None) -> ColorSystem:
        return self.__class__(*(round(value,n) for value in self))
    
    def __iter__(self):
        return iter(self.export())

    def __len__(self):
        return len(self.export())

    def __hash__(self):
        return hash(self.export())

    def __copy__(self):
        return eval(repr(self))

    def __contains__(self, item):
        return item in self.export()

    # ------------------------------------------------------------------------------------------------------------------
    # - Math Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    # ! Math Dunder which executes an operator between the left- and right-hand side of the operation.
    #   The returned object will be a new instance of the left-hand object's class.
    #   If the two sides of the operation are NOT of the same type,
    #       it will convert the right-hand object to the same type as the left-hand type.

    # noinspection PyTypeChecker
    def __add__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        """
        """
        result = dunder_func(func=CSD.add, left=self, right=other)
        if result is NotImplemented:
            return result
        return self.__class__(*result)

    # noinspection PyTypeChecker
    def __sub__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        result = dunder_func(func=CSD.sub, left=self, right=other)
        if result is NotImplemented:
            return result
        return self.__class__(*result)

    # noinspection PyTypeChecker
    def __mul__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        result = dunder_func(func=CSD.mul, left=self, right=other)
        if result is NotImplemented:
            return result
        return self.__class__(*result)

    # noinspection PyTypeChecker
    def __floordiv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        result = dunder_func(func=CSD.floordiv, left=self, right=other)
        if result is NotImplemented:
            return result
        return self.__class__(*result)

    # noinspection PyTypeChecker
    def __truediv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        result = dunder_func(func=CSD.truediv, left=self, right=other)
        if result is NotImplemented:
            return result
        return self.__class__(*result)

    # noinspection PyTypeChecker
    def __mod__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        result = dunder_func(func=CSD.mod, left=self, right=other)
        if result is NotImplemented:
            return result
        return self.__class__(*result)

    # noinspection PyTypeChecker
    def __pow__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        result = dunder_func(func=CSD.power, left=self, right=other)
        if result is NotImplemented:
            return result
        return self.__class__(*result)

    def __divmod__(self, other: ColorSystem|int|float|tuple):
        result = dunder_func(func=CSD.divmod_function, left=self, right=other)
        if result is NotImplemented:
            return result
        return self.__class__(*result[0]), self.__class__(*result[1])

    def __iadd__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        values = dunder_func(func=CSD.add, left=self, right=other)
        if values is NotImplemented:
            return values
        self._value_setter(values)
        return self
    def __isub__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        values = dunder_func(func=CSD.sub, left=self, right=other)
        if values is NotImplemented:
            return values
        self._value_setter(values)
        return self
    def __imul__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        values = dunder_func(func=CSD.mul, left=self, right=other)
        if values is NotImplemented:
            return values
        self._value_setter(values)
        return self
    def __ifloordiv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        values = dunder_func(func=CSD.floordiv, left=self, right=other)
        if values is NotImplemented:
            return values
        self._value_setter(values)
        return self
    def __itruediv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        values = dunder_func(func=CSD.truediv, left=self, right=other)
        if values is NotImplemented:
            return values
        self._value_setter(values)
        return self
    def __imod__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        values = dunder_func(func=CSD.mod, left=self, right=other)
        if values is NotImplemented:
            return values
        self._value_setter(values)
        return self
    def __ipow__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        values = dunder_func(func=CSD.power, left=self, right=other)
        if values is NotImplemented:
            return values
        self._value_setter(values)
        return self

    # ------------------------------------------------------------------------------------------------------------------
    # - Comparison Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    # ! Comparison Dunder which executes an operator between the left- and right-hand side of the operation.
    #   If the two sides of the operation are NOT of the same type,
    #       it will convert the right-hand object to the same type as the left-hand type.

    # noinspection PyTypeChecker
    def __gt__(self, other: ColorSystem|int|float|tuple) -> bool:
        return dunder_func(func=CSD.gt,left=self,right=other)

    # noinspection PyTypeChecker
    def __lt__(self, other: ColorSystem|int|float|tuple) -> bool:
        return dunder_func(func=CSD.lt,left=self,right=other)

    # noinspection PyTypeChecker
    def __eq__(self, other: ColorSystem|int|float|tuple) -> bool:
        return dunder_func(func=CSD.eq,left=self,right=other)

    # noinspection PyTypeChecker
    def __ne__(self, other: ColorSystem|int|float|tuple) -> bool:
        return dunder_func(func=CSD.ne,left=self,right=other)

    # noinspection PyTypeChecker
    def __le__(self, other: ColorSystem|int|float|tuple) -> bool:
        return dunder_func(func=CSD.le,left=self,right=other)

    # noinspection PyTypeChecker
    def __ge__(self, other: ColorSystem|int|float|tuple) -> bool:
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

    def _value_setter(self, values:tuple):
        self.r, self.g, self.b = values

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

    def __abs__(self) -> ColorSystem:
        return self.__class__(rgb_to_hex(*(abs(value) for value in self)))

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

    def _value_setter(self, values:tuple):
        self.r, self.g, self.b, self.a = values

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

    def __abs__(self) -> ColorSystem:
        return self.__class__(rgba_to_hexa(*(abs(value) for value in self)))

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

    def _value_setter(self, values:tuple):
        self.h,self.s,self.v = values

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

    def _value_setter(self, values:tuple):
        self.h,self.s,self.l = values

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

    def _value_setter(self, values:tuple):
        self.c,self.m,self.y,self.k = values

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

# needs to be placed here, as only after all the defining of all the colors, this map can be made
color_conversions_mapped ={
    RGB : {
        RGB: lambda r: r.export(),
        HEX: lambda r: r.export(),
        HSL: lambda r: hsl_to_rgb(*r.export()),
        HSV: lambda r: hsv_to_rgb(*r.export()),
        CMYK: lambda r: cmyk_to_rgb(*r.export()),
        RGBA: lambda r: (*r.export()[:-1],),
        HEXA: lambda r: (*r.export()[:-1],),
    },
    HEX : {
        RGB: lambda r: r.export(),
        HEX: lambda r: r.export(),
        HSL: lambda r: hsl_to_rgb(*r.export()),
        HSV: lambda r: hsv_to_rgb(*r.export()),
        CMYK: lambda r: cmyk_to_rgb(*r.export()),
        RGBA: lambda r: (*r.export()[:-1],),
        HEXA: lambda r: (*r.export()[:-1],),
    },
    HSL : {
        RGB: lambda r: rgb_to_hsl(*r.export()),
        HEX: lambda r: rgb_to_hsl(*r.export()),
        HSL: lambda r: r.export(),
        HSV: lambda r: hsv_to_hsl(*r.export()),
        CMYK: lambda r: cmyk_to_hsl(*r.export()),
        RGBA: lambda r: rgb_to_hsl(*r.export()[:-1]),
        HEXA: lambda r: rgb_to_hsl(*r.export()[:-1]),
    },
    HSV : {
        RGB: lambda r: rgb_to_hsv(*r.export()),
        HEX: lambda r: rgb_to_hsv(*r.export()),
        HSL: lambda r: hsl_to_hsv(*r.export()),
        HSV: lambda r: r.export(),
        CMYK: lambda r: cmyk_to_hsv(*r.export()),
        RGBA: lambda r: rgb_to_hsv(*r.export()[:-1]),
        HEXA: lambda r: rgb_to_hsv(*r.export()[:-1]),
    },
    CMYK : {
        RGB: lambda r: rgb_to_cmyk(*r.export()),
        HEX: lambda r: rgb_to_cmyk(*r.export()),
        HSL: lambda r: hsl_to_cmyk(*r.export()),
        HSV: lambda r: hsv_to_cmyk(*r.export()),
        CMYK: lambda r: r.export(),
        RGBA: lambda r: rgb_to_cmyk(*r.export()[:-1]),
        HEXA: lambda r: rgb_to_cmyk(*r.export()[:-1]),
    },
    RGBA : {
        RGB: lambda r: (*r.export(), init.transparentDefault[1]),
        HEX: lambda r: (*r.export(), init.transparentDefault[1]),
        HSL: lambda r: (*hsl_to_rgb(*r.export()), init.transparentDefault[1]),
        HSV: lambda r: (*hsv_to_rgb(*r.export()), init.transparentDefault[1]),
        CMYK: lambda r: (*cmyk_to_rgb(*r.export()), init.transparentDefault[1]),
        RGBA: lambda r: r.export(),
        HEXA: lambda r: r.export(),
    },
    HEXA : {
        RGB: lambda r: (*r.export(), init.transparentDefault[1]),
        HEX: lambda r: (*r.export(), init.transparentDefault[1]),
        HSL: lambda r: (*hsl_to_rgb(*r.export()), init.transparentDefault[1]),
        HSV: lambda r: (*hsv_to_rgb(*r.export()), init.transparentDefault[1]),
        CMYK: lambda r: (*cmyk_to_rgb(*r.export()), init.transparentDefault[1]),
        RGBA: lambda r: r.export(),
        HEXA: lambda r: r.export(),
    },
}
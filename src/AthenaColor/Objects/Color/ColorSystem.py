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
from AthenaColor.Functions.StrictTyping import StrictType, StrictError
from AthenaColor.Functions.General import RoundHalfUp,RoundToDecimals

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
            return right.export()[:-1]

    elif isinstance(left, HSL):
        if isinstance(right, (RGB,HEX)):
            return rgb_to_hsl(*right.export())
        elif isinstance(right,HSL):
            return right.export()
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
            return right.export()
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
            return right.export()
        elif isinstance(right, (RGBA,HEXA)):
            return rgb_to_cmyk(*right.export()[:-1])

    elif isinstance(left, (RGBA,HEXA)):
        if isinstance(right, (RGB,HEX)):
            return right.export(), init.transparent_default_float
        elif isinstance(right,HSL):
            return hsl_to_rgb(*right.export()), init.transparent_default_float
        elif isinstance(right,HSV):
            return hsv_to_rgb(*right.export()), init.transparent_default_float
        elif isinstance(right,CMYK):
            return cmyk_to_rgb(*right.export()), init.transparent_default_float
        elif isinstance(right, (RGBA,HEXA)):
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
        return type(self)(*dunder_func(func=CSD.add, left=self, right=other))

    # noinspection PyTypeChecker
    def __sub__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        """
        Math Dunder which executes an SUBTRACTION operator between the left- and right-hand side of the operation.
        The returned object will be a new instance of the left-hand object's class.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return type(self)(*dunder_func(func=CSD.sub, left=self, right=other))

    # noinspection PyTypeChecker
    def __mul__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        """
        Math Dunder which executes an MULTIPLICATION operator between the left- and right-hand side of the operation.
        The returned object will be a new instance of the left-hand object's class.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return type(self)(*dunder_func(func=CSD.mul, left=self, right=other))

    # noinspection PyTypeChecker
    def __floordiv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        """
        Math Dunder which executes an FLOOR DIVISION operator between the left- and right-hand side of the operation.
        The returned object will be a new instance of the left-hand object's class.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return type(self)(*dunder_func(func=CSD.floordiv, left=self, right=other))

    # noinspection PyTypeChecker
    def __truediv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        """
        Math Dunder which executes an DIVISION operator between the left- and right-hand side of the operation.
        The returned object will be a new instance of the left-hand object's class.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return type(self)(*dunder_func(func=CSD.truediv, left=self, right=other))

    # noinspection PyTypeChecker
    def __mod__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        """
        Math Dunder which executes an MODULO operator between the left- and right-hand side of the operation.
        The returned object will be a new instance of the left-hand object's class.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return type(self)(*dunder_func(func=CSD.mod, left=self, right=other))

    # noinspection PyTypeChecker
    def __pow__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        """
        Math Dunder which executes an POWER operator between the left- and right-hand side of the operation.
        The returned object will be a new instance of the left-hand object's class.
        If the two sides of the operation are NOT of the same type, it will convert the right-hand object to the same type as the left-hand type.
        """
        return type(self)(*dunder_func(func=CSD.pow, left=self, right=other))

    def __iadd__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return self.__add__(other)
    def __isub__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return self.__sub__(other)
    def __imul__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return self.__mul__(other)
    def __ifloordiv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return self.__floordiv__(other)
    def __itruediv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return self.__truediv__(other)
    def __imod__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return self.__mod__(other)
    def __ipow__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return self.__pow__(other)

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
    def __init__(self,r:int=0, g:int=0, b:int=0):
        try:
            StrictType(types=(int, float), objects=(r, g, b))
            self.r,self.g,self.b = r,g,b
        except StrictError:
            raise ValueError(f"RGB values r={r},g={g},b={b} did not consist of integer values")

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
        if not isinstance(value, (int,float)):
            raise ValueError
        self._r = RoundHalfUp(Constrain(value, 255)) if init.roundUp else round(Constrain(value, 255))

    @property
    def g(self) -> int:
        return self._g
    @g.setter
    def g(self, value: int|float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._g = RoundHalfUp(Constrain(value, 255)) if init.roundUp else round(Constrain(value, 255))

    @property
    def b(self) -> int:
        return self._b
    @b.setter
    def b(self, value: int|float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._b = RoundHalfUp(Constrain(value, 255)) if init.roundUp else round(Constrain(value, 255))

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
        if not isinstance(hex_value,str):
            raise ValueError(f"HEX value hex_value={hex_value} did not consist of a string value")
        super().__init__(*hex_to_rgb(hex_value))

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __str__(self) -> str:
        return rgb_to_hex(*self.export())

    def __repr__(self) -> str:
        return f"HEX(r={self.r},g={self.g},b={self.b})"

    # ------------------------------------------------------------------------------------------------------------------
    # - Math Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    # noinspection PyTypeChecker
    def __add__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return type(self)(rgb_to_hex(*dunder_func(func=CSD.add, left=self, right=other)))

    # noinspection PyTypeChecker
    def __sub__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return type(self)(rgb_to_hex(*dunder_func(func=CSD.sub, left=self, right=other)))

    # noinspection PyTypeChecker
    def __mul__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return type(self)(rgb_to_hex(*dunder_func(func=CSD.mul, left=self, right=other)))

    # noinspection PyTypeChecker
    def __floordiv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return type(self)(rgb_to_hex(*dunder_func(func=CSD.floordiv, left=self, right=other)))

    # noinspection PyTypeChecker
    def __truediv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return type(self)(rgb_to_hex(*dunder_func(func=CSD.truediv, left=self, right=other)))

    # noinspection PyTypeChecker
    def __mod__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return type(self)(rgb_to_hex(*dunder_func(func=CSD.mod, left=self, right=other)))

    # noinspection PyTypeChecker
    def __pow__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return type(self)(rgb_to_hex(*dunder_func(func=CSD.pow, left=self, right=other)))

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
        try:
            StrictType(types=(int,float),objects=(r,g,b,a))
            self.r,self.g,self.b,self.a = r,g,b,a
        except StrictError:
            raise ValueError(f"RGB values r={r},g={g},b={b},a={a} did not consist of integer values")

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
        if not isinstance(value, (int,float)):
            raise ValueError
        self._r = RoundHalfUp(Constrain(value, 255)) if init.roundUp else round(Constrain(value, 255))

    @property
    def g(self) -> int:
        return self._g
    @g.setter
    def g(self, value: int|float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._g = RoundHalfUp(Constrain(value, 255)) if init.roundUp else round(Constrain(value, 255))

    @property
    def b(self) -> int:
        return self._b
    @b.setter
    def b(self, value: int|float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._b = RoundHalfUp(Constrain(value, 255)) if init.roundUp else round(Constrain(value, 255))

    @property
    def a(self) -> int:
        return self._a
    @a.setter
    def a(self, value: int|float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._a = RoundHalfUp(Constrain(value, 255)) if init.roundUp else round(Constrain(value, 255))

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
        if not isinstance(hex_value,str):
            raise ValueError(f"HEXA value hex_value={hex_value} did not consist of a string value")
        super().__init__(*hexa_to_rgba(hex_value))

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __str__(self) -> str:
        return rgba_to_hexa(*self.export())

    def __repr__(self) -> str:
        return f"HEXA(r={self.r},g={self.g},b={self.b},a={self.a})"


    # ------------------------------------------------------------------------------------------------------------------
    # - Math Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    # noinspection PyTypeChecker
    def __add__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return type(self)(rgba_to_hexa(*dunder_func(func=CSD.add, left=self, right=other)))

    # noinspection PyTypeChecker
    def __sub__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return type(self)(rgba_to_hexa(*dunder_func(func=CSD.sub, left=self, right=other)))

    # noinspection PyTypeChecker
    def __mul__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return type(self)(rgba_to_hexa(*dunder_func(func=CSD.mul, left=self, right=other)))

    # noinspection PyTypeChecker
    def __floordiv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return type(self)(rgba_to_hexa(*dunder_func(func=CSD.floordiv, left=self, right=other)))

    # noinspection PyTypeChecker
    def __truediv__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return type(self)(rgba_to_hexa(*dunder_func(func=CSD.truediv, left=self, right=other)))

    # noinspection PyTypeChecker
    def __mod__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return type(self)(rgba_to_hexa(*dunder_func(func=CSD.mod, left=self, right=other)))

    # noinspection PyTypeChecker
    def __pow__(self, other: ColorSystem|int|float|tuple) -> ColorSystem:
        return type(self)(rgba_to_hexa(*dunder_func(func=CSD.pow, left=self, right=other)))

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
        try:
            StrictType(types=(int,float),objects=(h,s,v))
            self.h,self.s,self.v = h,s,v
        except StrictError:
            raise ValueError(f"HSV values h={h},s={s},v={v} did not consist of integer or float values")

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
        if not isinstance(value, (int,float)):
            raise ValueError
        self._h = RoundToDecimals(Constrain(value, 360), init.decimalPlaces)

    @property
    def s(self) -> int|float:
        return self._s
    @s.setter
    def s(self, value: int|float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._s = RoundToDecimals(Constrain(value, 1), init.decimalPlaces)

    @property
    def v(self) -> int|float:
        return self._v
    @v.setter
    def v(self, value: int|float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._v = RoundToDecimals(Constrain(value, 1), init.decimalPlaces)

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
        try:
            StrictType(types=(int,float),objects=(h,s,l))
            self.h,self.s,self.l = h,s,l
        except StrictError:
            raise ValueError(f"HSL values h={h},s={s},l={l} did not consist of integer or float values")

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
        if not isinstance(value, (int,float)):
            raise ValueError
        self._h = RoundToDecimals(Constrain(value, 360), init.decimalPlaces)

    @property
    def s(self) -> int|float:
        return self._s
    @s.setter
    def s(self, value: int|float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._s = RoundToDecimals(Constrain(value, 1), init.decimalPlaces)

    @property
    def l(self) -> int|float:
        return self._l
    @l.setter
    def l(self, value: int|float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._l = RoundToDecimals(Constrain(value, 1), init.decimalPlaces)

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
        try:
            StrictType(types=(int,float), objects=(c,m,y,k))
            self.c, self.m, self.y, self.k = c, m, y, k
        except StrictError:
            raise ValueError(f"CMYK values c={c},m={m},y={y},k={k} did not consist of integer or float values")

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
        if not isinstance(value, (int,float)):
            raise ValueError
        self._c = RoundToDecimals(Constrain(value, 1), init.decimalPlaces)

    @property
    def m(self) -> int|float:
        return self._m
    @m.setter
    def m(self, value: int|float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._m = RoundToDecimals(Constrain(value, 1), init.decimalPlaces)

    @property
    def y(self) -> int|float:
        return self._y
    @y.setter
    def y(self, value: int|float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._y = RoundToDecimals(Constrain(value, 1), init.decimalPlaces)

    @property
    def k(self) -> int|float:
        return self._k
    @k.setter
    def k(self, value: int|float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._k = RoundToDecimals(Constrain(value, 1), init.decimalPlaces)

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __repr__(self) -> str:
        return f"CMYK(c={self.c},m={self.m},y={self.y},k={self.k})"
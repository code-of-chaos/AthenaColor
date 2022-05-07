# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Tuple
# Custom Library

# Custom Packages
import AthenaColor.Functions.DunderFunctions as CSD
from AthenaColor.Objects.Color.ColorTupleConversion import *
from AthenaColor.InitClass import init
from AthenaColor.Functions.Constraints import Constrain
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
def _ColorConversionInput(fnc):
    def wrapper(self,other:ColorSystem|int|tuple):
        try:
            return fnc(self, color_conversions_mapped[type(self)][type(other)](other))
        except KeyError:
            return NotImplemented
    return wrapper

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

    def __hash__(self):
        return hash(self.export())

    def __copy__(self):
        return eval(repr(self))

    def __contains__(self, item):
        return item in self.export()

    @ _ColorConversionInput
    def __divmod__(self, other: tuple) -> tuple:
        div_ , mod_ = CSD.divmod_function(self.export(), other)
        return self.__class__(*div_),self.__class__(*mod_)

    # ------------------------------------------------------------------------------------------------------------------
    # - Math Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    # ! Math Dunder which executes an operator between the left- and right-hand side of the operation.
    #   The returned object will be a new instance of the left-hand object's class.
    #   If the two sides of the operation are NOT of the same type,
    #       it will convert the right-hand object to the same type as the left-hand type.

    @ _ColorConversionInput
    def __add__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self.__class__(*CSD.add(self.export(), other))
    @ _ColorConversionInput
    def __sub__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self.__class__(*CSD.sub(self.export(), other))
    @ _ColorConversionInput
    def __mul__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self.__class__(*CSD.mul(self.export(), other))
    @ _ColorConversionInput
    def __floordiv__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self.__class__(*CSD.floordiv(self.export(), other))
    @ _ColorConversionInput
    def __truediv__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self.__class__(*CSD.truediv(self.export(), other))
    @ _ColorConversionInput
    def __mod__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self.__class__(*CSD.mod(self.export(), other))
    @ _ColorConversionInput
    def __pow__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self.__class__(*CSD.power(self.export(), other))

    @ _ColorConversionInput
    def __iadd__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self._value_setter(CSD.add(self.export(), other))
    @ _ColorConversionInput
    def __isub__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self._value_setter(CSD.sub(self.export(), other))
    @ _ColorConversionInput
    def __imul__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self._value_setter(CSD.mul(self.export(), other))
    @ _ColorConversionInput
    def __ifloordiv__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self._value_setter(CSD.floordiv(self.export(), other))
    @ _ColorConversionInput
    def __itruediv__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self._value_setter(CSD.truediv(self.export(), other))
    @ _ColorConversionInput
    def __itruediv__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self._value_setter(CSD.truediv(self.export(), other))
    @ _ColorConversionInput
    def __imod__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self._value_setter(CSD.mod(self.export(), other))
    @ _ColorConversionInput
    def __ipow__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self._value_setter(CSD.power(self.export(), other))

    # ------------------------------------------------------------------------------------------------------------------
    # - Comparison Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    # ! Comparison Dunder which executes an operator between the left- and right-hand side of the operation.
    #   If the two sides of the operation are NOT of the same type,
    #       it will convert the right-hand object to the same tuple format as the left-hand type.

    @ _ColorConversionInput
    def __gt__(self, other: ColorSystem|int|float|tuple) -> bool:
        return CSD.gt(self.export(), other)
    @ _ColorConversionInput
    def __lt__(self, other: ColorSystem|int|float|tuple) -> bool:
        return CSD.lt(self.export(), other)
    @ _ColorConversionInput
    def __eq__(self, other: ColorSystem|int|float|tuple) -> bool:
        return CSD.eq(self.export(), other)
    @ _ColorConversionInput
    def __ne__(self, other: ColorSystem|int|float|tuple) -> bool:
        return CSD.ne(self.export(), other)
    @ _ColorConversionInput
    def __le__(self, other: ColorSystem|int|float|tuple) -> bool:
        return CSD.le(self.export(), other)
    @ _ColorConversionInput
    def __ge__(self, other: ColorSystem|int|float|tuple) -> bool:
        return CSD.ge(self.export(), other)

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
        self._r = round(Constrain(value, 255))

    @property
    def g(self) -> int:
        return self._g
    @g.setter
    def g(self, value: int|float):
        self._g = round(Constrain(value, 255))

    @property
    def b(self) -> int:
        return self._b
    @b.setter
    def b(self, value: int|float):
        self._b = round(Constrain(value, 255))

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
        super().__init__(*hex_to_rgb(hex_value))

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

    @ _ColorConversionInput
    def __divmod__(self, other: tuple) -> tuple:
        div_ , mod_ = CSD.divmod_function(self.export(), other)
        return self.__class__(rgb_to_hex(*div_)),self.__class__(rgb_to_hex(*mod_))

    # ------------------------------------------------------------------------------------------------------------------
    # - Math Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    @ _ColorConversionInput
    def __add__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self.__class__(rgb_to_hex(*CSD.add(self.export(), other)))
    @ _ColorConversionInput
    def __sub__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self.__class__(rgb_to_hex(*CSD.sub(self.export(), other)))
    @ _ColorConversionInput
    def __mul__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self.__class__(rgb_to_hex(*CSD.mul(self.export(), other)))
    @ _ColorConversionInput
    def __floordiv__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self.__class__(rgb_to_hex(*CSD.floordiv(self.export(), other)))
    @ _ColorConversionInput
    def __truediv__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self.__class__(rgb_to_hex(*CSD.truediv(self.export(), other)))
    @ _ColorConversionInput
    def __mod__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self.__class__(rgb_to_hex(*CSD.mod(self.export(), other)))
    @ _ColorConversionInput
    def __pow__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self.__class__(rgb_to_hex(*CSD.power(self.export(), other)))

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
        self._r = round(Constrain(value, 255))

    @property
    def g(self) -> int:
        return self._g
    @g.setter
    def g(self, value: int|float):
        self._g = round(Constrain(value, 255))

    @property
    def b(self) -> int:
        return self._b
    @b.setter
    def b(self, value: int|float):
        self._b = round(Constrain(value, 255))


    @property
    def a(self) -> int:
        return self._a
    @a.setter
    def a(self, value: int|float):
        self._a = round(Constrain(value, 255))
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

    @ _ColorConversionInput
    def __divmod__(self, other: tuple) -> tuple:
        div_ , mod_ = CSD.divmod_function(self.export(), other)
        return self.__class__(rgba_to_hexa(*div_)),self.__class__(rgba_to_hexa(*mod_))

    # ------------------------------------------------------------------------------------------------------------------
    # - Math Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    @ _ColorConversionInput
    def __add__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self.__class__(rgba_to_hexa(*CSD.add(self.export(), other)))
    @ _ColorConversionInput
    def __sub__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self.__class__(rgba_to_hexa(*CSD.sub(self.export(), other)))
    @ _ColorConversionInput
    def __mul__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self.__class__(rgba_to_hexa(*CSD.mul(self.export(), other)))
    @ _ColorConversionInput
    def __floordiv__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self.__class__(rgba_to_hexa(*CSD.floordiv(self.export(), other)))
    @ _ColorConversionInput
    def __truediv__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self.__class__(rgba_to_hexa(*CSD.truediv(self.export(), other)))
    @ _ColorConversionInput
    def __mod__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self.__class__(rgba_to_hexa(*CSD.mod(self.export(), other)))
    @ _ColorConversionInput
    def __pow__(self, other: ColorSystem|int|tuple) -> ColorSystem:
        return self.__class__(rgba_to_hexa(*CSD.power(self.export(), other)))

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
        self._h = RoundToDecimals(Constrain(value, 360))

    @property
    def s(self) -> int|float:
        return self._s
    @s.setter
    def s(self, value: int|float):
        self._s = RoundToDecimals(Constrain(value, 1))

    @property
    def v(self) -> int|float:
        return self._v
    @v.setter
    def v(self, value: int|float):
        self._v = RoundToDecimals(Constrain(value, 1))

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
        self._h = RoundToDecimals(Constrain(value, 360))

    @property
    def s(self) -> int|float:
        return self._s
    @s.setter
    def s(self, value: int|float):
        self._s = RoundToDecimals(Constrain(value, 1))

    @property
    def l(self) -> int|float:
        return self._l
    @l.setter
    def l(self, value: int|float):
        self._l = RoundToDecimals(Constrain(value, 1))

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
        self._c = RoundToDecimals(Constrain(value, 1))

    @property
    def m(self) -> int|float:
        return self._m
    @m.setter
    def m(self, value: int|float):
        self._m = RoundToDecimals(Constrain(value, 1))

    @property
    def y(self) -> int|float:
        return self._y
    @y.setter
    def y(self, value: int|float):
        self._y = RoundToDecimals(Constrain(value, 1))

    @property
    def k(self) -> int|float:
        return self._k
    @k.setter
    def k(self, value: int|float):
        self._k = RoundToDecimals(Constrain(value, 1))

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __repr__(self) -> str:
        return f"CMYK(c={self.c},m={self.m},y={self.y},k={self.k})"

# BELOW HERE IS FOR SPEED INCREASE!
# Possible because we now have a __hash__ on any given ColorSystem class
# needs to be placed here, as only after all the defining of all the colors, this map can be made
_r_export = lambda r: r.export()
_r_export_RGBAtoRGB = lambda r: (r.r, r.g, r.b)
_tuple3 = lambda r: (r,r,r)
_tuple4 = lambda r: (r,r,r,r)
_same =  lambda r: r
trnspDef = init.transparentDefault[1]
color_conversions_mapped ={
    RGB : {
        RGB: _r_export,
        HEX: _r_export,
        HSL: lambda r: hsl_to_rgb(r.h, r.s, r.l),
        HSV: lambda r: hsv_to_rgb(r.h, r.s, r.v),
        CMYK: lambda r: cmyk_to_rgb(r.c,r.m,r.y,r.k),
        RGBA: _r_export_RGBAtoRGB,
        HEXA: _r_export_RGBAtoRGB,
        int: _tuple3,
        float: _tuple3,
        tuple: _same
    },
    HEX : {
        RGB: _r_export,
        HEX: _r_export,
        HSL: lambda r: hsl_to_rgb(r.h, r.s, r.l),
        HSV: lambda r: hsv_to_rgb(r.h, r.s, r.v),
        CMYK: lambda r: cmyk_to_rgb(r.c,r.m,r.y,r.k),
        RGBA: _r_export_RGBAtoRGB,
        HEXA: _r_export_RGBAtoRGB,
        int: _tuple3,
        float: _tuple3,
        tuple: _same
    },
    HSL : {
        RGB: lambda r: rgb_to_hsl(r.r, r.g, r.b),
        HEX: lambda r: rgb_to_hsl(r.r, r.g, r.b),
        HSL: _r_export,
        HSV: lambda r: hsv_to_hsl(r.h, r.s, r.v),
        CMYK: lambda r: cmyk_to_hsl(r.c,r.m,r.y,r.k),
        RGBA: lambda r: rgb_to_hsl(r.r, r.g, r.b),
        HEXA: lambda r: rgb_to_hsl(r.r, r.g, r.b),
        int: _tuple3,
        float: _tuple3,
        tuple: _same
    },
    HSV : {
        RGB: lambda r: rgb_to_hsv(r.r, r.g, r.b),
        HEX: lambda r: rgb_to_hsv(r.r, r.g, r.b),
        HSL: lambda r: hsl_to_hsv(r.h, r.s, r.l),
        HSV: _r_export,
        CMYK: lambda r: cmyk_to_hsv(r.c,r.m,r.y,r.k),
        RGBA: lambda r: rgb_to_hsv(r.r, r.g, r.b),
        HEXA: lambda r: rgb_to_hsv(r.r, r.g, r.b),
        int: _tuple3,
        float: _tuple3,
        tuple: _same
    },
    CMYK : {
        RGB: lambda r: rgb_to_cmyk(r.r, r.g, r.b),
        HEX: lambda r: rgb_to_cmyk(r.r, r.g, r.b),
        HSL: lambda r: hsl_to_cmyk(r.h, r.s, r.l),
        HSV: lambda r: hsv_to_cmyk(r.h, r.s, r.v),
        CMYK: _r_export,
        RGBA: lambda r: rgb_to_cmyk(r.r, r.g, r.b),
        HEXA: lambda r: rgb_to_cmyk(r.r, r.g, r.b),
        int: _tuple4,
        float: _tuple4,
        tuple: _same
    },
    RGBA : {
        RGB: lambda r: (r.r, r.g, r.b, trnspDef),
        HEX: lambda r: (r.r, r.g, r.b, trnspDef),
        HSL: lambda r: (*hsl_to_rgb(r.h, r.s, r.l), trnspDef),
        HSV: lambda r: (*hsv_to_rgb(r.h, r.s, r.v), trnspDef),
        CMYK: lambda r: (*cmyk_to_rgb(r.c,r.m,r.y,r.k), trnspDef),
        RGBA: _r_export,
        HEXA: _r_export,
        int: _tuple4,
        float: _tuple4,
        tuple: _same
    },
    HEXA : {
        RGB: lambda r: (r.r, r.g, r.b, trnspDef),
        HEX: lambda r: (r.r, r.g, r.b, trnspDef),
        HSL: lambda r: (*hsl_to_rgb(r.h, r.s, r.l), trnspDef),
        HSV: lambda r: (*hsv_to_rgb(r.h, r.s, r.v), trnspDef),
        CMYK: lambda r: (*cmyk_to_rgb(r.c,r.m,r.y,r.k), trnspDef),
        RGBA: _r_export,
        HEXA: _r_export,
        int: _tuple4,
        float: _tuple4,
        tuple: _same
    },
}
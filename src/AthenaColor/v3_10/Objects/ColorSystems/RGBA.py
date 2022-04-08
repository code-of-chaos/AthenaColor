# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor.v3_10.InitClass import AthenaColorInitClass
from AthenaColor.v3_10.BoilerPlate import (
    Constrain,
    TestTypes,
    RoundHalfUp
)
from ._ColorSystem import (
    ColorSystem,
)
from AthenaColor.v3_10.Objects.ColorSystems._BASE_ColorSystem import BASE_RGB

# ------------------------------------------------------------------------------------------------------------------
# - Color -
# ------------------------------------------------------------------------------------------------------------------
class RGBA(ColorSystem,BASE_RGB):
    """
    Color Object for RGBA values.
    All r,g,b,a values are integer values which range between 0 and 255, including.
    """
    # ------------------------------------------------------------------------------------------------------------------
    # INIT method
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,r: int, g: int, b: int, a:int):
        if not TestTypes(types=(int,float),objects=(r,g,b,a)):
            raise ValueError(f"RGB values {r=},{g=},{b=},{a=} did not consist of integer values")
        self.r,self.g,self.b,self.a = r,g,b,a

    def export(self) -> tuple[RGBA.r, RGBA.g, RGBA.b, RGBA.a]:
         return self.r,self.g,self.b,self.a

    # ------------------------------------------------------------------------------------------------------------------
    # RGB Properties
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def r(self) -> int:
        return self._r
    @r.setter
    def r(self, value: int | float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._r = RoundHalfUp(Constrain(value, 255)) if AthenaColorInitClass.roundUp else round(Constrain(value, 255))

    @property
    def g(self) -> int:
        return self._g
    @g.setter
    def g(self, value: int | float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._g = RoundHalfUp(Constrain(value, 255)) if AthenaColorInitClass.roundUp else round(Constrain(value, 255))

    @property
    def b(self) -> int:
        return self._b
    @b.setter
    def b(self, value: int | float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._b = RoundHalfUp(Constrain(value, 255)) if AthenaColorInitClass.roundUp else round(Constrain(value, 255))

    @property
    def a(self) -> int:
        return self._a
    @a.setter
    def a(self, value: int | float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._a = RoundHalfUp(Constrain(value, 255)) if AthenaColorInitClass.roundUp else round(Constrain(value, 255))

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __repr__(self) -> str:
        return f"RGBA(r={self.r},g={self.g},b={self.b},a={self.a})"
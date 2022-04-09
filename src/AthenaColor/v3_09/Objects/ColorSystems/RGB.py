# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor.v3_09.InitClass import AthenaColorInitClass
from AthenaColor.v3_09.BoilerPlate import (
    Constrain,
    TestTypes,
    RoundHalfUp
)
from ._ColorSystem import (
    ColorSystem,
)
from AthenaColor.v3_09.Objects.ColorSystems._BASE_ColorSystem import BASE_RGB
from AthenaColor.v3_09.BoilerPlate.Union import IntFloat

# ------------------------------------------------------------------------------------------------------------------
# - Color -
# ------------------------------------------------------------------------------------------------------------------
class RGB(ColorSystem, BASE_RGB):
    """
    Color Object for RGB values.
    All r,g,b values are integer values which range between 0 and 255, including.
    """
    # ------------------------------------------------------------------------------------------------------------------
    # INIT method
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,r: int, g: int, b: int):
        if not TestTypes(types=(int,float),objects=(r,g,b)):
            raise ValueError(f"RGB values {r=},{g=},{b=} did not consist of integer values")
        self.r,self.g,self.b = r,g,b

    def export(self) -> tuple[int,int,int]:
         return self.r,self.g,self.b

    # ------------------------------------------------------------------------------------------------------------------
    # RGB Properties
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def r(self) -> int:
        return self._r
    @r.setter
    def r(self, value: IntFloat):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._r = RoundHalfUp(Constrain(value, 255)) if AthenaColorInitClass.roundUp else round(Constrain(value, 255))

    @property
    def g(self) -> int:
        return self._g
    @g.setter
    def g(self, value: IntFloat):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._g = RoundHalfUp(Constrain(value, 255)) if AthenaColorInitClass.roundUp else round(Constrain(value, 255))

    @property
    def b(self) -> int:
        return self._b
    @b.setter
    def b(self, value: IntFloat):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._b = RoundHalfUp(Constrain(value, 255)) if AthenaColorInitClass.roundUp else round(Constrain(value, 255))

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __repr__(self) -> str:
        return f"RGB(r={self.r},g={self.g},b={self.b})"
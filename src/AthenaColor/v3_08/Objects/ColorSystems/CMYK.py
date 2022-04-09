# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from typing import Tuple

# Custom Library

# Custom Packages
from AthenaColor.v3_08.BoilerPlate import (
    Constrain,
    TestTypes
)
from ._ColorSystem import (
    ColorSystem,
)
from AthenaColor.v3_08.Objects.ColorSystems._BASE_ColorSystem import BASE_CMYK
from AthenaColor.v3_08.BoilerPlate.Union import IntFloat

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CMYK(ColorSystem, BASE_CMYK):
    """
    Color Object for CMYK values.
    All c,m,y,k values are float values which range between 0 and 1, including
    """
    # ------------------------------------------------------------------------------------------------------------------
    # INIT method
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, c:IntFloat, m:IntFloat, y:IntFloat, k:IntFloat):
        if not TestTypes(types=(int,float), objects=(c,m,y,k)):
            raise ValueError(f"CMYK values c={c},m={m},y={y},k={k} did not consist of integer or float values")
        self.c,self.m,self.y,self.k = c,m,y,k

    def export(self) -> Tuple[IntFloat,IntFloat,IntFloat,IntFloat]:
         return self.c,self.m,self.y,self.k

    # ------------------------------------------------------------------------------------------------------------------
    # CMYK Properties
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def c(self) -> IntFloat:
        return self._c
    @c.setter
    def c(self, value: IntFloat):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._c = Constrain(value, 1)

    @property
    def m(self) -> IntFloat:
        return self._m
    @m.setter
    def m(self, value: IntFloat):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._m = Constrain(value, 1)

    @property
    def y(self) -> IntFloat:
        return self._y
    @y.setter
    def y(self, value: IntFloat):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._y = Constrain(value, 1)

    @property
    def k(self) -> IntFloat:
        return self._k
    @k.setter
    def k(self, value: IntFloat):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._k = Constrain(value, 1)

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __repr__(self) -> str:
        return f"CMYK(c={self.c},m={self.m},y={self.y},k={self.k})"

# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor.Functions.BoilerPlate import (
    Constrain,
    TestTypes
)
from ._ColorSystem import (
    ColorSystem,
    _HSL
)

# ------------------------------------------------------------------------------------------------------------------
# - Color -
# ------------------------------------------------------------------------------------------------------------------
class HSL(ColorSystem,_HSL):
    # ------------------------------------------------------------------------------------------------------------------
    # INIT method
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,h: int|float, s: int|float, l: int|float):
        if not TestTypes(types=(int,float),objects=(h,s,l)):
            raise ValueError(f"HSL values {h=},{s=},{l=} did not consist of integer or float values")

        self.h = h
        self.s = s
        self.l = l

    # ------------------------------------------------------------------------------------------------------------------
    # RGB Properties
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def h(self):
        return self._h
    @h.setter
    def h(self, value: int | float):
        self._h = Constrain(value, 360)

    @property
    def s(self):
        return self._s
    @s.setter
    def s(self, value: int | float):
        self._s = Constrain(value, 1)

    @property
    def l(self):
        return self._l
    @l.setter
    def l(self, value: int | float):
        self._l = Constrain(value, 1)

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __str__(self) -> str:
        return f"{self.h};{self.s};{self.l}"

    def __repr__(self) -> str:
        return f"HSL(h={self.h}, s={self.s}, l={self.l})"
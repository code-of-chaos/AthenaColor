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
from .OpaqueColorSystem import (
    OpaqueColorSystem,
    _HSV
)

# ------------------------------------------------------------------------------------------------------------------
# - Color -
# ------------------------------------------------------------------------------------------------------------------
class HSV(OpaqueColorSystem,_HSV):
    # ------------------------------------------------------------------------------------------------------------------
    # INIT method
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,h: int|float, s: int|float, v: int|float):
        if not TestTypes(types=(int,float),objects=(h,s,v)):
            raise ValueError(f"HSV values {h=},{s=},{v=} did not consist of integer or float values")
        self.h = h
        self.s = s
        self.v = v

    def _export(self) -> tuple:
         return self.h,self.s,self.v

    # ------------------------------------------------------------------------------------------------------------------
    # RGB Properties
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def h(self) -> int|float:
        return self._h
    @h.setter
    def h(self, value: int | float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._h = Constrain(value, 360)

    @property
    def s(self) -> int|float:
        return self._s
    @s.setter
    def s(self, value: int | float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._s = Constrain(value, 1)

    @property
    def v(self) -> int|float:
        return self._v
    @v.setter
    def v(self, value: int | float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._v = Constrain(value, 1)

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __str__(self) -> str:
        return f"{self.h};{self.s};{self.v}"

    def __repr__(self) -> str:
        return f"HSV(h={self.h}, s={self.s}, v={self.v})"
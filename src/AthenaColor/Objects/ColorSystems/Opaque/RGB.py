# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor import init
from AthenaColor.Functions.BoilerPlate import (
    Constrain,
    TestTypes,
    RoundCorrectly
)
from .OpaqueColorSystem import (
    OpaqueColorSystem,
    _RGB
)

# ------------------------------------------------------------------------------------------------------------------
# - Color -
# ------------------------------------------------------------------------------------------------------------------
class RGB(OpaqueColorSystem,_RGB):
    # ------------------------------------------------------------------------------------------------------------------
    # INIT method
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,r: int, g: int, b: int):
        if not TestTypes(types=(int,float),objects=(r,g,b)):
            raise ValueError(f"RGB values {r=},{g=},{b=} did not consist of integer values")
        self.r,self.g,self.b = r,g,b

    def _export(self) -> tuple[RGB.r,RGB.g,RGB.b]:
         return self.r,self.g,self.b

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
        self._r = RoundCorrectly(Constrain(value, 255)) if init.rgb_round_05_up else round(Constrain(value, 255))

    @property
    def g(self) -> int:
        return self._g
    @g.setter
    def g(self, value: int | float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._g = RoundCorrectly(Constrain(value, 255)) if init.rgb_round_05_up else round(Constrain(value, 255))

    @property
    def b(self) -> int:
        return self._b
    @b.setter
    def b(self, value: int | float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._b = RoundCorrectly(Constrain(value, 255)) if init.rgb_round_05_up else round(Constrain(value, 255))

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __str__(self) -> str:
        return f"{self.r};{self.g};{self.b}"

    def __repr__(self) -> str:
        return f"RGB(r={self.r}, g={self.g}, b={self.b})"
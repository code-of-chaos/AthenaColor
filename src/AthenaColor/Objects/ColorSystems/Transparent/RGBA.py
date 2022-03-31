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
    RouhdHalfUp
)
from .TransparentColorSystem import (
    TransparentColorSystem,
    _RGBA
)

# ------------------------------------------------------------------------------------------------------------------
# - Color -
# ------------------------------------------------------------------------------------------------------------------
class RGBA(TransparentColorSystem,_RGBA):
    # ------------------------------------------------------------------------------------------------------------------
    # INIT method
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,r: int, g: int, b: int, a:int):
        if not TestTypes(types=(int,float),objects=(r,g,b,a)):
            raise ValueError(f"RGB values {r=},{g=},{b=},{a=} did not consist of integer values")
        self.r,self.g,self.b,self.a = r,g,b,a

    def _export(self) -> tuple[RGBA.r,RGBA.g,RGBA.b,RGBA.a]:
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
        self._r = RouhdHalfUp(Constrain(value, 255)) if init.rgb_round_05_up else round(Constrain(value, 255))

    @property
    def g(self) -> int:
        return self._g
    @g.setter
    def g(self, value: int | float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._g = RouhdHalfUp(Constrain(value, 255)) if init.rgb_round_05_up else round(Constrain(value, 255))

    @property
    def b(self) -> int:
        return self._b
    @b.setter
    def b(self, value: int | float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._b = RouhdHalfUp(Constrain(value, 255)) if init.rgb_round_05_up else round(Constrain(value, 255))

    @property
    def a(self) -> int:
        return self._a
    @a.setter
    def a(self, value: int | float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._a = RouhdHalfUp(Constrain(value, 255)) if init.rgb_round_05_up else round(Constrain(value, 255))

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __str__(self) -> str:
        return f"{self.r};{self.g};{self.b};{self.a}"

    def __repr__(self) -> str:
        return f"RGB(r={self.r}, g={self.g}, b={self.b},a={self.a})"
# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor.Functions.BoilerPlate import (
    Constrain,
    TestTypes,
    RoundCorrectly
)
from ._ColorSystem import (
    ColorSystem,
    _RGBA
)

# ------------------------------------------------------------------------------------------------------------------
# - Color -
# ------------------------------------------------------------------------------------------------------------------
class RGBA(ColorSystem,_RGBA):
    # ------------------------------------------------------------------------------------------------------------------
    # INIT method
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,r: int, g: int, b: int, a:int):
        if not TestTypes(types=int,objects=(r,g,b,a)):
            raise ValueError(f"RGB values {r=},{g=},{b=},{a=} did not consist of integer values")

        self.r = r
        self.g = g
        self.b = b
        self.a = a

    # ------------------------------------------------------------------------------------------------------------------
    # RGB Properties
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def r(self):
        return self._r
    @r.setter
    def r(self, value: int | float):
        self._r = RoundCorrectly(Constrain(value, 255))

    @property
    def g(self):
        return self._g
    @g.setter
    def g(self, value: int | float):
        self._g = RoundCorrectly(Constrain(value, 255))

    @property
    def b(self):
        return self._b
    @b.setter
    def b(self, value: int | float):
        self._b = RoundCorrectly(Constrain(value, 255))

    @property
    def a(self):
        return self._a
    @a.setter
    def a(self, value: int | float):
        self._a = RoundCorrectly(Constrain(value, 255))

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __str__(self) -> str:
        return f"{self.r};{self.g};{self.b};{self.a}"

    def __repr__(self) -> str:
        return f"RGB(r={self.r}, g={self.g}, b={self.b},a={self.a})"
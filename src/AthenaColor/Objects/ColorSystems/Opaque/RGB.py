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
    _RGB
)

# ------------------------------------------------------------------------------------------------------------------
# - Color -
# ------------------------------------------------------------------------------------------------------------------
class RGB(ColorSystem,_RGB):
    # ------------------------------------------------------------------------------------------------------------------
    # INIT method
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,r: int, g: int, b: int):
        if not TestTypes(types=int,objects=(r,g,b)):
            raise ValueError(f"RGB values {r=},{g=},{b=} did not consist of integer values")

        self.r = r
        self.g = g
        self.b = b

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

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __str__(self) -> str:
        return f"{self.r};{self.g};{self.b}"

    def __repr__(self) -> str:
        return f"RGB(r={self.r}, g={self.g}, b={self.b})"
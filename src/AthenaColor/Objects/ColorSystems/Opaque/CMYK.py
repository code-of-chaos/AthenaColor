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
    OpaqueColorSystem,
    _CMYK
)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CMYK(OpaqueColorSystem,_CMYK):
    # ------------------------------------------------------------------------------------------------------------------
    # INIT method
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, c:int|float, m:int|float, y:int|float, k:int|float):
        if not TestTypes(types=(int,float), objects=(c,m,y,k)):
            raise ValueError(f"CMYK values {c=},{m=},{y=},{k=} did not consist of integer or float values")
        self.c = c
        self.m = m
        self.y = y
        self.k = k

    # ------------------------------------------------------------------------------------------------------------------
    # CMYK Properties
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def c(self) -> int|float:
        return self._c
    @c.setter
    def c(self, value: int | float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._c = Constrain(value, 1)

    @property
    def m(self) -> int|float:
        return self._m
    @m.setter
    def m(self, value: int | float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._m = Constrain(value, 1)

    @property
    def y(self) -> int|float:
        return self._y
    @y.setter
    def y(self, value: int | float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._y = Constrain(value, 1)

    @property
    def k(self) -> int|float:
        return self._k
    @k.setter
    def k(self, value: int | float):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._k = Constrain(value, 1)

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __str__(self) -> str:
        return f"{self.c};{self.m};{self.y};{self.k}"

    def __repr__(self) -> str:
        return f"CMYK(c={self.c}, m={self.m}, y={self.y}, k={self.k})"

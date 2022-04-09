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
from AthenaColor.v3_08.Objects.ColorSystems._BASE_ColorSystem import BASE_HSL
from AthenaColor.v3_08.BoilerPlate.Union import IntFloat

# ------------------------------------------------------------------------------------------------------------------
# - Color -
# ------------------------------------------------------------------------------------------------------------------
class HSL(ColorSystem, BASE_HSL):
    """
    Color Object for HSL values.
    The h value is a float value which ranges between 0 and 360, including.
    Both s,l values are float values which range between 0 and 1, including.
    """
    # ------------------------------------------------------------------------------------------------------------------
    # INIT method
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,h: IntFloat, s: IntFloat, l: IntFloat):
        if not TestTypes(types=(int,float),objects=(h,s,l)):
            raise ValueError(f"HSL values h={h},s={s},l={l} did not consist of integer or float values")
        self.h,self.s,self.l = h,s,l

    def export(self) -> Tuple[IntFloat,IntFloat,IntFloat]:
         return self.h,self.s,self.l

    # ------------------------------------------------------------------------------------------------------------------
    # RGB Properties
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def h(self) -> IntFloat:
        return self._h
    @h.setter
    def h(self, value: IntFloat):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._h = Constrain(value, 360)

    @property
    def s(self) -> IntFloat:
        return self._s
    @s.setter
    def s(self, value: IntFloat):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._s = Constrain(value, 1)

    @property
    def l(self) -> IntFloat:
        return self._l
    @l.setter
    def l(self, value: IntFloat):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._l = Constrain(value, 1)

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __repr__(self) -> str:
        return f"HSL(h={self.h},s={self.s},l={self.l})"
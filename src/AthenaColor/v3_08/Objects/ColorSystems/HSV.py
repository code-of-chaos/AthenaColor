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
from AthenaColor.v3_08.Objects.ColorSystems._BASE_ColorSystem import BASE_HSV
from AthenaColor.v3_08.BoilerPlate.Union import IntFloat

# ------------------------------------------------------------------------------------------------------------------
# - Color -
# ------------------------------------------------------------------------------------------------------------------
class HSV(ColorSystem, BASE_HSV):
    """
    Color Object for HSV values.
    The h value is a float value which ranges between 0 and 360, including.
    Both s,v values are float values which range between 0 and 1, including.
    """
    # ------------------------------------------------------------------------------------------------------------------
    # INIT method
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,h: IntFloat, s: IntFloat, v: IntFloat):
        if not TestTypes(types=(int,float),objects=(h,s,v)):
            raise ValueError(f"HSV values h={h},s={s},v={v} did not consist of integer or float values")
        self.h,self.s,self.v = h,s,v

    def export(self) -> Tuple[IntFloat,IntFloat,IntFloat]:
         return self.h,self.s,self.v

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
    def v(self) -> IntFloat:
        return self._v
    @v.setter
    def v(self, value: IntFloat):
        if not isinstance(value, (int,float)):
            raise ValueError
        self._v = Constrain(value, 1)

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __repr__(self) -> str:
        return f"HSV(h={self.h},s={self.s},v={self.v})"
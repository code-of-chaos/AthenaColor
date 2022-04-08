# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
import sys
import os

# Custom Packages
from AthenaColor.v3_10.Data.General import EscCodes

# ----------------------------------------------------------------------------------------------------------------------
# - Init Classes -
# ----------------------------------------------------------------------------------------------------------------------
class AthenaColorInitClass:
    _esc=EscCodes.hex
    _roundUp = True
    _transparentDefault = ("ff",255)

    def __init__(self):
        # prep the console for colors
        if sys.platform == 'win32':
            os.system("color")

    @property
    def roundUp(self):
        return self._roundUp
    @roundUp.setter
    def roundUp(self,value:bool):
        if isinstance(value,bool):
            self._roundUp = value
        else:
            raise ValueError

    @property
    def esc(self):
        return self._esc
    @esc.setter
    def esc(self,value:bool):
        if value in (EscCodes.hex,EscCodes.uni,EscCodes.octal):
            self._esc = value
        else:
            raise ValueError

    @property
    def transparentDefault(self):
        return self._transparentDefault
    @transparentDefault.setter
    def transparentDefault(self,value:str|int):
        if isinstance(value, float|int) and 0 <= value <= 255:
            self._transparentDefault = ("%02x" % round(value), value)
        elif isinstance(value, str) and len(value) == 2 and (value_int:=int(value[0:2], 16)) in range(256):
            self._transparentDefault = (value,value_int)
        else:
            raise ValueError

# ----------------------------------------------------------------------------------------------------------------------
# - Init Object -
# ----------------------------------------------------------------------------------------------------------------------
init = AthenaColorInitClass()
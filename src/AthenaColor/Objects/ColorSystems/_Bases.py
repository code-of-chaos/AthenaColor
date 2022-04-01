# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class _RGB:
    r:int
    g:int
    b:int

    def _export(self) -> tuple:...

class _HEX:
    r:int
    g:int
    b:int

    def _export(self) -> tuple:...

class _CMYK:
    c:float
    m:float
    y:float
    k:float

    def _export(self) -> tuple:...

class _HSL:
    h:float
    s:float
    l:float

    def _export(self) -> tuple:...

class _HSV:
    h:float
    s:float
    v:float

    def _export(self) -> tuple:...

class _RGBA:
    r:int
    g:int
    b:int
    a:int

    def _export(self) -> tuple:...

class _HEXA:
    r:int
    g:int
    b:int
    a:int

    def _export(self) -> tuple:...

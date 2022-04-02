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

    def export(self) -> tuple:...

class _HEX:
    r:int
    g:int
    b:int

    def export(self) -> tuple:...

class _CMYK:
    c:float
    m:float
    y:float
    k:float

    def export(self) -> tuple:...

class _HSL:
    h:float
    s:float
    l:float

    def export(self) -> tuple:...

class _HSV:
    h:float
    s:float
    v:float

    def export(self) -> tuple:...

class _RGBA:
    r:int
    g:int
    b:int
    a:int

    def export(self) -> tuple:...

class _HEXA:
    r:int
    g:int
    b:int
    a:int

    def export(self) -> tuple:...

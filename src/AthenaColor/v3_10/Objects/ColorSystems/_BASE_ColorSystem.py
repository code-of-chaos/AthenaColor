# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class BASE_ColorSystem:
    def export(self) -> tuple:...

class BASE_RGB(BASE_ColorSystem):
    r:int
    g:int
    b:int

class BASE_HEX(BASE_ColorSystem):
    r:int
    g:int
    b:int

class BASE_CMYK(BASE_ColorSystem):
    c:float
    m:float
    y:float
    k:float

class BASE_HSL(BASE_ColorSystem):
    h:float
    s:float
    l:float

class BASE_HSV(BASE_ColorSystem):
    h:float
    s:float
    v:float

class BASE_RGBA(BASE_ColorSystem):
    r:int
    g:int
    b:int
    a:int

class BASE_HEXA(BASE_ColorSystem):
    r:int
    g:int
    b:int
    a:int


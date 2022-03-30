# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from .BoilerPlate import Constrain

# ----------------------------------------------------------------------------------------------------------------------
# - Constraints for OPAQUE COLORSs -
# ----------------------------------------------------------------------------------------------------------------------
def ConstrainHSV(h:int|float,s:int|float,v:int|float)->tuple[int|float,int|float,int|float]:
    s,v = map(lambda x: Constrain(x, 1), (s,v))
    return Constrain(h, 360),s,v

def ConstrainHSL(h:int|float,s:int|float,l:int|float)->tuple[int|float,int|float,int|float]:
    s,l = map(lambda x: Constrain(x, 1), (s,l))
    return Constrain(h, 360),s,l

def ConstrainRGB(r:int,g:int,b:int)->tuple[int,int,int]:
    r,g,b = map(lambda x: Constrain(x, 255), (r,g,b))
    return r,g,b

def ConstrainCMYK(c:int|float,m:int|float,y:int|float,k:int|float)->tuple[int|float,int|float,int|float,int|float]:
    c,m,y,k = map(lambda x: Constrain(x, 1), (c,m,y,k))
    return c,m,y,k

# ----------------------------------------------------------------------------------------------------------------------
# - Constraints for TRANSPARENT COLORSs -
# ----------------------------------------------------------------------------------------------------------------------
def ConstrainRGBA(r:int,g:int,b:int,a:int)->tuple[int,int,int,int]:
    r,g,b,a = map(lambda x: Constrain(x, 255), (r,g,b,a))
    return r,g,b,a
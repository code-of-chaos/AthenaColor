# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from ..BoilerPlate import Constrain

# ----------------------------------------------------------------------------------------------------------------------
# - Constraints for ColorSystems -
# ----------------------------------------------------------------------------------------------------------------------
def ConstrainHSV(h,s,v)->tuple[int|float,int|float,int|float]:
    s,v = map(lambda x: Constrain(x, 1), (s,v))
    return Constrain(h, 360),s,v

def ConstrainHSL(h,s,l)->tuple[int|float,int|float,int|float]:
    s,l = map(lambda x: Constrain(x, 1), (s,l))
    return Constrain(h, 360),s,l

def ConstrainRGB(r,g,b)->tuple[int|float,int|float,int|float]:
    r,g,b = map(lambda x: Constrain(x, 255), (r,g,b))
    return r,g,b

def ConstrainCMYK(c,m,y,k)->tuple[int|float,int|float,int|float,int|float]:
    c,m,y,k = map(lambda x: Constrain(x, 1), (c,m,y,k))
    return c,m,y,k
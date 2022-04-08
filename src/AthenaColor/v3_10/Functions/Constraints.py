# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor.v3_10.BoilerPlate import Constrain

# ----------------------------------------------------------------------------------------------------------------------
# - Constraints for OPAQUE COLORSs -
# ----------------------------------------------------------------------------------------------------------------------
def ConstrainHSV(h:int|float,s:int|float,v:int|float)->tuple[int|float,int|float,int|float]:
    return Constrain(h, 360),Constrain(s,1),Constrain(v,1)

def ConstrainHSL(h:int|float,s:int|float,l:int|float)->tuple[int|float,int|float,int|float]:
    return Constrain(h, 360),Constrain(s,1),Constrain(l,1)

def ConstrainRGB(r:int,g:int,b:int)->tuple[int,int,int]:
    return Constrain(r, 255),Constrain(g, 255),Constrain(b, 255)

def ConstrainCMYK(c:int|float,m:int|float,y:int|float,k:int|float)->tuple[int|float,int|float,int|float,int|float]:
    return Constrain(c,1),Constrain(m,1),Constrain(y,1),Constrain(k,1)

# ----------------------------------------------------------------------------------------------------------------------
# - Constraints for TRANSPARENT COLORSs -
# ----------------------------------------------------------------------------------------------------------------------
def ConstrainRGBA(r:int,g:int,b:int,a:int)->tuple[int,int,int,int]:
    return Constrain(r, 255),Constrain(g, 255),Constrain(b, 255),Constrain(a, 255)
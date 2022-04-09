# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from typing import Tuple

# Custom Library

# Custom Packages
from AthenaColor.v3_07.BoilerPlate import Constrain
from AthenaColor.v3_07.BoilerPlate.Union import IntFloat

# ----------------------------------------------------------------------------------------------------------------------
# - Constraints for OPAQUE COLORSs -
# ----------------------------------------------------------------------------------------------------------------------
def ConstrainHSV(h:IntFloat,s:IntFloat,v:IntFloat)->Tuple[IntFloat,IntFloat,IntFloat]:
    return Constrain(h, 360),Constrain(s,1),Constrain(v,1)

def ConstrainHSL(h:IntFloat,s:IntFloat,l:IntFloat)->Tuple[IntFloat,IntFloat,IntFloat]:
    return Constrain(h, 360),Constrain(s,1),Constrain(l,1)

def ConstrainRGB(r:int,g:int,b:int)->Tuple[int,int,int]:
    return Constrain(r, 255),Constrain(g, 255),Constrain(b, 255)

def ConstrainCMYK(c:IntFloat,m:IntFloat,y:IntFloat,k:IntFloat)->Tuple[IntFloat,IntFloat,IntFloat,IntFloat]:
    return Constrain(c,1),Constrain(m,1),Constrain(y,1),Constrain(k,1)

# ----------------------------------------------------------------------------------------------------------------------
# - Constraints for TRANSPARENT COLORSs -
# ----------------------------------------------------------------------------------------------------------------------
def ConstrainRGBA(r:int,g:int,b:int,a:int)->Tuple[int,int,int,int]:
    return Constrain(r, 255),Constrain(g, 255),Constrain(b, 255),Constrain(a, 255)
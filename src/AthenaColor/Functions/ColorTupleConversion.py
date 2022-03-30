# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from .BoilerPlate import (
    NormalizeRgb,
    RoundCorrectly
)
from .TestValues import (
    testRGB,testHSV,testHSL,testCMYK,testHEX,
    testHEXA,testRGBA
)
from .Constraints import (
    ConstrainHSV, ConstrainHSL, ConstrainRGB, ConstrainCMYK,
    ConstrainRGBA
)

# ----------------------------------------------------------------------------------------------------------------------
# - OPAQUE COLORS -
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# - RGB -
# ----------------------------------------------------------------------------------------------------------------------
@testHEX
def hex_to_rgb(hexadecimal:str) -> tuple[int,int,int]:
    """
    Function to convert a hexadecimal string to a rgb tuple.
    Does not create an RGB object.
    """
    # Form hex value in usable state (cast away the '#' value)
    if hexadecimal[0] == "#":
        hex_v = hexadecimal[1:]
    elif len(hexadecimal) == 6:
        hex_v = hexadecimal
    else:
        raise ValueError("Hexadecimal was given in an incorrect format")

    # Actually convert to rgb integers
    r,g,b = tuple(
        int(hex_v[i:i + 2], 16)
        for i in (0, 2, 4)
    )

    return r,g,b

@testHSV
def hsv_to_rgb(h:float,s:float,v:float) -> tuple[int,int,int]:
    """
    Function to convert a hsv tuple to a rgb tuple.
    Does not create an RGB object.
    """
    h,s,v = ConstrainHSV(h,s,v)

    C = v*s
    h_ = h/60
    X = C*(1-abs((h_%2)-1))

    # map rgb correctly
    if      0   <= h_ < 1:  r_,g_,b_ = C,X,0
    elif    1   <= h_ < 2:  r_,g_,b_ = X,C,0
    elif    2   <= h_ < 3:  r_,g_,b_ = 0,C,X
    elif    3   <= h_ < 4:  r_,g_,b_ = 0,X,C
    elif    4   <= h_ < 5:  r_,g_,b_ = X,0,C
    else:                   r_,g_,b_ = C,0,X # 5 <= h_ < 6

    m = v-C

    return (
        RoundCorrectly((r_ + m) * 255),
        RoundCorrectly((g_ + m) * 255),
        RoundCorrectly((b_ + m) * 255)
    )

@testCMYK
def cmyk_to_rgb(c:float,m:float,y:float,k:float) -> tuple[int,int,int]:
    """
    Function to convert a cmyk tuple to a rgb tuple.
    Does not create an RGB object.
    """
    c,m,y,k = ConstrainCMYK(c,m,y,k)
    return (
        RoundCorrectly(255 * (1 - c) * (1 - k)),  #r
        RoundCorrectly(255 * (1 - m) * (1 - k)),  #g
        RoundCorrectly(255 * (1 - y) * (1 - k))  #b
    )

@testHSL
def hsl_to_rgb(h:float,s:float,l:float) -> tuple[int,int,int]:
    """
    Function to convert a hsl tuple to a rgb tuple.
    Does not create an RGB object.
    """
    h,s,l =ConstrainHSL(h,s,l)

    C = (1-abs((2*l)-1))*s
    X = C*(1-abs(((h/60)%2)-1))
    h_ = h/60

    # map rgb correctly
    if      0   <= h_ < 1:  r_,g_,b_ = C,X,0
    elif    1   <= h_ < 2:  r_,g_,b_ = X,C,0
    elif    2   <= h_ < 3:  r_,g_,b_ = 0,C,X
    elif    3   <= h_ < 4:  r_,g_,b_ = 0,X,C
    elif    4   <= h_ < 5:  r_,g_,b_ = X,0,C
    else:                   r_,g_,b_ = C,0,X # 5 <= h_ < 6

    m = l-(C/2)

    return (
        RoundCorrectly((r_ + m) * 255),
        RoundCorrectly((g_ + m) * 255),
        RoundCorrectly((b_ + m) * 255)
    )

# ----------------------------------------------------------------------------------------------------------------------
# - Hexadecimal -
# ----------------------------------------------------------------------------------------------------------------------
@testRGB
def rgb_to_hex(r:int,g:int,b:int) -> str:
    """
    Function to convert a rgb to a hexadecimal string.
    Does not create a HEX object.
    """
    return '#%02x%02x%02x' % ConstrainRGB(r,g,b)

@testHSV
def hsv_to_hex(h:int|float,s:int|float, v:int|float) -> str:
    """
    Function to convert a hsv to a hexadecimal string.
    Does not create a HEX object.
    """
    return rgb_to_hex(*hsv_to_rgb(*ConstrainHSV(h,s,v)))

@testCMYK
def cmyk_to_hex(c:int|float,m:int|float,y:int|float,k:int|float) -> str:
    """
    Function to convert a cmyk to a hexadecimal string.
    Does not create a HEX object.
    """
    return rgb_to_hex(*cmyk_to_rgb(*ConstrainCMYK(c,m,y,k)))

@testHSL
def hsl_to_hex(h:int|float,s:int|float,l:int|float) -> str:
    """
    Function to convert a hsl to a hexadecimal string.
    Does not create a HEX object.
    """
    return rgb_to_hex(*hsl_to_rgb(*ConstrainHSL(h,s,l)))


# ----------------------------------------------------------------------------------------------------------------------
# - HSV -
# ----------------------------------------------------------------------------------------------------------------------
@testRGB
def rgb_to_hsv(r:int,g:int,b:int) -> tuple[float,float,float]:
    """
    Function to convert a rgb tuple to a hsv tuple.
    Does not create an HSV object.
    """
    # Normalize
    r_,g_,b_ = NormalizeRgb(*ConstrainRGB(r,g,b))

    # Find max and min
    Max = max(r_, g_, b_)
    Min = min(r_, g_, b_)

    # Assemble delta to be used later
    Delta = Max-Min

    # Find Hue
    if Delta == 0:
        Hue = 0
    elif r_ == Max:            # Red value is Max
        Hue = 60 * (((g_-b_)/Delta)%6.)
    elif g_ == Max:          # Green value is Max
        Hue = 60 * (((b_-r_)/Delta)+2)
    else:                   # Blue value is Max
        Hue = 60 * (((r_-g_)/Delta)+4)

    # Find Saturation
    if Max == 0:
        Sat = 0
    else:
        Sat = Delta/Max

    return (
        Hue, # H
        Sat, # S
        Max  # V
    )

@testHEX
def hex_to_hsv(hexadecimal:str) -> tuple[float,float,float]:
    """
    Function to convert a hexadecimal string to a hsv tuple.
    Does not create an HSV object.
    """
    return rgb_to_hsv(*hex_to_rgb(hexadecimal))

@testCMYK
def cmyk_to_hsv(c:float,m:float,y:float,k:float) -> tuple[float,float,float]:
    """
    Function to convert a cmyk tuple to a hsv tuple.
    Does not create an HSV object.
    """
    return rgb_to_hsv(*cmyk_to_rgb(*ConstrainCMYK(c,m,y,k)))

@testHSL
def hsl_to_hsv(h:float,s:float,l:float) -> tuple[float,float,float]:
    """
    Function to convert a hsl tuple to a hsv tuple.
    Does not create an HSV object.
    """
    return rgb_to_hsv(*hsl_to_rgb(*ConstrainHSL(h,s,l)))

# ----------------------------------------------------------------------------------------------------------------------
# - CMYK -
# ----------------------------------------------------------------------------------------------------------------------
@testRGB
def rgb_to_cmyk(r:int,g:int,b:int) -> tuple[float,float,float,float]:
    """
    Function to convert a rgb tuple to a cmyk tuple.
    Does not create an CMYK object.
    """
    # Normalize
    r_, g_, b_ = NormalizeRgb(*ConstrainRGB(r,g,b))
    k = 1 - max(r_, g_, b_)

    c = (1-r_-k) / (1-k)
    m = (1-g_-k) / (1-k)
    y = (1-b_-k) / (1-k)

    return c,m,y,k

@testHEX
def hex_to_cmyk(hexadecimal:str) -> tuple[float,float,float,float]:
    """
    Function to convert a hexadecimal string to a cmyk tuple.
    Does not create an CMYK object.
    """
    return rgb_to_cmyk(*hex_to_rgb(hexadecimal))

@testHSV
def hsv_to_cmyk(h:float,s:float,v:float) -> tuple[float,float,float,float]:
    """
    Function to convert a hsv tuple to a cmyk tuple.
    Does not create an CMYK object.
    """
    return rgb_to_cmyk(*hsv_to_rgb(*ConstrainHSV(h,s,v)))

@testHSL
def hsl_to_cmyk(h:float,s:float,l:float) -> tuple[float,float,float,float]:
    """
    Function to convert a hsl tuple to a cmyk tuple.
    Does not create an CMYK object.
    """
    return rgb_to_cmyk(*hsl_to_rgb(*ConstrainHSL(h,s,l)))

# ----------------------------------------------------------------------------------------------------------------------
# - HSL -
# ----------------------------------------------------------------------------------------------------------------------
@testRGB
def rgb_to_hsl(r:int,g:int,b:int) -> tuple[float,float,float]:
    """
    Function to convert a rgb tuple to a hsl tuple.
    Does not create an HSL object.
    """
    # Normalize
    r_, g_, b_ = NormalizeRgb(*ConstrainRGB(r,g,b))
    # Find max and min
    Max = max(r_, g_, b_)
    Min = min(r_, g_, b_)

    # Assemble delta to be used later
    Delta = Max - Min

    # Find Hue
    if Delta == 0:
        Hue = 0
    elif r_ == Max:  # Red value is Max
        Hue = 60 * (((g_ - b_) / Delta) % 6.)
    elif g_ == Max:  # Green value is Max
        Hue = 60 * (((b_ - r_) / Delta) + 2)
    else:  # Blue value is Max
        Hue = 60 * (((r_ - g_) / Delta) + 4)

    # Find Luminance
    Lum = (Max+Min)/2

    # Find Saturation
    if Delta == 0:
        Sat = 0
    else:
        Sat = Delta/(1-abs((2*Lum)-1))

    return (
        Hue,    # H
        Sat,    # S
        Lum     # L
    )

@testHEX
def hex_to_hsl(hexadecimal:str) -> tuple[float,float,float]:
    """
    Function to convert a hexadecimal string to a hsl tuple.
    Does not create an HSL object.
    """
    return rgb_to_hsl(*hex_to_rgb(hexadecimal))

@testHSV
def hsv_to_hsl(h:float,s:float,v:float) -> tuple[float,float,float]:
    """
    Function to convert a hsv tuple to a hsl tuple.
    Does not create an HSL object.
    """
    return rgb_to_hsl(*hsv_to_rgb(*ConstrainHSV(h,s,v)))

@testCMYK
def cmyk_to_hsl(c:float,m:float,y:float,k:float) -> tuple[float,float,float]:
    """
    Function to convert a cmyk tuple to a hsl tuple.
    Does not create an HSL object.
    """
    return rgb_to_hsl(*cmyk_to_rgb(*ConstrainCMYK(c,m,y,k)))

# ----------------------------------------------------------------------------------------------------------------------
# - TRANSPARENT COLORS -
# ----------------------------------------------------------------------------------------------------------------------
@testHEXA
def hexa_to_rgba(hexadecimal:str) -> tuple[int,int,int,int]:
    """
    Function to convert a hexadecimal string to a rgb tuple.
    Does not create an RGBA object.
    """
    # Form hex value in usable state (cast away the '#' value)
    if hexadecimal[0] == "#":
        hex_v = hexadecimal[1:]
    elif len(hexadecimal) == 8:
        hex_v = hexadecimal
    else:
        raise ValueError("Hexadecimal was given in an incorrect format")

    # Actually convert to rgb integers
    r, g, b, a = tuple(
        int(hex_v[i:i + 2], 16)
        for i in (0, 2, 4,6)
    )

    return r, g, b, a
@testRGBA
def rgba_to_hexa(r:int,g:int,b:int,a:int) -> str:
    """
    Function to convert a rgba tuple to a hexa string.
    Does not create an HEXA object.
    """
    return '#%02x%02x%02x%02x' % ConstrainRGBA(r,g,b,a)
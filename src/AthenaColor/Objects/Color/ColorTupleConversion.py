# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Tuple

# Custom Library

# Custom Packages
from AthenaColor.Functions.General import (
    Normalize,RoundHalfUp,RoundToDecimals
)
from AthenaColor.Functions.Constraints import (
    ConstrainHSV, ConstrainHSL, ConstrainRGB, ConstrainCMYK,ConstrainRGBA
)
from AthenaColor.Functions.TypeTesting import InputTest

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = [
    "hsl_to_hsv","hsv_to_hsl","hex_to_hsl","hsl_to_hex","hex_to_hsv","hsv_to_hex","rgb_to_hsl","hsl_to_rgb",
    "rgb_to_hsv","hsv_to_rgb","hsv_to_cmyk","cmyk_to_hsv","cmyk_to_hsl","hsl_to_cmyk","hex_to_cmyk","cmyk_to_hex",
    "rgb_to_cmyk","cmyk_to_rgb","hex_to_rgb","hexa_to_rgba","rgba_to_hexa","rgb_to_hex"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def NormalizeRgb(r:int,g:int,b:int) -> Tuple[float, ...]:
    return Normalize(r,255),Normalize(g,255),Normalize(b,255)

# ----------------------------------------------------------------------------------------------------------------------
# - RGB -
# ----------------------------------------------------------------------------------------------------------------------
@InputTest.str
def hex_to_rgb(hexadecimal:str) -> Tuple[int, ...]:
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
    return tuple(
        int(hex_v[i:i + 2], 16)
        for i in (0, 2, 4)
    )

@InputTest.number
def hsv_to_rgb(h:int|float,s:int|float,v:int|float) -> Tuple[int,int,int]:
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
        RoundHalfUp((r_ + m) * 255),
        RoundHalfUp((g_ + m) * 255),
        RoundHalfUp((b_ + m) * 255)
    )

@InputTest.number
def cmyk_to_rgb(c:int|float,m:int|float,y:int|float,k:int|float) -> Tuple[int,int,int]:
    """
    Function to convert a cmyk tuple to a rgb tuple.
    Does not create an RGB object.
    """
    c,m,y,k = ConstrainCMYK(c,m,y,k)
    return (
        RoundHalfUp(255 * (1 - c) * (1 - k)),  #r
        RoundHalfUp(255 * (1 - m) * (1 - k)),  #g
        RoundHalfUp(255 * (1 - y) * (1 - k))  #b
    )

@InputTest.number
def hsl_to_rgb(h:int|float,s:int|float,l:int|float) -> Tuple[int,int,int]:
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
        RoundHalfUp((r_ + m) * 255),
        RoundHalfUp((g_ + m) * 255),
        RoundHalfUp((b_ + m) * 255)
    )

# ----------------------------------------------------------------------------------------------------------------------
# - Hexadecimal -
# ----------------------------------------------------------------------------------------------------------------------
@InputTest.number
def rgb_to_hex(r:int,g:int,b:int) -> str:
    """
    Function to convert a rgb to a hexadecimal string.
    Does not create a HEX object.
    """
    return '#%02x%02x%02x' % ConstrainRGB(int(r),int(g),int(b))

@InputTest.number
def hsv_to_hex(h:int|float,s:int|float, v:int|float) -> str:
    """
    Function to convert a hsv to a hexadecimal string.
    Does not create a HEX object.
    """
    return rgb_to_hex(*hsv_to_rgb(*ConstrainHSV(h,s,v)))

@InputTest.number
def cmyk_to_hex(c:int|float,m:int|float,y:int|float,k:int|float) -> str:
    """
    Function to convert a cmyk to a hexadecimal string.
    Does not create a HEX object.
    """
    return rgb_to_hex(*cmyk_to_rgb(*ConstrainCMYK(c,m,y,k)))

@InputTest.number
def hsl_to_hex(h:int|float,s:int|float,l:int|float) -> str:
    """
    Function to convert a hsl to a hexadecimal string.
    Does not create a HEX object.
    """
    return rgb_to_hex(*hsl_to_rgb(*ConstrainHSL(h,s,l)))


# ----------------------------------------------------------------------------------------------------------------------
# - HSV -
# ----------------------------------------------------------------------------------------------------------------------
@InputTest.number
def rgb_to_hsv(r:int,g:int,b:int) -> Tuple[float,float,float]:
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

    return (
        RoundToDecimals(Hue),
        RoundToDecimals(Delta/Max if Max != 0 else 0),
        RoundToDecimals(Max)
    )

@InputTest.str
def hex_to_hsv(hexadecimal:str) -> Tuple[float,float,float]:
    """
    Function to convert a hexadecimal string to a hsv tuple.
    Does not create an HSV object.
    """
    return rgb_to_hsv(*hex_to_rgb(hexadecimal))

@InputTest.number
def cmyk_to_hsv(c:int|float,m:int|float,y:int|float,k:int|float) -> Tuple[float,float,float]:
    """
    Function to convert a cmyk tuple to a hsv tuple.
    Does not create an HSV object.
    """
    return rgb_to_hsv(*cmyk_to_rgb(*ConstrainCMYK(c,m,y,k)))

@InputTest.number
def hsl_to_hsv(h:int|float,s:int|float,l:int|float) -> Tuple[float,float,float]:
    """
    Function to convert a hsl tuple to a hsv tuple.
    Does not create an HSV object.
    """
    return rgb_to_hsv(*hsl_to_rgb(*ConstrainHSL(h,s,l)))

# ----------------------------------------------------------------------------------------------------------------------
# - CMYK -
# ----------------------------------------------------------------------------------------------------------------------
@InputTest.number
def rgb_to_cmyk(r:int,g:int,b:int) -> Tuple[float,float,float,float]:
    """
    Function to convert a rgb tuple to a cmyk tuple.
    Does not create an CMYK object.
    """
    # Normalize
    r_, g_, b_ = NormalizeRgb(*ConstrainRGB(r,g,b))
    k = 1 - max(r_, g_, b_)

    return (
        RoundToDecimals((1 - r_ - k) / (1 - k)),
        RoundToDecimals((1 - g_ - k) / (1 - k)),
        RoundToDecimals((1 - b_ - k) / (1 - k)),
        RoundToDecimals(k)
    )

@InputTest.str
def hex_to_cmyk(hexadecimal:str) -> Tuple[float,float,float,float]:
    """
    Function to convert a hexadecimal string to a cmyk tuple.
    Does not create an CMYK object.
    """
    return rgb_to_cmyk(*hex_to_rgb(hexadecimal))

@InputTest.number
def hsv_to_cmyk(h:int|float,s:int|float,v:int|float) -> Tuple[float,float,float,float]:
    """
    Function to convert a hsv tuple to a cmyk tuple.
    Does not create an CMYK object.
    """
    return rgb_to_cmyk(*hsv_to_rgb(*ConstrainHSV(h,s,v)))

@InputTest.number
def hsl_to_cmyk(h:int|float,s:int|float,l:int|float) -> Tuple[float,float,float,float]:
    """
    Function to convert a hsl tuple to a cmyk tuple.
    Does not create an CMYK object.
    """
    return rgb_to_cmyk(*hsl_to_rgb(*ConstrainHSL(h,s,l)))

# ----------------------------------------------------------------------------------------------------------------------
# - HSL -
# ----------------------------------------------------------------------------------------------------------------------
@InputTest.number
def rgb_to_hsl(r:int,g:int,b:int) -> Tuple[float,float,float]:
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

    return (
        RoundToDecimals(Hue),    # H
        RoundToDecimals(Delta/(1-abs((2*Lum)-1)) if Delta != 0 else 0),
        RoundToDecimals(Lum)     # L
    )

@InputTest.str
def hex_to_hsl(hexadecimal:str) -> Tuple[float,float,float]:
    """
    Function to convert a hexadecimal string to a hsl tuple.
    Does not create an HSL object.
    """
    return rgb_to_hsl(*hex_to_rgb(hexadecimal))

@InputTest.number
def hsv_to_hsl(h:int|float,s:int|float,v:int|float) -> Tuple[float,float,float]:
    """
    Function to convert a hsv tuple to a hsl tuple.
    Does not create an HSL object.
    """
    return rgb_to_hsl(*hsv_to_rgb(*ConstrainHSV(h,s,v)))

@InputTest.number
def cmyk_to_hsl(c:int|float,m:int|float,y:int|float,k:int|float) -> Tuple[float,float,float]:
    """
    Function to convert a cmyk tuple to a hsl tuple.
    Does not create an HSL object.
    """
    return rgb_to_hsl(*cmyk_to_rgb(*ConstrainCMYK(c,m,y,k)))

# ----------------------------------------------------------------------------------------------------------------------
# - TRANSPARENT COLORS -
# ----------------------------------------------------------------------------------------------------------------------
@InputTest.str
def hexa_to_rgba(hexadecimal:str) -> Tuple[int,...]:
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

    return tuple(
        int(hex_v[i:i + 2], 16)
        for i in (0, 2, 4,6)
    )
@InputTest.number
def rgba_to_hexa(r:int,g:int,b:int,a:int) -> str:
    """
    Function to convert a rgba tuple to a hexa string.
    Does not create an HEXA object.
    """
    return '#%02x%02x%02x%02x' % ConstrainRGBA(r,g,b,a)
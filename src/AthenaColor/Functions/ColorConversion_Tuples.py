__all__ = [
    # to RGB
    "hex_to_rgb", "hsv_to_rgb", "cmyk_to_rgb", "hsl_to_rgb",
    # to hexadecimal
    "rgb_to_hex","hsv_to_hex","cmyk_to_hex","hsl_to_hex",
    # to HSV
    "rgb_to_hsv", "hexa_to_hsv", "cmyk_to_hsv", "hsl_to_hsv",
    # to CMYK
    "rgb_to_cmyk", "hex_to_cmyk", "hsv_to_cmyk", "hsl_to_cmyk",
    # to HSL
    "rgb_to_hsl","hex_to_hsl","cmyk_to_hsl","hsv_to_hsl",
]

# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from .BoilerPlate import (
    NormalizeRgb,
    TestTypes,
    testRGB_Tuple,
    testHSV_Tuple,
    testHSL_Tuple,
    testCMYK_Tuple,
    testHEX_Tuple
)

# ----------------------------------------------------------------------------------------------------------------------
# - RGB -
# ----------------------------------------------------------------------------------------------------------------------
@testHEX_Tuple
def hex_to_rgb(hexadecimal:str) -> tuple[int,int,int]:
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

@testHSV_Tuple
def hsv_to_rgb(h:float,s:float,v:float) -> tuple[int,int,int]:
    if not TestTypes(types=(int,float), objects=(h,s,v)):
        raise ValueError("HSV values did not consist of integer or float values")

    C = v*s
    X = C*(1-abs(
        ((h/60)%2)-1)
           )
    m = v-C

    if 0 <= h < 60:
        r_,g_,b_ = C,X,0
    elif 60 <= h < 120:
        r_,g_,b_ = X,C,0
    elif 120 <= h < 180:
        r_,g_,b_ = 0,C,X
    elif 180 <= h < 240:
        r_,g_,b_ = 0,X,C
    elif 240 <= h < 300:
        r_,g_,b_ = X,0,C
    else: #300 <= h < 360
        r_,g_,b_ = C,0,X

    return (
        round((r_+m)*255) ,
        round((g_+m)*255) ,
        round((b_+m)*255)
    )

@testCMYK_Tuple
def cmyk_to_rgb(c:float,m:float,y:float,k:float) -> tuple[int,int,int]:
    return (
        round(255*(1-c)*(1-k)),#r
        round(255*(1-m)*(1-k)),#g
        round(255*(1-y)*(1-k)) #b
    )

@testHSL_Tuple
def hsl_to_rgb(h:float,s:float,l:float) -> tuple[int,int,int]:
    C = (1-abs((2*l)-1))*s
    X = C*(1-abs(((h/60)%2)-1))
    m = l-(C/2)

    if 0 <= h < 60:
        r_,g_,b_ = C,X,0
    elif 60 <= h < 120:
        r_,g_,b_ = X,C,0
    elif 120 <= h < 180:
        r_,g_,b_ = 0,C,X
    elif 180 <= h < 240:
        r_,g_,b_ = 0,X,C
    elif 240 <= h < 300:
        r_,g_,b_ = X,0,C
    else: #300 <= h < 360
        r_,g_,b_ = C,0,X

    return (
        round((r_+m)*255) ,
        round((g_+m)*255) ,
        round((b_+m)*255)
    )

# ----------------------------------------------------------------------------------------------------------------------
# - Hexadecimal -
# ----------------------------------------------------------------------------------------------------------------------
@testRGB_Tuple
def rgb_to_hex(r:int,g:int,b:int) -> str:
    return '#%02x%02x%02x' % (r, g, b)

@testHSV_Tuple
def hsv_to_hex(h:int|float,s:int|float, v:int|float) -> str:
    return rgb_to_hex(*hsv_to_rgb(h,s,v))

@testCMYK_Tuple
def cmyk_to_hex(c:int|float,m:int|float,y:int|float,k:int|float) -> str:
    return rgb_to_hex(*cmyk_to_rgb(c,m,y,k))

@testHSL_Tuple
def hsl_to_hex(h:int|float,s:int|float,l:int|float) -> str:
    return rgb_to_hex(*hsl_to_rgb(h,s,l))


# ----------------------------------------------------------------------------------------------------------------------
# - HSV -
# ----------------------------------------------------------------------------------------------------------------------
@testRGB_Tuple
def rgb_to_hsv(r:int,g:int,b:int) -> tuple[float,float,float]:
    # Normalize
    r_,g_,b_ = NormalizeRgb(r,g,b)

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

@testHEX_Tuple
def hexa_to_hsv(hexadecimal:str) -> tuple[float,float,float]:
    return rgb_to_hsv(*hex_to_rgb(hexadecimal))

@testCMYK_Tuple
def cmyk_to_hsv(c:float,m:float,y:float,k:float) -> tuple[float,float,float]:
    return rgb_to_hsv(*cmyk_to_rgb(c,m,y,k))

@testHSL_Tuple
def hsl_to_hsv(h:float,s:float,l:float) -> tuple[float,float,float]:
    return rgb_to_hsv(*hsl_to_rgb(h,s,l))

# ----------------------------------------------------------------------------------------------------------------------
# - CMYK -
# ----------------------------------------------------------------------------------------------------------------------
@testRGB_Tuple
def rgb_to_cmyk(r:int,g:int,b:int) -> tuple[float,float,float,float]:
    # Normalize
    r_, g_, b_ = NormalizeRgb(r, g, b)
    K = 1 - max(r_, g_, b_)

    return (
        (1-r_-K) / (1/K), #C
        (1-g_-K) / (1/K), #M
        (1-b_-K) / (1/K), #Y
        K
    )

@testHEX_Tuple
def hex_to_cmyk(hexadecimal:str) -> tuple[float,float,float,float]:
    return rgb_to_cmyk(*hex_to_rgb(hexadecimal))

@testHSV_Tuple
def hsv_to_cmyk(h:float,s:float,v:float) -> tuple[float,float,float,float]:
    return rgb_to_cmyk(*hsv_to_rgb(h,s,v))

@testHSL_Tuple
def hsl_to_cmyk(h:float,s:float,l:float) -> tuple[float,float,float,float]:
    return rgb_to_cmyk(*hsl_to_rgb(h,s,l))

# ----------------------------------------------------------------------------------------------------------------------
# - HSL -
# ----------------------------------------------------------------------------------------------------------------------
@testRGB_Tuple
def rgb_to_hsl(r:int,g:int,b:int) -> tuple[float,float,float]:
    # Normalize
    r_, g_, b_ = NormalizeRgb(r, g, b)
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
    if Max == 0:
        Sat = 0
    else:
        Sat = 1-abs((2*Lum)-1)

    return (
        Hue,    # H
        Sat,    # S
        Lum     # L
    )

@testHEX_Tuple
def hex_to_hsl(hexadecimal:str) -> tuple[float,float,float]:
    return rgb_to_hsl(*hex_to_rgb(hexadecimal))

@testHSV_Tuple
def hsv_to_hsl(h:float,s:float,v:float) -> tuple[float,float,float]:
    return rgb_to_hsl(*hsv_to_rgb(h,s,v))

@testCMYK_Tuple
def cmyk_to_hsl(c:float,m:float,y:float,k:float) -> tuple[float,float,float]:
    return rgb_to_hsl(*cmyk_to_rgb(c,m,y,k))
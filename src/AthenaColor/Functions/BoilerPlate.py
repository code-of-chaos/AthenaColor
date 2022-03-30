# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from typing import Any

# Custom Library

# Custom Packages
from AthenaColor.Objects import (
    RGB,
    HEX,
    HSL,
    HSV,
    CMYK
)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def NormalizeRgb(r:int,g:int,b:int) -> tuple[float,float,float]:
    return r/255,g/255,b/255

def TestTypes(types: Any, objects:object|tuple[object]) -> bool:
    return all(map(lambda n: isinstance(n, types),objects))

# ----------------------------------------------------------------------------------------------------------------------
# - Support Decorators for testing -
# ----------------------------------------------------------------------------------------------------------------------
# RGB tests
def testRGB_Tuple(fnc):
    def wrapper(*args,**kwargs):
        if not TestTypes(types=int, objects=(*args,*kwargs.values())):
            raise ValueError(f"RGB values did not consist of integer values")
        return fnc(*args,**kwargs)
    return wrapper

def testRGB(fnc):
    def wrapper(*args,**kwargs):
        if not TestTypes(types=RGB, objects=(*args,*kwargs.values())):
            raise ValueError(f"No RGB object given")
        return fnc(*args,**kwargs)
    return wrapper

# HEX tests
def testHEX_Tuple(fnc):
    def wrapper(*args,**kwargs):
        if not TestTypes(types=str, objects=(*args,*kwargs.values())):
            raise ValueError(f"HEX values did not consist of a string value")
        return fnc(*args,**kwargs)
    return wrapper

def testHEX(fnc):
    def wrapper(*args,**kwargs):
        if not TestTypes(types=HEX, objects=(*args,*kwargs.values())):
            raise ValueError(f"No HEX object given")
        return fnc(*args,**kwargs)
    return wrapper

# HSV tests
def testHSV_Tuple(fnc):
    def wrapper(*args,**kwargs):
        if not TestTypes(types=(int,float), objects=(*args,*kwargs.values())):
            raise ValueError(f"HSL values did not consist of integer or float values")
        return fnc(*args,**kwargs)
    return wrapper

def testHSV(fnc):
    def wrapper(*args,**kwargs):
        if not TestTypes(types=HSV, objects=(*args,*kwargs.values())):
            raise ValueError(f"No HSV object given")
        return fnc(*args,**kwargs)
    return wrapper

# HSL tests
def testHSL_Tuple(fnc):
    def wrapper(*args,**kwargs):
        if not TestTypes(types=(int,float), objects=(*args,*kwargs.values())):
            raise ValueError(f"HSL values did not consist of integer or float values")
        return fnc(*args,**kwargs)
    return wrapper

def testHSL(fnc):
    def wrapper(*args,**kwargs):
        if not TestTypes(types=HSL, objects=(*args,*kwargs.values())):
            raise ValueError(f"No HSL object given")
        return fnc(*args,**kwargs)
    return wrapper

# CMYK tests
def testCMYK_Tuple(fnc):
    def wrapper(*args,**kwargs):
        if not TestTypes(types=(int,float), objects=(*args,*kwargs.values())):
            raise ValueError(f"CMYK values did not consist of integer or float values")
        return fnc(*args,**kwargs)
    return wrapper

def testCMYK(fnc):
    def wrapper(*args,**kwargs):
        if not TestTypes(types=CMYK, objects=(*args,*kwargs.values())):
            raise ValueError(f"No CMYK object given")
        return fnc(*args,**kwargs)
    return wrapper
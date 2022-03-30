# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor.Objects import (
    RGB,
    HEX,
    HSL,
    HSV,
    CMYK
)
from .BoilerPlate import TestTypes

# ----------------------------------------------------------------------------------------------------------------------
# - Support Decorators for testing -
# ----------------------------------------------------------------------------------------------------------------------

# RGB tests
def testRGB(fnc):
    def wrapper(*args,**kwargs):
        if not TestTypes(types=RGB, objects=(*args,*kwargs.values())):
            raise ValueError(f"No RGB object given")
        return fnc(*args,**kwargs)
    return wrapper

# HEX tests
def testHEX(fnc):
    def wrapper(*args,**kwargs):
        if not TestTypes(types=HEX, objects=(*args,*kwargs.values())):
            raise ValueError(f"No HEX object given")
        return fnc(*args,**kwargs)
    return wrapper

# HSV tests
def testHSV(fnc):
    def wrapper(*args,**kwargs):
        if not TestTypes(types=HSV, objects=(*args,*kwargs.values())):
            raise ValueError(f"No HSV object given")
        return fnc(*args,**kwargs)
    return wrapper

# HSL tests
def testHSL(fnc):
    def wrapper(*args,**kwargs):
        if not TestTypes(types=HSL, objects=(*args,*kwargs.values())):
            raise ValueError(f"No HSL object given")
        return fnc(*args,**kwargs)
    return wrapper

# CMYK tests
def testCMYK(fnc):
    def wrapper(*args,**kwargs):
        if not TestTypes(types=CMYK, objects=(*args,*kwargs.values())):
            raise ValueError(f"No CMYK object given")
        return fnc(*args,**kwargs)
    return wrapper
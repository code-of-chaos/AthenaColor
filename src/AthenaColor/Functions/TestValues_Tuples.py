# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from .BoilerPlate import TestTypes

# ----------------------------------------------------------------------------------------------------------------------
# - Support Decorators for testing -
# ----------------------------------------------------------------------------------------------------------------------

# RGB tests
def testRGB_Tuple(fnc):
    def wrapper(*args,**kwargs):
        if not TestTypes(
                types=int,
                objects=(arguments:= args if not kwargs else (*args,*kwargs.values()))
        ):
            raise ValueError(f"RGB values {arguments=} did not consist of integer values")
        return fnc(*args,**kwargs)
    return wrapper

# HEX tests
def testHEX_Tuple(fnc):
    def wrapper(*args,**kwargs):
        if not TestTypes(
                types=str,
                objects=(arguments:= args if not kwargs else (*args,*kwargs.values()))
        ):
            raise ValueError(f"HEX values {arguments=} did not consist of a string value")
        return fnc(*args,**kwargs)
    return wrapper

# HSV tests
def testHSV_Tuple(fnc):
    def wrapper(*args,**kwargs):
        if not TestTypes(
                types=(int,float),
                objects=(arguments:= args if not kwargs else (*args,*kwargs.values()))
        ):
            raise ValueError(f"HSV values {arguments=} did not consist of integer or float values")
        return fnc(*args,**kwargs)
    return wrapper

# HSL tests
def testHSL_Tuple(fnc):
    def wrapper(*args,**kwargs):
        if not TestTypes(
                types=(int,float),
                objects=(arguments:= args if not kwargs else (*args,*kwargs.values()))
        ):
            raise ValueError(f"HSL values {arguments=} did not consist of integer or float values")
        return fnc(*args,**kwargs)
    return wrapper

# CMYK tests
def testCMYK_Tuple(fnc):
    def wrapper(*args,**kwargs):
        if not TestTypes(
                types=(int,float),
                objects=(arguments:= args if not kwargs else (*args,*kwargs.values()))
        ):
            raise ValueError(f"CMYK values {arguments=} did not consist of integer or float values")
        return fnc(*args,**kwargs)
    return wrapper
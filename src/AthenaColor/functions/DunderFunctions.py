# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import operator

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = [
    "add", "sub", "mul", "truediv", "floordiv", "mod", "power",
    "gt", "ge", "lt", "le", "eq", "ne"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Math Dunders -
# ----------------------------------------------------------------------------------------------------------------------
def add(left:tuple, right:tuple)->tuple:
    return tuple(map(operator.add, left, right))

def sub(left:tuple, right:tuple)->tuple:
    return tuple(map(operator.sub, left, right))

def mul(left:tuple, right:tuple)->tuple:
    return tuple(map(operator.mul, left, right))

def floordiv(left:tuple, right:tuple)->tuple:
    return tuple(map(operator.floordiv, left, right))

def truediv(left:tuple, right:tuple)->tuple:
    return tuple(map(operator.truediv, left, right))

def mod(left:tuple, right:tuple)->tuple:
    return tuple(map(operator.mod, left, right))

def power(left:tuple, right:tuple)->tuple:
    return tuple(map(operator.pow, left, right))

def divmod_function(left:tuple, right:tuple)->tuple:
    return floordiv(left,right), mod(left,right)

# ----------------------------------------------------------------------------------------------------------------------
# - Comparator Dunders -
# ----------------------------------------------------------------------------------------------------------------------
def gt(left:tuple,right:tuple)->bool:
    return all(map(operator.gt, left, right))

def lt(left:tuple,right:tuple)->bool:
    return all(map(operator.lt, left, right))

def eq(left:tuple,right:tuple)->bool:
    return all(map(operator.eq, left, right))

def ne(left:tuple,right:tuple)->bool:
    return all(map(operator.ne, left, right))

def le(left:tuple,right:tuple)->bool:
    return all(map(operator.le, left, right))

def ge(left:tuple,right:tuple)->bool:
    return all(map(operator.ge, left, right))
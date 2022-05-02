# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

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
    return tuple(
        lr[0] + lr[1]
        for lr in zip(left, right)
    )

def sub(left:tuple, right:tuple)->tuple:
    return tuple(
        lr[0] - lr[1]
        for lr in zip(left, right)
    )

def mul(left:tuple, right:tuple)->tuple:
    return tuple(
        lr[0] * lr[1]
        for lr in zip(left, right)
    )

def floordiv(left:tuple, right:tuple)->tuple:
    return tuple(
        lr[0] // lr[1]
        for lr in zip(left, right)
    )

def truediv(left:tuple, right:tuple)->tuple:
    return tuple(
        lr[0] / lr[1]
        for lr in zip(left, right)
    )

def mod(left:tuple, right:tuple)->tuple:
    return tuple(
        lr[0] % lr[1]
        for lr in zip(left, right)
    )

def power(left:tuple, right:tuple)->tuple:
    return tuple(
        lr[0] ** lr[1]
        for lr in zip(left, right)
    )

# ----------------------------------------------------------------------------------------------------------------------
# - Comparator Dunders -
# ----------------------------------------------------------------------------------------------------------------------
def gt(left:tuple,right:tuple)->bool:
    return all(
        lr[0] > lr[1]
        for lr in zip(left, right)
    )

def lt(left:tuple,right:tuple)->bool:
    return all(
        lr[0] < lr[1]
        for lr in zip(left, right)
    )

def eq(left:tuple,right:tuple)->bool:
    return all(
        lr[0] == lr[1]
        for lr in zip(left, right)
    )

def ne(left:tuple,right:tuple)->bool:
    return all(
        lr[0] != lr[1]
        for lr in zip(left, right)
    )

def le(left:tuple,right:tuple)->bool:
    return all(
        lr[0] <= lr[1]
        for lr in zip(left, right)
    )

def ge(left:tuple,right:tuple)->bool:
    return all(
        lr[0] >= lr[1]
        for lr in zip(left, right)
    )
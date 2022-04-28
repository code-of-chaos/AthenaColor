# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor.AthenaLib.StrictAnnotated import StrictAnnotated

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = [
    "add", "sub", "mul", "truediv", "floordiv", "mod", "pow",
    "gt", "ge", "lt", "le", "eq", "ne"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Math Dunders -
# ----------------------------------------------------------------------------------------------------------------------
@StrictAnnotated
def add(left:tuple, right:tuple)->tuple:
    return tuple(
        lr[0] + lr[1]
        for lr in zip(left, right)
    )

@StrictAnnotated
def sub(left:tuple, right:tuple)->tuple:
    return tuple(
        lr[0] - lr[1]
        for lr in zip(left, right)
    )

@StrictAnnotated
def mul(left:tuple, right:tuple)->tuple:
    return tuple(
        lr[0] * lr[1]
        for lr in zip(left, right)
    )

@StrictAnnotated
def floordiv(left:tuple, right:tuple)->tuple:
    return tuple(
        lr[0] // lr[1]
        for lr in zip(left, right)
    )

@StrictAnnotated
def truediv(left:tuple, right:tuple)->tuple:
    return tuple(
        lr[0] / lr[1]
        for lr in zip(left, right)
    )

@StrictAnnotated
def mod(left:tuple, right:tuple)->tuple:
    return tuple(
        lr[0] % lr[1]
        for lr in zip(left, right)
    )
# noinspection PyShadowingBuiltins
@StrictAnnotated
def pow(left:tuple, right:tuple)->tuple:
    return tuple(
        lr[0] ** lr[1]
        for lr in zip(left, right)
    )

# ----------------------------------------------------------------------------------------------------------------------
# - Comparator Dunders -
# ----------------------------------------------------------------------------------------------------------------------
@StrictAnnotated
def gt(left:tuple,right:tuple)->bool:
    return all(
        lr[0] > lr[1]
        for lr in zip(left, right)
    )

@StrictAnnotated
def lt(left:tuple,right:tuple)->bool:
    return all(
        lr[0] < lr[1]
        for lr in zip(left, right)
    )

@StrictAnnotated
def eq(left:tuple,right:tuple)->bool:
    return all(
        lr[0] == lr[1]
        for lr in zip(left, right)
    )

@StrictAnnotated
def ne(left:tuple,right:tuple)->bool:
    return all(
        lr[0] != lr[1]
        for lr in zip(left, right)
    )

@StrictAnnotated
def le(left:tuple,right:tuple)->bool:
    return all(
        lr[0] <= lr[1]
        for lr in zip(left, right)
    )

@StrictAnnotated
def ge(left:tuple,right:tuple)->bool:
    return all(
        lr[0] >= lr[1]
        for lr in zip(left, right)
    )
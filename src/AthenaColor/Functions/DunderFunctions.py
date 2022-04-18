# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages

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
def add(left:tuple, right:tuple)->tuple:
    return tuple(
        lr[0] + lr[1]
        for lr in zip(left, right, strict=True)
    )
def sub(left:tuple, right:tuple)->tuple:
    return tuple(
        lr[0] - lr[1]
        for lr in zip(left, right, strict=True)
    )
def mul(left:tuple, right:tuple)->tuple:
    return tuple(
        lr[0] * lr[1]
        for lr in zip(left, right, strict=True)
    )
def floordiv(left:tuple, right:tuple)->tuple:
    return tuple(
        lr[0] // lr[1]
        for lr in zip(left, right, strict=True)
    )
def truediv(left:tuple, right:tuple)->tuple:
    return tuple(
        lr[0] / lr[1]
        for lr in zip(left, right, strict=True)
    )
def mod(left:tuple, right:tuple)->tuple:
    return tuple(
        lr[0] % lr[1]
        for lr in zip(left, right, strict=True)
    )
# noinspection PyShadowingBuiltins
def pow(left:tuple, right:tuple)->tuple:
    return tuple(
        lr[0] ** lr[1]
        for lr in zip(left, right, strict=True)
    )

# ----------------------------------------------------------------------------------------------------------------------
# - Comparator Dunders -
# ----------------------------------------------------------------------------------------------------------------------
def gt(left:tuple,right:tuple)->bool:
    return all(
        lr[0] > lr[1]
        for lr in zip(left, right, strict=True)
    )
def lt(left:tuple,right:tuple)->bool:
    return all(
        lr[0] < lr[1]
        for lr in zip(left, right, strict=True)
    )
def eq(left:tuple,right:tuple)->bool:
    return all(
        lr[0] == lr[1]
        for lr in zip(left, right, strict=True)
    )
def ne(left:tuple,right:tuple)->bool:
    return all(
        lr[0] != lr[1]
        for lr in zip(left, right, strict=True)
    )
def le(left:tuple,right:tuple)->bool:
    return all(
        lr[0] <= lr[1]
        for lr in zip(left, right, strict=True)
    )
def ge(left:tuple,right:tuple)->bool:
    return all(
        lr[0] >= lr[1]
        for lr in zip(left, right, strict=True)
    )
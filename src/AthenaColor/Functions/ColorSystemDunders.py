# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Math Dunders -
# ----------------------------------------------------------------------------------------------------------------------
def add(left:tuple, right:tuple)->tuple:
    return tuple(map(
        (lambda lr: lr[0] + lr[1]),
        zip(left, right)
    ))
def sub(left:tuple, right:tuple)->tuple:
    return tuple(map(
        (lambda lr: lr[0] - lr[1]),
        zip(left, right)
    ))
def mul(left:tuple, right:tuple)->tuple:
    return tuple(map(
        (lambda lr: lr[0] * lr[1]),
        zip(left, right)
    ))
def floordiv(left:tuple, right:tuple)->tuple:
    return tuple(map(
        (lambda lr: lr[0] // lr[1]),
        zip(left, right)
    ))
def truediv(left:tuple, right:tuple)->tuple:
    return tuple(map(
        (lambda lr: lr[0] / lr[1]),
        zip(left, right)
    ))
def mod(left:tuple, right:tuple)->tuple:
    return tuple(map(
        (lambda lr: lr[0] % lr[1]),
        zip(left, right)
    ))
def pow(left:tuple, right:tuple)->tuple:
    return tuple(map(
        (lambda lr: lr[0] ** lr[1]),
        zip(left, right)
    ))

# ----------------------------------------------------------------------------------------------------------------------
# - Comparator Dunders -
# ----------------------------------------------------------------------------------------------------------------------
def gt(left:tuple,right:tuple)->bool:
    return all(map(
        (lambda lr: lr[0] > lr[1]),
        zip(left, right)
    ))
def lt(left:tuple,right:tuple)->bool:
    return all(map(
        (lambda lr: lr[0] < lr[1]),
        zip(left, right)
    ))
def eq(left:tuple,right:tuple)->bool:
    return all(map(
        (lambda lr: lr[0] == lr[1]),
        zip(left, right)
    ))
def ne(left:tuple,right:tuple)->bool:
    return all(map(
        (lambda lr: lr[0] != lr[1]),
        zip(left, right)
    ))
def le(left:tuple,right:tuple)->bool:
    return all(map(
        (lambda lr: lr[0] <= lr[1]),
        zip(left, right)
    ))
def ge(left:tuple,right:tuple)->bool:
    return all(map(
        (lambda lr: lr[0] >= lr[1]),
        zip(left, right)
    ))
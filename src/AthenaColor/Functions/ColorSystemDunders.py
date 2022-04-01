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
    """
    Zips two tuples together and ADDS the elements of the zipped pairs together.
    Returns a tuple of the newly formed elements
    """
    return tuple(map(
        (lambda lr: lr[0] + lr[1]),
        zip(left, right)
    ))
def sub(left:tuple, right:tuple)->tuple:
    """
    Zips two tuples together and SUBTRACTS the elements of the zipped pairs from each other.
    Returns a tuple of the newly formed elements
    """
    return tuple(map(
        (lambda lr: lr[0] - lr[1]),
        zip(left, right)
    ))
def mul(left:tuple, right:tuple)->tuple:
    """
    Zips two tuples together and MULTIPLIES the elements of the zipped pairs together.
    Returns a tuple of the newly formed elements
    """
    return tuple(map(
        (lambda lr: lr[0] * lr[1]),
        zip(left, right)
    ))
def floordiv(left:tuple, right:tuple)->tuple:
    """
    Zips two tuples together and FLOOR DIVIDE the elements of the zipped pairs together.
    Returns a tuple of the newly formed elements
    """
    return tuple(map(
        (lambda lr: lr[0] // lr[1]),
        zip(left, right)
    ))
def truediv(left:tuple, right:tuple)->tuple:
    """
    Zips two tuples together and DIVIDES the elements of the zipped pairs together.
    Returns a tuple of the newly formed elements
    """
    return tuple(map(
        (lambda lr: lr[0] / lr[1]),
        zip(left, right)
    ))
def mod(left:tuple, right:tuple)->tuple:
    """
    Zips two tuples together and preforms a MODULO on the elements of the zipped pairs.
    Returns a tuple of the newly formed elements
    """
    return tuple(map(
        (lambda lr: lr[0] % lr[1]),
        zip(left, right)
    ))
def pow(left:tuple, right:tuple)->tuple:
    """
    Zips two tuples together and POWERS the elements of the zipped pairs together.
    Returns a tuple of the newly formed elements
    """
    return tuple(map(
        (lambda lr: lr[0] ** lr[1]),
        zip(left, right)
    ))

# ----------------------------------------------------------------------------------------------------------------------
# - Comparator Dunders -
# ----------------------------------------------------------------------------------------------------------------------
def gt(left:tuple,right:tuple)->bool:
    """
    Zips two tuples together and compares the elements of the zipped pairs against each other.
    Returns a TRUE value if all left-handed are GREATER THAN the right-handed sides.
    """
    return all(map(
        (lambda lr: lr[0] > lr[1]),
        zip(left, right)
    ))
def lt(left:tuple,right:tuple)->bool:
    """
    Zips two tuples together and compares the elements of the zipped pairs against each other.
    Returns a TRUE value if all left-handed are SMALLER THAN the right-handed sides.
    """
    return all(map(
        (lambda lr: lr[0] < lr[1]),
        zip(left, right)
    ))
def eq(left:tuple,right:tuple)->bool:
    """
    Zips two tuples together and compares the elements of the zipped pairs against each other.
    Returns a TRUE value if all left-handed are EQUAL TO the right-handed sides.
    """
    return all(map(
        (lambda lr: lr[0] == lr[1]),
        zip(left, right)
    ))
def ne(left:tuple,right:tuple)->bool:
    """
    Zips two tuples together and compares the elements of the zipped pairs against each other.
    Returns a TRUE value if all left-handed are NOT EQUAL TO the right-handed sides.
    """
    return all(map(
        (lambda lr: lr[0] != lr[1]),
        zip(left, right)
    ))
def le(left:tuple,right:tuple)->bool:
    """
    Zips two tuples together and compares the elements of the zipped pairs against each other.
    Returns a TRUE value if all left-handed are SMALLER OR EQUAL TO the right-handed sides.
    """
    return all(map(
        (lambda lr: lr[0] <= lr[1]),
        zip(left, right)
    ))
def ge(left:tuple,right:tuple)->bool:
    """
    Zips two tuples together and compares the elements of the zipped pairs against each other.
    Returns a TRUE value if all left-handed are GRATER OR EQUAL TO the right-handed sides.
    """
    return all(map(
        (lambda lr: lr[0] >= lr[1]),
        zip(left, right)
    ))
# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from typing import Iterable

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "StrictError",
    "StrictType",
    "StrictInput", "StrictOutput"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class StrictError(Exception):
    pass

def StrictType(types, objects):
    if isinstance(objects, Iterable):
        if not all(isinstance(n, types) for n in objects):
            raise StrictError
    else:
        if not isinstance(objects,types):
            raise StrictError

class StrictInput:
    """
    Decorator which runs TestTypes on the function's arguments.
    Raises a StrictError when not all off the arguments can be matched to the given type
    """
    # PreDefined
    @staticmethod
    def int(fnc):
        def wrapper(*args, **kwargs):
            StrictType(
                types=int,
                objects=(args if not kwargs else (*args, *kwargs.values()))
            )
            return fnc(*args, **kwargs)
        return wrapper

    @staticmethod
    def str(fnc):
        def wrapper(*args, **kwargs):
            StrictType(
                types=str,
                objects=(args if not kwargs else (*args, *kwargs.values()))
            )
            return fnc(*args, **kwargs)

        return wrapper

    @staticmethod
    def float(fnc):
        def wrapper(*args, **kwargs):
            StrictType(
                types=float,
                objects=(args if not kwargs else (*args, *kwargs.values()))
            )
            return fnc(*args, **kwargs)

        return wrapper

    @staticmethod
    def number(fnc):
        def wrapper(*args, **kwargs):
            StrictType(
                types=(float,int),
                objects=(args if not kwargs else (*args, *kwargs.values()))
            )
            return fnc(*args, **kwargs)

        return wrapper

    # Custom one
    @staticmethod
    def Custom(types):
        def decorator(fnc):
            def wrapper(*args, **kwargs):
                StrictType(
                    types=types,
                    objects=(args if not kwargs else (*args, *kwargs.values()))
                )
                return fnc(*args, **kwargs)
            return wrapper
        return decorator


class StrictOutput:
    """
    Decorator which runs TestTypes on the function's arguments.
    Raises a StrictError when not all off the arguments can be matched to the given type
    """

    # PreDefined
    @staticmethod
    def int(fnc):
        def wrapper(*args, **kwargs):
            result = fnc(*args, **kwargs)
            StrictType(types=int, objects=result)
            return result
        return wrapper

    @staticmethod
    def str(fnc):
        def wrapper(*args, **kwargs):
            result = fnc(*args, **kwargs)
            StrictType(types=str, objects=result)
            return result

        return wrapper

    @staticmethod
    def float(fnc):
        def wrapper(*args, **kwargs):
            result = fnc(*args, **kwargs)
            StrictType(types=float, objects=result)
            return result

        return wrapper

    # Custom one
    @staticmethod
    def Custom(types):
        def decorator(fnc):
            def wrapper(*args, **kwargs):
                result = fnc(*args, **kwargs)
                StrictType(types=types, objects=result)
                return result
            return wrapper
        return decorator

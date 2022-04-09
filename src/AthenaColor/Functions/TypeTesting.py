# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "TestTypes",
    "InputTest","OutputTest"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def TestTypes(types, objects) -> bool:
    """
    Runs an isinstance(object,(type,...)) against multiple objects.
    All have to pass, for the function to return a TRUE
    """
    return all(isinstance(n, types) for n in objects)

class InputTest:
    """
    Decorator which runs TestTypes on the function's arguments.
    Raises a ValueError when not all off the arguments can be matched to the given type
    """
    # PreDefined
    @staticmethod
    def int(fnc):
        def wrapper(*args, **kwargs):
            if not TestTypes(
                    types=int,
                    objects=(args if not kwargs else (*args, *kwargs.values()))
            ):
                raise ValueError
            return fnc(*args, **kwargs)

        return wrapper

    @staticmethod
    def str(fnc):
        def wrapper(*args, **kwargs):
            if not TestTypes(
                    types=str,
                    objects=(args if not kwargs else (*args, *kwargs.values()))
            ):
                raise ValueError
            return fnc(*args, **kwargs)

        return wrapper

    @staticmethod
    def float(fnc):
        def wrapper(*args, **kwargs):
            if not TestTypes(
                    types=float,
                    objects=(args if not kwargs else (*args, *kwargs.values()))
            ):
                raise ValueError
            return fnc(*args, **kwargs)

        return wrapper

    @staticmethod
    def number(fnc):
        def wrapper(*args, **kwargs):
            if not TestTypes(
                    types=(float,int),
                    objects=(args if not kwargs else (*args, *kwargs.values()))
            ):
                raise ValueError
            return fnc(*args, **kwargs)

        return wrapper

    # Custom one
    @staticmethod
    def Custom(types):
        def decorator(fnc):
            def wrapper(*args, **kwargs):
                if not TestTypes(
                        types=types,
                        objects=(args if not kwargs else (*args, *kwargs.values()))
                ):
                    raise ValueError
                return fnc(*args, **kwargs)
            return wrapper
        return decorator


class OutputTest:
    """
    Decorator which runs TestTypes on the function's arguments.
    Raises a ValueError when not all off the arguments can be matched to the given type
    """

    # PreDefined
    @staticmethod
    def int(fnc):
        def wrapper(*args, **kwargs):
            result = fnc(*args, **kwargs)
            if not TestTypes(types=int,objects=result):
                raise ValueError
            return result

        return wrapper

    @staticmethod
    def str(fnc):
        def wrapper(*args, **kwargs):
            result = fnc(*args, **kwargs)
            if not TestTypes(types=str,objects=result):
                raise ValueError
            return result

        return wrapper

    @staticmethod
    def float(fnc):
        def wrapper(*args, **kwargs):
            result = fnc(*args, **kwargs)
            if not TestTypes(types=float,objects=result):
                raise ValueError
            return result

        return wrapper

    # Custom one
    @staticmethod
    def Custom(types):
        def decorator(fnc):
            def wrapper(*args, **kwargs):
                result = fnc(*args, **kwargs)
                if not TestTypes(types=types,objects=result):
                    raise ValueError
                return result

            return wrapper

        return decorator

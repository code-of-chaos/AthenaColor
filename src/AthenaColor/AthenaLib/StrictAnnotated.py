# ----------------------------------------------------------------------------------------------------------------------
# - COMMENT -
# ----------------------------------------------------------------------------------------------------------------------
# Direct import from the AthenaLib
#   Done to be a true dependency less package
#   Some changes:
#       - init variable to enable or disable this functionality
#       - Compatibilty changes 3.7 to 3.10
#
# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import inspect
from typing import Callable,get_type_hints,Tuple, List

# Custom Library

# Custom Packages
from AthenaColor.InitClass import init
from AthenaColor.AthenaLib.SubscriptedGeneric import fix_SubscriptedGeneric_Full

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
class StrictError(TypeError):
    pass

_ErrorMsg= lambda val, t: f"'{val}' was not the same type as the expected Strongly typed: '{t}'"

def _TypeChecker(CombinedInput,annotation):
    for k, v in CombinedInput:
        if k in annotation:
            if not isinstance(v, annotation[k]):
                raise StrictError(_ErrorMsg(v, annotation[k]))

def _PrepFunction(fnc:Callable, method:bool=False) -> tuple[inspect.FullArgSpec,list[str], dict]:
    # do the inspection before a function is esxecuted
    #   as now it is only done once, instead of every function
    fncspec: inspect.FullArgSpec = inspect.getfullargspec(fnc)
    if method:
        fncspec_args = [a for a in fncspec.args if a != 'self']
    else:
        fncspec_args = fncspec.args

    if fncspec.varargs is not None:
        fncspec_args.append(fncspec.varargs)

    # Fix any Subscripted Generics so only the base type is checked
    try:
        annotation = get_type_hints(fnc)
    except TypeError: # a union was found basically
        # Fix for pre 3.10 stuff
        annotation = {}
        for k, v in fncspec.annotations.items():
            if isinstance(v, str):
                annotation[k] = eval(v.replace("|",","))
            else:
                annotation[k] = v

    return fncspec,fncspec_args, fix_SubscriptedGeneric_Full(annotation)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def StrictAnnotated(fnc):
    # - Special addition for AthenaColor -
    if not init.stictAnnotated:
        def wrapper(*args, **kwargs):
            return fnc(*args, **kwargs)
        return wrapper
    # ------------------------------------

    # Prepare and extract all information from function
    fncspec,fncspec_args,annotation = _PrepFunction(fnc)

    if fncspec.annotations and 'return' in fncspec.annotations:
        def wrapper(*args, **kwargs):
            _TypeChecker(CombinedInput=zip(fncspec_args, args), annotation=annotation)
            _TypeChecker(CombinedInput=kwargs.items(), annotation=annotation)

            result = fnc(*args, **kwargs)
            if not isinstance(result,annotation["return"]):
                raise StrictError(_ErrorMsg(result, fncspec.annotations["return"]))
            return result

    elif fncspec.annotations:
        def wrapper(*args, **kwargs):
            _TypeChecker(CombinedInput=zip(fncspec_args, args), annotation=annotation)
            _TypeChecker(CombinedInput=kwargs.items(), annotation=annotation)
            return fnc(*args, **kwargs)
    else:
        def wrapper(*args, **kwargs):
            return fnc(*args, **kwargs)

    return wrapper

def StrictAnnotatedMethod(fnc):
    # - Special addition for AthenaColor -
    if not init.stictAnnotated:
        def wrapper(*args, **kwargs):
            return fnc(*args, **kwargs)
        return wrapper
    # ------------------------------------

    # Prepare and extract all information from method
    fncspec,fncspec_args,annotation = _PrepFunction(fnc)

    if fncspec.annotations and 'return' in fncspec.annotations:
        def wrapper(self,*args, **kwargs):
            _TypeChecker(CombinedInput=zip(fncspec_args, args), annotation=annotation)
            _TypeChecker(CombinedInput=kwargs.items(), annotation=annotation)
            # noinspection PyTypeHints
            result = fnc(self,*args, **kwargs)
            if not isinstance(result,annotation["return"]):
                raise StrictError(_ErrorMsg(result, fncspec.annotations["return"]))
            return result

    elif fncspec.annotations:
        def wrapper(self,*args, **kwargs):
            _TypeChecker(CombinedInput=zip(fncspec_args, args), annotation=annotation)
            _TypeChecker(CombinedInput=kwargs.items(), annotation=annotation)
            return fnc(self,*args, **kwargs)
    else:
        def wrapper(self,*args, **kwargs):
            return fnc(self,*args, **kwargs)

    return wrapper
# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Iterable

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------

# SubscriptedGenericTypes = Union[_UnionGenericAlias,GenericAlias,_GenericAlias,UnionType]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def fix_SubscriptedGeneric(annotation:type) -> type:
    print(annotation)

    # if isinstance(annotation, _UnionGenericAlias):
    #     for a in annotation.__args__:
    #         if isinstance(a, GenericAlias|_GenericAlias):
    #             return a.__origin__
    #
    # if isinstance(annotation, GenericAlias|_GenericAlias):
    #     return annotation.__origin__
    #
    # elif isinstance(annotation, UnionType):
    #     return Union[tuple(a.__origin__ if isinstance(a, GenericAlias|_GenericAlias) else a for a in annotation.__args__)]

    return annotation

def fix_SubscriptedGeneric_Full(Iter:Iterable|dict) -> Iterable|dict:
    if isinstance(Iter, type):
        raise ValueError("A type cannot be in itself multi stripped")
    elif isinstance(Iter, dict):
        content = [(k, fix_SubscriptedGeneric(v)) for k,v in Iter.items()]
    else:
        content = [fix_SubscriptedGeneric(i) for i in Iter]
    return type(Iter)(content)
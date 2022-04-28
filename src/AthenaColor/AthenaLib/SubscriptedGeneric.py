# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import _GenericAlias, Iterable

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def fix_SubscriptedGeneric(annotation) -> type:
    if isinstance(annotation, _GenericAlias):
        return annotation.__origin__
    return annotation

def fix_SubscriptedGeneric_Full(Iter:Iterable|dict) -> Iterable|dict:
    if isinstance(Iter, type):
        raise ValueError("A type cannot be in itself multi stripped")
    elif isinstance(Iter, dict):
        content = [(k, fix_SubscriptedGeneric(v)) for k,v in Iter.items()]
    else:
        content = [fix_SubscriptedGeneric(i) for i in Iter]
    return type(Iter)(content)
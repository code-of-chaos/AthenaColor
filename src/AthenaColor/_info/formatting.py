# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaColor import ForeNest, StyleNest

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = [
    "title", "header", "sub_modules", "reference"
]
# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
# some helper commands to not have repeated stuff and style breaks between them
def title(title_text:str, to_str:bool):
    return StyleNest.Bold(title_text) if not to_str else title_text

def header(header_text:str, to_str:bool):
    return ForeNest.SlateGray(header_text) if not to_str else header_text

def sub_modules(module_text:str, to_str:bool):
    return StyleNest.Bold(ForeNest.Pink(module_text)) if not to_str else module_text

def reference(reference_text:str, to_str:bool):
    return StyleNest.Italic(reference_text) if not to_str else reference_text
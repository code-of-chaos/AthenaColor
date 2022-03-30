# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from abc import ABC, abstractmethod

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ColorSystem(ABC):
    @abstractmethod
    def __str__(self): ...
    @abstractmethod
    def __repr__(self): ...

    @abstractmethod
    def __add__(self, other: ColorSystem | int | float | tuple) -> ColorSystem: ...
    @abstractmethod
    def __sub__(self, other: ColorSystem | int | float | tuple) -> ColorSystem: ...
    @abstractmethod
    def __mul__(self, other: ColorSystem | int | float | tuple) -> ColorSystem: ...
    @abstractmethod
    def __floordiv__(self, other: ColorSystem | int | float | tuple) -> ColorSystem: ...
    @abstractmethod
    def __truediv__(self, other: ColorSystem | int | float | tuple) -> ColorSystem: ...
    @abstractmethod
    def __mod__(self, other: ColorSystem | int | float | tuple) -> ColorSystem: ...
    @abstractmethod
    def __pow__(self, other: ColorSystem | int | float | tuple) -> ColorSystem: ...

    @abstractmethod
    def __gt__(self, other: ColorSystem | int | float | tuple) -> bool: ...
    @abstractmethod
    def __lt__(self, other: ColorSystem | int | float | tuple) -> bool: ...
    @abstractmethod
    def __eq__(self, other: ColorSystem | int | float | tuple) -> bool: ...
    @abstractmethod
    def __ne__(self, other: ColorSystem | int | float | tuple) -> bool: ...
    @abstractmethod
    def __le__(self, other: ColorSystem | int | float | tuple) -> bool: ...
    @abstractmethod
    def __ge__(self, other: ColorSystem | int | float | tuple) -> bool: ...

    def __iadd__(self, other: ColorSystem | int | float | tuple) -> ColorSystem:
        return self.__add__(other)
    def __isub__(self, other: ColorSystem | int | float | tuple) -> ColorSystem:
        return self.__sub__(other)
    def __imul__(self, other: ColorSystem | int | float | tuple) -> ColorSystem:
        return self.__mul__(other)
    def __ifloordiv__(self, other: ColorSystem | int | float | tuple) -> ColorSystem:
        return self.__floordiv__(other)
    def __itruediv__(self, other: ColorSystem | int | float | tuple) -> ColorSystem:
        return self.__truediv__(other)
    def __imod__(self, other: ColorSystem | int | float | tuple) -> ColorSystem:
        return self.__mod__(other)
    def __ipow__(self, other: ColorSystem | int | float | tuple) -> ColorSystem:
        return self.__pow__(other)
from __future__ import annotations

from abc import ABC, abstractmethod


class ColorSystem(ABC):
    @abstractmethod
    def __str__(self): ...
    @abstractmethod
    def __repr__(self): ...

    @abstractmethod
    def __add__(self, other: ColorSystem | int | float): ...
    @abstractmethod
    def __sub__(self, other: ColorSystem | int | float): ...
    @abstractmethod
    def __mul__(self, other: ColorSystem | int | float): ...
    @abstractmethod
    def __floordiv__(self, other: ColorSystem | int | float): ...
    @abstractmethod
    def __truediv__(self, other: ColorSystem | int | float): ...
    @abstractmethod
    def __mod__(self, other: ColorSystem | int | float): ...
    @abstractmethod
    def __pow__(self, other: ColorSystem | int | float): ...

    @abstractmethod
    def __gt__(self, other: ColorSystem | int | float): ...
    @abstractmethod
    def __lt__(self, other: ColorSystem | int | float): ...
    @abstractmethod
    def __eq__(self, other: ColorSystem | int | float): ...
    @abstractmethod
    def __ne__(self, other: ColorSystem | int | float): ...
    @abstractmethod
    def __le__(self, other: ColorSystem | int | float): ...
    @abstractmethod
    def __ge__(self, other: ColorSystem | int | float): ...

    def __iadd__(self, other: ColorSystem | int | float) -> ColorSystem:
        return self.__add__(other)
    def __isub__(self, other: ColorSystem | int | float) -> ColorSystem:
        return self - other
    def __imul__(self, other: ColorSystem | int | float) -> ColorSystem:
        return self * other
    def __ifloordiv__(self, other: ColorSystem | int | float) -> ColorSystem:
        return self // other
    def __itruediv__(self, other: ColorSystem | int | float) -> ColorSystem:
        return self / other
    def __imod__(self, other: ColorSystem | int | float) -> ColorSystem:
        return self % other
    def __ipow__(self, other: ColorSystem | int | float) -> ColorSystem:
        return self ** other
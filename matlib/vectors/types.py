from __future__ import annotations

from decimal import Decimal
import functools
from typing import NamedTuple
from math import sqrt, sin, cos, atan2

class Vector(NamedTuple):
    """Vector Definition"""
    x: float
    y: float

    def __eq__(self, other):
        return self.x == other.x and \
            self.y == other.y

    @functools.singledispatchmethod
    def  __add__(self, _):
        raise NotImplementedError

    @functools.singledispatchmethod
    def __sub__(self, _):
        raise NotImplementedError

    @functools.singledispatchmethod
    def __mul__(self, _):
        raise NotImplementedError

    def length(self) -> float:
        """
        calculates the length
        Returns:
            float: length
        """
        return sqrt(self.x**2 + self.y**2)

    def to_polar(self) -> Vector:
        """
        converts to polar coordinate

        Returns:
            Vector: converted vector
        """
        return Vector(self.length(), atan2(self.y, self.x))

    def to_cartesian(self) -> Vector:
        """
        converts to cartesian coordinate

        Returns:
            Vector: converted vector
        """
        length, angle = self.x, self.y
        return Vector(length*cos(angle),length*sin(angle))

@Vector.__add__.register(Decimal) # pylint: disable=no-member
@Vector.__add__.register(float) # pylint: disable=no-member
@Vector.__add__.register(int) # pylint: disable=no-member
def  _(self, value):
    return Vector(self.x + value, self.y + value)

@Vector.__add__.register(Vector) # pylint: disable=no-member
def  _(self, other):
    return Vector(self.x + other.x, self.y + other.y)

@Vector.__sub__.register(Decimal) # pylint: disable=no-member
@Vector.__sub__.register(float) # pylint: disable=no-member
@Vector.__sub__.register(int) # pylint: disable=no-member
def  _(self, value):
    return Vector(self.x - value, self.y - value)

@Vector.__sub__.register(Vector) # pylint: disable=no-member
def  _(self, other):
    return Vector(self.x - other.x, self.y - other.y)

@Vector.__mul__.register(Decimal) # pylint: disable=no-member
@Vector.__mul__.register(float) # pylint: disable=no-member
@Vector.__mul__.register(int) # pylint: disable=no-member
def  _(self, value):
    return Vector(self.x * value, self.y * value)

@Vector.__mul__.register(Vector) # pylint: disable=no-member
def  _(self, other):
    return Vector(self.x * other.x, self.y * other.y)

def make_vector( v : tuple[float, float]) -> Vector:
    """
    converts a tuple(x,y) to a vector
    Args:
        v (tuple[float, float]): [description]

    Returns:
        Vector: [description]
    """
    return Vector._make(v)

def make_vectors( points : list[tuple[float, float]]) -> Vector:
    """
    converts a set of points to a Vector type.

    Args:
        points (list[tuple[float, float]]): points to convert

    Returns:
        Vector: new instance
    """
    return [make_vector(p) for p in points]

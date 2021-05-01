from decimal import Decimal
from typing import NamedTuple
from functools import singledispatchmethod
from math import sqrt, sin, cos, atan2

class Vector(NamedTuple):
    """Vector Definition"""
    x: float
    y: float

    def __eq__(self, other):
        return self.x == other.x and \
            self.y == other.y
    
    @singledispatchmethod
    def  __add__(self, _):
        raise NotImplemented
    
    @singledispatchmethod
    def __sub__(self, _):
        raise NotImplemented

    @singledispatchmethod
    def __mul__(self, _):
        raise NotImplemented

    def length(self):
        return sqrt(self.x**2 + self.y**2)

    def to_polar(self):
        return Vector(self.length(), atan2(self.y, self.x))
    
    def to_cartesian(self):
        length, angle = self.x, self.y
        return Vector(length*cos(angle),length*sin(angle))

@Vector.__add__.register(Decimal)
@Vector.__add__.register(float)
@Vector.__add__.register(int)
def  _(self, value):
    return Vector(self.x + value, self.y + value)

@Vector.__add__.register(Vector)
def  _(self, other):
    return Vector(self.x + other.x, self.y + other.y)

@Vector.__sub__.register(Decimal)
@Vector.__sub__.register(float)
@Vector.__sub__.register(int)
def  _(self, value):
    return Vector(self.x - value, self.y - value)

@Vector.__sub__.register(Vector)
def  _(self, other):
    return Vector(self.x - other.x, self.y - other.y)

@Vector.__mul__.register(Decimal)
@Vector.__mul__.register(float)
@Vector.__mul__.register(int)
def  _(self, value):
    return Vector(self.x * value, self.y * value)

@Vector.__mul__.register(Vector)
def  _(self, other):
    return Vector(self.x * other.x, self.y * other.y)

def make_vector( v : tuple[float, float]) -> Vector:
    return Vector._make(v)

def make_vectors( points : list[tuple[float, float]]) -> Vector:
    return [make_vector(p) for p in points]
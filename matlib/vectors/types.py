from typing import NamedTuple, List

from math import sqrt

class Vector(NamedTuple):
    """Vector Definition"""
    x: float
    y: float

    def __eq__(self, other):
        return self.x == other.x and \
            self.y == other.y

    def  __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def length(self):
        return sqrt(self.x**2 + self.y**2)

def make_vector( v : tuple[float, float]) -> Vector:
    return Vector._make(v)

def make_vectors( points : list[tuple[float, float]]) -> Vector:
    return [make_vector(p) for p in points]
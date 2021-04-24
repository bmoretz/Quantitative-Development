from typing import NamedTuple, List

class Vector(NamedTuple):
    """Vector Definition"""
    x: float
    y: float

def make_vector(points : list[tuple[float, float]]) -> Vector:
    return [Vector._make(p) for p in points]
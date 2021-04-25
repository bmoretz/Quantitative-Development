from matlib.vectors.types import Vector

def add(v1 : Vector, v2 : Vector) -> Vector:
    return v1 + v2

def subtract(v1 : Vector, v2 : Vector) -> Vector:
    return v1 - v2

def multiply(v1 : Vector, v2 : Vector) -> Vector:
    return v1 * v2

def length( v : Vector) -> float:
    return v.length()

def distance( v1 : Vector, v2 : Vector) -> float:
    return length(v1 - v2)
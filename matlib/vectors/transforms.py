from matlib.vectors.types import Vector

def shift(vectors : list[Vector], x : float, y : float) -> Vector:
    return [Vector(v.x + x, v.y + y) for v in vectors]

def scale(vectors : list[Vector], k : float):
    return [Vector(v.x*k, v.y*k) for v in vectors]

def flip(vectors : list[Vector]):
    return [Vector(-v.x, -v.y) for v in vectors]
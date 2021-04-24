from matlib.vectors.types import Vector

def shift(vectors : list[Vector], k : float) -> Vector:
    for v in vectors:
        yield Vector(v.x + k, v.y + k)
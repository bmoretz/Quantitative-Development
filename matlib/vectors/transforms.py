from ..vectors.types import Vector

def shift(vectors : list[Vector], x : float, y : float) -> Vector:
    """shifts / translates a set of vectors.

    Args:
        vectors (list[Vector]): input vectors
        x (float): x shift
        y (float): y shit

    Returns:
        Vector: mutated vectors
    """
    return [Vector(v.x + x, v.y + y) for v in vectors]

def scale(vectors : list[Vector], k : float):
    """scales a set of vectors.

    Args:
        vectors (list[Vector]): input vectors.
        k (float): amount to scale.

    Returns:
        [type]: mutated vectors
    """
    return [Vector(v.x*k, v.y*k) for v in vectors]

def flip(vectors : list[Vector]):
    """flips a set of vectors.

    Args:
        vectors (list[Vector]): input vectors

    Returns:
        [type]: mutated vectors
    """
    return [Vector(-v.x, -v.y) for v in vectors]
from ..vectors.types import Vector

def shift(vectors : list[Vector], x : float, y : float) -> list[Vector]:
    """shifts / translates a set of vectors.

    Args:
        vectors (list[Vector]): input vectors
        x (float): x shift
        y (float): y shit

    Returns:
        list[Vector]: mutated vectors
    """
    return [Vector(v.x + x, v.y + y) for v in vectors]

def scale(vectors : list[Vector], k : float) -> list[Vector]:
    """scales a set of vectors.

    Args:
        vectors (list[Vector]): input vectors.
        k (float): amount to scale.

    Returns:
        [type]: mutated vectors
    """
    return [Vector(v.x*k, v.y*k) for v in vectors]

def flip(vectors : list[Vector]) -> list[Vector]:
    """flips a set of vectors.

    Args:
        vectors (list[Vector]): input vectors

    Returns:
        list[Vector]: mutated vectors
    """
    return [Vector(-v.x, -v.y) for v in vectors]

def rotate(vectors : list[Vector], angle : float = 0) -> list[Vector]:
    """rotates a set of vectors by the specified
    angle.

    Args:
        vectors (list[Vector]): input vectors
        angle (float): angle to rotate by
    Returns:
        list[Vector]: mutated vectors
    """
    return [Vector(p.x, p.y + angle).to_cartesian() for 
                p in [v.to_polar() for v in vectors]]
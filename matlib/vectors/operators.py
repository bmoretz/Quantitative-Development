from ..vectors.types import Vector

def add(left : Vector, right : Vector) -> Vector:
    """
    vector addition
    Args:
        left (Vector): lhs
        right (Vector): rhs

    Returns:
        Vector: operation result
    """
    return left + right

def subtract(left : Vector, right : Vector) -> Vector:
    """
    vector subtraction
    Args:
        left (Vector): lhs
        right (Vector): rhs

    Returns:
        Vector: operation result
    """
    return left - right

def multiply(left : Vector, right : Vector) -> Vector:
    """
    vector multiplication
    Args:
        left (Vector): lhs
        right (Vector): rhs

    Returns:
        Vector: operation result
    """
    return left * right

def length( vec : Vector) -> float:
    """
    length operator
    Args:
        vec (Vector): the vector

    Returns:
        float: length
    """
    return vec.length()

def distance( left : Vector, right : Vector) -> float:
    """
    distance between vectors
    Args:
        left (Vector): lhs
        right (Vector): rhs

    Returns:
        float: cartesian distance
    """
    return length(left - right)

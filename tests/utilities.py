from decimal import Decimal #pylint: disable=missing-module-docstring
from typing import Any
from functools import singledispatch
from matlib.vectors.types import Vector

@singledispatch
def almost_equal(left : Any, right : Any, accuracy : Decimal = 10**-8) -> None:
    """[summary]

    Args:
        left ([type]): lhs
        right ([type]): rhs
        accuracy ([type], optional): threshold. Defaults to 10**-8.

    Raises:
        NotImplementedError: not supported for any types
    """
    raise NotImplementedError('Unsupported')

@almost_equal.register(Decimal)
@almost_equal.register(float)
def _(left, right, accuracy : Decimal = 10**-8) -> bool:
    """
    equality comparision within specified threshold.
    Args:
        left ([type]): lhs
        right ([type]): rhs
        accuracy ([type], optional): threshold. Defaults to 10**-8.

    Returns:
        bool: returns equality within the specified threshold.
    """
    return abs(left - right) < accuracy

@almost_equal.register(Vector)
def _(vec1 : Vector, vec2 : Vector, accuracy : Decimal = 10**-8) -> bool:
    """
    equality compairsion within specified threshold.

    Args:
        vec1 ([type]): lhs
        vec2 ([type]): rhs
        accuracy ([type], optional): [description]. Defaults to 10**-8.

    Returns:
        bool: equality within specified threshold.
    """
    x1, y1 = vec1.x, vec1.y
    x2, y2 = vec2.x, vec2.y

    x_eq = almost_equal(x1, x2, accuracy)
    y_eq = almost_equal(y1, y2, accuracy)

    return x_eq and y_eq

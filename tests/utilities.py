from decimal import Decimal
from functools import singledispatch
from matlib.vectors.types import Vector

@singledispatch
def almost_equal(l, r) -> None:
    raise NotImplementedError('Unsupported')

@almost_equal.register(Decimal)
@almost_equal.register(float)
def _(val1, val2 , accuracy = 10**-8) -> bool:
    return abs(val1 - val2) < accuracy

@almost_equal.register(Vector)
def _(vec1, vec2, accuracy = 10**-8) -> bool:
    
    x1, y1 = vec1.x, vec1.y
    x2, y2 = vec2.x, vec2.y

    x_eq = almost_equal(x1, x2, accuracy)
    y_eq = almost_equal(y1, y2, accuracy)

    return x_eq and y_eq
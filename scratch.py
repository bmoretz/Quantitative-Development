from typing import List, Tuple

from matlib.enums import Color
from matlib.plotting import draw_shapes
from matlib.vectors.types import Vector, make_vectors
from matlib.vectors.shapes import Points, Polygon, Segment
from matlib.vectors.transforms import shift

dino_vectors = make_vectors([(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)])

dino_vectors2 = shift(dino_vectors, k=2)

draw_shapes(
    Points(*dino_vectors),
    Polygon(*dino_vectors,color=Color.Blue)
)
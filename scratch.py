from typing import List, Tuple

from matlib.enums import Color
from matlib.plotting import draw_shapes
from matlib.vectors.types import Vector, make_vectors
from matlib.vectors.shapes import Points, Polygon, Segment, Arrow
from matlib.vectors.transforms import shift, scale, flip

dino_vectors = make_vectors([(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)])

shapes = []

y_offset = 10
for row in range(0, 10):
    
    x_offset = 2

    for col in range(0, 10):
        scaled = scale(dino_vectors, .1)
        transformed = shift(scaled, x_offset, y_offset)
        shapes += [Polygon(*transformed, color=Color.Blue)]
        x_offset = x_offset + 2

    y_offset = y_offset - 1

draw_shapes(*shapes)
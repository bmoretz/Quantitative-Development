from typing import List, Tuple

from matlib.enums import Color
from matlib.plotting import draw_shapes
from matlib.vectors.types import Vector, make_vectors, distance
from matlib.vectors.shapes import Points, Polygon, Segment, Arrow
from matlib.vectors.transforms import shift, scale, flip

dino_vectors = make_vectors([(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)])


vectors = make_vectors([(1,0), (1,1), (0,1), (0,0)])

n = len(vectors)

perimeter = 0.
for index in range(1, len(vectors)):
    cur, prev = vectors[index], vectors[index-1]
    perimeter += distance(cur, prev)
    
perimeter += distance(vectors[0], vectors[n-1])

print(perimeter)

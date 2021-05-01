from typing import List, Tuple

from matlib.enums import Color
from matlib.plotting import draw_shapes
from matlib.vectors import *

dino_vectors = make_vectors([(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)])


vectors = make_vectors([(1,0), (1,1), (0,1), (0,0)])

point = Vector(-2, 3)

p = point.to_polar()

x, y = p

print(round(x,5), round(y, 5))
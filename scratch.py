from math import sin, cos, tan, pi, atan2

from matlib.enums import Color
from matlib.plotting import draw_shapes
from matlib.vectors import *

dino_vectors = make_vectors([(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)])

points = regular_polygon(7)

draw_shapes(Polygon(*points, color=Color.Blue))
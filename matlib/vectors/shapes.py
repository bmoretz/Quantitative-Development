from typing import List
from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
from matplotlib.pyplot import xlim, ylim

from matlib.vectors.types import Vector
from matlib.enums import Color

class shape(ABC):
    """abstract base class for shapes.

    Args:
        ABC ([type]): specifies abstract base class.
    """
    @abstractmethod
    def plot(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass

class Polygon(shape):
    """Polygon.

    Args:
        shape ([type]): inheres shape.
    """    
    def __init__(self, *vertices : Vector, color=Color.Blue, fill=None, alpha=0.4):
        self.vertices = list(vertices)
        self.color = color
        self.fill = fill
        self.alpha = alpha

    def plot(self):

        for index, vertex in enumerate(self.vertices):
            x1, y1 = self.vertices[index]
            x2, y2 = self.vertices[(index+1)%len(self.vertices)]
            plt.plot([x1,x2], [y1, y2],color=self.color)

            if self.fill:
                xs = [v.x for v in self.vertices]
                ys = [v.y for v in self.vertices]
                plt.gca().fill(xs, ys, self.fill, alpha=self.alpha)

    def __iter__(self):
        for v in self.vertices:
            yield v

class Points(shape):
    """Points.

    Args:
        shape ([type]): inheres shape.
    """
    def __init__(self, *vectors : Vector, color=Color.Black,alpha=1):
        self.vectors = list(vectors)
        self.color = color
        self.alpha = alpha

    def plot(self):
        xs = [v.x for v in self.vectors]
        ys = [v.y for v in self.vectors]
        plt.scatter(xs, ys, color=self.color, alpha=self.alpha)

    def __iter__(self):
        for v in self.vectors:
            yield v

class Arrow(shape):
    """Arrow.

    Args:
        shape ([type]): inheres shape.
    """
    def __init__(self, tip : Vector, tail=Vector(0,0), color=Color.Red):
        self.tip = tip
        self.tail = tail
        self.color = color

    def plot(self):
        from math import sqrt

        tip, tail = self.tip, self.tail
        tip_length = (xlim()[1] - xlim()[0]) / 20.
        
        length = sqrt((tip.y-tail.y)**2 + (tip.x-tail.x)**2)
        new_length = length - tip_length

        new_y = (tip.y - tail.y) * (new_length / length)
        new_x = (tip.x - tail.x) * (new_length / length)

        plt.gca().arrow(tail.x, tail.y, new_x, new_y,
            head_width=tip_length/1.5, head_length=tip_length,
            fc=self.color, ec=self.color)

    def __iter__(self):
        yield self.tip
        yield self.tail

class Segment(shape):
    """Line Segment.

    Args:
        shape ([type]): inheres shape.
    """
    def __init__(self, start_point, end_point, color=Color.Blue):
        self.start_point = start_point
        self.end_point = end_point
        self.color = color

    def plot(self):
        x1, y1 = self.start_point
        x2, y2 = self.end_point
        plt.plot([x1, x2], [y1,y2], color=self.color)
        
    def __iter__(self):
        yield self.start_point
        yield self.end_point


def perimeter(*vectors : Vector) -> float:
    from matlib.vectors.operators import distance
    
    perimeter, n = 0., len(vectors)
    if n <= 1: return perimeter

    for index in range(1, len(vectors)):
        cur, prev = vectors[index], vectors[index-1]
        perimeter += distance(cur, prev)

    perimeter += vectors[0].distance(vectors[n-1])
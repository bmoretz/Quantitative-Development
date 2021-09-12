from math import pi, sqrt
from abc import ABC, abstractmethod
from typing import Iterable, Iterator

import matplotlib.pyplot as plt
from matplotlib.pyplot import xlim, ylim #pylint: disable=unused-import

from ..vectors.types import Vector
from ..vectors.operators import distance
from ..enums import Color

class Shape(ABC):

    """abstract base class for shapes.

    Args:
        ABC ([type]): specifies abstract base class.
    """
    @abstractmethod
    def plot(self) -> None:
        """
        abstract plot method
        """

    @abstractmethod
    def __iter__(self) -> Iterator[Vector]:
        """
        returns iterable vectors that make up the shape.

        Yields:
            Iterator[Vector]: vectors that make up the shape.
        """
class Polygon(Shape):
    """
    polygon shape
    Args:
        shape ([type]): inheres shape.
    """
    def __init__(self, *vertices : Vector, color=Color.Blue, fill=None, alpha=0.4) -> None:
        """
        initializes a polygon shape.

        Args:
            color ([type], optional): [description]. Defaults to Color.Blue.
            fill ([type], optional): [description]. Defaults to None.
            alpha (float, optional): [description]. Defaults to 0.4.
        """
        self.vertices = list(vertices)
        self.color = color
        self.fill = fill
        self.alpha = alpha

    def plot(self) -> None:
        """
        plots the polygon
        """
        for index, _ in enumerate(self.vertices):

            x1, y1 = self.vertices[index]
            x2, y2 = self.vertices[(index+1) % len(self.vertices)]
            plt.plot([x1,x2], [y1, y2],color=self.color)

            if self.fill:
                xs = [v.x for v in self.vertices]
                ys = [v.y for v in self.vertices]
                plt.gca().fill(xs, ys, self.fill, alpha=self.alpha)

    def __iter__(self) -> Iterator[Vector]:
        """
        returns the points in the polygon.

        Yields:
            Iterator[Vector]: the points (iterable)
        """
        for v in self.vertices:
            yield v
class Points(Shape):
    """
    points shape

    Args:
        shape ([type]): inheres shape.
    """
    def __init__(self, *vectors : Vector, color=Color.Black,alpha=1) -> None:
        self.vectors = list(vectors)
        self.color = color
        self.alpha = alpha

    def plot(self) -> None:
        """
        plots the points
        """
        xs = [v.x for v in self.vectors]
        ys = [v.y for v in self.vectors]
        plt.scatter(xs, ys, color=self.color, alpha=self.alpha)

    def __iter__(self):
        """
        returns the points

        Yields:
            Iterator[Vector]: the points (iterable)
        """    
        for v in self.vectors:
            yield v
class Arrow(Shape):
    """
    arrow.

    Args:
        shape ([type]): inheres shape.
    """
    def __init__(self, tip : Vector, tail=Vector(0,0), color=Color.Red) -> None:
        self.tip = tip
        self.tail = tail
        self.color = color

    def plot(self) -> None:
        """
        plots the arrow
        """
        tip, tail = self.tip, self.tail
        tip_length = (xlim()[1] - xlim()[0]) / 20.

        length = sqrt((tip.y-tail.y)**2 + (tip.x-tail.x)**2)
        new_length = length - tip_length

        new_y = (tip.y - tail.y) * (new_length / length)
        new_x = (tip.x - tail.x) * (new_length / length)

        plt.gca().arrow(tail.x, tail.y, new_x, new_y,
            head_width=tip_length/1.5, head_length=tip_length,
            fc=self.color, ec=self.color)

    def __iter__(self) -> Iterable[Vector]:
        """
        returns the points in the polygon.
        Yields:
            Iterator[Vector]: the points (iterable)
        """
        yield self.tip
        yield self.tail

class Segment(Shape):
    """
    line segment

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

    def __iter__(self) -> Iterable[Vector]:
        """
        returns the points in the polygon.

        Yields:
            Iterator[Vector]: the points (iterable)
        """        
        yield self.start_point
        yield self.end_point

def regular_polygon(sides : int, length = 1., center = Vector(0, 0)) -> list[Vector]:
    """
    a regular polygon

    Args:
        sides (int): number of sides
        length ([type], optional): side lengths. Defaults to 1..
        center ([type], optional): center point. Defaults to Vector(0, 0).

    Returns:
        list[Vector]: a regular polygon with k sides of length n centered
        at point p.
    """

    return [Vector(length, 2*pi*k/sides).to_cartesian() + center
            for k in range(0, sides)]

def merge_vectors( shapes : list[Shape] ) -> Iterable[Vector]:
    """
    merges to sets of vectors

    Args:
        shapes (list[Shape]): the vectors

    Returns:
        Iterable[Vector]: merge result

    Yields:
        Iterator[Iterable[Vector]]: iterable Vectors
    """
    for shape in shapes:
        yield from shape

def perimeter( shape : Shape ) -> float:
    """
    calculates the perimeter of a shape

    Args:
        shape (Shape): the shape

    Returns:
        float: perimeter
    """
    vectors = list(shape)

    peri, n = 0., len(vectors)

    if n <= 1:
        return peri

    for index in range(1, len(vectors)):
        cur, prev = vectors[index], vectors[index-1]
        peri += distance(cur, prev)

    peri += distance(vectors[0], vectors[n-1])

    return peri

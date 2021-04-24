from typing import Final
from math import ceil, floor

import matplotlib
import matplotlib.patches

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import xlim, ylim

from matlib.enums import Color
from matlib.vectors.types import Vector

def merge_vectors( shapes ):

    for shape in shapes:
        yield from shape

def draw_shapes(*shapes : Vector, origin=True, axes=True, grid=(1,1), nice_aspect_ratio=True,
                width=6, save_as=None) -> None:

    all_vectors = merge_vectors(shapes)
    xs, ys = zip(*all_vectors)

    max_x, max_y, min_x, min_y = max(0, *xs), max(0, *ys), min(0, *xs), min(0, *ys)

    # sizing
    if grid:

        pad: Final=0.05

        x_padding = max(ceil(pad*(max_x-min_x)), grid[0])
        y_padding = max(ceil(pad*(max_y-min_y)), grid[1])

        def round_up_to_multiple(val, size):
            return floor((val + size) / size) * size

        def round_down_to_multiple(val, size):
            return -floor((-val - size) / size) * size

        plt.xlim(floor((min_x - x_padding) / grid[0]) * grid[0],
            ceil((max_x + x_padding) / grid[0]) * grid[0])

        plt.ylim(floor((min_y - y_padding) / grid[1]) * grid[1],
            ceil((max_y + y_padding) / grid[1]) * grid[1])

    if origin:
        plt.scatter([0], [0], color=Color.Black, marker='x')

    if grid:
        plt.gca().set_xticks(np.arange(plt.xlim()[0],plt.xlim()[1],grid[0]))
        plt.gca().set_yticks(np.arange(plt.ylim()[0],plt.ylim()[1],grid[1]))
        plt.grid(True)
        plt.gca().set_axisbelow(True)

    if axes:
        plt.gca().axhline(linewidth=2, color=Color.Black)
        plt.gca().axvline(linewidth=2, color=Color.Black)

    for shape in shapes:
        shape.plot()

    fig = matplotlib.pyplot.gcf()

    if nice_aspect_ratio:
        coords_height = (ylim()[1] - ylim()[0])
        coords_width = (xlim()[1] - xlim()[0])
        fig.set_size_inches(width , width * coords_height / coords_width)

    if save_as:
        plt.savefig(save_as)

    plt.show()
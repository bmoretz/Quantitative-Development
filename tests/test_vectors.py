import unittest

import sys
sys.path.append('./')

from matlib.vectors import *
from tests.utilities import almost_equal

class TestMakeVector(unittest.TestCase):
    """test methods for making vectors.

    Args:
        unittest ([type]): unit test
    """
    def test_single(self):

        u = (1., 1.)
        assert isinstance(u, tuple)
        v = make_vector(u)
        assert isinstance(v, Vector)

    def test_multiple(self):

        u = [(1,1), (0,1), (0,0), (1,0)]

        v = make_vectors(u)

        for z in v:
            assert isinstance(z, Vector)

class TestVectorOperators(unittest.TestCase):

    def test_add1(self):

        u, v = make_vectors([(2,-1), (1, 0)])

        assert u + v == Vector(3, -1)

    def test_add2(self):
        u, v = make_vectors([(2,-1), (1, 0)])

        assert add(u, v) == Vector(3, -1)

    def test_add3(self):
        u = Vector(3,1)
        v = 3

        assert u + v == Vector(6, 4)

    def test_sub1(self):
        u, v = make_vectors([(2,-1), (1, 0)])

        assert u - v == Vector(1, -1)

    def test_sub2(self):
        u, v = make_vectors([(2,-1), (1, 0)])

        assert subtract(u, v) == Vector(1, -1)

    def test_sub3(self):
        u = Vector(3,1)
        v = 1

        assert u - v == Vector(2, 0)

    def test_multiply1(self):

        u, v = make_vectors([(2,-1), (1, 1)])

        assert u * v == Vector(2, -1)

    def test_multiply2(self):

        u, v = make_vectors([(2,-1), (1, 1)])

        assert multiply(u, v) == Vector(2, -1)

    def test_multiply3(self):
        u = Vector(3,1)
        v = 3

        assert u * v == Vector(9, 3)

    def test_length1(self):

        u = make_vector((4, 2))

        actual = round(u.length(), 3)
        expected = 4.472

        assert actual == expected

    def test_length2(self):

        u = make_vector((4, 2))

        actual = round(length(u), 3)
        expected = 4.472

        assert actual == expected

    def test_distance(self):

        u, v = make_vectors([(2,-1), (1, 0)])

        actual = round(distance(u, v), 3)
        expected = 1.414

        assert actual == expected


class TestVectorTransforms(unittest.TestCase):

    def test_scale(self):
    
        vectors = make_vectors([(1,0), (1,1), (0,1), (0,0)])

        actual = scale(vectors, .5)
        expected = make_vectors([(.5, 0), (.5, .5), (0, .5), (0, 0)])

        for index in range(len(vectors)):
            assert actual[index] == expected[index]


    def test_shift(self):

        vectors = make_vectors([(1,0), (1,1), (0,1), (0,0)])

        actual = shift(vectors, x=1, y=1)
        expected = make_vectors([(2, 1), (2, 2), (1, 2), (1, 1)])

        for index in range(len(vectors)):
            assert actual[index] == expected[index]

    def test_flip(self):

        vectors = make_vectors([(1,0), (1,1), (0,1), (0,0)])

        actual = flip(vectors)
        expected = make_vectors([(-1, 0), (-1, -1), (0, -1), (0, 0)])

        for index in range(len(vectors)):
            assert actual[index] == expected[index]


class TestVectorShapes(unittest.TestCase):

    def test_perimeter(self):

        vectors = make_vectors([(1,0), (1,1), (0,1), (0,0)])

        actual = perimeter(Points(*vectors))
        expected = 4

        assert actual == expected

class TestVectorCoordinates(unittest.TestCase):

    def test_to_polar1(self):

        v = Vector(-2, 3)

        actual = v.to_polar()
        expected = Vector(3.60555, 2.1588)

        assert almost_equal(actual, expected, accuracy=10**-5)

    def test_to_cartesian1(self):

        v = Vector(3.60555, 2.1588)

        actual = v.to_cartesian()
        expected = Vector(-2, 3)

        assert almost_equal(actual, expected, accuracy=10**-5)
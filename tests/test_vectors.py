import sys
sys.path.append('./')

import unittest

from matlib.vectors import *

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

    def test_sub1(self):
        u, v = make_vectors([(2,-1), (1, 0)])

        assert u - v == Vector(1, -1)

    def test_sub2(self):
        u, v = make_vectors([(2,-1), (1, 0)])

        assert subtract(u, v) == Vector(1, -1)

    def test_multiply1(self):

        u, v = make_vectors([(2,-1), (1, 1)])

        assert u * v == Vector(2, -1)

    def test_multiply2(self):

        u, v = make_vectors([(2,-1), (1, 1)])

        assert multiply(u, v) == Vector(2, -1)

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
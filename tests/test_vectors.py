import unittest, sys

from matlib.vectors import (
    Vector, Points,
    add, subtract, multiply,
    length, distance, perimeter,
    scale, shift, flip,
    make_vector, make_vectors
)

from tests.utilities import almost_equal

sys.path.append('./')

class TestMakeVector(unittest.TestCase):
    """test methods for making vectors.

    Args:
        unittest ([type]): vector
    """
    @staticmethod
    def test_single() -> None:
        """
        single
        """
        u = (1., 1.)
        assert isinstance(u, tuple)
        v = make_vector(u)
        assert isinstance(v, Vector)

    @staticmethod
    def test_multiple() -> None:
        """
        multiply
        """
        u = [(1,1), (0,1), (0,0), (1,0)]

        v = make_vectors(u)

        for z in v:
            assert isinstance(z, Vector)

class TestVectorOperators(unittest.TestCase):
    """
    test vector operators
    Args:
        unittest ([type]): Vector
    """
    @staticmethod
    def test_add1():
        """
        add uc 1
        """
        u, v = make_vectors([(2,-1), (1, 0)])

        assert u + v == Vector(3, -1)

    @staticmethod
    def test_add2():
        """
        add uc 2
        """
        u, v = make_vectors([(2,-1), (1, 0)])

        assert add(u, v) == Vector(3, -1)

    @staticmethod
    def test_add3():
        """
        add uc3
        """
        u = Vector(3,1)
        v = 3

        assert u + v == Vector(6, 4)

    @staticmethod
    def test_sub1():
        """
        sub uc 1
        """
        u, v = make_vectors([(2,-1), (1, 0)])

        assert u - v == Vector(1, -1)

    @staticmethod
    def test_sub2():
        """
        sub uc 2
        """
        u, v = make_vectors([(2,-1), (1, 0)])

        assert subtract(u, v) == Vector(1, -1)

    @staticmethod
    def test_sub3():
        """
        sub uc 3
        """
        u = Vector(3,1)
        v = 1

        assert u - v == Vector(2, 0)

    @staticmethod
    def test_multiply1():
        """
        multiply uc 1
        """
        u, v = make_vectors([(2,-1), (1, 1)])

        assert u * v == Vector(2, -1)

    @staticmethod
    def test_multiply2():
        """
        multiply uc 2
        """
        u, v = make_vectors([(2,-1), (1, 1)])

        assert multiply(u, v) == Vector(2, -1)

    @staticmethod
    def test_multiply3() -> None:
        """
        multiply uc 3
        """
        u = Vector(3,1)
        v = 3

        assert u * v == Vector(9, 3)

    @staticmethod
    def test_length1() -> None:
        """
        length uc 1
        """
        u = make_vector((4, 2))

        actual = round(u.length(), 3)
        expected = 4.472

        assert actual == expected

    @staticmethod
    def test_length2() -> None:
        """
        length uc 2
        """
        u = make_vector((4, 2))

        actual = round(length(u), 3)
        expected = 4.472

        assert actual == expected

    @staticmethod
    def test_distance() -> None:
        """
        distance
        """
        u, v = make_vectors([(2,-1), (1, 0)])

        actual = round(distance(u, v), 3)
        expected = 1.414

        assert actual == expected

class TestVectorTransforms(unittest.TestCase):
    """
    class for testing transformations
    Args:
        unittest ([type]): Vector
    """
    @staticmethod
    def test_scale() -> None:
        """
        test scale
        """
        vectors = make_vectors([(1,0), (1,1), (0,1), (0,0)])

        actual = scale(vectors, .5)
        expected = make_vectors([(.5, 0), (.5, .5), (0, .5), (0, 0)])

        for index in range(len(vectors)):
            assert actual[index] == expected[index]

    @staticmethod
    def test_shift() -> None:
        """
        test shift
        """
        vectors = make_vectors([(1,0), (1,1), (0,1), (0,0)])

        actual = shift(vectors, x=1, y=1)
        expected = make_vectors([(2, 1), (2, 2), (1, 2), (1, 1)])

        for index in range(len(vectors)):
            assert actual[index] == expected[index]

    @staticmethod
    def test_flip() -> None:
        """
        test flip
        """
        vectors = make_vectors([(1,0), (1,1), (0,1), (0,0)])

        actual = flip(vectors)
        expected = make_vectors([(-1, 0), (-1, -1), (0, -1), (0, 0)])

        for index in range(len(vectors)):
            assert actual[index] == expected[index]

class TestVectorShapes(unittest.TestCase):
    """
    test perimeter
    Args:
        unittest ([type]): class for testing shape
        functions.
    """
    @staticmethod
    def test_perimeter() -> None:
        """
        test perimiter
        """
        vectors = make_vectors([(1,0), (1,1), (0,1), (0,0)])

        actual = perimeter(Points(*vectors))
        expected = 4

        assert actual == expected

class TestVectorCoordinates(unittest.TestCase):
    """
    test coordinate conversions
    Args:
        unittest ([type]): [description]
    """
    @staticmethod
    def test_to_polar1() -> None:
        """
        test to_polar
        """
        v = Vector(-2, 3)

        actual = v.to_polar()
        expected = Vector(3.60555, 2.1588)

        assert almost_equal(actual, expected, accuracy=10**-5)

    @staticmethod
    def test_to_cartesian1() -> None:
        """
        test to_cartesian
        """
        v = Vector(3.60555, 2.1588)

        actual = v.to_cartesian()
        expected = Vector(-2, 3)

        assert almost_equal(actual, expected, accuracy=10**-5)

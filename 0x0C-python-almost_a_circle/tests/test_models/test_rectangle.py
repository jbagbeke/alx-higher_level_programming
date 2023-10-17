#!/usr/bin/python3
"""
Unittest for module rectangle.py
"""
import unittest
from models.rectangle import Rectangle


class Args_test(unittest.TestCase):
    """
    Unittest for Rectangle class
    """

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(2)

    def test_two_args(self):
        r1 = Rectangle(6, 2)
        r2 = Rectangle(2, 3)
        self.assertEqual(r2.id, r1.id + 1)

    def test_three_args(self):
        r1 = Rectangle(1, 2, 3)
        r2 = Rectangle(4, 5, 6)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(2, 3, 4, 5)
        r2 = Rectangle(34, 5, 2, 5)
        self.assertEqual(r1.id, r2.id - 1)

    def test_all_args(self):
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12)


class height_test(unittest.TestCase):
    """
    Test cases for initialising height attribute
    """

    def test_height_str(self):
        wir = Rectangle(10, 20)
        self.assertEqual(r.height, 20)

    def test_height_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(10, "2")

    def test_height_dict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(10, {"height":"20.1"})

    def test_height_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, (2, 5))

    def test_height_set(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(10, {1, 32})

    def test_height_None(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(10, None)

    def test_height_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(10, 5.32)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(10, -5.32)

    def test_height_neg(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(10, -5)

    def test_height_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(10, 0)


class x_test(unittest.TestCase):
    """
    Test Cases for initialising x attribute
    """

    def test_x_int(self):
        r = Rectangle(10, 2, 12)
        self.assertEqual(r.x, 12)

    def test_x_zero(self):
        r = Rectangle(10, 2, 0)
        self.assertEqual(r.x, 0)

    def test_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 2, {})

    def test_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 2, "23")

    def test_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 2, (1, 3))

    def test_x_None(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 2, None)

    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 2, 4.5)

    def test_x_neg(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(10, 2, -4)


class width_test(unittest.TestCase):
    """
    Test cases for initialising width attribute
    """

    def test_width_int(self):
        r = Rectangle(23, 3)
        self.assertEqual(r.width, 23)

    def test_width_less(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-10, 3)

    def test_width_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle({}, 3)

    def test_width_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle((1, 2), 3)

    def test_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(-13.33, 3)

    def test_width_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(None, 3)

    def test_width_dict_one(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle({"name":"Jay"}, 3)


class y_test(unittest.TestCase):
    """
    Test cases for initialising y attribute
    """

    def test_y_less(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(10, 2, 3, -1)

    def test_y_int(self):
        r = Rectangle(10, 2, 2, 12)
        self.assertEqual(r.y, 12)

    def test_y_zero(self):
        r = Rectangle(10, 2, 50, 0)
        self.assertEqual(r.y, 0)

    def test_y_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 2, 4, {})

    def test_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 2, 5, "23")

    def test_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 2, 3, (1, 3))

    def test_y_None(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 2, 7, None)

    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 2, 1, 4.5)

    def test_y_neg(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(10, 2, 3, -4)

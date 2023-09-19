#!/usr/bin/python3
"""
Unittest for module rectangle.py
"""
import unittest
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
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

    def test_height_int(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, "2")

    def test_x_int(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, {})

    def test_width_less(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-10, 3)


    def test_y_less(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, 3, -1)

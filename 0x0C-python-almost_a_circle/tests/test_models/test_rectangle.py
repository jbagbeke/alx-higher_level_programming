#!/usr/bin/python3
"""
Unittest for module base.py
"""
import unittest
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """
    Unittest for Base class
    """

    def test_all_args(self):
        """
        Passing None Argument to Base class
        """

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

#!/usr/bin/python3
"""
Unittest for module base.py
"""
import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """
    Unittest for Base class
    """

    def test_None(self):
        """
        Passing None Argument to Base class
        """

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
    def test_One_Arg(self):
        """
        Passing one arg to Base
        """

        b1 = Base(34)
        self.assertEqual(b1.id, 34)
        b2 = Base(940)
        self.assertEqual(b2.id, 940)
        b3 = Base(1)
        self.assertEqual(b3.id, 1)

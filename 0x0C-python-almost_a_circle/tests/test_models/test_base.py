#!/usr/bin/python3
"""
Unittest for module base.py
"""
import unittest
from ...models.base import Base


class BaseTest(unittest.TestCase):
    """
    Unittest for Base class
    """

    def test_None(self):
        """
        Passing None Argument to Base class
        """

        b1 = Base()
        self.assertEqual(print(b1.id), 1)

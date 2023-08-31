#!/usr/bin/python3
"""
Purpose: A class definition with instantiation and assignment of integers
"""


class Square:
    """
    Assigns an integer to a private instance attibute
    """
    def __init__(self, size=0):
        """
        Instantiation with private 'size' attribute, and checks for valid input
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns area of a square
        """
        result = self.__size ** 2
        return result

    @property
    def size(self):
        """
        Retrieves the original value of area of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Initialises the private attribute to a value
        Args: Value(int)
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __getattr__(self, name):
        """
        Gets the name of attribute being assessed of the object
        """
        if name == 'size':
            raise AttributeError("'Square' object has no attribute 'size'")
        if name == '__size':
            raise AttributeError("'Square' object has no attribute '__size'")




my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)

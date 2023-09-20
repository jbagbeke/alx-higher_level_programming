#!/usr/bin/python3
"""
A  class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class inheriting from the rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class contructor for Square class
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Executes when print function is called
        """

        w = self.width
        x = self.x
        y = self.y
        i_d = self.id
        return str("[Square] ({}) {}/{} - {}".format(i_d, x, y, w))

    @property
    def size(self):
        """
        Retrieves value of size att
        """

        return self.width

    @size.setter
    def size(self, size):
        """
        Sets width and height of a rectangle to size
        """

        self.width = size
        self.height = size

    def to_dictionary(self):
        """
        Returns the dictionary representation of Square class
        """

        my_dict = {}

        if self.id is not None:
            my_dict['id'] = self.id

        my_dict['x'] = self.x
        my_dict['size'] = self.width
        my_dict['y'] = self.y
        return my_dict

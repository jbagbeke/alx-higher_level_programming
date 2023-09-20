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

    def update(self, *args, **kwargs):
        """
        Update the class Square to assign attributes
        """

        if args is not None and len(args) > 0:
            index = 0
            for arg in args:
                if index == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                if index == 1:
                    self.size = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
                index += 1
        elif kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is not None:
                        self.id = value
                    else:
                        self.__init__(self.size, self.x, self.y)
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

#!/usr/bin/python3
"""
A  class Square that inherits from Rectangle
"""
from rectangle import Rectangle


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
        return str("[Rectangle] ({}) {}/{} - {}".format(i_d, x, y, w))

    @property
    def size(self):
        """
        Retrieves value of size att
        """

        return self._Rectangle__width

    @size.setter
    def size(self, size):
        """
        Sets width and height of a rectangle to size
        """

        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > than 0")
        self._Rectangle__width = size
        self._Rectangle__height = size

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




if __name__ == "__main__":

    s1 = Square(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1 == s2)

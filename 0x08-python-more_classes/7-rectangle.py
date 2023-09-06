#!/usr/bin/python3

"""
    An empty class that defines a rectangle
"""


class Rectangle:
    """
    Defines a rectangle and attributes
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Instantiates the attributes of a rectangle
        Args 1: An int(width)
        Args 2: An int(height)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """
        Retrieves and returns area of a rectangle
        Args: None
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            self.perimeter = 0
        else:
            self.perimeter = 2 * (self.__width + self.__height)
        return self.perimeter

    @property
    def width(self):
        """
        Retrieves the width of a rectangle
        Args: None
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value of the width of a rectangle
        Args: An int
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of a rectangle
        Args: None
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the value of the height of a rectangle
        Args: An int
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """
        Returns the '#' representation of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect_str = ""
        for h in range(self.__height):
            for w in range(self.__width):
                rect_str += str(self.print_symbol)
            if h < self.__height - 1:
                rect_str += '\n'
        return rect_str

    def __repr__(self):
        """
        Returns string representation of a rectangle
        """
        repr_str = "Rectangle(" + str(self.__width)
        repr_str += ", " + str(self.__height) + ")"
        return repr_str

    def __del__(self):
        """
        Prints message when an instance is being deleted
        """
        if Rectangle.number_of_instances != 0:
            Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

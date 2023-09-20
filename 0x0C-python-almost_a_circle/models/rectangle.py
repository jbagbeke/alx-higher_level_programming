#!/usr/bin/python3
"""
inherits from class 'Base'
"""
from models.base import Base


class Rectangle(Base):
    """
    Instantiates public instance attributes
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor that initiates private variables

         Args:
            Arg1: (width) width of the new Rectangle.
            Arg2: (height) height of new Rectangle.
            Arg3: (x) x coordinate of new Rectangle.
            Arg4: (y) y coordinate of new Rectangle.
            Arg5: (id)identity of the new Rectangle.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Retrieves width of a rectangle
        """

        return self.__width

    @width.setter
    def width(self, width):
        """
        Sets the width of a rectangle
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        Retrieves height of a rectangle
        """

        return self.__height

    @height.setter
    def height(self, height):
        """
        Sets height of a rectangle
        """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        Retrieves the x value of rectangle
        """

        return self.__x

    @x.setter
    def x(self, x):
        """
        Sets the x value of a rectangle
        """

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        Retrieves the y value of a rectangle
        """

        return self.__y

    @y.setter
    def y(self, y):
        """
        Sets the y value of a rectangle
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        Returns the area value of the Rectangle instance
        """

        return self.__width * self.__height

    def display(self):
        """
        Prints in stdout the Rectangle instance with the char #
        """

        if self.__width == 0 or self.__height == 0:
            print("")
            return
        for y_d in range(self.__y):
            print("")

        for h in range(self.__height):
            print(" " * self.__x, end="")
            for w in range(self.__width):
                print("{}".format('#'), end="")
            print("")

    def __str__(self):
        """
        Executes when print function is called
        """

        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y
        i_d = self.id
        return str("[Rectangle] ({}) {}/{} - {}/{}".format(i_d, x, y, w, h))

    def update(self, *args, **kwargs):
        """
        Update the class Rectangle by adding the public method
        """

        if args is not None and len(args) > 0:
            index = 0
            for arg in args:
                if index == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                if index == 1:
                    self.width = arg
                elif index == 2:
                    self.height = arg
                elif index == 3:
                    self.x = arg
                elif index == 4:
                    self.y = arg
                index += 1
        elif kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is not None:
                        self.id = value
                    else:
                        w = self.width
                        h = self.height
                        self.__init__(w, h, self.x, self.y)
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle
        """

        my_dict = {}
        my_dict['x'] = self.x
        my_dict['y'] = self.y

        if self.id is not None:
            my_dict['id'] = self.id

        my_dict['height'] = self.height
        my_dict['width'] = self.width
        return my_dict

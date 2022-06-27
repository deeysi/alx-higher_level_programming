#!/usr/bin/python3
"""
    5-rectangle Module
"""


class Rectangle:
    """
        Rectangle class
    """

    def __init__(self, width=0, height=0) -> None:
        """
            Initializion of Objects at creation

            Args:
                width: width of rectangle
                height: height of rectangle
        """
        self.width = width
        self.height = height

    def __str__(self) -> str:
        """
            returns string representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ''

        length = list()
        for i in range(self.__height):
            for j in range(self.__width):
                length.append('#')
            if i + 1 != self.__height:
                length.append('\n')
        return ''.join(length)

    def __repr__(self) -> str:
        """
            returns string representation that can be evaluated
            with the eval function
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
            called when the instance is getting deleted
        """
        print("Bye rectangle...")

    @property
    def width(self):
        """
            Gets the private instance to be used by class
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """
            Gets the private instance height to be used by class
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """
            computes the area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
            computes the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

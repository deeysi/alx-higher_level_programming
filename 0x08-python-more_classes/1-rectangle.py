#!/usr/bin/python3
"""
    1-rectangle Module
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

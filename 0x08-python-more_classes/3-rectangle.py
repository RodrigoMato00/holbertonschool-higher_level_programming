#!/usr/bin/python3
"""Modulo Rectangle
"""


class Rectangle:
    """
    objeto clase Rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def height(self):
        self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        return self._width * self._height

    def perimeter(self):
        if (self._width == 0) or (self._height == 0):
            self.perimeter = 0
        else:
            return (self._width + self._height) * 2

    def _str_(self):
        if (self._width == 0) or (self._height == 0):
            return("")
        else:
            s = []
            for i in range(self.__height):
                for j in range(self.__width):
                    s.append("#")
                s.append("\n")
        del s[-1]
        return("".join(s))

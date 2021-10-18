#!/usr/bin/python3
"""

"""

from models.base import Base
"""
"""


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)


    @property
    def width(self):
        """
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        """
        self.__width = width

        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        """
        self.__height = height

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be >= 0")

    @property
    def x(self):
        """
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        """
        self.__x = x
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be > 0")

    @property
    def y(self):
        """
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        """
        self.__y = y
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be > 0")

    def area(self):
        """
        """
        return self.width * self.height

    def display(self):
        """
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        """
        return("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height))

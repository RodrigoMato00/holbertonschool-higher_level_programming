#!/usr/bin/python3
"""Modulo Rectangl
"""


class Rectangle:
    """A nuestra clase rectangulo
       que ya tiene un largop y ancho ahora le
       agregamos el valculo del Area y del perimetro"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        return self.__width * self.__height

    def perimeter(self):
        if (self.__width == 0) or (self.__height == 0):
            self.perimeter = 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        if (self.__width == 0) or (self.__height == 0):
            return("")
        else:
            a = []
            for c in range(self.__height):
                for d in range(self.__width):
                    a.append("#")
                a.append("\n")
        del a[-1]
        return("".join(a))

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
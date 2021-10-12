#!/usr/bin/python3
"""
Module:
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square 
    """
    def __init__(self, size):
        """ init 
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ area 
        """
        return (self.__size * self.__size)

    def __str__(self):
        """self
        """
        return("[Square] {}/{}".format(self.__size, self.__size))

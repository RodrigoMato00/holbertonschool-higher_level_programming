#!/usr/bin/python3
""" algo algo
    Algo
"""


class Square:
    """Algo Alguito"""

    def __init__(self, size=0):
        self.__size = size
    
    @property
    def size(self):
        """Algo algo algo"""
        return(self.__size)
    
    @size.setter
    def size(self, value):
        """Algo algo algo"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Algo"""
        return(self.__size ** 2)

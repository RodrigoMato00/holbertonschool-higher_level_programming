#!/usr/bin/python3
"""Algo algo algo
"""


class Square:
    """Algo Alguito"""
    def __init__(self, size=0, position=(0, 0)):
        """Algo algo algo"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
    @property
    def position(self):
        """Algo algo algo"""
        return self.__position
    @position.setter
    def position(self, value):
        """Algo algo algo algo"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    def area(self):
        """Más y más y más"""
        return self.__size ** 2

    

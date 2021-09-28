#!/usr/bin/python3
"""Algo algo
"""


class Square:
    """Alguito algo
    """
    def __init__(self, size=0):
        """Algo algo y más"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
    """Un poco algo más"""
        return (self.__size * self.__size)

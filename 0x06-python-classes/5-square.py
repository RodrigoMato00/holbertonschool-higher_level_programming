#!/usr/bin/python3
"""Algo algo
   Alguien paso por aqui
"""


class Square:
    """No me gustan los comentarios"""
    def __init__(self, size=0):
        """Comentario"""
        self.__size = size
    @property
    def size(self):
        """Alguien o algo"""
        return(self.__size)
    @size.setter
    def size(self, value):
        """Comentar es para tontos"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        """Hola hola"""
        return(self.__size ** 2)
    def my_print(self):
        """Algo algote"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)

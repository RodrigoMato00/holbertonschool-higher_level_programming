#!/usr/bin/python3
"""modulo Rectangle
"""

class Rectangle:
     """A nuestra clase Rectangle
        le agregamos un largo y un ancho"""
     def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

     @property
     def height(self):
          return self.__height

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
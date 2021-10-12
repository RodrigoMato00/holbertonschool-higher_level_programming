#!/usr/bin/python3
"""
Module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class REctangle"""
    def __init__(self, width, height):
        """ init
        """
        self.__width = width
        self.integer_validator("width", width)
        self.height = height
        self.integer_validator("height", height)

#!/usr/bin/python3
"""
Module __init__(self, width, height)
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""class BaseGeometry"""


class Rectangle(BaseGeometry):
    """class REctangle"""
    def __init__(self, width, height):
        """ init
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.height = height

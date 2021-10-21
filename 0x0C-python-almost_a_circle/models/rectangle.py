#!/usr/bin/python3
"""
=======================================================
Creation if the class Rectabgle that inherits from Base
=======================================================
"""

from models.base import Base


class Rectangle(Base):
    """ class Rectangle from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init Rectangle class """
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """kdkxjucyvukxnd
        """
        return self.__width

    @width.setter
    def width(self, width):
        """kfkcmvbdtyid
        """
        self.__width = width

        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """ldkcmdfsydif
        """
        return self.__height

    @height.setter
    def height(self, height):
        """lfidxmdvstdufk
        """
        self.__height = height

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be >= 0")

    @property
    def x(self):
        """lxlxodfsvcxbchud
        """
        return self.__x

    @x.setter
    def x(self, x):
        """fkjcnndfrirodkc
        """
        self.__x = x
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be > 0")

    @property
    def y(self):
        """dkdkcmdndufid
        """
        return self.__y

    @y.setter
    def y(self, y):
        """odlcldofodpoc
        """
        self.__y = y
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be > 0")

    def area(self):
        """kdccmfkrodlf
        """
        return self.width * self.height

    def display(self):
        """oflcmfdkifogod
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
        """lfldndbvdtfu
        """
        return("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):

        if len(args) > 0:

            for i in range(len(args)):

                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]
        else:
            if len(kwargs) > 0:

                k = kwargs.keys()

                for i in k:

                    if i == 'id':
                        self.id = kwargs['id']
                    if i == 'width':
                        self.width = kwargs['width']
                    if i == 'height':
                        self.height = kwargs['height']
                    if i == 'x':
                        self.x = kwargs['x']
                    if i == 'y':
                        self.y = kwargs['y']

    def to_dictionary(self):
        """iddmcfidxkcfif
        """

        dictionary = {}
        dictionary['id'] = self.id
        dictionary['width'] = self.width
        dictionary['height'] = self.height
        dictionary['x'] = self.x
        dictionary['y'] = self.y
        return dictionary

#!/usr/bin/python3
"""
class Student that defines a
student by: (based on 9-student.py)
"""

class Student:
    """ class student
    """


    def __init__(self, first_name, last_name, age):
        """ init
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to json
        """
        
        if type(attrs) is list:
            c = {}

            for a in attrs:
                if a in self.__dict__:
                    c[a] = self.__dict__[a]
            return c

        return self.__dict__

#!/usr/bin/python3
""" My class module
"""


class MyClass:
    """ My class
    """

    score = 0

    def __init__(self, name, number=4):
        """init
        """
        self.__name = name
        self.number = number
        self.is_team_red = (self.number % 2) == 0

    def win(self):
        """win
        """
        self.score += 1

    def lose(self):
        """lose
        """
        self.score -= 1

    def __str__(self):
        """str
        """
        return
        "[MyClass] {} - {} => {}".format(self.__name, self.number, self.score)

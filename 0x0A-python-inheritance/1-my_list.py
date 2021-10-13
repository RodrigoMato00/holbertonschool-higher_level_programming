#!/usr/bin/python3
"""
module print_sorted
"""


class MyList(list):
    """ MyList
    """

    def print_sorted(self):
        """
         prints the list,
         but sorted (ascending sort)
        """
        print(sorted(self))

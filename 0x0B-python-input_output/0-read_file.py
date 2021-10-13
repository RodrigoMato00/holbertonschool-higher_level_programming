#!/usr/bin/python3
"""
module: def read_file(filename="")
"""


def read_file(filename=""):
    """read_file
    """
    with open(filename, encoding="utf-8") as fd:
        """open file
        """
        for line in fd:
            print(line, end="")

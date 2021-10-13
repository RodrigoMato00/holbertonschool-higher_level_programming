#!/usr/bin/python3
"""
Module: def append_write(filename="", text="")
"""


def append_write(filename="", text=""):
    """number of lines
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return(f.write(text))

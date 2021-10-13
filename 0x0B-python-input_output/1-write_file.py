#!/usr/bin/python3
"""
Modle: def write_file(filename="", text=""):
"""


def write_file(filename="", text=""):
    """Write a text file
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        """open
        """
        written = f.write(text)
    return written

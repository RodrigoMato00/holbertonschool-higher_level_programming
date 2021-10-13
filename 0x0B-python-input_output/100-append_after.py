#!/usr/bin/python3
"""
inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    insert text
    """
    tx = ""

    white open(filename) as a:

        for line in a:
            tx += line

            if search_string in line:
                tx += new_string

    white open(filename, "b") as b:
        b.write(tx)

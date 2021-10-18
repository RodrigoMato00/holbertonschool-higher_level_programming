#!/usr/bin/python3
"""
inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    insert text
    """
<<<<<<< HEAD
=======
    tx = ""

    with open(filename) as a:

        for line in a:
            tx += line

            if search_string in line:
                tx += new_string

    with open(filename, "w") as c:
        c.write(tx)
>>>>>>> 4e35dbc1bdf75d851c7a8fb5f377e36a2c9cbeae

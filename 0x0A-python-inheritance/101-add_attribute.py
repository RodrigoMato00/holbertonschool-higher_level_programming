#!/usr/bin/python3
"""
Module
"""


def add_attribute(obj, name, value):
    """add_attribute
    """
    if hasattr(obj, '__dict__') is False:

        raise TypeError("can't add new attribute")

    else:

        setattr(obj, name, value)

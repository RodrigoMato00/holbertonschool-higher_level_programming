#!/usr/bin/python3
"""
Modulo lookup
"""


def lookup(obj):
    """returns the list of available attributes
    and methods of an object
    """
    list = dir(obj)
    return list
    

#!/usr/bin/python3
"""crear clase LockedClass"""


class LockedClass:
    """previene que el usuario cree una instancia"""
    __slots__ = ["first_name"]

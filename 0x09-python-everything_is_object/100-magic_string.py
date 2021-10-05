#!/usr/bin/python3
def magic_string(a=[]):
    magic_string.a = getattr(magic_string, a, 0) + 1
    return ", ".join(["BestSchool" for b in range(magic_string.a)])

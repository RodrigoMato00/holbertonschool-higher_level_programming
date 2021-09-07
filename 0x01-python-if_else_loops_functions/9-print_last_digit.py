#!/usr/bin/python3
def print_last_digit(number):
    var = int(repr(number)[-1])
    print("{}".format(var), end="")
    return var

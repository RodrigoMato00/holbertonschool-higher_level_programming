#!/usr/bin/env python3
def fizzbuzz():
    for num in range(1, 101):
        if (num % 15 == 0):
            print("fizzbuzz ", end="")
        elif (num % 3 == 0):
            print("fizz ", end="")
        elif (num % 5 == 0):
            print("buzz ", end="")
        else:
            print("{:d} ".format(num), end="")

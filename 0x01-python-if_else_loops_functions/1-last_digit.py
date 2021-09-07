#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
nextnum = abs(number) % 10
if number < 0:
    nextnum = -nextnum
print("Last digit of {} is {} ".format(number, nextnum), end="")
if nextnum > 5:
    print("and is greater than 5".format(number, nextnum))
elif number % 10 == 0:
    print("and this 0".format(number, nextnum))
elif nextnum < 6 and nextnum != 0:
    print("and is less than 6 and not 0".format(number, nextnum))

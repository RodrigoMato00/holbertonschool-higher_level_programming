#!/usr/bin/python3
n1 = 1
n2 = 0
while(n2 < 9):
    n = n1
    while(n < 10):
        if(n == 9 and n2 == 8):
            print('{:d}{:d}'.format(n2, n))
        else:
            print("{:d}{:d}".format(n2, n), end=", ")
        n = n + 1
    n1 = n1 + 1
    n2 = n2 + 1

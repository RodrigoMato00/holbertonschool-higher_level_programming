#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the
URL and displays the body of the response.
the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code.
"""

from requests import get
from sys import argv

if __name__ == "__main__":
        r_g = get(argv[1])
        if r_g.status_code < 400:
                print(r_g.text)
        else:
                print("Error code: {}".format(r_g.status_code))

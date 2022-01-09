#!/usr/bin/python3
"""

"""

import urllib.request as request
import urllib.error as error
from sys import argv

if __name__ == "__main__":

    r_r = request.Request(argv[1])
    try:
        with request.urlopen(r_r) as r:
            print(r.read().decode("utf-8"))
    except error.HTTPError as ur_err:
        print("Error code: {}".format(ur_err.code))

#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""

import urllib as request

if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as r:
        rr = r.read()
        print("Body response:")
        print("    - type: {}".format(type(rr)))
        print("    - content: {}".format(rr))
        print("    - utf8 content: {}".format(rr.decode("utf-8")))

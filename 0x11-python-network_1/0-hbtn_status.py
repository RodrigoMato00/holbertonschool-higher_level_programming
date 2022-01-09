#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""

import urllib.request as request

if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as r:
        rr = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(rr)))
        print("\t- content: {}".format(rr))
        print("\t- utf8 content: {}".format(rr.decode("utf-8")))

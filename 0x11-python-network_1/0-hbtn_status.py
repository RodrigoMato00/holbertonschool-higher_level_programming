#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""

import urllib.request as request

if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as r:
        print("Body response:")
        print("\t- type: {}".format(type(r.read())))
        print("\t- content: {}".format(r.read()))
        print("\t- utf8 content: {}".format(r.read().decode("utf-8")))

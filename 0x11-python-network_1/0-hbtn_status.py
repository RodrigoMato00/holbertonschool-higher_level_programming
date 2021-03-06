#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""

from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen('https://intranet.hbtn.io/status') as r:
        r_r = r.read()
        print('Body response:')
        print("\t- type: {}".format(type(r_r)))
        print("\t- content: {}".format(r_r))
        print("\t- utf8 content: {}".format(r_r.decode('utf-8')))

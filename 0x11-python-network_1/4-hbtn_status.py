#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
use the package requests
"""
from requests import get

if __name__ == "__main__":
    r_g = get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r_g.text)))
    print("\t- content: {}".format(r_g.text))

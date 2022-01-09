#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response (decoded in utf-8)
"""
import urllib.request as request
import urllib.parse as parse
from sys import argv

if __name__ == "__main__":
    email = {'email': argv[2]}
    comp = urllib.parse.urlencode(email).encode('ascii')
    r_r = urllib.request.Request(argv[1], comp)
    with urllib.request.urlopen(req) as r:
        print(r.read().decode('utf-8'))

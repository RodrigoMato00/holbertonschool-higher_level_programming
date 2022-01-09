#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
       and uses the GitHub API to display your id.
-The first argument will be your username
-The second argument will be your password (in your case, a personal
        access token as password)
"""

from requests import get
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    pas = HTTPBasicAuth(argv[1], argv[2])
    r_g = get("https://api.github.com/user", auth=pas)
    print(r_g.json().get("id"))

#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.
-The first argument will be the repository name.
-The second argument will be the owner name.
"""

from requests import get
from sys import argv

if __name__ == "__main__":
    init = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])
    r_g = get(init)
    commits = r_g.json()

    try:
        for count in range(10):
            print("{}: {}".format(commits[i].get("sha"), commits[i].get("commit").get("author").get("name")))

    except IndexError:
        pass

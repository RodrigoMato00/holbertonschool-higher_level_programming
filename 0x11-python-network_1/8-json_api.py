#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q.
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>.
"""
from requests import post
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:

        q = ""

    r = post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:

        r_dic = r.json()
        if len(r_dic.keys()) > 0:
            print("[{}] {}".format(r_dic.get('id'), r_dic.get('name')))

        else:
            print("No result")

    except:
        print("Not a valid JSON")

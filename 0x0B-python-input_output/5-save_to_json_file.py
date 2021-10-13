#!/usr/bin/python3
"""
Module: def save_to_json_file(my_obj, filename):
"""

import json


def save_to_json_file(my_obj, filename):
    """ save to json
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))

#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        i = fct(*args)
    except Exception as err:
        i = None
        print("Exception: {}".format(err), file=sys.stderr)
    finally:
        return i

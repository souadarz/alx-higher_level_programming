#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except ZeroDivisionError:
        result = None
        print("Exception: division by zero", file=sys.stderr)
    except IndexError:
        result = None
        print("Exception: list index out of range", file=sys.stderr)
    return (result)

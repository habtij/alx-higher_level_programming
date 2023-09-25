#!/usr/bin/python3

def safe_function(fct, *args):
    """executes a function safely"""
    try:
        res = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (None)
    return (res)

#!/usr/bin/python3

def safe_print_integers(value):
    try:
        print("{:d}."format(value))
        return True
    except TypeError:
        return False

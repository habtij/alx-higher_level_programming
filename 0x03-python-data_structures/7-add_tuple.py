#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Add the first two elements of tuples"""
    if not tuple_a and not tuple_b:
        return(0, 0)
    if not tuple_a:
        return(tuple_b)
    elif not tuple_b:
        return(tuple_a)
    if len(tuple_a) < 2:
        second_a = 0
    elif len(tuple_a) >= 2:
        second_a = tuple_a[1]

    if len(tuple_b) < 2:
        second_b = 0
    elif len(tuple_b) >= 2:
        second_b = tuple_b[1]

    return((tuple_a[0] + tuple_b[0], second_a + second_b))

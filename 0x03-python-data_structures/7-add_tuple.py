#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if not tuple_a and not tuple_b:
        return ((0, 0))
    if len(tuple_a) < 2:
        sec_a = 0
    else:
        sec_a = tuple_a[1]

    if len(tuple_b) < 2:
        sec_b = 0
    else:
        sec_b = tuple_b[1]

    if not tuple_a:
        return (tuple_b)
    elif not tuple_b:
        return (tuple_a)
    else:
        return ((tuple_a[0] + tuple_b[0], sec_a + sec_b))

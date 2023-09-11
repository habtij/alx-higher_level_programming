#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) < 1:
        return (None)
    max_val = my_list[0]
    for i in range(1, len(my_list)):
        if max_val > my_list[i]:
            continue
        else:
            max_val = my_list[i]
    return (max_val)

#!/usr/bin/python3

def no_c(my_string):
    """Remove all characters c and C from a string"""
    new_string = ""
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        else:
            new_string += my_string[i]
    return (new_string)

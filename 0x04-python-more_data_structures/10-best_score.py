#!/usr/bin/python3

def best_score(a_dictionary):
    """returns a key with the biggest integer value"""
    if a_dictionary is None:
        return (None)
    keys = sorted(a_dictionary)
    max_val = a_dictionary[keys[0]]
    max_key = keys[0]
    for i in a_dictionary:
        if a_dictionary[i] > max_val:
            max_val = a_dictionary[i]
            max_key = i
    return (max_key)

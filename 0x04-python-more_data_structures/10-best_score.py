#!/usr/bin/python3

def best_score(a_dictionary):
    """returns a key with the biggest integer value"""
    keys = sorted(a_dictionary)
    max_val = a_dictionary[keys[0]]
    max_key = keys[0]
    for i in keys:
        if a_dictionary[i] > max_val:
            max_val = a_dictionary[i]
            max_key = i
    return (max_key)

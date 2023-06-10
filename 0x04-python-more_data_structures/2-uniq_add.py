#!/usr/bin/python3

def uniq_add(my_list=[]):
    """adds all unique integers in a list"""
    if len(my_list) != 0:
        unique_num = set(my_list)
        return(sum(unique_num))
    return(0)

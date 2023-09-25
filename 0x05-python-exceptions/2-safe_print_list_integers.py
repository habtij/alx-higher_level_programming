#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers."""
    total_prnted = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            total_prnted += 1
        except (TypeError, ValueError, IndexError):
            print()
            return (total_prnted)
    print()
    return (total_prnted)

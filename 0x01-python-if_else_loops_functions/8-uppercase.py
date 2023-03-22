#!/usr/bin/python3

def uppercase(str):
    """Print string in uppercase character"""
    for chr in str:
        if ord(chr) >= 97 and ord(chr) <= 122:
            c = chr(ord(chr) - 32)
        print("{}".format(c), end="")
    print("\n")

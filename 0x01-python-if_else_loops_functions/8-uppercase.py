#!/usr/bin/python3

def uppercase(str):
    """Print string in uppercase character"""
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            ch = chr(ord(ch) - 32)
        print("{}".format(ch), end="")
    print("\n")

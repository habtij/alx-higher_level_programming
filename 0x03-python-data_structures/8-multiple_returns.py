#!/usr/bin/python3

def multiple_returns(sentence):
    """returns a tuple with length of string and its first char"""
    if len(sentence) == 0:
        return((0, None))
    else:
        return((len(sentence), sentence[0]))

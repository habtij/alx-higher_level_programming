#!/usr/bin/python3

def print_last_digit(number):
    """prints and return the last digit of a number"""
    if (number < 0):
        number = -number
    print(number % 10, end="")
    return (number % 10)

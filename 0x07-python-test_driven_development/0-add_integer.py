#usr/bin/python3

def add_integer(a, b=98):
    """return the sum of a and b"""

    if int(a) != a or float(a) != a:
        raise TypeError("a must be an integer")
    elif int(b) != b or float(b) != b:
        raise TypeError("b must be an integer")
    if a != "":
        return (int(a) + int(b))
#!/usr/bin/python3
"""Define a function ``pascal_triangle``"""


def pascal_triangle(n):
    """Represent pascal's triangle of size n"""
    if n <= 0:
        return []

    p_triangle = [[1]]
    while len(p_triangle) != n:
        tri = p_triangle[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        p_triangle.append(tmp)
    return p_triangle

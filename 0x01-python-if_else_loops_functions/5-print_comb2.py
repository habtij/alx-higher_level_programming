#!/usr/bin/python3
for i in range(100):
    if i < 10 or i < 99:
        print("{:02}".format(i), end=', ')
    if i == 99:
        print("{}".format(i))

#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)
    roman_dict = \
        {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_len = len(roman_string)
    if roman_len == 1:
        return (roman_dict[roman_string])

    num = 0
    for i in range(roman_len):
        if roman_string[i] == "I":
            if i+1 != roman_len and roman_string[i+1] == "V":
                i += 1
                num += 4
                break
            elif i+1 != roman_len and roman_string[i+1] == "X":
                i += 1
                num += 9
                break
            else:
                num += 1
        elif roman_string[i] == "X":
            if i+1 != roman_len and roman_string[i+1] == "L":
                i += 1
                num += 40
                break
            elif i+1 != roman_len and roman_string[i+1] == "C":
                i += 1
                num += 90
                break
            else:
                num += 10
        elif roman_string[i] == "C":
            if i+1 != roman_len and roman_string[i+1] == "D":
                i += 1
                num += 400
                break
            elif i+1 != roman_len and roman_string[i+1] == "M":
                i += 1
                num += 900
                break
            else:
                num += 100
        elif roman_string[i] == "V":
            num += 5
        elif roman_string[i] == "L":
            num += 50
        elif roman_string[i] == "D":
            num += 500
        elif roman_string[i] == "M":
            num += 1000
    return (num)

#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is int or roman_string is None:
        return 0
    add = 0
    for i in roman_string:
        if i == 'I':
            add += 1
        if i == 'V':
            add += 5
        if i == 'X':
            add += 10
        if i == 'L':
            add += 50
        if i == 'C':
            add += 100
        if i == 'D':
            add += 500
        if i == 'M':
            add += 1000
    return add

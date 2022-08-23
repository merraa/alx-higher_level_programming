#!/usr/bin/python3
for num1 in range(0, 9):
    for num2 in range(num1 + 1, 10):
        if (num1 == 8) & (num2 == 9):
            print("89")
        print("{0:d}{1:d}, ".format(num1, num2), end="")

#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        number = number * -1
    toStr = str(number)
    if (toStr.isnumeric()):
        last_digit = toStr[-1]
        print(last_digit, end="")
        return last_digit

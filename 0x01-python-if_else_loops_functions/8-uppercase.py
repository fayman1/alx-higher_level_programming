#!/usr/bin/python3
def uppercase(str):
    strs = ""
    for x in (str):
        y = ord(x)
        if y in range(97, 123):
            y = y - 32
            upperCase = chr(y)
        else:
            upperCase = x
        strs = strs + upperCase
    print("{}".format(strs))

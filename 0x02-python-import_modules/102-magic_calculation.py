#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    c = 0
    if a < b:
        c = add(a, b)
        for x in range(4, 6):
            c = add(c, x)
        return c
    else:
        c = sub(a, b)
        return c

#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    for p in range(x):
        try:
            print(my_list[p], end="")
            y += 1
        except IndexError:
            break
    print()
    return y

#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            n.append(True)
        else:
            n.append(False)
    return n

#!/usr/bin/python3
def uniq_add(my_list=[]):
    num = 0
    for x in set(my_list):
        num += x
    return num

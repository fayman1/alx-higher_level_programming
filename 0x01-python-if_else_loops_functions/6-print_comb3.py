#!/usr/bin/python3
for m in range(0, 10):
    for num2 in range(m+1, 10):
        t = str(m) + str(num2)
        if m < 8:
            print("{}".format(t), end=", ")
        else:
            print("{}".format(t))

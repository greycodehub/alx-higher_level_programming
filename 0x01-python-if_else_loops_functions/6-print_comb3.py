#!/usr/bin/python3

for numb in range(0, 10):
    for num in range(numb + 1, 10):
        if numb == 8 and num == 9:
            print("{}{}".format(numb, num))
        else:
            print("{}{}".format(numb, num), end=", ")

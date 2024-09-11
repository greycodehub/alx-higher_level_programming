#!/usr/bin/python3
import random

number = random.randint(-10, 10)
# condition to check for sign
if number < 0:
    print("{} is negative".format(number))
elif number > 0:
    print("{} is positive".format(number))
else:
    print("{} is zero".format(number))

#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Print all the integers of a list in reverse order."""
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))

#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """prints all the integers of a list"""
    for l in range(len(my_list)):
            print("{:d}".format(my_list[l]))

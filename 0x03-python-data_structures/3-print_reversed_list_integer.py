#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    [print("{:d}".format(x)) for x in range(len(my_list), 0, -1)]

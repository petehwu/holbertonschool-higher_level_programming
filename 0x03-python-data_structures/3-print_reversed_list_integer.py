#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if (len(my_list) == 0):
        print("None")
        return "None"
    else:
        [print("{:d}".format(x)) for x in my_list[::-1]]

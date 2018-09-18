#!/usr/bin/python3
def max_integer(my_list=[]):
    if (len(my_list) == 0):
        return ("None")
    tmp = my_list.copy()
    tmp.sort()
    return (tmp[-1])

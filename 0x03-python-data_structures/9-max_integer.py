#!/usr/bin/python3
def max_integer(my_list=[]):
    tmp = my_list.copy()
    tmp.sort()
    return (tmp[-1])

#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return None
    my_list.sort()
    prev = 0
    tot = 0
    for val in my_list:
        if val != prev:
            tot+= val
        prev = val
    return tot

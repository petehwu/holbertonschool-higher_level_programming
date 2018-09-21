#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or not my_list:
        return 0
    val = 0
    weight = 0
    for v, w in my_list:
        val += v * w
        weight += w
    return val / weight

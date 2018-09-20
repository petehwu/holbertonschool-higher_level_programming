#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    return [val if val != search else replace for val in my_list]

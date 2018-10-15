#!/usr/bin/python3


class MyList(list):
    """ MyList class inherts from list class """

    def print_sorted(self):
        """ prints out sorted list """
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)

#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nl = []
    val = 0
    for i in range(list_length):
        try:
            val = my_list_1[i] / my_list_2[i]
        except TypeError:
            val = 0
            print("{:s}".format("wrong type"))
        except ZeroDivisionError:
            val = 0
            print("{:s}".format("division by 0"))
        except IndexError:
            val = 0
            print("{:s}".format("out of range"))
        finally:
            nl.append(val)
    return nl

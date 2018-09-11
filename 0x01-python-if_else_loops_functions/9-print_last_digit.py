#!/usr/bin/python3
def print_last_digit(number):
    lastdig = int(str(number)[-1])
    print("{}".format(lastdig), end="")
    return(lastdig)

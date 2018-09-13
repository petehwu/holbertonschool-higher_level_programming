#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    numarg = len(argv) - 1
    print("{:d} argument".format(numarg), end="")
    if (numarg == 0):
        print("{}".format("s."))
    elif (numarg == 1):
        print("{}".format(":"))
    else:
        print("{}".format("s:"))
    for i in range(1, numarg + 1):
        print("{:d}: {}".format(i, argv[i]))

#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    numargs = len(argv)
    tot = 0
    for i in range(1, numargs):
        tot += int(argv[i])
    print("{:d}".format(tot))

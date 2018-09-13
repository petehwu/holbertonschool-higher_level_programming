#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add
    from calculator_1 import sub 
    from calculator_1 import mul
    from calculator_1 import div
    from sys import argv
    from sys import exit

    numargs = len(argv)
    if (numargs != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if (op == "+"):
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, add(a, b)))
    elif (op == "-"):
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, sub(a, b)))
    elif (op == "*"):
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, mul(a, b)))
    elif (op == "/"):
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    

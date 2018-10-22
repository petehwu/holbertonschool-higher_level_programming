#!/usr/bin/python3
""" 10-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(vars(s1))
    print(s1.size)
    s1.size = 10
    print(s1)
    print(s1.size)

    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    print("after error s1.size: {}".format(s1.size))
    print(vars(s1))

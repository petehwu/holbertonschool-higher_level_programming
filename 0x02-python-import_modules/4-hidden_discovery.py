#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    funcs = dir(hidden_4)

    for i in funcs:
        if i[0] != "_":
            print("{}".format(i))

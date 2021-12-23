#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    p = len(argv)
    if p == 1:
        print("0 arguments.")
    elif p == 2:
        print("1 argument:")
        print("1:", argv[1])
    else:
        print("{:d} arguments:".format(p - 1))
        for i in range(1, p):
            print("{:d}:".format(i), argv[i])

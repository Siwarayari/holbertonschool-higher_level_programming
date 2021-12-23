#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    p = len(argv)
    if p == 1:
        print("0")
    elif p == 2:
        print(argv[1])
    else:
        s = 0
        for i in range(1, p):
            s += int(argv[i])
        print("{:d}".format(s))

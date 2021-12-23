#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for c in dir(hidden_4):
        if c[:2] != "__":
            print("{:s}".format(c))

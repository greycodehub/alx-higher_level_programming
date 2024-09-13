#!/usr/bin/python3

if __name__ == "__main__":
    """the number of and list of arguments."""
    import sys

    counted = len(sys.argv) - 1
    if counted == 0:
        print("0 arguments.")
    elif counted == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(counted))
    for i in range(counted):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

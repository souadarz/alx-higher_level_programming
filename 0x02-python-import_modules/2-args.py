#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv) - 1
    if n == 1:
        print("{:d} argument".format(n))
    else:
        print("{:d} arguments".format(n))
    for i in range(1, n + 1):
        print("{:d}: {:s}".format(i, argv[i]))

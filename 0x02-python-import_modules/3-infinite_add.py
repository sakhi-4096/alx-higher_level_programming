#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    size = len(argv)
    total = 0
    if size > 1:
        for i in range(1, size):
            total += int(argv[i])
    print("{:d}".format(total))

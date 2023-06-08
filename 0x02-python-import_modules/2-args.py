#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    user_args = argv[1:]
    size = len(user_args)
    print("{:d} {:s}{:s}".
          format(size,
                 "arguments" if (size) != 1 else "argument",
                 "." if (size) == 0 else ":"))
    for i, arg in enumerate(user_args):
        print("{:d}: {:s}".format(i + 1, arg))

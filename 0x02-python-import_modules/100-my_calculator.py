#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    size = len(argv)
    if size != 4:
        print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)

    operator = argv[2]
    func = {"+": add, "-": sub, "*": mul, "/": div}
    if operator not in func:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, func[operator](a, b)))

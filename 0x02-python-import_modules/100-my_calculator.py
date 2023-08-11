#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    arg_len = len(argv)
    usage = "Usage: ./100-my_calculator.py <a> <operator> <b>"
    operators = "Unknown operator. Available operators: +, -, * and /"
    if (arg_len - 1) != 3:
        print(usage)
        exit(1)
    
    if (arg_len - 1) >= 3:
        opcode = 2
        for opcode in range(opcode, arg_len - 1, 3):
            if argv[opcode] == '+':
                a = int(argv[opcode - 1])
                b = int(argv[opcode + 1])
                print("{} + {} = {}".format(a, b, add(a, b)))
                continue
            if argv[opcode] == '-':
                a = int(argv[opcode - 1])
                b = int(argv[opcode + 1])
                print("{} - {} = {}".format(a, b, sub(a, b)))
                continue
            if argv[opcode] == '*':
                a = int(argv[opcode - 1])
                b = int(argv[opcode + 1])
                print("{} * {} = {}".format(a, b, mul(a, b)))
                continue
            if argv[opcode] == '/':
                a = int(argv[opcode - 1])
                b = int(argv[opcode + 1])
                print("{} / {} = {}".format(a, b, div(a, b)))
                continue
            else:
                print(operators)
                exit(1)

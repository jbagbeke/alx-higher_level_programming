#!/usr/bin/python3
from calculator_1 import add_it, mul_it, sub_it, div_it
if __name__ == "__main__":
    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add_it()))
    print("{} - {} = {}".format(a, b, sub_it()))
    print("{} / {} = {}".format(a, b, div_it()))
    print("{} * {} = {}".format(a, b, mul_it()))

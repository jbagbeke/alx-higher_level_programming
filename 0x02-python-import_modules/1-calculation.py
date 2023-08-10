#!/usr/bin/python3
from calculator_1 import add_it, mul_it, sub_it, div_it
if __name__ == "__main__":
    a = 10
    b = 5

    add_result = add_it(a, b)
    sub_result = sub_it(a, b)
    div_result = div_it(a, b)
    mul_result = mul_it(a, b)

    print("{} + {} = {}".format(a, b, add_result))
    print("{} - {} = {}".format(a, b, sub_result))
    print("{} / {} = {}".format(a, b, div_result))
    print("{} * {} = {}".format(a, b, mul_result))

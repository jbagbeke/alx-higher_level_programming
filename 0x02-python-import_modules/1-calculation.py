#!/usr/bin/python3
from calculator_1 import add_it, mul_it, sub_it, div_it
a = 10
b = 5
print("{} + {} = {}".format(a, b, add_it(a, b)))
print("{} - {} = {}".format(a, b, sub_it(a, b)))
print("{} / {} = {}".format(a, b, div_it(a, b)))
print("{} * {} = {}".format(a, b, mul_it(a, b)))

#!/usr/bin/python3
from sys import argv
arg_len = len(argv)
if arg_len < 2:
    print("{} arguments.".format(0))
if arg_len == 2:
    print("{} argument:\n{}: {}".format(1, 1, argv[1]))
if arg_len > 2:
    print("{} arguments:".format(arg_len - 1))
    for i in range(arg_len - 1):
        print("{}: {}".format(i+1, argv[i+1]))

#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arg_len = len(argv)
    total_sum = 0
    if arg_len < 2:
        print("{}".format(0))
    if arg_len == 2:
        print("{}".format(argv[1]))
    if arg_len > 2:
        for i in range(arg_len - 1):
            total_sum += int(argv[i + 1])
        print("{}".format(total_sum))

#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    index = -1
    for reverse in range(len(my_list)):
        print("{:d}".format(my_list[index]))
        index += -1

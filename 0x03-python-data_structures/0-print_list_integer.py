#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for num in range(len(my_list)):
        print("{}".format(my_list[num]))



my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

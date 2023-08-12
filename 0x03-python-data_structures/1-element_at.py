#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > (len(my_list) - 1):
        return (None)

    for index in range(len(my_list)):
        if index == idx:
            return (my_list[index])

#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if isinstance(my_list, list):
        list_len = len(my_list)

        if idx < 0 or idx > (list_len - 1):
            return (my_list)

        for index in range(list_len):
            if index == idx:
                del (my_list[index])
                return (my_list)

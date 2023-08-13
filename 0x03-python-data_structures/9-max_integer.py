#!/usr/bin/python3
def max_integer(my_list=[]):
    if isinstance(my_list, list):
        list_len = len(my_list)
        if list_len == 0:
            return (None)

        max_int = my_list[0]
        for index in (range(list_len)):
            if max_int > my_list[index]:
                continue
            else:
                max_int = my_list[index]
        return (max_int)

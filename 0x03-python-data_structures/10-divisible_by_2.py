#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if isinstance(my_list, list):
        list_len = len(my_list)
        new_list = my_list.copy()
        for div in range(list_len):
            if (new_list[div] % 2) == 0:
                new_list[div] = True
                continue
            else:
                new_list[div] = False
        return (new_list)

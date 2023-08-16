#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if isinstance(my_list, list):
        new_list = my_list.copy()
        if search in my_list:
            list_len = len(my_list)
            for idx in range(list_len):
                if new_list[idx] == search:
                    new_list[idx] = replace
        return (new_list)

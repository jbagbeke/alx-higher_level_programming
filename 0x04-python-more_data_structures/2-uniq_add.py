#!/usr/bin/python3

def uniq_add(my_list=[]):
    if isinstance(my_list, list):
        uniq_list = []
        for index in my_list:
            if index not in uniq_list:
                uniq_list.append(index)
        add_it = 0
        for idx in range(len(uniq_list)):
            add_it += uniq_list[idx]
        return (add_it)

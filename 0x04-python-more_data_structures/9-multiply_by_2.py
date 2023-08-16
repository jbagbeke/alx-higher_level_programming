#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    if isinstance(a_dictionary, dict):
        new_dict = a_dictionary.copy()
        for val in new_dict:
            tmp = new_dict[val]
            new_dict[val] = tmp * 2
        return (new_dict)

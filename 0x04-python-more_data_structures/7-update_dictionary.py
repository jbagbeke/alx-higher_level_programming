#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if isinstance(a_dictionary, dict) and value != None:
        if key in a_dictionary:
            a_dictionary[key] = value
        if key not in a_dictionary:
            new_dict = dict(key)
            new_dict[key] = value
            a_dictionary | new_dict
        return (a_dictionary)

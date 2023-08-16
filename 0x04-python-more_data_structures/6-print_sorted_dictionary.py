#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if isinstance(a_dictionary, dict):
        sorted_key = sorted(a_dictionary.keys())

        for key in sorted_key:
            print("{}: {}".format(key, a_dictionary[key]))

#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return (None)

    if isinstance(a_dictionary, dict):
        values = max(a_dictionary.values())
        for val in a_dictionary:
            tmp = int(a_dictionary[val])
            if tmp == values:
                return (val)
    else:
        return (None)

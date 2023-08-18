#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if isinstance(a_dictionary, dict):
        dic_len = len(a_dictionary)
        del_list = []
        for key in a_dictionary:
            if a_dictionary[key] == value:
                del_list.append(key)
        for key_del in del_list:
            del (a_dictionary[key_del])
        del_list[:] = []
        return (a_dictionary)

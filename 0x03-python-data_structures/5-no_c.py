#!/usr/bin/python3
def no_c(my_string):
    if isinstance(my_string, str):
        new_string = ""
        for index in my_string:
            if index == "c" or index == "C":
                continue
            else:
                new_string += index
        return (new_string)

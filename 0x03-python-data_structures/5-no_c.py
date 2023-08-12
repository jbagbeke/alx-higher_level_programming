#!/usr/bin/python3
def no_c(my_string):
    new_list = list(my_string)
    empty = ""
    for index in range(len(new_list)):
        if new_list[index] == "C":
            del (new_list[index])
            for i in new_list:
                empty += i
            my_string = empty
        return (my_string)

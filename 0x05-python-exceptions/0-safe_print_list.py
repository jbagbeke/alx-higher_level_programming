#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if isinstance(my_list, list):
        index = 0
        length = 0
        for i in my_list:
            length += 1
        for n in range(x):
            try:
                print("{}".format(my_list[n]), end='\n' if n == (length - 1) else '')
            except IndexError:
                pass
            except Exception:
                pass
            else:
                index += 1
        return (index)

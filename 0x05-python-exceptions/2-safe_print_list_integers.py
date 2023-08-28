#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if isinstance(my_list, list):
        index = 0
        for n in range(x):
            try:
                print("{:d}".format(my_list[n]), end='')
                index += 1
            except (TypeError, ValueError):
                pass
            except IndexError:
                raise
        print('')
        return (index)

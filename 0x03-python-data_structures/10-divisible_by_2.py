#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if isinstance(my_list, list):
        list_len = len(my_list)
        new_list = my_list.copy()
        for div in range(list_len):
            if (new_list[div] % 2) == 0:
                new_list[div] = True
                continue
            else:
                new_list[div] = False
        return (new_list)

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1


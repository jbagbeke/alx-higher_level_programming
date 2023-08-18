#!/usr/bin/python3
def weight_average(my_list=[]):
    if isinstance(my_list, list):
        if not my_list:
            return (0)
        list_len = len(my_list)
        numerator = 0
        denominator = 0
        for avg in range(list_len):
            numerator += (my_list[avg][0] * my_list[avg][1])
            denominator += my_list[avg][1]
        average = numerator / denominator
        return (average)

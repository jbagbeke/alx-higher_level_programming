#!/usr/bin/python3
""" Finds peak of numbers in list """


def find_peak(list_of_integers):
    """ Finds a peak in a list of unsorted integers """

    llen = len(list_of_integers)
    list_int = list_of_integers
    peak_list = []

    for idx in range(llen):
        if idx - 1 < 0 and idx + 1 < llen:
            if list_int[idx] >= list_int[idx + 1]:
                peak_list.append(list_int[idx])
        if idx - 1 > 0 and idx + 1 >= llen:
            if list_int[idx] >= list_int[idx - 1]:
                peak_list.append(list_int[idx])
        if idx - 1 > 0 and idx + 1 < llen:
            num = list_int[idx]
            if num >= list_int[idx - 1] and num >= list_int[idx + 1]:
                if num not in peak_list:
                    peak_list.append(num)

    if peak_list:
        return max(peak_list)

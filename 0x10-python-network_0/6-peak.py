#!/usr/bin/python3
""" Finds peak of numbers in list """


def find_peak(list_of_integers):
    """ Finds a peak in a list of unsorted integers """

    llen = len(list_of_integers)
    llist = list_of_integers
    peak_list = []

    for idx in range(0, llen, 2):
        if idx - 1 < 0 and idx + 1 < llen:
            tmp = []
            if llist[idx] not in peak_list:
                tmp.extend([llist[idx], llist[idx + 1]])
                peak_list.append(max(tmp))
        if idx + 1 >= llen and idx - 1 > 0:
            tmp = []
            if llist[idx] not in peak_list:
                tmp.extend([llist[idx], llist[idx - 1]])
                peak_list.append(max(tmp))
        if idx - 1 > 0 and idx + 1 < llen:
            tmp = []
            tmp.extend([llist[idx], llist[idx - 1], llist[idx + 1]])
            if max(tmp) == llist[idx]:
                peak_list.append(llist[idx])

    if peak_list:
        return max(peak_list)

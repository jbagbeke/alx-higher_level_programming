#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    if isinstance(set_1, set) and isinstance(set_2, set):
        diff_list = []
        for idx_1 in set_1:
            if idx_1 not in set_2 and idx_1 not in diff_list:
                diff_list.append(idx_1)

        for idx_2 in set_2:
            if idx_2 not in set_1 and idx_2 not in diff_list:
                diff_list.append(idx_2)

        return (set(diff_list))

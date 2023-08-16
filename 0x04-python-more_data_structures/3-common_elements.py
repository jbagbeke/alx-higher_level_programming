#!/usr/bin/python3

def common_elements(set_1, set_2):
    if isinstance(set_1, set) and isinstance(set_2, set):
        com_list = []
        for idx_1 in set_1:
            for idx_2 in set_2:
                if idx_1 == idx_2 and idx_1 not in com_list:
                    com_list.append(idx_1)
        return (set(com_list))

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

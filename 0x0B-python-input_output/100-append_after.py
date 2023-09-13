#!/usr/bin/python3
"""
Inserts a line of text to a file, after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts line of text to file, after each line containing a specific string

    Args:
        Arg1: (filename) Name of file to read from
        Arg2: (search_string) Target string
        Arg3: (new_string) String to insert after target string
    """

    new_lines = []
    with open(filename, "r", encoding="UTF-8") as file:
        for lines in file:
            if search_string in lines:
                new_lines.append(lines)
                new_lines.append(new_string)
            else:
                new_lines.append(lines)

    with open(filename, "w", encoding="UTF-8") as file:
        file.writelines(new_lines)

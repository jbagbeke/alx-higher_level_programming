#!/usr/bin/python3
def uppercase(input_str):
    upper_letter = ''
    for letter in input_str:
        if 'a' <= letter <= 'z':
            letter = chr(ord(letter) - 32)
            upper_letter += letter
        else:
            upper_letter += letter

    print("{}".format(upper_letter))

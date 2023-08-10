#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    match argv[2]:
        case '+':
            a = 1 + 5
            print(a)
        case '-':
            print("hello")
        case _:
            print("Funny")

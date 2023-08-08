#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    if ord(c) >= 65 and ord(c) <= 90:
        return False



print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))

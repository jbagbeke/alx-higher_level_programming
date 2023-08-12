string = "Hello world"
empty = ""

for i in string:
    if i == "o" or i == "O":
        continue
    else:
        empty += i

print(empty)

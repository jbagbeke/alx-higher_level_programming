string = "Hello World"

lists = list(string)
print(lists)
del (lists[0])
stg = ""
for i in lists:
    stg = stg + i
print(stg)

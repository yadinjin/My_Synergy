from pprint import pprint

dict = {}
for i in range(10, -6, -1):
    dict[i] = i ** i
pprint(dict)
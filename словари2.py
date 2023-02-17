from pprint import pprint

tmp = {}
for i in range(10, -6, -1):
    tmp[i] = i ** i
pprint(tmp)
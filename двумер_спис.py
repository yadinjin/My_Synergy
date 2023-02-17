def pl(t):
    for i in t:
        print(*i)
x = int(input())
y = int(input())
house = [[0 for i in range(y)] for i in range(x)]
cnt = 1

for i in range(-1, -x - 1, -1):
    if i % 2 == 1:
        for j in range(y):
            house[i][j] = cnt
            cnt += 1
    else:
        for j in range(-1, -y - 1, -1):
            house[i][j] = cnt
            cnt += 1
pl(house)
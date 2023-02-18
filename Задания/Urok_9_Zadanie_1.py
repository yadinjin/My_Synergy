print('Введите количество чисел:')
k = 1
n = int(input())
s = list(map(int,input().split())) [:n]
print(s)
for i in range(0, n-1):
    if s[i] != s[i+1]:
        k += 1
print("Количество различных чисел в списке: ",k)
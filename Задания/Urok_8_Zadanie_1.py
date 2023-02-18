n = int(input("Введите количество чисел: "))
res = []
for i in range(n):
     a = int(input(f"Введите {i+1}-е число: "))
     res.append(a)
print(res)
res.reverse()
print(res)
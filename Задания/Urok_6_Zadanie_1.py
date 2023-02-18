print('Введите количество чисел:')
n = int(input())
cnt = 0
for i in range(n):
    a = int(input(f"Введите число {i+1}: "))
    if a == 0:
        cnt += 1
print("Количество введенных нулей = ",cnt)
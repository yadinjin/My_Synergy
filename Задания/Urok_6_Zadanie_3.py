print('Введите число A:')
A = int(input())
print('Введите число B:')
B = int(input())
if A > B:
    print('А больше В, введите другие числа!')
elif A%2 == 0:
    for i in range(A, B+1, 2):
        print(i, end=' ')
else:
    for i in range(A+1, B+1, 2):
        print(i, end=' ')
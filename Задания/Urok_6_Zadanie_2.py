print('Введите число:')
x = int(input())
cnt = 0
if x<=2e6:
    for i in range(1, x+1):
        if x%i == 0:
            cnt += 1
            print(i)
    print('Количество натуральных делителей числа ', x, ' (включая 1 и само число) - ',cnt)
else:
    print('Введите число меньше 2 млрд')
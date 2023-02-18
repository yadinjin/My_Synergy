print('Введите минимальную сумму инвестиций, $:')
min_invest = int(input())
print('Введите сумму, которой располагает Майкл, $:')
sum_Mike = int(input())
print('Введите сумму, которой располагает Иван, $:')
sum_Ivan = int(input())
if (sum_Mike >= min_invest) and (sum_Ivan>=min_invest):
    print('2')
elif sum_Mike >= min_invest:
    print('Mike')
elif sum_Ivan >= min_invest:
    print('Ivan')
elif sum_Mike+sum_Ivan >= min_invest:
    print('1')
else:
    print('0')
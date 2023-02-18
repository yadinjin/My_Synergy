print('Введите максимальную массу, которую может выдержать одна лодка: ')
m = int(input())
print('Введите количество рыбаков: ')
n = int(input())
fishers = [] 
for i in range(n):
    print(f'Введите вес {i+1} рыбака' )
    fishers.insert(i, int(input()))
fishers.sort()
print(fishers)  
boat = 0  
for i in range(n):
    if fishers[i] == m: # проверяем если вес рыбака равен грузоподъемности лодки
        boat += 1       # увеличиваем счетчик лодок на 1
        fishers[i]=0    # исключаем рыбака из списка, обнуляем :)
        print('цикл 1', fishers, i)
for i in range(n):
    for j in range(1, n, 1):
        if i != j and fishers[i]+fishers[j] == m:  # проверка i != j необходима для исключения сравнения рыбака с самим собой
            boat += 1     # затем проверяем сумму веса соседних рыбаков и если она равна грузоподъемности лодки, увеличиваем счетчик лодок на 1
            fishers[i]=0  # исключаем обоих рыбаков из списка, обнуляем :)        
            fishers[j]=0
            print('цикл 2', fishers, i, j)
for i in range(n):
    for j in range(1, n, 1):
        if i != j and fishers[i] > 0 and fishers[j] > 0 and fishers[i]-fishers[j] == 0: # проверяем рыбаков на обнуление :)
            boat += 1   # если вес соседних рыбаков одинаковый, увеличиваем счетчик лодок на 1, при этом рыбаки с общим весом 
            fishers[i]=0
            fishers[j]=0
            print('цикл 3', fishers, i, j)            
for i in range(n):
    for j in range(1, n, 1):
        if i != j and fishers[i] > 0 and fishers[j] > 0 and fishers[i]+fishers[j] < m and fishers[i]-fishers[j] != 0 and fishers[j]-fishers[i] > 0:
            boat += 1
            fishers[i]=0
            fishers[j]=0
            print('цикл 4', fishers, i, j)
print('Для переправки',n,'рыбаков необходимо:',boat,'лодок')
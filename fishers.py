print('Введите максимальную массу, которую может выдержать одна лодка: ')
m = int(input())
print('Введите количество рыбаков: ')
n = int(input())
fishers = [] 
for i in range(n):
    print(f'Введите вес {i+1} рыбака' )
    fishers.insert(i, int(input()))
#fishers.sort()
print(fishers)  
boat = 0  
for i in range(n):
    if fishers[i] == m:
        boat += 1
        fishers.pop(i)
        print(fishers)
for i in range(len(fishers)):
    for j in range(len(fishers)):
        if i != j and fishers[i]+fishers[j] == m:
            boat += 1
            fishers.pop(i)
            fishers.pop(j)
            print('цикл 2', fishers, i, j)
print('Для переправки',n,'рыбаков необходимо:',boat,'лодок')
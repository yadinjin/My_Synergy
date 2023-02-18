print('Введите пятизначное число:')
a = int(input())
one = a%10
ten = a%100//10
hundred = a%1000//100
thousand = a%10000//1000
hundredsofthousands = a%100000//10000
print(hundredsofthousands, thousand, hundred, ten, one)
itog = (ten**one)*hundred/(hundredsofthousands-thousand)
print(itog)
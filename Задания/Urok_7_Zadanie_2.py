print('Введите строку:')
str = input()
tmp = str.split()         # удаляем пробелы
tmp = ' '.join(tmp)
print(tmp)
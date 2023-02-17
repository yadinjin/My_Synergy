class Kassa(object):
    
    def __init__(self, summa):
        self.summa = summa
    
    def top_up(self, X):
        self.summa += X
    
    def count_1000(self):
        return self.summa // 1000
    
    def take_away(self,X):
        if (self.summa - X) < 0:
            print('Недостаточно средств')
        else:
            return self.summa - X
        
kkm = Kassa(0)        
command = ()
while command != 'stop':
    print("Введите команду")
    print("1 - внесение в кассу")
    print("2 - остаток 1000 купюр в кассе")
    print("3 - изъятие из кассы")
    print("stop - закрыть смену")
    command = input()
    if command == '1':
        X = int(input('Введите сумму для внесения в кассу: '))
        kkm.top_up(X)
        print(f'Сумма в кассе {kkm.summa} рублей')
    elif command == '2':
        ost = kkm.count_1000()
        print(f'В кассе {ost} купюр номиналом 1000 рублей')
    elif command == '3':
        X = int(input('Введите сумму для изъятия из кассы: '))
        ost = kkm.take_away(X)
        print(f'В кассе  осталось {ost} рублей')
    else:
        if command != 'stop':
            print('Ошибка! Повторите ввод')
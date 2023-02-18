import collections
#from pprint import pprint

def create():
    last = collections.deque(pets, maxlen=1)[0]
    pets_name = input("Введите имя питомца: ")
    kind_of_pet = input("Вид питомца: ")
    age_of_pet = int(input("Возраст питомца: "))
    owners_name= input("Имя владельца: ")
    new_pets = {
        pets_name: {
            "Вид питомца": kind_of_pet,
            "Возраст питомца": age_of_pet,
            "Имя владельца": owners_name
             }
    }
    pets[last+1] = new_pets

def read():
    def get_suffix(k):
     # функция, с помощью которой можно получить суффикс
     # 'год', 'года', 'лет'
     # реализацию этой функции вам предстоит придумать самостоятельно
     # функция будет возвращать соответствующую строку
     key = list(pets[k])[0]
     if (2 <= pets[k].get(key).get("Возраст питомца") % 10 <=4) \
      and not(11 <= pets[k].get(key).get("Возраст питомца") %100 <=14): 
        age = 'года'
     elif pets[k].get(key).get("Возраст питомца") % 10 == 1 \
      and pets[k].get(key).get("Возраст питомца") % 100 != 11: 
        age = 'год'
     else: 
        age = 'лет'
     return age
    
    k = int(input('Введите номер записи, которую хотите просмотреть: '))
    
    if k in pets.keys():
        age = get_suffix(k)
        key = list(pets[k])[0]
        print("Это",pets[k].get(key).get("Вид питомца"), \
            "по кличке",key,"Возраст питомца",pets[k].get(key).get("Возраст питомца")\
            ,age,"Имя владельца",pets[k].get(key).get("Имя владельца")) 
    else:
        print('Записи с таким номером не найдено')   
    return k
   
def update():
    k = int(input('Введите номер записи, которую хотите изменить: '))
    key = list(pets[k])[0]
    print('Чтобы изменить данные введите ключ и новое значение в формате \
    "ключ":"значение" без кавычек')
    new_data = input()
    new_data1,new_data2 = new_data.split(':')
    if new_data1 == 'Возраст питомца':
        new_data2 = int(new_data2)
        pets[k][key][new_data1] = new_data2 
    pets[k][key][new_data1] = new_data2 
    
    
def delete():
    d = int(input('Выберите номер записи, которую нужно удалить: '))
    pets.pop(d, 'Выбран неверный номер записи либо такой записи не существует')
    pets_list()
    
#def get_pet(ID):
  # функция, с помощью которой вы получите информацию о питомце в виде словаря
  # сделайте проверку, если питомца с таким ID нету в нашей "базе данных"
  # верните в этом случае False
  # а если питомец всё же есть в "базе данных" - верните информацию о нём
  # выглядеть это может примерно так:
  #  return pets[ID] if ID in pets.keys() else False

def pets_list():
  # Эта функция будет создана для удобства отображения всего списка питомцев
  # Информацию по каждому питомцу можно вывести с помощью цикла for
     for k in pets:
        print(k,':',pets[k])
        
pets = {
    1:
        {
            "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": 9,
                "Имя владельца": "Павел"
            },
        },
    2:
        {
            "Каа": {
                "Вид питомца": "желторотый питон",
                "Возраст питомца": 21,
                "Имя владельца": "Саша"
            },
        },
    # и так далее
}    
command = ()
while command != 'stop':
    print("Введите команду")
    print("create - создать новую запись")
    print("read - вывести информацию о питомце")
    print("update - обновить информацию о питомце")
    print("delete - удалить запись о питомце")
    print("stop - для заверения работы с программой")
    command = input()
    if command == 'create':
        pets_list()
        create()
    elif command == 'read':
        pets_list()
        read()
    elif command == 'update':
        pets_list()
        update()
    elif command == 'delete':
        pets_list()
        delete()   
pets_list()        
#pprint(pets)
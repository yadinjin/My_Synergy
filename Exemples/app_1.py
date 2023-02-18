from pprint import pprint
import collections

#def switch():
#    switcher = {
#        1: create,
#        2: "read",
#        3: "update",
#        4: "delete",
#        5: "stop"
#        }
  
 
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
    continue_ = input("Желаете продолжить ввод новых данных? Да/Нет: ")
    return continue_

def update():
    k = int(input('Введите номер записи, которую хотите изменить: '))
    key = list(pets[k])[0]
    print('Чтобы изменить данные введите ключ и новое значение в формате \
    "ключ":"значение" без кавычек')
    new_data = input()
    new_data1,new_data2 = new_data.split(':')
    print(new_data1, new_data2)
    if new_data1 == 'Возраст питомца':
        new_data2 =int(new_data2)
        print(new_data2)
        pets[k][key][new_data1] = new_data2
    pets[k][key][new_data1] = new_data2
    

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
                "Возраст питомца": 19,
                "Имя владельца": "Саша"
            },
        },
    # и так далее
}
last = collections.deque(pets, maxlen=1)[0]
print(last)
print("Введите команду")
print("create - создать новую запись")
print("read - вывести информацию о питомце")
print("update - обновить информацию о питомце")
print("delete - удалить запись о питомце")
print("stop - для заверения работы с программой")
command = input()
update()
pprint(pets)
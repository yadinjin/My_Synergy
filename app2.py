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
#items = pets.items()
#print(items)
keys = pets.keys()
print(list(keys))
#values = pets.values()
#print(list(values))
#print(list(pets[1])[0])
k = int(input('Введите номер записи, которую хотите изменить: '))
key = list(pets[k])[0]
print(key)
#print('Чтобы изменить данные введите ключ и новое значение в формате \
#    "ключ":"значение" без кавычек')
#    new_data = input()
#    new_data1,new_data2 = new_data.split(':')
#    if new_data1 == 'Возраст питомца':
#        new_data2 = map(int, new_data2)
print(pets[k].get(key).get('Возраст питомца'))# = new_data2
pets[k][key]['Возраст питомца'] = 15 
print(pets[k].get(key).get('Возраст питомца'))
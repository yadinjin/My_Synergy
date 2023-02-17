pets_name = input("Введите имя питомца: ")
kind_of_pet = input("Вид питомца: ")
age_of_pet = int(input("Возраст питомца: "))
owners_name= input("Имя владельца: ")
age =()
pets = {
     "Питомец": 
        {
            "Имя питомца" : pets_name,
            "Вид питомца" : kind_of_pet, 
            "Возраст питомца" : age_of_pet, 
            "Имя владельца" : owners_name
        } 
}

if (2 <= age_of_pet % 10 <=4) and not(11 <= age_of_pet %100 <=14): 
    age = 'года'
elif age_of_pet % 10 == 1 and age_of_pet % 100 != 11: 
    age = 'год'
else: 
    age = 'лет'
    
print("Это",pets["Питомец"]["Вид питомца"],"по кличке",pets["Питомец"]["Имя питомца"])
print("Возраст питомца",pets["Питомец"]["Возраст питомца"],age)
print("Имя владельца",pets["Питомец"]["Имя владельца"]) 
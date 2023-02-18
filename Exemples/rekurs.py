my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def func(my_list):
    if len(my_list) == 0:
        print("Конец списка")
    else:
        print(my_list.pop(0))
        func(my_list)
        
func(my_list)

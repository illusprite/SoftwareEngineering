import copy

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
def correction(a):
    copy_a = copy.deepcopy(a)
    main_list = [*set(a)] #Массив с одним вхождением
    for x in main_list:  # Убираем первое вхождение в основном массиве
        if x in a:
            a.remove(x)
    main_list = [*set(copy_a)]
    for x in a: #Пробегается по элементам Основного
        b = x
        while b in main_list:
            b = str(b) + str(x)
        main_list.append(b)
    print(set(main_list))

correction(list_1)
correction(list_2)
correction(list_3)

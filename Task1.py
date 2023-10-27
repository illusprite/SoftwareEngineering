from datetime import datetime #импортируем функцию datetime из библиотеки datetime
from math import sqrt #импортируем функцию sqrt из библиотеки math
def main(**kwargs): # Определение функции main с использованием параметров kwargs
    for key in kwargs.items(): # Проход по каждой паре ключ-значение в словаре
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2) # Вычисление квадратного корня
        print(result) # Вывод результата


#Следующий блок кода будет выполнен только при запуске модуля напрямую
if __name__ == '__main__':
    start_time = datetime.now() # Запись текущего времени перед выполнением функции main
    main(  # Вызов функции main с передачей словаря аргументов
        one = [10, 3],
        two = [5, 4],
        three = [15, 13],
        four = [93, 53],
        five = [133, 15]
    )
    time_costs = datetime.now() - start_time  # Рассчет времени выполнения
    print(f"Время выполнения программы - {time_costs}") # Вывод времени выполнения
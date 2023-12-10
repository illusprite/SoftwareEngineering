from check_selection import check_selection
from quotes_and_chart import run
from search_securities import search_figi_securities, search_all_securities

if __name__ == '__main__':

    #Стартовый блок

    #Тут происходит выбор типа финансового иснтрумента
    print(f"Доступные типы инструментов:\n1 - Акции\n2 - Облигации\n3 - Валюта")
    choice_type = int(input("Введите номер типа искомого инструмента: "))
    if choice_type < 1 or choice_type > 3: choice_type = check_selection(choice_type, 1, 3)#Повтор кода в отдельной функции

    #Список активов(Пример)
    spisok = int(input("Вывести как пример список активов в выбранном типе? 1 - Да, 2 - Нет "))
    if spisok < 1 or spisok > 2: choice_type = check_selection(spisok, 1, 2)  # Повтор кода в отдельной функции
    if spisok==1: print(search_all_securities(choice_type))

    # Ввод ТИКЕРА(Яндекс - YNDX)
    print("\nПримечание! Тикеры нужно специально находить. У акций могут быть простые тикеры в отилчие от валют и облигаций.")
    choice_ticker = input("Введите ТИКЕР искомого инструмента(Яндекс - YNDX): ")
    choice_figi = search_figi_securities(choice_ticker, choice_type)

    # Выбор временного отрезка
    print(f"Доступные интервалы времени:\n1 - Неделя\n2 - Месяц\n3 - Год")
    choice_time = int(input("Введите номер типа искомого инструмента: "))
    if choice_time < 1 or choice_time > 2: choice_time = check_selection(choice_time, 1, 4)  # Повтор кода в отдельной функции
    print(f"Вы выбрали:\n")

    run(choice_figi, choice_time)
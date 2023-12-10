def check_selection(selection, selection_min, selection_max):
    if selection < selection_min or selection > selection_max:
        while selection < selection_min or selection > selection_max:
            print(f"Нужно выбрать от {selection_min} до {selection_max}!")
            selection = int(input("Введите номер типа искомого инструмента: "))
    return selection
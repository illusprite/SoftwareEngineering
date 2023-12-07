def add_two_numbers():
    try:
        user_input = input("Введите число: ")
        number = float(user_input)
        result = 2 + number
        print(f"Результат сложения 2 и введенного числа: {result}")

    except ValueError:
        print("Ошибка: Неподходящий тип данных. Ожидалось число.")


add_two_numbers()  # 3.5
add_two_numbers()  # "abc"
add_two_numbers()  # 7.8
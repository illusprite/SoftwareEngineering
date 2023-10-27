"""
Сред арифм от аргументов функции с условием того, что изанчальнео кол-во аргументов неизвестно

1 ф
1 т входа


я так вижу
вводится число, выводится среднее и предложение ввести новое число
"""
def calculate_average(*args):
    if not args:
        return 0
    total = sum(args)
    average = total / len(args)
    return average

if __name__ == "__main__":
    user_input = input("Введите числа: ")
    numbers = [float(num) for num in user_input.split()]
    result = calculate_average(*numbers)
    print(f"Среднее арифметическое: {result}")

user_input = input("Введите числа: ")
numbers_list = [int(num) for num in user_input.split()]
numbers_tuple = tuple(numbers_list)
print(f"Список: {numbers_list} \nКортеж: {numbers_tuple}")
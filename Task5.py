class CustomException(Exception):
    def __init__(self, message="Произошла ошибка"):
        self.message = message
        super().__init__(self.message)
def f_one(value):
    try:
        if value < 0:
            raise CustomException("Значение не может быть отрицательным")
        else:
            print("Функция one выполнена")
    except CustomException as e:
        print(f"Ошибка: {e}")
def f_two():
    try:
        print("Функция two выполнена")
        # Генерация исключения
        raise CustomException("Пример ошибки в функции two")
    except CustomException as e:
        print(f"Ошибка: {e}")

# Тесты
f_one(34)     # Выполнится успешно
f_one(-36)    # Вызовет исключение
f_two()      # Вызовет исключение
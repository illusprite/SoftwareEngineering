try:

    with open("empty_file.txt", "r") as file:
        content = file.read()

        if not content:
            raise Exception("Файл пустой")

        print("Содержимое файла:")
        print(content)

except FileNotFoundError:
    print("Файл не найден")

except Exception as e:
    print(f"Исключение: {e}")
    print("Файл пустой")
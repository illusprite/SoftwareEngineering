transport = int(input("Введите затраты на проезд: "))
food = int(input("Введите затраты на питание: "))
house = int(input("Введите затраты на квартиру: "))
total = transport + food + house

with open("file2.txt", "w") as file:
    file.write(f"Итого:\n"
      f"Проезд: {transport} р.\n"
      f"Питание: {food} р.\n"
      f"Квартира: {house} р.\n"
      f"Всего: {total} р.")

print(f"Итого:\n"
      f"Проезд: {transport} р.\n"
      f"Питание: {food} р.\n"
      f"Квартира: {house} р.\n"
      f"Всего: {total} р.")
c = int(input("Введите число от 0 до 10: "))
if c>10 or c<0:
    print("Числе не в диапазоне.")
elif (c >= 0 and c < 4):
    print("От 0 до 3")
elif (c >= 4 and c < 6):
    print("От 3 до 6")
elif (c >= 6 and c < 11):
    print("От 6 до 10")
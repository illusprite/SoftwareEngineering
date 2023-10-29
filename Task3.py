line = input("Введите последовательность чисел: ")
while len(line)<=15:
    print("нужно минимум 15 символов.")
    line = input("Введите последовательность чисел: ")
def top_3_numbers(line):
    line = list(map(int, line))
    my_dict = {x: line.count(x) for x in range(10)}
    print(my_dict)

top_3_numbers(line)
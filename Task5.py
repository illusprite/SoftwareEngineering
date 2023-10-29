def tuple_remove(my_tuple):
    for i in range(len(my_tuple)):
        if i in my_tuple:
            my_tuple.remove(i)
    result_tuple = tuple(my_tuple)
    print(result_tuple)

if __name__ == "__main__":
    x = input("Входные данные: ")
    input_list = []
    for k in x:
        if k.isdigit():
            input_list.append(int(k))
    tuple_remove(input_list)
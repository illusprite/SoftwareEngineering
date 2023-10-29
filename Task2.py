def tuple_remove(my_tuple, ch):
    if ch in my_tuple:
        my_tuple.remove(ch)
    result_tuple = tuple(my_tuple)
    print(result_tuple)

if __name__ == "__main__":
    x = input("Входные данные: ")
    input_list = []
    for k in x:
        if k.isdigit():
            input_list.append(int(k))
    ch = input_list[len(input_list)-1]
    input_list.pop()
    tuple_remove(input_list, ch)

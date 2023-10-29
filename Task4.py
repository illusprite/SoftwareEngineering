def tuple_remove(my_tuple, ch):
    if my_tuple.count(ch)>=2:
        my_tuple = my_tuple[my_tuple.index(ch):my_tuple.index(ch, 2)+1]
        print(tuple(my_tuple))
    elif ch in my_tuple:
        my_tuple = my_tuple[my_tuple.index(ch):len(my_tuple)]
        print(tuple(my_tuple))
    else:
        print(tuple())

if __name__ == "__main__":
    x = input("Входные данные: ")
    input_list = []
    for k in x:
        if k.isdigit():
            input_list.append(int(k))
    ch = input_list[len(input_list)-1]
    input_list.pop()
    tuple_remove(input_list, ch)
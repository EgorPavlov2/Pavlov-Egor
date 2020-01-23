con = ""


def main():
    print("Что вы хотите зделать?")
    print("Кодировать или Декодировать")
    cod = input()  # запрашиваю команду на действие
    if cod == "Кодировать":  # Выполняю команду
        print(encode_to_morse(text))
    elif cod == "Декодировать":
        print(decode_from_morse(code))
    else:
        print("Ошибка, если хотите попобовать ещё раз отправте в консоль 1, если нет 0")
        global con
        con = input()  # даю пользователю 2 шанс


if con == "1":
    con == ""
    main()

name = None

def welcome_user():
    global name
    name = input("Введите свое имя: ")
    print(f"Приятно познакомиться, {name}")
    return name

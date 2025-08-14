name = None

def welcome_user():
    global name
    name = input("May I have your name? ")
    print(f"Hello, {name}")
    return name

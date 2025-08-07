import random

MIN_NUMBER = 1
MAX_NUMBER = 100

def game_rules():   
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")


def game():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)

    answer = input(f"Question: {number} ")
    correct_answer = is_prime(number)

    return answer, correct_answer


def is_prime(num):
    if num <= 1:
        return "yes"
    if num == 2:
        return "no"
    if num % 2 == 0:
        return "no"
    # Проверяем делимость только до квадратного корня из n
    sqrt_n = int(num ** 0.5) + 1
    for i in range(3, sqrt_n, 2):
        if num % i == 0:
            return "no"
    return "no"
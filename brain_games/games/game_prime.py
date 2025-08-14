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
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return "no"
    return "yes"
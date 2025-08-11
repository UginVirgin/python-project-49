import random

MIN_NUMBER = 1
MAX_NUMBER = 100

def game_rules():   
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")

def game():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    answer = input(f"Question: {number}  ")

    correct_answer = "yes" if is_even_number(number) else "no"
    return answer, correct_answer

def is_even_number(number):
    return number % 2 == 0


    
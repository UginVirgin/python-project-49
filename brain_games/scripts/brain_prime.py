import random

from ..cli import welcome_user
from .brain_games import greet

def game_rules():   
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")

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


#переменная вынесена в глобальную область видимости для использования в функции last()
count_correct_answers = 0


def questions(name):
    global count_correct_answers
    count_correct_answers = 0
    total_questions = 3

    for q in range(total_questions):
        
        number = random.randint(1, 10000)

        answer = input(f"Question: {number} ")
        correct_answer = is_prime(number)

        if correct_answer == answer:
            print("Correct!")
            count_correct_answers += 1
        elif correct_answer != answer:
            print(f"\"{answer}\" is wrong answer ;(. Correct answer was \"{correct_answer}\". Let's try again, {name}")

    return count_correct_answers

def last(name):
    if count_correct_answers == 3:
        print(f"Congratulations, {name}!")
    else:
        print(f"Good try, {name}! You answered {count_correct_answers} out of 3 questions correctly.")

def main():
    greet()
    name = welcome_user()
    game_rules()
    questions(name)
    last(name)

if __name__ == "__main__":
    main()








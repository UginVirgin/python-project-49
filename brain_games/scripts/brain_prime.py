import random

from ..cli import welcome_user
from .brain_games import greet
from .brain_question import FINAL_RESULTS


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
answer = None
correct_answer = None


def questions(name):
    from .brain_question import checking_correct_answer

    global count_correct_answers
    global answer
    global correct_answer
    
    count_correct_answers = 0
    total_questions = 3

    for q in range(total_questions):
        
        number = random.randint(1, 10000)

        answer = input(f"Question: {number} ")
        correct_answer = is_prime(number)


        if checking_correct_answer(answer, correct_answer, name):
            count_correct_answers += 1

    return count_correct_answers, answer, correct_answer


def main():
    greet()
    name = welcome_user()
    game_rules()
    questions(name)
    FINAL_RESULTS(name)


if __name__ == "__main__":
    main()








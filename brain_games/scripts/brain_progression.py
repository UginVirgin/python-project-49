import random

from ..cli import welcome_user
from .brain_games import greet

def game_rules():   
    print("Find the greatest common divisor of given numbers.")

def currentElement():
    currentElement = start + index * step

#переменная вынесена в глобальную область видимости для использования в функции last()
count_correct_answers = 0


def questions(name):
    global count_correct_answers
    count_correct_answers = 0
    total_questions = 3

    for q in range(total_questions):
        count = 10
        start = random.randint(1, 100)
        step = random.randint(1, 100)

        progression = [start + i * step for i in range(count)]

        index_to_replace = random.randint(0, count - 1)
        replaced_number = progression[index_to_replace]

        progression[index_to_replace] = '...'

        answer = input(f"Question: {progression} ")
        correct_answer = replaced_number

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








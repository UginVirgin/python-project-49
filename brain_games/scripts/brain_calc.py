import random

from ..cli import welcome_user
from .brain_games import greet

def game_rules():   
    print("What is the result of the expression?")

def choice_operator():
    operators = ["+","-","*"]
    operator = random.choice(operators)
    return operator



#переменная вынесена в глобальную область видимости для использования в функции last()
count_correct_answers = 0


def questions(name):
    global count_correct_answers
    count_correct_answers = 0
    total_questions = 3

    for q in range(total_questions):
        number1 = random.randint(1,100)
        number2 = random.randint(1,100)
        answer = input(f"Question: {number1} {choice_operator} {number2} ")
        operator = choice_operator()
        correct_answer = eval(f'{number1} {operator} { number2}')

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








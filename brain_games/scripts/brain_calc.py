import random

from ..cli import welcome_user
from .brain_games import greet

def game_rules():
    print("What is the result of the expression?")

def choice_operator():
    operators = ["+", "-", "*"]
    return random.choice(operators)

# переменная для подсчета правильных ответов
count_correct_answers = 0

def questions(name):
    global count_correct_answers
    count_correct_answers = 0
    total_questions = 3

    for _ in range(total_questions):
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        operator = choice_operator()  # выбираем оператор один раз для каждого вопроса

        # выводим вопрос
        print(f"Question: {number1} {operator} {number2}")
        answer_str = input("Your answer: ")

        # пытаемся преобразовать ответ в число
        try:
            answer = int(answer_str)
        except ValueError:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}". Let\'s try again, {name}')
            continue

        # вычисляем правильный ответ
        correct_answer = eval(f'{number1} {operator} {number2}')

        if answer == correct_answer:
            print("Correct!")
            count_correct_answers += 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}". Let\'s try again, {name}')

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
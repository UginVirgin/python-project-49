import random

MIN_NUMBER = 1
MAX_NUMBER = 100

def game_rules():
    print("What is the result of the expression?")


def game():
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = choice_operator()

    print(f"Question: {number1} {operator} {number2}")
    answer_str = input("Your answer: ")
    correct_answer = eval(f'{number1} {operator} {number2}')

    try:
        answer = int(answer_str)
    except ValueError:
        print(
            f'"{answer}" is wrong answer ;(. '
            f'Correct answer was "{correct_answer}". '
            f"Let's try again, {name}"
            )

    return answer, correct_answer


def choice_operator():
    operators = ["+", "-", "*"]
    return random.choice(operators)
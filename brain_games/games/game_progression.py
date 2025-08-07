import random

MIN_NUMBER = 1
MAX_NUMBER = 10


def game_rules():   
    print("What number is missing in the progression?")


def game():
    count = 10
    start = random.randint(MIN_NUMBER, MAX_NUMBER)
    step = random.randint(MIN_NUMBER, MAX_NUMBER)

    progression = [start + i * step for i in range(count)]
    index_to_replace = random.randint(0, count - 1)
    replaced_number = progression[index_to_replace]
    progression[index_to_replace] = '...'
    answer_str = input(f"Question: {progression} ")

    try:
        answer = int(answer_str)
    except ValueError:
        print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}". Let\'s try again, {name}')

    correct_answer = replaced_number
    return answer, correct_answer
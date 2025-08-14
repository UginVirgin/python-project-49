import random

MIN_NUMBER = 1
MAX_NUMBER = 10


def game_rules():   
    print("What number is missing in the progression?")


def game(name):
    count = 10
    start = random.randint(MIN_NUMBER, MAX_NUMBER)
    step = random.randint(MIN_NUMBER, MAX_NUMBER)

    progression = [start + i * step for i in range(count)]
    index_to_replace = random.randint(0, count - 1)
    replaced_number = progression[index_to_replace]
    progression_with_hole = progression.copy()
    progression_with_hole[index_to_replace] = '..'

    answer_str = input(
        'Question: ' + ' '.join(str(x) for x in progression_with_hole) + " "
        )
    correct_answer = replaced_number

    try:
        answer = int(answer_str)
    except ValueError:
        answer = answer_str

    return answer, correct_answer
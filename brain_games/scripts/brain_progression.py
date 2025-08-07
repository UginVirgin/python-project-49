import random

from ..cli import welcome_user
from .brain_games import greet
from .brain_question import FINAL_RESULTS


def game_rules():   
    print("What number is missing in the progression?")


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
        count = 10
        start = random.randint(1, 10)
        step = random.randint(1, 10)

        progression = [start + i * step for i in range(count)]
        index_to_replace = random.randint(0, count - 1)
        replaced_number = progression[index_to_replace]
        progression[index_to_replace] = '...'
        answer_str = input(f"Question: {progression} ")

        # преобразовываем ответ в число если это не число
        try:
            answer = int(answer_str)
        except ValueError:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}". Let\'s try again, {name}')
            continue

        correct_answer = replaced_number

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








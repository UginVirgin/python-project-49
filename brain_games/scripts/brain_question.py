from ..cli import welcome_user

def checking_correct_answer(answer, correct_answer, name):
    from .brain_progression import count_correct_answers, answer, correct_answer
    from .brain_prime import count_correct_answers, answer, correct_answer

    if correct_answer == answer:
            print("Correct!")
            return True
    elif correct_answer != answer:
        print(f"\"{answer}\" is wrong answer ;(. Correct answer was \"{correct_answer}\". Let's try again, {name}")
        return False


def FINAL_RESULTS(name):
    from .brain_progression import count_correct_answers
    if count_correct_answers == 3:
        print(f"Congratulations, {name}!")
    else:
        print(f"Good try, {name}! You answered {count_correct_answers} out of 3 questions correctly.")
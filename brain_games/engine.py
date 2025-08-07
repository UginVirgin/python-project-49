from brain_games.cli import welcome_user


def game_engine(game, games_rules):
    name = welcome_user()
    games_rules()

    count_correct_answers = 0
    TOTAL_QUESTIONS = 3

    for _ in range(TOTAL_QUESTIONS):
        answer, correct_answer = game()
        if correct_answer == answer:
            print("Correct!")
            count_correct_answers += 1
        elif correct_answer != answer:
            print(f"\"{answer}\" is wrong answer ;(. Correct answer was \"{correct_answer}\". Let's try again, {name}")
            break
    else:
        print(f"Congratulations, {name}!")
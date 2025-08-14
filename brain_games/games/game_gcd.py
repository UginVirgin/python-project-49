import random


def game_rules():   
    print("Find the greatest common divisor of given numbers.")


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


def game():
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 50)

    answer_str = input(f"Question: {number1} {number2} ")
    correct_answer = gcd(number1, number2)
    
    try:
        answer = int(answer_str)
    except ValueError:
        answer = answer_str
    
    return answer, correct_answer
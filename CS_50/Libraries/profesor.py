
import random

def generate_problem():
    x = random.randint(0, 99)
    y = random.randint(0, 99)
    return x, y, x + y

def prompt_level():
    while True:
        level = input("Enter a level (1, 2, or 3): ")
        if level in ['1', '2', '3']:
            return int(level)
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

def prompt_answer(problem):
    tries = 0
    while tries < 3:
        answer = input(f"What is {problem[0]} + {problem[1]}? ")
        try:
            answer = int(answer)
            if answer == problem[2]:
                return True
            else:
                print("EEE")
        except ValueError:
            print("EEE")
        tries += 1
    print(f"The correct answer is: {problem[2]}")
    return False

def main():
    level = prompt_level()
    score = 0
    for _ in range(10):
        problem = generate_problem()
        print(f"Solve: {problem[0]} + {problem[1]} = ")
        if prompt_answer(problem):
            score += 1
    print(f"Your score is: {score}/10")

if __name__ == "__main__":
    main()

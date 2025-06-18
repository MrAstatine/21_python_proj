import random

COLORS = ["R", "W", "O", "G", "B", "Y"]
TRIES = 10
CODE_LEN = 4


def generate_code():
    return [random.choice(COLORS) for _ in range(4)]


# print(generate_code())


def guess_code():
    guess = (
        input("Enter your guess (4 colors from R, W, O, G, B, Y): ")
        .strip()
        .upper()
        .split(" ")
    )
    if len(guess) != CODE_LEN or any(color not in COLORS for color in guess):
        print(f"Invalid guess. Please enter exactly {CODE_LEN} colors from {COLORS}.")
        return guess_code()
    return guess


def check_code(guess, real_code):
    color_count = {}
    correct_pos = 0
    incorrect_pos = 0
    for color in real_code:
        if color not in color_count:
            color_count[color] = 0
        color_count[color] += 1
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_count[guess_color] -= 1
        elif guess_color in color_count and color_count[guess_color] > 0:
            incorrect_pos += 1
            color_count[guess_color] -= 1
    return correct_pos, incorrect_pos


def game():
    print("Welcome to the 4 Color Match Game!")
    print(
        f"You have {TRIES} tries to guess the code. The code is {CODE_LEN} colors long."
    )
    print(f"Available colors: {', '.join(COLORS)}")
    print("Let's start the game!")
    code = generate_code()
    for attempt in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        print("Attempt", attempt)
        print(f"Correct colors in correct position: {correct_pos}")
        print(f"Correct colors in incorrect position: {incorrect_pos}")
        if correct_pos == CODE_LEN:
            print("Congratulations! You've guessed the code!")
            break
    else:
        print("Sorry, you've used all your attempts.")
        print(f"The correct code was: {' '.join(code)}")


if __name__ == "__main__":
    game()

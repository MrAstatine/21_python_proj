import random

option = ["rock", "paper", "scissors"]
user_win = 0
comp_win = 0
while True:
    user_choice = input(
        "Enter a choice (rock, paper, scissors) or 'q' to quit: "
    ).lower()
    if user_choice == "q":
        break
    while user_choice not in option:
        user_choice = input(
            "Invalid input. Enter a choice (rock, paper, scissors): "
        ).lower()
    random_no = random.randint(0, 2)
    # rock=0, paper=1, scissor=2
    comp_guess = option[random_no]
    print(f"\nComputer chose {comp_guess}, you chose {user_choice}.\n")
    if user_choice == comp_guess:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == "rock" and comp_guess == "scissors":
        print("Rock smashes scissors! You win!")
        user_win += 1
    elif user_choice == "rock" and comp_guess == "paper":
        print("Paper covers rock! You lose!")
        comp_win += 1
    elif user_choice == "paper" and comp_guess == "scissors":
        print("Scissors cuts paper! You lose!")
        comp_win += 1
    elif user_choice == "paper" and comp_guess == "rock":
        print("Paper covers rock! You win!")
        user_win += 1
    elif user_choice == "scissors" and comp_guess == "paper":
        print("Scissors cuts paper! You win!")
        user_win += 1
    elif user_choice == "scissors" and comp_guess == "rock":
        print("Rock smashes scissors! You lose!")
        comp_win += 1
    print("___________________________________________________________________")
print(" Final score - You " + str(user_win) + "  || Computer " + str(comp_win))
print("Goodbye!!")

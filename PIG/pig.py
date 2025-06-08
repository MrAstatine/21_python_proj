import random


def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val, max_val)
    return roll


# roll()  # This will return a random number between 1 and 6.
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Please enter a number between 2 and 4.")
    else:
        print("Invalid input.")
max_score = 50
player_score = [0 for _ in range((players))]
# print(player_score)
while max(player_score) < max_score:
    for player_idx in range(players):
        print("\nPlayer ", player_idx + 1, "turn\n")
        print("Current score: ", player_score[player_idx], "\n")
        current_score = 0
        while True:
            should_roll = (
                input("Would you like to roll (Y)es or (N)o? ").lower().strip()
            )
            if should_roll != "y":
                break
            value = roll()
            if value == 1:
                print("You rolled a 1. Turn done.")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)
            print("Your score is : ", current_score)
        player_score[player_idx] += current_score
        print(" Player ", player_idx + 1, " score is : ", player_score[player_idx])
max_score = max(player_score)
winning_indx = player_score.index(max_score)
print(" Player ", winning_indx + 1, " wins with a score of ", max_score)

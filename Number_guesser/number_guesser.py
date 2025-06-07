import random

"""
 r = random.randrange(-1, 10)
 this gives no between -1 and 9. 10 not given. ig u hv just written 10 it will give 0 to 9.
 print(r)
 random.randint(-1,11)   this will include 11 in the range
"""
top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a positive number greater than 0")
        quit()
else:
    print("Not a valid number. Please type a number greater than 0")
    quit()
random_number = random.randint(0, top_of_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a Guess : ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print(" Not a valid number. Please type a number")
        continue
    if user_guess == random_number:
        print("You have guessed it right")
        break
    elif user_guess > random_number:
        print("Too high")
    else:
        print("Too low")
print("You got it in ", guesses, "guesses")

name = input("Type your name: ")
print("Hello, " + name + "! Welcome to the Adventure!")
answer = input(
    "You are on a dirt road. It has come to an end and you can go left or right. What would you like to do? Type 'Left' or 'Right': "
).lower()
if answer == "left":
    answer = input(
        "You have come to a river. You can walk around it or swim through it. Type 'Walk' to walk around or 'Swim' to swim through: "
    ).lower()
    if answer == "walk":
        print(
            "----You walked for miles and miles and eventually ran out of water. You died of dehydration."
        )
    elif answer == "swim":
        print("----You swam through the river and were caught by a crocodile!")
    else:
        print("----Come on dude. Use your brain a bit. It ain't that hard. Try again.")
elif answer == "right":
    answer = input(
        "You come to a bridge. It looks wobbly. Do you want to cross it or walk back. Type 'Cross' to cross it or 'Back' to walk back: "
    ).lower()
    if answer == "cross":
        answer = input(
            "You cross the bridge and meet a strnager. Do you talk to them? Type 'Yes' to talk or 'No' to not talk: "
        ).lower()
        if answer == "yes":
            print("----You talked to the stranger and were rewarded. You won the game!")
        elif answer == "no":
            print(
                "----You didn't talk to the stranger and were punished. You lost the game!"
            )
        else:
            print(
                "----I think that you have exhausted your brain capacity that's why you can't think of anything. Try again."
            )
    elif answer == "back":
        print("----You go back and get eaten by a bear!")
    else:
        print(
            "----Did you eat the intoxicating mushrooms on the way, that you are not able to decide properly?"
        )
else:
    print(f"----Seriously {name}, you had two option and you still messed up!!!")
print("Thank you for playing!")

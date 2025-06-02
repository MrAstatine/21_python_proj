print("Welcome to my Quiz!")
playing = input("Do you want to play?(yes/no): ")
print(playing)
if playing.lower() != "yes":
    quit()
print("Okay! Let's play!😁")
score = 0
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("You got " + str(score) + " correct!")
print("You got " + str((score / 4) * 100) + "%.")

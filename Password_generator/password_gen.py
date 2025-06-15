import random
import string


def generate_password(min_length=12, use_numbers=True, use_special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    characters = letters
    if use_numbers:
        characters += digits
    if use_special_chars:
        characters += special_chars
    pwd = ""
    meet_criteria = False
    has_no = False
    has_spl = False
    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        if new_char in digits:
            has_no = True
        elif new_char in special_chars:
            has_spl = True
        meet_criteria = True
        if use_numbers:
            meet_criteria = has_no
        if use_special_chars:
            meet_criteria = meet_criteria and has_spl
    return pwd


min_len = int(input("Enter minimum length of password: "))
has_no = input("Include numbers? (yes/no): ").strip().lower() == "yes"
has_spl = input("Include special characters? (yes/no): ").strip().lower() == "yes"
if min_len < 1:
    print("Minimum length should be greater than 0")
else:
    print("The generated password is: ", generate_password(min_len, has_no, has_spl))

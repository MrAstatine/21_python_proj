from cryptography.fernet import Fernet

"""
uncomment this to generate a key in key.key     
If u leave this uncommented then each time u run the code then key changes
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


write_key()
"""


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            # print(line.rstrip())
            data = line.rstrip()
            user, passw = data.split("|")
            print(
                f"\tUser: {user} ||| Password: ", fer.decrypt(passw.encode()).decode()
            )


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "\nWould you like to add a password or view all passwords? Type 'Add' to add a password or 'View' to view all passwords or 'Q' to quit: "
    ).lower()
    if mode == "q":
        print("Goodbye!")
        break
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode. Please try again.")

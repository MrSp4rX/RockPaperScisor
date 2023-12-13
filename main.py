import random, os

os.system("clear")

choices = {
    1 : "rock",
    2 : "paper",
    3 : "scisor"
}

def replay():
    while True:
        n = input("Wanna Play Again? (y/n) - ")
        if n.lower() == "y":
            return True
        elif n.lower() == "n":
            return False
        else:
            print("Didn't Get you?")
            input("Press Enter to Continue.")
            os.system("clear")

def getInput():
    choice = input("Enter Your Choice-\n1. Rock\n2. Paper\n3. Scisor\n")
    if choice.isnumeric():
        choice = int(choice)
        if choice <= 3 and choice > 0:
            return choices.get(choice)
        else:
            print("Please Choose Correct Option.")
            input("Press Enter to Continue.")
            os.system("clear")
            getInput()
    else:
        choice = str(choice)
        if choice.lower() == "q":
            print("Exiting...")
            input("Press Enter to Continue.")
            os.system("clear")
            exit()
        else:
            print("Only Numeric Keys are Allowed.\nPress q to Quite.")
            input("Press Enter to Continue.")
            os.system("clear")
            getInput()

def getwinner(uinput, pcinput):
    winner = False

    if uinput == "rock" and pcinput == "scisor":
        winner = True
    
    elif uinput == "paper" and pcinput == "rock":
        winner = True

    elif uinput == "scisor" and pcinput == "paper":
        winner = True
    
    return winner

def final(choice):
    pc_choice = random.choice(["rock", "paper", "scisor"])
    if choice == pc_choice:
        print("Match Tied!")
        print(f"You - {choice.capitalize()} and Computer - {pc_choice.capitalize()}")
        if replay():
            os.system("clear")
            main()
        else:
            input("Press Enter to Continue.")
            os.system("clear")
            print("Game Finally Closed!")
    elif getwinner(choice, pc_choice):
        print(f"You - {choice.capitalize()} and Computer - {pc_choice.capitalize()}")
        print("Won!")
        if replay():
            os.system("clear")
            main()
        else:
            print("Game Finally Closed!")
    else:
        print(f"You - {choice.capitalize()} and Computer - {pc_choice.capitalize()}")
        print("Loose!")
        if replay():
            os.system("clear")
            main()
        else:
            print("Game Finally Closed!")
            input("Press Enter to Continue.")
            os.system("clear")

def main():
    choice = getInput()
    final(choice)

if __name__ == "__main__":
    main()
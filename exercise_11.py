# PIEDRA PAPEL O TIJERA

import random

options = ("rock", "paper", "scissors")
running = True

print("PYTHON GAME ROCK, PAPER AND SCISSORS")

while running:
    ans  =  None
    choice = random.choice(options)
    while ans not in options:
        ans = input("Select choose of them (rock, paper and scissors): ").lower()
        if ans == choice:
            print("IT'S A TIE!")
        elif ans == "rock" and choice == "scissors":
            print("YOU WIN!")
        elif ans == "paper" and choice == "rock":
            print("YOU WIN!")
        elif ans == "scissors" and choice == "paper":
            print("YOU WIN!")
        else:
            print("YOU LOSE!")

        print(f"Player: {ans}")
        print(f"Computer: {choice}")

    again = input("Play again (Y/N)?: ").upper()
    if not again == "Y":
        running = False

print("Thanks for playing!")
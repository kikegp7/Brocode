# Ahorcado

import random

words = ["ferrari", "apple", "nvidia", "alienware", "perro"]

hangman_art = { 0: ("   ",
                    "   ",
                    "   ",),
                1: (" O ",
                    "   ",
                    "   ",),
                2: (" O ",
                    " | ",
                    "   ",),
                3: (" O ",
                    "/| ",
                    "   ",),
                4: (" O ",
                    "/|\\",
                    "   ",),
                5: (" O  ",
                    "/|\\",
                    "/  ",),
                6: (" O  ",
                    "/|\\",
                    "/ \\",), }


def display_man(wrong_guesses):
    print("--------------------")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("--------------------")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    letters_guesses = set()
    is_running = True

    while is_running:

        display_man(wrong_guesses)
        display_hint(hint)
        user_guess = input("Enter a letter: ").lower()

        if len(user_guess) != 1 or not user_guess.isalpha():
            print("Invalid input!")
            continue

        if user_guess in letters_guesses:
            print(f"The {user_guess} is already guessed.")
            continue

        letters_guesses.add(user_guess)

        if user_guess in answer:
            for i in range(len(answer)):
                if answer[i] == user_guess:
                    hint[i] = user_guess
        else:
            wrong_guesses += 1


        if wrong_guesses >= len(hangman_art)-1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Lose!")
            is_running = False

        if "".join(hint) == answer:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Win!") 
            is_running = False   

               


if __name__ == '__main__':
    main()
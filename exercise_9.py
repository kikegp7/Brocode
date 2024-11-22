# Python Quiz Game

questions = ("How many elements are in the periodic table?",
             "Which animal lays the largest eggs?",
             "What is the most abundant gas in Earth's atmosphere?",
             "How many bones are the human body?",
             "Which planet in the solar system is the hottest?")

options = (("A. 116","B. 117","C. 118","D. 119"),
           ("A. Whale","B. Cocodrile","C. Ostrich","D. Elephant"),
           ("A. Nitrogen","B. Oxygen","C. Carbon-Dioxide ","D. Hydrogen"),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Earth ","B. Venus","C. Jupiter","D. Mercury"))

answers = ("C","D","A","A","B")

guesses =[]
score = 0
question_number = 0

print("WELCOME TO QUIZ GAME")


for question in questions:
    print(f"{question_number+1}.- {question}")
    print(f"The options are: ", end="")
    for option in range(len(options[question_number])):
        print(f"{options[question_number][option]}", end=" ")
    print()
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("CORRECT!")
    else: 
        print("INCORRECT!")
        print(f"{answers[question_number]} is the correct answer.")
    print()
    question_number += 1

print("--------------------")
print("       RESULTS      ")
print("--------------------")

print("answers: ", end="")
for ans in answers:
    print(ans, end=" ")
print()
print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")

print()
print(f"Your score is {score}!")
# Exercise 1 calculate the area of a rectangle 

length: float = float(input("Introduce the length: ")) 
width: float = float(input("Introduce the width: ")) 

area: float = length * width

print(f"The rectangle area is {area} cm2.")

options = (("A. 116","B. 117","C. 118","D. 119"),
           ("A. Whale","B. Cocodrile","C. Ostrich","D. Elephant"),
           ("A. Nitrogen","B. Oxygen","C. Carbon-Dioxide ","D. Hydrogen"),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Earth ","B. Venus","C. Jupiter","D. Mercury"))

question_number = 0

print(len(options[question_number]))
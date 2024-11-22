# Calculetor 

operator: str = input("Introduce the operator (+-/*): ")
number1: float = float(input("Introduce number one: "))
number2: float = float(input("Introduce number two: "))

if operator == "+":
    print(f"The result of {number1} {operator} {number2} = {number1 + number2}")
elif operator == "-":
    print(f"The result of {number1} {operator} {number2} = {number1 - number2}")
elif operator == "*":
    print(f"The result of {number1} {operator} {number2} = {number1 * number2}")
elif operator == "/":
    print(f"The result of {number1} {operator} {number2} = {number1 / number2}")
else:
    print("Please select a valid operator.")
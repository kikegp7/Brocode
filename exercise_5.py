# Python weight converter


while True:
    choose: str = input("Choose kg or lb: ")
    if choose != "kg" and choose != "lb":
        print(f"{choose} is not a valid option!")
    else:
        break
        
weight: float = float(input(f"Insert your weight in {choose}: "))

if choose == "kg":
    kg = weight
    lb = kg * 2.20462
    print(f"Your weight in kilograms is {kg:.3f} kg and your weight in pounds is {lb:.3f} lb")
elif choose == "lb":
    lb = weight
    kg = lb * 0.453592
    print(f"Your weight in kilograms is {kg:.3f} kg and your weight in pounds is {lb:.3f} lb")
else:
    print(f"{choose} is not a valid option!")


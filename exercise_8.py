# Shopping cart program 

foods = []
prices = []
total = 0

while True:

    food = input("Enter the food to buy (q to quit): ")
    if food.lower() == "q":
        break
    if not food.isalpha():
        break
    
    try:
        price = float(input(f"Enter the price of {food}: $"))
    except ValueError:
        print("Please insert a valid data. It can only be numbers!")

    foods.append(food)
    prices.append(price)

print("Your list of fruits: ")

c = 0
for y in foods:
    c+=1
    print(f"{c}.- {y}")
    
for x in prices:
    total = total + x

print(f"Your total is ${total:.2f}")
    
    
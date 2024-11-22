# Exercise 2 Shopping cart program

item:str = input("What item you would like to buy?: ")
price:float = float(input("What is the price?: "))
quantity:int = int(input("How many you would like?: ")) 

total = price * quantity

print(f"You have bougth {quantity} x {item}/s")
print(f"Your total is {total} dollars")
# CONCESSION STAND PROGRAM

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print("----- MOVIE MENU -----")
for key, value in menu.items():
    print(f"{key:10} = ${value:.2f}")

print()

while True:
    
    choose = input("Select an item (q to quit): ").lower()
    if choose == "q":
        break
    elif menu.get(choose) is not None:
        cart.append(choose)

for key in menu.keys():
    if key in cart:
        total = total + menu[key]

print()
print("-----   YOUR ORDER  -----")

if len(cart) == 0:
    print("Your cart is empty. See you soon!")
else:
    for num, item in enumerate(cart):
        if num == len(cart):
            break
        else:
            print(f"{num+1}.- {item}")
    print(f"Your total is ${total:.2f}!")
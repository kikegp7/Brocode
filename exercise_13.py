# BANKING PROGRAM
# Consta de 4 fases: Mostrar el balance, depositar, sacar dinero y salir.

def show_balance(balance):
    print("------------------")
    print(f"Your balance is ${balance:,.2f}.")
    print("------------------")

def deposit():
    print("------------------")
    amount = float(input("Enter the amount you want to deposit: "))
    if amount < 0 :
        print("------------------")
        print("That is not valid amount. ")
        return 0
    else:
        return amount

def withdraw(balance):
    print("------------------")
    amount = float(input("Enter the amount you want to withdraw: "))
    if amount < 0:
        print("------------------")
        print("That is not valid amount. ")
        return 0
    elif amount > balance:
        print("Inssuficent founds!")
        return 0
    else: 
        return amount

def exit():
    print("------------------")
    print("Thanks, Goodbye!")
    return False

print("-----  BANKING  -----")


def main():
    cont = True
    balance = 0

    while cont:
        print("------------------")
        print("1. Show Balance.")
        print("2. Deposit.")
        print("3. Withdraw.")
        print("4. Exit")
        print("------------------")

        user_input = int(input("Enter your choice: "))

        match user_input:

            case 1:
                show_balance(balance)

            case 2:
                balance += deposit()

            case 3: 
                balance -= withdraw(balance)

            case 4: 
                cont = exit()
            
            case _:
                print("------------------")
                print("This is not a valid choice.")
                


if __name__ == '__main__':
    main()
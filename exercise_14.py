# PYTHON SLOT MACHINE
import random

def spin_row():
    symbols = ["🍒","🍉","🍋","🔔", "⭐"]
    results = [random.choice(symbols) for _ in range(3)]
    return results

def print_row(row):
    print("-------------------------- ")
    print(" | ".join(row))
    print("-------------------------- ")

def get_payout(row: list, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
        
    return 0

def main():
    balance = 100
    print("-------------------------- ")
    print("WELCOME TO PYTHON SLOT  ")
    print("SYMBOLS: 🍒 🍉 🍋 🔔 ⭐ ")
    print("-------------------------- ")

    while balance > 0:
        print(f"Current balance: ${balance:.2f}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("-------------------------- ")
            print("Please enter a valid number!")
            print("-------------------------- ")
            continue

        bet = int(bet)

        if bet > balance:
            print("-------------------------- ")
            print("Inssuficient funds!")
            print("-------------------------- ")
            continue

        if bet <= 0:
            print("-------------------------- ")
            print("Bet must be greater than 0.")
            print("-------------------------- ")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning.....")
        print_row(row)

        payout = get_payout(row,bet)

        if payout > 0:
            print(f"You won ${payout:,}.")
        else:
            print("Sorry you lost this round.")

        balance += payout

        play_again = input("Do you want to play again?(Y/N): ").upper()

        if play_again != "Y":
            break
    print("-------------------------- ")
    print(f"Game over! Your final balance is ${balance:,}")
    print("-------------------------- ")

if __name__ == '__main__':
    main()
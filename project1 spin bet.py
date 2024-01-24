import random

Max_lines = 3
Max_bet = 100
Min_bet = 1

def deposit():
    while True:
        amount = input("Enter the amount you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount should be greater than zero.")
        else:
            print("Enter a valid number.")

def get_number_of_line():
    while True:
        Lines = input("Enter the number of lines you bet on(1-" + str(Max_lines) + ")? ")
        if Lines.isdigit():
            Lines = int(Lines)
            if 1 <= Lines <= Max_lines:
                break
            else:
                print("Lines should be greater than zero.")
        else:
            print("Enter a number.")

    return Lines

def get_bet():
    while True:
        amount = input("Enter the amount you want to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if Min_bet <= amount <= Max_bet:
                return amount
            else:
                print(f"Amount must be in between ${Min_bet}-${Max_bet}.")
        else:
            print("Enter a valid number.")

def main():
    balance = deposit()
    lines = get_number_of_line()

    # Move these lines after getting the bet value
    bet = get_bet()
    if bet is None:
        return  # Handle the case where get_bet() returns None
    Total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} lines equal to ${Total_bet}")

    while True:
        bet = get_bet()
        if bet is None:
            return  # Handle the case where get_bet() returns None
        Total_bet = bet * lines  # Now calculate Total_bet after getting the bet value
        if Total_bet > balance:
            print(f"You don't have enough amount, your current balance is ${balance}")
        else:
            break

    play_slots(balance, bet, Total_bet)  # Pass Total_bet as an argument

def spin_slot():
    slot1 = random.randint(1, 9)
    slot2 = random.randint(1, 9)
    slot3 = random.randint(1, 9)
    return slot1, slot2, slot3

def check_win(slot1, slot2, slot3, bet):
    if slot1 == slot2 == slot3:
        return bet * 10
    else:
        return -bet

def play_slots(balance, bet, Total_bet):  # Accept Total_bet as an argument
    while balance > 0:
        lines = get_number_of_line()
        Total_bet = bet * lines
        if Total_bet > balance:
            print(f"You don't have enough balance to place that bet. Your current balance is ${balance}.\n")
            break
        print(f"You are betting ${bet} on {lines} lines equal to ${Total_bet}.\n")
        slot1, slot2, slot3 = spin_slot()
        print(f"Slot 1: {slot1}, Slot 2: {slot2}, Slot 3: {slot3}\n")
        win = check_win(slot1, slot2, slot3, bet)
        if win > 0:
            print(f"Congratulations! You won ${win}!\n")
            balance += win
        else:
            print("Sorry, you didn't win this time.\n")
            balance -= Total_bet
        print(f"Your current balance is ${balance}.\n")
    if balance == 0:
        print("You have run out of balance. Thanks for playing!")

main()

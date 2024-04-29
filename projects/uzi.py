def load_data():
    global bank_data, cash_in_hand
    file= open(data_file, "r")
    lines = file.readlines()
    cash_in_hand = float(lines[0].strip())
    for line in lines[1:]:
        account_number, name, balance = line.strip().split(',')
        bank_data[account_number] = {"name": name, "balance": float(balance)}


def save_data():
    with open(data_file, "w") as file:
        file.write(str(cash_in_hand) + "\n")
        for account_number, data in bank_data.items():
            file.write(f"{account_number},{data['name']},{data['balance']}\n")

def create_account():
    account_number = input("Enter account number: ")
    name = input("Enter name: ")
    initial_deposit = float(input("Enter initial deposit: "))
    bank_data[account_number] = {"name": name, "balance": initial_deposit}
    print(f"Account created for {name} with account number {account_number}.\n")
    save_data()

def deposit_money():
    global cash_in_hand
    account_number = input("Enter account number: ")
    amount = float(input("Enter amount to deposit: "))
    bank_data[account_number]["balance"] += amount
    cash_in_hand += amount
    print(f"Deposited {amount} to account number {account_number}. Cash in hand is now {cash_in_hand}.\n")
    save_data()

def withdraw_money():
    global cash_in_hand
    account_number = input("Enter account number: ")
    amount = float(input("Enter amount to withdraw: "))
    if amount > bank_data[account_number]["balance"]:
        print("Insufficient balance.\n")
    else:
        bank_data[account_number]["balance"] -= amount
        cash_in_hand -= amount  
        print(f"Withdrew {amount} from account number {account_number}. Cash in hand is now {cash_in_hand}.\n")
        save_data()

def check_balance():
    account_number = input("Enter account number: ")
    print(f"Balance for account number {account_number} is {bank_data[account_number]['balance']}.\n")

def transfer_money():
    from_account = input("Enter account number to transfer from: ")
    to_account = input("Enter account number to transfer to: ")
    amount = float(input("Enter amount to transfer: "))
    if amount > bank_data[from_account]["balance"]:
        print("Insufficient balance.\n")
    else:
        bank_data[from_account]["balance"] -= amount
        bank_data[to_account]["balance"] += amount
        print(f"Transferred {amount} from account number {from_account} to account number {to_account}.\n")
        save_data()

def check_cash_in_hand():
    global cash_in_hand
    print(f"Cash in hand is {cash_in_hand}.\n")

def main():
    load_data()
    while True:
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. Check Cash in Hand")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            transfer_money()
        elif choice == 6:
            check_cash_in_hand()
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please choose a valid option.\n")

if __name__ == "__main__":
    bank_data = {}
    cash_in_hand = 0.0
    data_file = "bank_data.txt"
    main()

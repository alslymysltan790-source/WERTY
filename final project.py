print("Welcome to Faris Bank for Development and Investment")

users = {
    "sultan": {"code": 1111, "balance": 1000.0, "economy": 500.0},
    "mohammed": {"code": 2222, "balance": 1500.0, "economy": 800.0},
    "faris": {"code": 2727, "balance": 2000.0, "economy": 1000.0}
}

bills = {
    "sultan": {"Electricity": 100, "Water": 50, "Internet": 70},
    "mohammed": {"Electricity": 120, "Water": 60, "Internet": 80},
    "faris": {"Electricity": 90, "Water": 40, "Internet": 60}
}

name = input("Enter your name: ").lower()

if name in users:
    try:
        code = int(input("Enter your code: "))
    except ValueError:
        print("Invalid code. Exiting.")
        exit()

    if code == users[name]["code"]:
        print(f"Welcome {name}!")

        while True:
            print("\nChoose an operation:")
            print("1: Withdraw")
            print("2: Deposit")
            print("3: Transfer to another user")
            print("4: Donate to Ehssan")
            print("5: Pay Bills")
            print("6: Economy Management")
            print("7: Account Statement")
            print("8: Exit")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Enter a valid number")
                continue

            if choice == 1:
                try:
                    w = float(input("Enter withdrawal amount: "))
                except ValueError:
                    print("Invalid amount")
                    continue
                if w <= 0:
                    print("Amount must be positive")
                    continue
                if users[name]["balance"] >= w:
                    users[name]["balance"] -= w
                    print("New balance:", users[name]["balance"])
                else:
                    print("Insufficient funds")

            elif choice == 2:
                try:
                    d = float(input("Enter deposit amount: "))
                except ValueError:
                    print("Invalid amount")
                    continue
                if d <= 0:
                    print("Amount must be positive")
                    continue
                users[name]["balance"] += d
                print("New balance:", users[name]["balance"])

            elif choice == 3:
                recipient = input("Enter recipient name: ").lower()
                if recipient == name:
                    print("Cannot transfer to yourself")
                    continue
                if recipient not in users:
                    print("Recipient does not exist.")
                    create = input("Do you want to create a new user? (yes/no): ").lower()
                    if create == "yes":
                        try:
                            new_code = int(input("Enter new user's code: "))
                            new_balance = float(input("Enter new user's initial balance: "))
                        except ValueError:
                            print("Invalid input. Canceling new user creation.")
                            continue
                        users[recipient] = {"code": new_code, "balance": new_balance, "economy": 0.0}
                        bills[recipient] = {"Electricity": 0, "Water": 0, "Internet": 0}
                        print(f"New user '{recipient}' created successfully.")
                    else:
                        continue

                try:
                    amount = float(input("Enter transfer amount: "))
                except ValueError:
                    print("Invalid amount")
                    continue
                if amount <= 0:
                    print("Amount must be positive")
                    continue
                if users[name]["balance"] >= amount:
                    users[name]["balance"] -= amount
                    users[recipient]["balance"] += amount
                    print(f"Transferred {amount} to {recipient}. New balance: {users[name]['balance']}")
                else:
                    print("Insufficient funds for transfer")

            elif choice == 4:
                try:
                    donation = float(input("Enter donation amount for Ehssan: "))
                except ValueError:
                    print("Invalid amount")
                    continue
                if donation <= 0:
                    print("Amount must be positive")
                    continue
                if users[name]["balance"] >= donation:
                    users[name]["balance"] -= donation
                    print(f"Thank you for your donation of {donation} to Ehssan!")
                    print("New balance:", users[name]["balance"])
                else:
                    print("Insufficient funds for donation")

            elif choice == 5:
                user_bills = bills[name]
                print("\nYour Bills:")
                for bill, amount in user_bills.items():
                    print(f"{bill}: {amount}")
                bill_name = input("Enter bill to pay: ").title()
                if bill_name in user_bills:
                    amount = user_bills[bill_name]
                    if users[name]["balance"] >= amount:
                        users[name]["balance"] -= amount
                        user_bills[bill_name] = 0
                        print(f"{bill_name} bill paid successfully. New balance: {users[name]['balance']}")
                    else:
                        print("Insufficient funds to pay this bill")
                else:
                    print("Invalid bill name")

            elif choice == 6:
                print("\nEconomy Management:")
                print(f"Your economy balance: {users[name]['economy']}")
                print("1: Deposit to economy")
                print("2: Withdraw from economy")
                try:
                    eco_choice = int(input("Enter your choice: "))
                except ValueError:
                    print("Invalid choice")
                    continue

                if eco_choice == 1:
                    try:
                        amount = float(input("Enter amount to deposit into economy: "))
                    except ValueError:
                        print("Invalid amount")
                        continue
                    if amount <= 0:
                        print("Amount must be positive")
                        continue
                    if users[name]["balance"] >= amount:
                        users[name]["balance"] -= amount
                        users[name]["economy"] += amount
                        print(f"Deposited {amount} to economy. New economy balance: {users[name]['economy']}")
                    else:
                        print("Insufficient funds to deposit into economy")

                elif eco_choice == 2:
                    try:
                        amount = float(input("Enter amount to withdraw from economy: "))
                    except ValueError:
                        print("Invalid amount")
                        continue
                    if amount <= 0:
                        print("Amount must be positive")
                        continue
                    if users[name]["economy"] >= amount:
                        users[name]["economy"] -= amount
                        users[name]["balance"] += amount
                        print(f"Withdrawn {amount} from economy. New economy balance: {users[name]['economy']}")
                    else:
                        print("Insufficient economy balance")

                else:
                    print("Invalid economy option")

            elif choice == 7:
                print("\nAccount Statement:")
                print(f"Welcome {name}")
                print("Current Balance:", users[name]["balance"])
                print("Economy Balance:", users[name]["economy"])
                print("Outstanding Bills:")
                for bill, amount in bills[name].items():
                    print(f"{bill}: {amount}")

            elif choice == 8:
                print("Goodbye!")
                break

            else:
                print("Invalid choice")
    else:
        print("Incorrect code!")
else:
    print("User not found")

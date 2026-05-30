class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # Private variable (Encapsulation)

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance+amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    # Withdraw method
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance =self.__balance- amount
            print(f"₹{amount} withdrawn successfully.")

    # Getter method to access private balance
    def get_balance(self):
        return self.__balance

    # Display account details
    def display(self):
        print("\n--- Account Details ---")
        print("Account Holder:", self.name)
        print("Current Balance: ₹", self.__balance)


# Main Program
account = BankAccount("Rahul", 1000)

while True:
    print("\n===== MINI BANK MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Account Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: ₹"))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: ₹"))
        account.withdraw(amount)

    elif choice == "3":
        print("Available Balance: ₹", account.get_balance())

    elif choice == "4":
        account.display()

    elif choice == "5":
        print("Thank you for using Mini Bank.")
        break

    else:
        print("Invalid choice. Try again.")
#A banking account class pogramme

class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return "Owner: Mr.{} \nBalance: {} USD".format(self.owner, self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposit {} USD accepted".format(amount))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Funds Unavailable!")
        else:
            if amount == self.balance:
                self.balance -= amount
                print(f"Withdraw {amount} USD, but Current balance is ZERO.")
            else:
                self.balance -= amount
                print(f"Withdraw {amount} USD accepted.")

def get_valid_input(prompt, input_type):
    while True:
        try:
            user_input = input(prompt)
            if input_type == 'str' and not user_input.isalpha():
                raise ValueError("Invalid input. Please enter a valid string.")
            elif input_type == 'float':
                user_input = float(user_input)
            elif input_type == 'int':
                user_input = int(user_input)
            break
        except ValueError as ve:
            print(ve)
    return user_input

try:
    print("Welcome To The Chill MY Life Bank")
    owner_name = get_valid_input("Enter the Owner name: ", 'str')
    initial_balance = get_valid_input("Enter The initial Desired Balance(USD): ", 'float')
    myAccount = Account(owner_name, initial_balance)

    # Display the account
    print(myAccount)

    # Ask the user if they want to make a deposit
    deposit_choice = get_valid_input("Do you want to make a deposit? (yes/no): ", 'str').lower()

    if deposit_choice == "yes":
        deposit_amount = get_valid_input("Enter The Deposit amount(USD): ", 'float')
        myAccount.deposit(deposit_amount)
        print("Updated account details:")
        print(myAccount)
    elif deposit_choice == "no":
        print("No deposit made.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

    # Ask the user if they want to make a withdrawal
    withdrawal_choice = get_valid_input("Do you want to make a withdrawal? (yes/no): ", 'str').lower()

    if withdrawal_choice == "yes":
        withdrawal_amount = get_valid_input("Enter The withdrawal amount(USD): ", 'float')
        myAccount.withdraw(withdrawal_amount)
        print("Updated account details:")
        print(myAccount)
    elif withdrawal_choice == "no":
        print("No withdrawal made.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

except Exception as e:
    print(f"An error occurred: {e}")

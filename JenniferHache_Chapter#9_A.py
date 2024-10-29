

class BankAcc:
    # initialize a new bank account with the account holder's name, account number, and initial balance.
    def __init__(self, acct_name, acct_num, initial_balance):
        self.acct_num = acct_num
        self.acct_name = acct_name
        self.balance = initial_balance

    # create function for deposited money in bank account.
    def deposit(self):
        try:
            # ask user to enter their deposit as a positive number.
            # error code will appear if user entered anything other than a number.
            amount = float(input("Enter deposited amount: "))
            if amount > 0:
                # add amount to the initial balance.
                self.balance += amount
                print(f"\nAmount Deposited: ${amount:.2f}.")
            else:
                print("Deposit amount must be a positive number.")
        except ValueError:
            print("Error. Please enter numerical value.")

    # create function for withdrawn money from bank account.
    def withdraw(self):
        try:
            amount = float(input("Enter withdrawn amount: "))
            # create if statement that will check for a positive amount.
            # program will print a message if there is an insufficient balances.
            if amount > 0:
                # make sure there is enough money in account.
                if self.balance >= amount:
                    self.balance -= amount
                    print(f"\nYou Withdrew: ${amount:.2f}.")
                else:
                    print("\nInsufficient balance.")
            else:
                print("Withdrawal amount must be positive, try again.")
        # program will let user know to enter a valid numerical value.
        except ValueError:
            print("Error. Please enter numerical value.")

    # create function for interest rate for balance.
    def add_interest(self, interest_rate):
        #Add interest to the user's account.
        if interest_rate > 0:
            # use calculation for interest rate
            interest = self.balance * (interest_rate / 100)
            self.balance += interest
            # program will display interest added to new balance.
            print(f"\nInterest added: ${interest:.2f}. New balance: ${self.balance:.2f}.")
        else:
            print("Interest rate must be positive, try again.")

    # display account information including name, balance, and account number.
    def acct_info(self):
        print(f"\nAccount Name: {self.acct_name} \nAccount Balance: ${self.balance:.2f} \nAccount Number: {self.acct_num}")

    # display the current available balance in the account.
    def display(self):
        print("\nNet Available Balance =", self.balance)

    # return a string of the bank account.
    def __str__(self):
        return (f"Account Name: {self.acct_name}\n"
                f"Account Number: {self.acct_num}\n"
                f"Current Balance: ${self.balance:.2f}")


# Test function below
# Enter bank account name, account num, and balance on account.
def test_bank_acct():
    # BankAcc instance to show bank info of user
    account = BankAcc("Jane Doe", "11223344", 2000.00)

    # display initial account info
    print(account)

    # test account.deposit method
    account.deposit()
    print(account)

    # test account.withdraw method
    account.withdraw()
    print(account)

    # test adding interest
    # enter interest amount
    account.add_interest(2)
    print(account)

    # test account information display
    print(account.acct_info())

    # display account.balance
    account.display()

# run function
if __name__ == "__main__":
    test_bank_acct()
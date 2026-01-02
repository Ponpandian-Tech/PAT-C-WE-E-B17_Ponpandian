class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)
        else:
            print("Not enough balance")


class SavingsAccount(BankAccount):
    def __init__(self, acc_no, balance, interest):
        BankAccount.__init__(self, acc_no, balance)
        self.interest = interest

    def add_interest(self):
        print("Interest:", self.balance * self.interest / 100)


class CurrentAccount(BankAccount):
    def __init__(self, acc_no, balance, min_balance):
        BankAccount.__init__(self, acc_no, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)
        else:
            print("Minimum balance required")


# Example
s = SavingsAccount(101, 1000, 5)
s.deposit(500)
s.add_interest()
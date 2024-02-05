class Account:  # parent class
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    # withdrawal method subtracts the amount from the balance

    def with_drawal(self, amount):
        self.balance = self.balance - amount

    # deposit method adds the amount to the balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    # this method just returns the value of balance

    def get_balance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interest_rate=0):
        super().__init__(title, balance)
        self.interest_rate = interest_rate

    # computes interest amount using the interest rate

    def interest_amount(self):
        return (self.balance * self.interest_rate / 100)


obj1 = SavingsAccount("Steve", 5000, 10)
print("Initial Balance:", obj1.get_balance())
obj1.with_drawal(1000)
print("Balance after withdrawal:", obj1.get_balance())
obj1.deposit(500)
print("Balance after deposit:", obj1.get_balance())
print("Interest on current balance:", obj1.interest_amount())

class Account(object):
    # class variable, shared by all instances.
    num_accounts = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Account.num_accounts += 1

    def __del__(self):
        Account.num_accounts -= 1

    # instance method.
    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        self.balance -= amt

    def inquiry(self):
        return self.balance


if __name__ == '__main__':
    a = Account('Guido', 1000.00)
    b = Account('Bill', 100.00)

    print(a.inquiry())
    a.deposit(100)
    print(a.inquiry())
    print(a.name)
import random
from classes.class_def import Account


class EvilAccount(Account):
    def __init__(self, name, balance, evil_factor):
        Account.__init__(self, name, balance)
        self.evil_factor = evil_factor

    def inquiry(self):
        if random.randint(0, 4) == 1:
            return self.balance * self.evil_factor
        else:
            return self.balance


class MoreEvilAccount(EvilAccount):
    def deposit(self, amt):
        self.withdraw(5.00)  # subtract the 'convenience' fee
        super(MoreEvilAccount, self).deposit(amt)


class DepositCharge(object):
    fee = 5.00

    def deposit_fee(self):
        self.withdraw(self.fee)


class WithdrawCharge(object):
    fee = 2.50

    def withdraw_fee(self):
        self.withdraw(self.fee)


class MostEvilAccount(EvilAccount, DepositCharge, WithdrawCharge):
    def deposit(self, amt):
        self.deposit_fee()
        super(MostEvilAccount, self).deposit(amt)

    def withdraw(self, amt):
        self.withdraw_fee()
        super(MostEvilAccount, self).withdraw(amt)


if __name__ == '__main__':
    c = EvilAccount("George", 1000.0, 1.2)
    c.deposit(10.0)
    print(c.inquiry())

    print(MostEvilAccount.__mro__)

    d = MostEvilAccount("jobs", 500.0, 1.1)
    print(d.inquiry())
    d.deposit_fee()
    print(d.inquiry())
    d.withdraw_fee()
    print(d.inquiry())
"""
    This program implements classes.
"""

#CLASSES:
class BankAccount():
    def __init__(self, accno, name, balance):
        self.accno = accno
        self.name = name
        self.balance = balance
    
    def checkBalance(self):
        print(f"\nBalance: {self.balance}.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("\nSuccessfully Deposited.")
        else:
            print("\nInvalid amount!!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("\nNot enough balance!!.")
        else:
            self.balance -= amount
            print("\nSuccessfully withdrawn.")


acc1 = BankAccount(2001, "Silven", 800)
acc2 = BankAccount(2005, "Moin", 0)

acc1.checkBalance()
acc2.checkBalance()

acc1.withdraw(100)
acc2.deposit(100)


class SavingsBankAccount(BankAccount):
    def __init__(self, no, name, bal, rate):
        super().__init__(no, name, bal)
        self.interestRate = rate



class CurrentBankAccount(BankAccount):
    def __init__(self, no, name, bal, overDraftLimit):
        super().__init__(no, name, bal)
        self.overDraftLimit = overDraftLimit

    def withdraw(self, amount):
        if amount > self.balance:
            if amount < self.overDraftLimit:
                self.balance -= amount
                print("\nSuccessfully withdrawn through overDraftLimit.")
            else:
                print("\nNot enough balance even through overDraftLimit.")
        else:
            self.balance -= amount
            print("\nSuccessfully withdrawn.")


class FixedDepositAccount(BankAccount):
    def __init__(self, no, name, bal, Tenure):
        super().__init__(no, name, bal)
        self.Tenure = Tenure

    def withdraw(self, TimePeriod, amount):
        if TimePeriod < self.Tenure:
            print("\nTenure of your hasn't completed. Unable to withdraw.")
        else:
            self.balance -= amount
            print("Successfully withdrawn.")


SB = SavingsBankAccount(2001, "silven", 500, 2)
CB = CurrentBankAccount(2005, "Moin", 100, 1000)
FD = FixedDepositAccount(2008, "Lawry", 200, 3)

print(f"Interest Rate: {SB.interestRate}")
CB.withdraw(2000)
CB.withdraw(999)
CB.deposit(1000)
CB.checkBalance()

FD.withdraw(2, 100)
FD.withdraw(3, 50)
FD.checkBalance()

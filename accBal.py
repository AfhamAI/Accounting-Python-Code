class account:
    def __init__(self, bal , accNo):
        self.balance = bal
        self.accNumber = accNo
    def debit(self, amount):
        self.balance -= amount
        print(f"{amount} was debbited from your acc")
    def credit(self, amount):
        self.balance += amount
        print(f"{amount} was creddited to your acc")
    def bala(self):
        print(self.balance)



acc1 = account(5,239847689324)

acc1.credit(5000)
acc1.bala()

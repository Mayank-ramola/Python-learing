#create a account class with 2 attributes - balance & account no. 
#create method for debit , credit & printing the balance.

class account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    #debit method
    def debit (self, amount):
        self.balance -= amount
        print("Rs.",amount,"is debited.")
        print("Toatl balnce:", self.get_balance())

    #credit method
    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"is credited")
        print("Toatl balnce:", self.get_balance())


    def get_balance(self):
        return self.balance
    
acc1 = account(999999, 4548648)
acc1.debit(5000)
acc1.credit(10001)
acc1.debit(5000)
acc1.debit(10000)
acc1.credit(500)
    
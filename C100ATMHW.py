class ATM(object):
    def __init__(self, CardNumber, PinNumber):
        self.CardNumber = CardNumber
        self.PinNumber = PinNumber
    def withdrawl(self):
        print("Your amount has been successfully withdrawl")
    def balance(self):
        print("Balance in your account: ####")

customer = ATM(7348924729, 7890)
customer.withdrawl()
customer.balance()
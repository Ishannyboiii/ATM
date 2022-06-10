class ATM():
    def __init__(self,cardNumber,pin):
        self.cardNumber = cardNumber
        self.pin = pin
        self.balance = 420000
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("The new balance has been added")
        print("Your new balance is: ")
        print(self.balance)
    def withdraw(self,amount):
        self.balance = self.balance - amount
        print("The money has been taken out of your account")
        print("Your new balance is: ")
        print(self.balance)
    def checkBalance(self):
        print("Your balance is: ")
        print(self.balance)

def main():
    cardNumber = input("Please insert your card number")
    pin = input("Please enter your pin number")
    user = ATM(cardNumber,pin)
    print("Enter your choice: ")
    print("1:Balance, 2:Withdrawl, 3:Deposit")
    choose = int(input("Please select an option: "))
    if choose == 1:
        user.checkBalance()
    elif choose == 2:
        draw = int(input("How much would you like to withdraw?"))
        user.withdraw(draw)
    elif choose == 3:
        add = int(input("How much money would you like to deposit?")) 
        user.deposit(add)
    else:
        print("You have entered an invalid choice")
    
main()    

        


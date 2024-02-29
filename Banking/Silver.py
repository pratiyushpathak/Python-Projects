class Silver:
    def __init__(self):
        self.balance=50000
        self.loan=0

    def view(self):
        print('Your limit is: ',self.balance)
        print('Your loan is: ',self.loan)

    def withdraw(self):
        amount = int(input('Enter the amount to withdraw: '))
        if self.balance>=amount:
            self.balance -= amount
            self.loan += amount
        else:
            print("You can't withdraw more than your Limit")

    def deposit(self):
        print('Your outstanding amount is:',self.loan)
        amount = int(input('Enter the amount to deposit: '))
        if amount<=self.loan:
            self.loan -= amount
            self.balance += amount
        else:
            print("You can't deposit more than your outstanding loan amount!")

    def increaseLimit(self):
        print("This funtion is not available for Silver card users")

class Gold:
    def __init__(self):
        self.balance=100000
        self.loan=0
        self.count=0

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
        if self.count==0:
            self.balance += 50000
            print('Limit Extended Successfully')
            self.count += 1
        else:
            print('You can extend your limit only once!')



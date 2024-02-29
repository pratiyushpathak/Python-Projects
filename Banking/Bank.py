from Banking.Utility import Utility
class Bank:

    def start(self):
        flag = False
        while not flag:
            print("*************************MAIN MENU************************")
            print("1. Silver Card")
            print("2. Gold Card")
            print("3. Exit")
            options = int(input('Enter your choice: '))
            match options:
                case 1:
                    Utility.cardOption(1)
                case 2:
                    Utility.cardOption(2)
                case 3:
                    flag = True
                case _:
                    print('Enter a valid choice')

bank=Bank()
bank.start()


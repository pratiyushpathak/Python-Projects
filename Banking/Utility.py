from Banking.Silver import Silver
from Banking.Gold import Gold

class Utility:
    def subMenu(self):
        print('1. View')
        print('2. Withdraw')
        print('3. Deposit')
        print('4. Increase Limit')
        print('5. Exit')

    def cardOption(num):
        flag = False
        cardObject = Silver() if num == 1 else Gold()

        while not flag:
            print(f"*********{'SILVER' if num == 1 else 'GOLD'}**********")
            Utility.subMenu(None)
            options = int(input('Enter your choice: '))

            match options:
                case 1:
                    cardObject.view()
                case 2:
                    cardObject.withdraw()
                case 3:
                    cardObject.deposit()
                case 4:
                    cardObject.increaseLimit()
                case 5:
                    flag = True
                case _:
                    print('Enter a valid choice')

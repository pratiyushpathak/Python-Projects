from ConnectDatabase import formCollection
from AddUser import add_user
from UpdateUser import update_user
from DisplayUser import show_users
from DeleteUsers import delete_user

collection = formCollection()
while True:
    try:
        print('==============Users===============')
        print('1. Add User')
        print('2. Update User Details')
        print('3. Display Users')
        print('4. Delete User')
        print('5. Exit')
        print('==================================')

        choice = int(input('Enter your CHOICE: '))

        print('==================================')

        match choice:
            case 1:
                add_user(collection)
            case 2:
                update_user(collection)
            case 3:
                show_users(collection)
            case 4:
                delete_user(collection)
            case 5:
                break
    except:
        print('Enter a valid numeric value')

